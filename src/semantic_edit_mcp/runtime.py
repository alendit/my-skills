"""Journaled operations. Requires exclusive worktree use outside this server too."""
from __future__ import annotations

import asyncio
import fcntl
import hashlib
import json
import os
from pathlib import Path
import signal
import sqlite3
import stat
import subprocess
import time
import tempfile
import uuid
from contextlib import contextmanager
from dataclasses import dataclass

from jsonschema import validate

RESULT_SCHEMA = {
    'type': 'object', 'additionalProperties': False,
    'properties': {
        'status': {'enum': ['APPLIED', 'BLOCKED', 'FAILED']},
        'summary': {'type': 'string'},
        'verification': {'type': 'array', 'items': {'type': 'object', 'additionalProperties': False,
            'properties': {'command': {'type': 'string'}, 'outcome': {'enum': ['passed', 'failed', 'not_run']}},
            'required': ['command', 'outcome']}},
        'adaptations': {'type': 'array', 'items': {'type': 'string'}},
        'unresolved': {'type': 'array', 'items': {'type': 'string'}},
        'changed_files': {'type': 'array', 'items': {'type': 'string'}},
    },
    'required': ['status', 'summary', 'verification', 'adaptations', 'unresolved', 'changed_files'],
}


INSPECTION_SCHEMA = {
    'type': 'object', 'additionalProperties': False,
    'properties': {
        'summary': {'type': 'string'},
        'facts': {'type': 'array', 'items': {
            'type': 'object', 'additionalProperties': False,
            'properties': {
                'claim': {'type': 'string'},
                'basis': {'enum': ['observed', 'inferred']},
                'sources': {'type': 'array', 'items': {'type': 'string'}, 'minItems': 1},
            }, 'required': ['claim', 'basis', 'sources']}},
        'uncertainty': {'type': 'array', 'items': {'type': 'string'}},
    }, 'required': ['summary', 'facts', 'uncertainty'],
}


async def spawn_owned(*args, **kwargs):
    """Cancellation during spawn still obtains and stops the created process."""
    pending = asyncio.create_task(asyncio.create_subprocess_exec(*args, **kwargs))
    try:
        return await asyncio.shield(pending)
    except asyncio.CancelledError:
        process = await pending
        try:
            os.killpg(process.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        await process.wait()
        raise


def encoded(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=True, separators=(',', ':'))


def digest(value):
    return hashlib.sha256(encoded(value).encode()).hexdigest()


@dataclass(frozen=True)
class Config:
    repository: Path
    state_dir: Path
    codex: str = 'codex'
    model: str = 'gpt-5.6-luna'
    reasoning_effort: str = 'high'
    timeout_seconds: float = 1800


class Runtime:
    def __init__(self, config: Config):
        self.config = config
        self.active = {}
        self.cancel_requested = set()
        self.repo = config.repository.resolve()
        root = Path(self.git('rev-parse', '--show-toplevel').decode().strip()).resolve()
        if self.repo != root:
            raise ValueError('repository must be the exact Git worktree root')
        if any(line.startswith(b'160000 ') for line in self.git('ls-files', '--stage').splitlines()):
            raise ValueError('submodules are not supported by the initial snapshot contract')
        self.state = config.state_dir.resolve()
        if self.state == self.repo or self.repo in self.state.parents:
            raise ValueError('state-dir must be outside the repository')
        self.state.mkdir(parents=True, exist_ok=True, mode=0o700)
        if self.state.stat().st_uid != os.getuid() or stat.S_IMODE(self.state.stat().st_mode) != 0o700:
            raise ValueError('state-dir must be owned by the current user with permissions 0700')
        (self.state / 'blobs').mkdir(exist_ok=True)
        self.db = sqlite3.connect(self.state / 'operations.sqlite', isolation_level=None)
        self.db.row_factory = sqlite3.Row
        self.db.executescript('''
            PRAGMA journal_mode=WAL;
            CREATE TABLE IF NOT EXISTS binding (id INTEGER PRIMARY KEY, value TEXT);
            CREATE TABLE IF NOT EXISTS contexts (id TEXT PRIMARY KEY, thread TEXT, state TEXT);
            CREATE TABLE IF NOT EXISTS operations (
              id TEXT PRIMARY KEY, fingerprint TEXT, context TEXT, slice TEXT,
              phase TEXT, before_state TEXT, result TEXT, evidence TEXT, pid INTEGER);
        ''')
        binding = encoded({'repository': str(self.repo), 'model': config.model,
                           'reasoning_effort': config.reasoning_effort, 'codex': config.codex})
        self.db.execute('INSERT OR IGNORE INTO binding VALUES (1, ?)', (binding,))
        if self.db.execute('SELECT value FROM binding').fetchone()[0] != binding:
            raise ValueError('state-dir belongs to a different repository or backend configuration')
        # Fixed per-user location coordinates even servers with distinct state dirs.
        lock_dir = Path(tempfile.gettempdir()) / f'semantic-edit-locks-{os.getuid()}'
        lock_dir.mkdir(mode=0o700, exist_ok=True)
        if lock_dir.is_symlink() or lock_dir.stat().st_uid != os.getuid() or stat.S_IMODE(lock_dir.stat().st_mode) != 0o700:
            raise ValueError('unsafe shared lock directory')
        self.lock_path = lock_dir / (digest(str(self.repo)) + '.lock')

    def git(self, *args):
        return subprocess.run(['git', '-C', str(self.repo), *args], check=True,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout

    @contextmanager
    def locked(self):
        descriptor = os.open(self.lock_path, os.O_RDWR | os.O_CREAT | os.O_NOFOLLOW, 0o600)
        with os.fdopen(descriptor, 'r+') as handle:
            try:
                fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError:
                raise ValueError('worktree busy: another semantic operation is active') from None
            try:
                binding = handle.read().strip()
                if binding and binding != str(self.state):
                    raise ValueError('worktree is bound to another state-dir; reuse its authoritative journal')
                if not binding:
                    handle.write(str(self.state))
                    handle.flush()
                    os.fsync(handle.fileno())
                self.lock_fd = handle.fileno()
                yield
            finally:
                fcntl.flock(handle, fcntl.LOCK_UN)

    def snapshot(self):
        files = {}
        paths = self.git('ls-files', '-z', '--cached', '--others', '--exclude-standard').split(b'\0')
        for raw in sorted(set(paths) - {b''}):
            name = os.fsdecode(raw)
            path = self.repo / name
            try:
                info = path.lstat()
                if stat.S_ISLNK(info.st_mode):
                    content = os.fsencode(os.readlink(path))
                elif stat.S_ISREG(info.st_mode):
                    content = path.read_bytes()
                else:
                    raise ValueError(f'unsupported non-regular worktree path: {name}')
                content_hash = hashlib.sha256(content).hexdigest()
                blob = self.state / 'blobs' / content_hash
                if not blob.exists():
                    try:
                        with blob.open('xb') as target:
                            target.write(content)
                    except FileExistsError:
                        pass
                files[name] = [stat.S_IFMT(info.st_mode) | stat.S_IMODE(info.st_mode), content_hash]
            except FileNotFoundError:
                files[name] = None
        try:
            head = self.git('rev-parse', '--verify', 'HEAD').decode().strip()
        except subprocess.CalledProcessError:
            head = None
        value = {'head': head, 'index': self.git('ls-files', '--stage', '-z').hex(), 'files': files}
        return {'identity': digest(value), **value}

    def row(self, request_id):
        return self.db.execute('SELECT * FROM operations WHERE id=?', (request_id,)).fetchone()

    def operation_status(self, request_id: str):
        row = self.row(request_id)
        if not row:
            raise ValueError('unknown request_id')
        if row['result']:
            return json.loads(row['result'])
        current_state = None
        try:
            with self.locked():
                current_state = self.snapshot()['identity']
        except ValueError:
            pass  # An active writer prevents a meaningful state observation.
        return {'status': 'UNKNOWN', 'request_id': request_id, 'context_id': row['context'],
                'slice_id': row['slice'], 'mutation': 'unknown', 'evidence_ref': row['evidence'],
                'observed_state': current_state,
                'summary': 'Operation is running or interrupted; never replay automatically. Recovery requires the worktree lock.'}

    async def cancel_change(self, request_id: str):
        """Request cancellation without cancelling the MCP result/cleanup owner."""
        row = self.row(request_id)
        if not row:
            raise ValueError('unknown request_id')
        if row['result']:
            result = json.loads(row['result'])
            context = self.db.execute('SELECT thread FROM contexts WHERE id=?', (row['context'],)).fetchone()
            return {'control_status': 'settled', 'writer_stopped': True,
                    'context_resumable': bool(context and context['thread']), 'result': result}
        task = self.active.get(request_id)
        if task is None:
            return {'control_status': 'unavailable', 'writer_stopped': False,
                    'request_id': request_id,
                    'summary': 'This server does not own the active execution. Use its owning server or documented status/recovery; no cancellation delivered.'}
        if not task.done() and request_id not in self.cancel_requested:
            self.cancel_requested.add(request_id)
            task.cancel()
        return {'control_status': 'requested', 'writer_stopped': False,
                'request_id': request_id,
                'summary': 'Await the recorded operation result for settlement and exact state; cancellation does not roll back partial work.'}

    async def inspect_semantics(self, question: str, expected_state: str | None = None):
        """Answer a bounded question in a fresh, read-only backend context."""
        if not question.strip():
            raise ValueError('question must be nonempty')
        with self.locked():
            before = self.snapshot()
            if expected_state is not None and expected_state != before['identity']:
                raise ValueError('stale expected_state')
            if self.db.execute("SELECT 1 FROM operations WHERE phase='running'").fetchone():
                raise ValueError('unresolved operation; establish settlement before inspection')
            evidence = self.state / 'evidence' / uuid.uuid4().hex
            evidence.mkdir(parents=True)
            (evidence / 'inspection.json').write_text(encoded({'question': question, 'state': before['identity']}))
            backend = asyncio.create_task(self.run_backend(
                None, None, 'inspection', question, None, evidence, None, read_only=True))
            try:
                result = await asyncio.shield(backend)
            except asyncio.CancelledError:
                if not backend.done():
                    backend.cancel()
                while not backend.done():
                    try:
                        await asyncio.shield(backend)
                    except asyncio.CancelledError:
                        pass  # Keep the lock through repeated caller cancellation.
                if not backend.cancelled():
                    backend.result()  # Observe cleanup errors rather than hiding them.
                raise
            after = self.snapshot()
            (evidence / 'after.json').write_text(encoded(after))
            if before['identity'] != after['identity']:
                raise ValueError('worktree changed during read-only inspection; evidence is invalid, partial work preserved')
            packet = {**result, 'inspected_state': before['identity'], 'mutation': 'unchanged',
                      'evidence_ref': str(evidence), 'context': 'fresh_read_only',
                      'acceptance': 'not an acceptance decision; required independent reviewer remains separate'}
            (evidence / 'result.json').write_text(encoded(packet))
            return packet

    def acknowledge_interruption(self, request_id: str, expected_state: str):
        with self.locked():
            row = self.row(request_id)
            if not row:
                raise ValueError('unknown request_id')
            if row['result']:
                return json.loads(row['result'])
            if row['pid']:
                try:
                    os.kill(row['pid'], 0)
                except ProcessLookupError:
                    pass
                else:
                    raise ValueError('recorded backend process still exists; stop it before recovery')
            after = self.snapshot()
            if after['identity'] != expected_state:
                raise ValueError('stale expected_state')
            before = json.loads(row['before_state'])
            result = self.finish(row, before, after, self.failure('Interrupted operation acknowledged; inspect at slice acceptance.'))
            return result

    @staticmethod
    def failure(message):
        return {'status': 'FAILED', 'summary': message, 'verification': [],
                'adaptations': [], 'unresolved': [message], 'changed_files': []}

    def finish(self, row, before, after, model_result):
        changed = sorted(k for k in set(before['files']) | set(after['files'])
                         if before['files'].get(k) != after['files'].get(k))
        model_result = dict(model_result)
        claimed = model_result.pop('changed_files', [])
        if before['head'] != after['head'] or before['index'] != after['index']:
            model_result = self.failure('Backend changed HEAD or index outside its authorization.')
        elif model_result['status'] == 'APPLIED' and sorted(set(claimed)) != changed:
            model_result = self.failure('Reported changed_files disagree with the observed delta; reconcile at the semantic boundary.')
        mutation = 'unchanged' if before['identity'] == after['identity'] else (
            'complete' if model_result['status'] == 'APPLIED' else 'partial')
        result = {**model_result, 'request_id': row['id'], 'context_id': row['context'],
                  'slice_id': row['slice'], 'change_id': row['id'], 'result_state': after['identity'],
                  'mutation': mutation, 'changed_files': changed, 'evidence_ref': row['evidence']}
        Path(row['evidence'], 'after.json').write_text(encoded(after))
        Path(row['evidence'], 'result.json').write_text(encoded(result))
        self.db.execute('BEGIN IMMEDIATE')
        try:
            self.db.execute('UPDATE operations SET phase=?,result=? WHERE id=?', ('finished', encoded(result), row['id']))
            self.db.execute('UPDATE contexts SET state=? WHERE id=?', (after['identity'], row['context']))
            self.db.execute('COMMIT')
        except BaseException:
            self.db.execute('ROLLBACK')
            raise
        return result

    async def realize_change(self, request_id: str, slice_id: str, specification: str,
                             context_id: str | None = None, expected_state: str | None = None,
                             acceptance: str | None = None):
        if not request_id or not slice_id or not specification:
            raise ValueError('request_id, slice_id and specification must be nonempty')
        fingerprint = digest([request_id, slice_id, specification, context_id, expected_state, acceptance])
        existing = self.row(request_id)
        if existing:
            if existing['fingerprint'] != fingerprint:
                raise ValueError('request_id reused with different payload')
            return self.operation_status(request_id)
        with self.locked():
            # The lock makes this insertion and the entire backend run exclusive.
            existing = self.row(request_id)
            if existing:
                if existing['fingerprint'] != fingerprint:
                    raise ValueError('request_id reused with different payload')
                return self.operation_status(request_id)
            if self.db.execute("SELECT 1 FROM operations WHERE phase='running'").fetchone():
                raise ValueError('unresolved interrupted operation; recover before new work')
            before = self.snapshot()
            if expected_state is not None and expected_state != before['identity']:
                raise ValueError('stale expected_state')
            context = None
            if context_id:
                context = self.db.execute('SELECT * FROM contexts WHERE id=?', (context_id,)).fetchone()
                if not context:
                    raise ValueError('unknown context_id')
                if context['state'] != before['identity'] and expected_state is None:
                    raise ValueError('context state changed; supply current expected_state explicitly')
                if not context['thread']:
                    raise ValueError('context has no durable backend identity; start a new context explicitly')
            else:
                context_id = 'ctx_' + uuid.uuid4().hex
                self.db.execute('INSERT INTO contexts VALUES (?,NULL,?)', (context_id, before['identity']))
            evidence = self.state / 'evidence' / uuid.uuid4().hex
            evidence.mkdir(parents=True)
            (evidence / 'before.json').write_text(encoded(before))
            (evidence / 'request.json').write_text(encoded({'specification': specification, 'acceptance': acceptance}))
            self.db.execute('INSERT INTO operations VALUES (?,?,?,?,?,?,?,?,NULL)',
                (request_id, fingerprint, context_id, slice_id, 'running', encoded(before), None, str(evidence)))
            row = self.row(request_id)
            backend = asyncio.create_task(self.run_backend(context_id, context['thread'] if context else None,
                                                slice_id, specification, acceptance, evidence, request_id))
            self.active[request_id] = backend
            caller_cancelled = False
            try:
                try:
                    result = await asyncio.shield(backend)
                except asyncio.CancelledError:
                    caller_cancelled = bool(asyncio.current_task().cancelling())
                    if not backend.done() and request_id not in self.cancel_requested:
                        self.cancel_requested.add(request_id)
                        backend.cancel()
                    # Cleanup is owned by the backend, never by the control request.
                    while not backend.done():
                        try:
                            await asyncio.shield(backend)
                        except asyncio.CancelledError:
                            # Repeated caller cancellation must not release the writer lock.
                            caller_cancelled |= bool(asyncio.current_task().cancelling())
                    if not backend.cancelled():
                        # Completion can win a cancellation race. Preserve its actual result.
                        result = backend.result()
                    else:
                        result = self.failure('Cancellation completed; backend stopped, partial work preserved.')
                except Exception as exc:
                    result = self.failure(f'Backend execution failed: {type(exc).__name__}: {exc}')
                final = self.finish(row, before, self.snapshot(), result)
                if caller_cancelled:
                    raise asyncio.CancelledError
                return final
            finally:
                self.active.pop(request_id, None)
                self.cancel_requested.discard(request_id)

    async def run_backend(self, context_id, thread, slice_id, specification, acceptance, evidence, request_id, *, read_only=False):
        # Enumerate configuration without starting servers; never persist this output,
        # which can contain credentials. Explicit per-name overrides avoid TOML map merging.
        discovery = await spawn_owned(self.config.codex, '-c', 'features.plugins=false',
            'mcp', 'list', '--json', cwd=self.repo, stdin=asyncio.subprocess.DEVNULL,
            stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE,
            start_new_session=True, pass_fds=(self.lock_fd,))
        try:
            raw, _ = await asyncio.wait_for(discovery.communicate(), 15)
            if discovery.returncode:
                raise ValueError('MCP configuration discovery failed; no backend launched')
            try:
                configured = json.loads(raw)
                if not isinstance(configured, list) or any(not isinstance(item, dict) or
                        not isinstance(item.get('name'), str) for item in configured):
                    raise ValueError()
                server_transports = []
                for item in configured:
                    transport = item.get('transport', {}).get('type')
                    if transport not in ('stdio', 'streamable_http'):
                        raise ValueError()
                    server_transports.append((item['name'], transport))
            except (ValueError, UnicodeDecodeError):
                raise ValueError('MCP configuration discovery returned an invalid inventory') from None
        finally:
            try:
                os.killpg(discovery.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
            await discovery.wait()
        schema_path = evidence / 'schema.json'
        schema_path.write_text(encoded(INSPECTION_SCHEMA if read_only else RESULT_SCHEMA))
        output = evidence / 'model-result.json'
        command = [self.config.codex, 'exec', '--ignore-user-config', '--json',
                   '--model', self.config.model, '-c', 'approval_policy="never"',
                   '-c', 'sandbox_mode="read-only"' if read_only else 'sandbox_mode="workspace-write"', '-c', 'sandbox_workspace_write.network_access=false',
                   '-c', 'features.multi_agent=false', '-c', 'features.apps=false',
                   '-c', 'features.plugins=false', '-c', 'features.memories=false',
                   '-c', 'service_tier="default"',
                   '-c', 'web_search="disabled"', '-c', f'model_reasoning_effort={json.dumps(self.config.reasoning_effort)}',
                   '--output-schema', str(schema_path), '--output-last-message', str(output)]
        disabled_servers = []
        for name, transport in server_transports:
            # User inventory is a superset of --ignore-user-config. A disabled entry
            # still needs a valid transport when no underlying entry survives.
            if transport == 'stdio':
                fields = 'enabled=false, command="false"'
            else:
                fields = 'enabled=false, url="https://disabled.invalid/mcp"'
            disabled_servers.append(f'{json.dumps(name)}={{{fields}}}')
        # Codex splits override key paths on dots without honoring quoted segments.
        # Keep server names as TOML inline-table keys inside the override value.
        command += ['-c', 'mcp_servers={' + ','.join(disabled_servers) + '}']
        if read_only:
            command += ['--ephemeral']
        if thread:
            command += ['resume', thread, '-']
        else:
            command += ['-']
        prompt = f'''You realize semantic changes for Astra. Reuse this context; current specification overrides remembered assumptions.
Repository: {self.repo}. Slice: {slice_id}.
The parent implements and integrates the slice; you realize only the one specific edit selected now.
Slice context and acceptance scenarios are background, not authority to finish remaining slice work.
Resolve source adaptation, checks, and repairs only within this edit. Return BLOCKED for necessary scope expansion.
If the request delegates a broader package rather than one specific change, return BLOCKED and ask the parent to select the next edit.
Follow applicable repository instructions. Local completion is the selected behavior and checks, not whole-slice readiness.
Do not delegate, use plugins/apps, access network, commit, push, publish, or modify Git refs/index.
Do not leave background processes running; the runtime terminates the operation process group at completion.
Return BLOCKED for a decision changing binding semantics; describe assumption, evidence, consequence and needed decision in unresolved.
Report material adaptations. APPLIED requires applicable checks actually passed, with commands and outcomes, and no unresolved issues.
Report changed_files as repository-relative paths with actual final differences from immediately before this operation, excluding unrelated pre-existing dirty paths.
Summarize compactly; detailed implementation and logs stay in this session. Do not ask the parent to supervise routine progress.
Specification:\n{specification}\nAcceptance scenarios:\n{acceptance or 'Use the specification and repository checks.'}'''
        if read_only:
            prompt = f"""Inspect the repository read-only for one bounded semantic question.
Repository: {self.repo}. Use a fresh context; do not implement, repair, run writing checks, or modify any files.
Do not delegate, use plugins/apps, access network, or leave background processes.
Return compact facts about behavior, interfaces, ownership, state, ordering or failure boundaries.
Ground every claim in repository-relative source locations (path:line). Distinguish observed facts from inference.
State missing evidence or uncertainty explicitly. Prefer semantic prose without code dumps or raw logs.
This is evidence for the parent's decision, not acceptance or proof from the editing context.
Question: {specification}"""
        (evidence / 'command.json').write_text(encoded(command))
        process = await spawn_owned(*command, cwd=self.repo, stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE, start_new_session=True,
            pass_fds=(self.lock_fd,), limit=16 * 1024 * 1024)
        self.db.execute('UPDATE operations SET pid=? WHERE id=?', (process.pid, request_id))

        started_at = time.monotonic()
        usage = []
        async def read_events():
            observed = None
            with (evidence / 'events.jsonl').open('wb') as log:
                async for line in process.stdout:
                    log.write(line)
                    log.flush()
                    try:
                        event = json.loads(line)
                    except (ValueError, UnicodeDecodeError):
                        continue
                    if event.get('type') == 'thread.started':
                        identity = event.get('thread_id')
                        if not isinstance(identity, str) or not identity or (thread and identity != thread):
                            raise ValueError('backend context identity mismatch')
                        if observed and identity != observed:
                            raise ValueError('multiple backend context identities')
                        observed = identity
                        self.db.execute('UPDATE contexts SET thread=? WHERE id=?', (identity, context_id))
                    if event.get('type') == 'turn.completed':
                        usage.append(event.get('usage'))
            return observed

        async def stderr_log():
            with (evidence / 'stderr.log').open('wb') as log:
                while chunk := await process.stderr.read(65536):
                    log.write(chunk)

        async def execute():
            process.stdin.write(prompt.encode())
            await process.stdin.drain()
            process.stdin.close()
            identity, _ = await asyncio.gather(read_events(), stderr_log())
            await process.wait()
            return identity

        try:
            identity = await asyncio.wait_for(execute(), self.config.timeout_seconds)
        finally:
            if process.returncode is None:
                try:
                    os.killpg(process.pid, signal.SIGTERM)
                except ProcessLookupError:
                    pass
                try:
                    await asyncio.wait_for(process.wait(), 3)
                except asyncio.TimeoutError:
                    try:
                        os.killpg(process.pid, signal.SIGKILL)
                    except ProcessLookupError:
                        pass
                    await process.wait()
            # Also terminate any descendants left after the direct backend exits.
            try:
                os.killpg(process.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
            (evidence / 'metrics.json').write_text(encoded({'elapsed_seconds': time.monotonic() - started_at,
                'usage': usage, 'model': self.config.model, 'reasoning_effort': self.config.reasoning_effort,
                'service_tier': 'default'}))
        if process.returncode:
            raise ValueError(f'backend exited {process.returncode}; see retained evidence')
        if not identity:
            raise ValueError('backend omitted thread.started identity')
        result = json.loads(output.read_text())
        validate(result, INSPECTION_SCHEMA if read_only else RESULT_SCHEMA)
        if not read_only and result['status'] == 'APPLIED' and (result['unresolved'] or not result['verification'] or
                any(item['outcome'] != 'passed' for item in result['verification'])):
            raise ValueError('APPLIED requires passing checks and no unresolved issues')
        return result

    def slice_summary(self, context_id: str, slice_id: str):
        rows = self.db.execute('SELECT id FROM operations WHERE context=? AND slice=? ORDER BY rowid',
                               (context_id, slice_id)).fetchall()
        if not rows:
            raise ValueError('unknown context/slice')
        with self.locked():
            if self.db.execute("SELECT 1 FROM operations WHERE phase='running'").fetchone():
                raise ValueError('operation running or interrupted; resolve before slice acceptance')
            current_state = self.snapshot()['identity']
        results = [self.operation_status(row['id']) for row in rows]
        return {'context_id': context_id, 'slice_id': slice_id, 'result_state': current_state,
                'evidence_stale': results[-1].get('result_state') != current_state,
                'acceptance': 'pending independent slice acceptance', 'operations': results,
                'evidence_refs': [item['evidence_ref'] for item in results],
                'summary': 'Operation outcomes are historical; later corrections may resolve earlier blockers. Evaluate against the current slice contract.'}

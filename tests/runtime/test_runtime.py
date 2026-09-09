import asyncio
import json
import os
from pathlib import Path
import subprocess
import sys

import pytest
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from semantic_edit_mcp.runtime import Config, Runtime, digest


@pytest.fixture
def setup(tmp_path):
    repo = tmp_path / 'repo'
    repo.mkdir()
    subprocess.run(['git', 'init', '-q', str(repo)], check=True)
    fake = tmp_path / 'fake-codex'
    fake.write_text('''#!/usr/bin/env python3
import json,sys,pathlib,time
args=sys.argv[1:]
if 'list' in args and 'mcp' in args:
 if (pathlib.Path.cwd().parent/'inventory-fail').exists(): print('invalid SECRET'); sys.exit(0)
 print(json.dumps([{'name':'project.server', 'transport':{'type':'stdio'}, 'env':{'SECRET':'must-not-persist'}}, {'name':'project.http', 'transport':{'type':'streamable_http'}}])); sys.exit(0)
prompt=sys.stdin.read().split('Specification:')[-1]
repo=pathlib.Path.cwd()
with (repo.parent/'calls').open('a') as f: f.write(json.dumps(args)+'\\n')
thread=args[args.index('resume')+1] if 'resume' in args else 'thread-exact-123'
print(json.dumps({'type':'thread.started','thread_id':thread}),flush=True)
if 'PARTIAL_SLEEP' in prompt:
 (repo/'partial.txt').write_text('preserved')
 time.sleep(20)
if 'SLEEP' in prompt: time.sleep(20)
if 'EDIT' in prompt: (repo/'changed.txt').write_text(prompt.split('Specification:')[-1])
if 'BEHAVIOR_BUG' in prompt: (repo/'behavior.py').write_text('def add(a, b): return a - b')
if 'BEHAVIOR_FIX' in prompt: (repo/'behavior.py').write_text('def add(a, b): return a + b')
if 'EXIT' in prompt: sys.exit(3)
result={'status':'BLOCKED' if 'BLOCK' in prompt else 'APPLIED','summary':'done','verification':[{'command':'fake check','outcome':'passed'}],'adaptations':[],'unresolved':['decision needed'] if 'BLOCK' in prompt else [],'changed_files':['changed.txt'] if 'EDIT' in prompt else (['behavior.py'] if 'BEHAVIOR_' in prompt else [])}
if 'BADAPPLIED' in prompt: result['unresolved']=['missing']
if 'sandbox_mode="read-only"' in args:
 result={'summary':'bounded inspection', 'facts':[{'claim':'partial state is preserved', 'basis':'observed', 'sources':['partial.txt:1']}], 'uncertainty':['fixture evidence only']}
 if 'INSPECT_MUTATE' in prompt: (repo/'forbidden.txt').write_text('bad')
out=pathlib.Path(args[args.index('--output-last-message')+1])
out.write_text('bad json' if 'MALFORMED' in prompt else json.dumps(result))
print(json.dumps({'type':'turn.completed','usage':{'input_tokens':40,'output_tokens':10}}),flush=True)
''')
    fake.chmod(0o755)
    config = Config(repo, tmp_path / 'state', str(fake), timeout_seconds=2)
    return Runtime(config), config


async def test_context_blocker_correction_idempotence(setup):
    runtime, config = setup
    first = await runtime.realize_change('1', 'slice', 'EDIT BLOCK')
    assert first['status'] == 'BLOCKED' and first['mutation'] == 'partial'
    assert first['changed_files'] == ['changed.txt']
    second = await runtime.realize_change('2', 'slice', 'EDIT corrected', first['context_id'], first['result_state'])
    assert second['status'] == 'APPLIED'
    assert await runtime.realize_change('2', 'slice', 'EDIT corrected', first['context_id'], first['result_state']) == second
    calls = [json.loads(s) for s in (config.repository.parent / 'calls').read_text().splitlines()]
    assert len(calls) == 2
    assert calls[1][calls[1].index('resume')+1] == 'thread-exact-123'
    assert '--last' not in calls[1]
    override = next(arg for arg in calls[1] if arg.startswith('mcp_servers='))
    assert '"project.server"={enabled=false, command="false"}' in override
    assert '"project.http"={enabled=false, url="https://disabled.invalid/mcp"}' in override
    assert 'must-not-persist' not in Path(second['evidence_ref'], 'command.json').read_text()
    with pytest.raises(ValueError, match='different payload'):
        await runtime.realize_change('2', 'slice', 'different')
    assert len(runtime.slice_summary(first['context_id'], 'slice')['operations']) == 2
    restarted = Runtime(config)
    assert restarted.operation_status('2') == second


@pytest.mark.parametrize('spec', ['EDIT EXIT', 'EDIT MALFORMED', 'EDIT BADAPPLIED'])
async def test_failures_keep_partial_evidence(setup, spec):
    runtime, _ = setup
    result = await runtime.realize_change('1', 'slice', spec)
    assert result['status'] == 'FAILED' and result['mutation'] == 'partial'
    assert Path(result['evidence_ref'], 'events.jsonl').exists()


async def test_stale_and_cross_process_lock(setup):
    runtime, config = setup
    before = runtime.snapshot()['identity']
    (config.repository / 'dirty.txt').write_text('outside edit')
    with pytest.raises(ValueError, match='stale'):
        await runtime.realize_change('1', 'slice', 'EDIT', expected_state=before)
    with runtime.locked():
        other = Runtime(Config(config.repository, config.state_dir.parent / 'other', config.codex))
        with pytest.raises(ValueError, match='busy'):
            await other.realize_change('2', 'slice', 'EDIT')
    assert not (config.repository.parent / 'calls').exists()


async def test_timeout_and_cancellation(setup):
    runtime, _ = setup
    result = await runtime.realize_change('1', 'slice', 'SLEEP')
    assert result['status'] == 'FAILED'
    task = asyncio.create_task(runtime.realize_change('2', 'slice', 'SLEEP'))
    await asyncio.sleep(.2)
    task.cancel()
    with pytest.raises(asyncio.CancelledError):
        await task
    assert runtime.operation_status('2')['status'] == 'FAILED'
    with runtime.locked():
        pass


async def test_restart_unknown_never_replays(setup):
    runtime, config = setup
    # A running journal entry simulates abrupt loss before the backend launched.
    original = runtime.run_backend
    async def crash(*args):
        raise BaseException('simulated process crash')
    runtime.run_backend = crash
    with pytest.raises(BaseException, match='simulated process crash'):
        await runtime.realize_change('1', 'slice', 'EDIT')
    resumed = Runtime(config)
    assert (await resumed.realize_change('1', 'slice', 'EDIT'))['status'] == 'UNKNOWN'
    with pytest.raises(ValueError, match='interrupted'):
        await resumed.realize_change('2', 'slice', 'EDIT')
    result = resumed.acknowledge_interruption('1', resumed.snapshot()['identity'])
    assert result['status'] == 'FAILED'
    assert not (config.repository.parent / 'calls').exists()


async def test_actual_stdio_tools(setup):
    _, config = setup
    params = StdioServerParameters(command=sys.executable, args=['-m', 'semantic_edit_mcp.server',
        '--repository', str(config.repository), '--state-dir', str(config.state_dir), '--codex', config.codex])
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as client:
            await client.initialize()
            names = {t.name for t in (await client.list_tools()).tools}
            assert names == {'realize_change', 'slice_summary', 'operation_status', 'acknowledge_interruption', 'cancel_change', 'inspect_semantics'}
            response = await client.call_tool('realize_change', {'request_id': 'wire1', 'slice_id': 'slice', 'specification': 'EDIT'})
            assert not response.isError
            result = json.loads(response.content[0].text)
            assert result['status'] == 'APPLIED'
            duplicate = await client.call_tool('operation_status', {'request_id': 'wire1'})
            assert json.loads(duplicate.content[0].text) == result

async def test_hard_server_death_retains_writer_lock(setup):
    runtime, config = setup
    command = [sys.executable, '-c',
        'import asyncio,sys; from pathlib import Path; from semantic_edit_mcp.runtime import Runtime,Config; '
        'r=Runtime(Config(Path(sys.argv[1]),Path(sys.argv[2]),sys.argv[3],timeout_seconds=30)); '
        'asyncio.run(r.realize_change("crash", "slice", "SLEEP"))',
        str(config.repository), str(config.state_dir), config.codex]
    parent = subprocess.Popen(command)
    try:
        for _ in range(100):
            row = runtime.row('crash')
            if row and row['pid'] and (config.repository.parent / 'calls').exists():
                break
            await asyncio.sleep(.02)
        else:
            pytest.fail('backend did not launch')
        parent.kill()
        parent.wait()
        with pytest.raises(ValueError, match='busy'):
            with runtime.locked():
                pass
        import signal
        os.killpg(row['pid'], signal.SIGTERM)
        for _ in range(100):
            try:
                with runtime.locked():
                    break
            except ValueError:
                await asyncio.sleep(.02)
        else:
            pytest.fail('backend lock did not release after termination')
        assert runtime.operation_status('crash')['status'] == 'UNKNOWN'
    finally:
        if parent.poll() is None:
            parent.kill()
            parent.wait()


async def test_changed_evidence_and_state_binding(setup):
    runtime, config = setup
    result = await runtime.realize_change('1', 'slice', 'EDIT')
    assert result['status'] == 'APPLIED'
    (config.repository / 'external').write_text('different')
    assert runtime.slice_summary(result['context_id'], 'slice')['evidence_stale']
    other = Runtime(Config(config.repository, config.state_dir.parent / 'other', config.codex))
    with pytest.raises(ValueError, match='another state-dir'):
        await other.realize_change('2', 'slice', 'EDIT')

async def test_snapshot_dirty_index_symlink_and_report_mismatch(setup):
    runtime, config = setup
    path = config.repository / 'preexisting'
    path.write_text('before')
    baseline = runtime.snapshot()['identity']
    path.write_text('after')
    assert runtime.snapshot()['identity'] != baseline
    symlink = config.repository / 'link'
    symlink.symlink_to('preexisting')
    before = runtime.snapshot()['identity']
    symlink.unlink()
    symlink.symlink_to('other')
    assert runtime.snapshot()['identity'] != before
    async def misreport(*args):
        (config.repository / 'unreported').write_text('new')
        return {'status': 'APPLIED', 'summary': 'ok', 'verification': [{'command': 'test', 'outcome': 'passed'}],
                'adaptations': [], 'unresolved': [], 'changed_files': []}
    runtime.run_backend = misreport
    result = await runtime.realize_change('1', 'slice', 'change')
    assert result['status'] == 'FAILED'
    assert result['changed_files'] == ['unreported']
    assert 'disagree' in result['summary']


def test_submodules_rejected(setup):
    runtime, config = setup
    subprocess.run(['git', '-C', str(config.repository), 'update-index', '--add', '--cacheinfo',
                    '160000,' + 'a' * 40 + ',submodule'], check=True)
    with pytest.raises(ValueError, match='submodules'):
        Runtime(config)

async def test_independent_slice_acceptance_and_same_context_correction(setup):
    runtime, config = setup
    first = await runtime.realize_change('1', 'addition', 'BEHAVIOR_BUG: implement addition')
    assert first['status'] == 'APPLIED'
    second = await runtime.realize_change('2', 'addition', 'EDIT: document addition',
                                          first['context_id'], first['result_state'])
    # Between calls the parent consumed summaries only. Inspect behavior now at acceptance.
    packet = runtime.slice_summary(first['context_id'], 'addition')
    assert not packet['evidence_stale']
    assert len(packet['operations']) == 2
    probe = ['python3', '-B', '-c', 'from behavior import add; assert add(2, 3) == 5']
    assert subprocess.run(probe, cwd=config.repository, capture_output=True).returncode != 0
    correction = await runtime.realize_change('3', 'addition',
        'BEHAVIOR_FIX: acceptance observed add(2,3) returns -1; implement addition returning 5.',
        first['context_id'], second['result_state'])
    assert correction['status'] == 'APPLIED'
    assert subprocess.run(probe, cwd=config.repository, capture_output=True).returncode == 0
    corrected = runtime.slice_summary(first['context_id'], 'addition')
    assert len(corrected['operations']) == 3
    assert corrected['operations'][0] == first
    assert not corrected['evidence_stale']
    assert corrected['result_state'] == correction['result_state']
    metrics = [json.loads(Path(item['evidence_ref'], 'metrics.json').read_text()) for item in corrected['operations']]
    assert sum(m['usage'][0]['input_tokens'] for m in metrics) == 120
    assert sum(m['usage'][0]['output_tokens'] for m in metrics) == 30
    assert all(m['elapsed_seconds'] > 0 for m in metrics)
    calls = [json.loads(line) for line in (config.repository.parent / 'calls').read_text().splitlines()]
    assert calls[2][calls[2].index('resume') + 1] == 'thread-exact-123'

async def test_mcp_inventory_failure_prevents_backend_launch(setup):
    runtime, config = setup
    (config.repository.parent / 'inventory-fail').touch()
    result = await runtime.realize_change('1', 'slice', 'EDIT')
    assert result['status'] == 'FAILED'
    assert result['mutation'] == 'unchanged'
    assert not (config.repository.parent / 'calls').exists()
    assert 'SECRET' not in json.dumps(result)
    assert not Path(result['evidence_ref'], 'events.jsonl').exists()

async def test_disabled_transport_overrides_parse_with_real_codex(setup):
    """Config-only CLI probe: no agent turn and no MCP server is started."""
    import shutil
    codex = shutil.which('codex')
    if codex is None:
        pytest.skip('Codex CLI not installed; runtime tests still use the fake backend')
    runtime, config = setup
    result = await runtime.realize_change('config-probe', 'slice', 'EDIT')
    assert result['status'] == 'APPLIED'
    generated = json.loads(Path(result['evidence_ref'], 'command.json').read_text())
    overrides = []
    for index, arg in enumerate(generated):
        if arg == '-c':
            overrides.extend([arg, generated[index + 1]])
    probe = subprocess.run([codex, *overrides, 'mcp', 'list', '--json'], cwd=config.repository,
                           capture_output=True, timeout=15)
    assert probe.returncode == 0, 'Generated overrides must pass the real Codex config parser'
    # Captured inventory may include secret environment values; never log it.
    selected = {item['name']: item for item in json.loads(probe.stdout)
                if item['name'] in ('project.server', 'project.http')}
    assert selected['project.server']['enabled'] is False
    assert selected['project.server']['transport']['type'] == 'stdio'
    assert selected['project.server']['transport']['command'] == 'false'
    assert selected['project.http']['enabled'] is False
    assert selected['project.http']['transport']['type'] == 'streamable_http'
    assert selected['project.http']['transport']['url'] == 'https://disabled.invalid/mcp'


async def wait_until(predicate):
    for _ in range(200):
        if predicate():
            return
        await asyncio.sleep(.01)
    raise AssertionError('fixture did not reach expected state')


async def test_explicit_control_partial_duplicate_and_resume(setup):
    runtime, config = setup
    task = asyncio.create_task(runtime.realize_change('active', 'slice', 'PARTIAL_SLEEP'))
    await wait_until(lambda: (config.repository / 'partial.txt').exists())
    for _ in range(2):
        assert (await runtime.cancel_change('active'))['control_status'] == 'requested'
    with pytest.raises(ValueError, match='busy'):
        await runtime.realize_change('second', 'slice', 'EDIT')
    result = await task
    assert result['status'] == 'FAILED' and result['mutation'] == 'partial'
    assert (config.repository / 'partial.txt').read_text() == 'preserved'
    stopped = await runtime.cancel_change('active')
    assert stopped['writer_stopped'] and stopped['context_resumable']
    assert stopped['result'] == result
    corrected = await runtime.realize_change('corrected', 'slice', 'EDIT',
        context_id=result['context_id'], expected_state=result['result_state'])
    assert corrected['status'] == 'APPLIED' and corrected['context_id'] == result['context_id']
    calls = [json.loads(x) for x in (config.repository.parent / 'calls').read_text().splitlines()]
    assert calls[-1][calls[-1].index('resume') + 1] == 'thread-exact-123'
    assert runtime.row('active')['fingerprint'] == digest(['active', 'slice', 'PARTIAL_SLEEP', None, None, None])


async def test_cancel_before_launch_and_other_owner(setup):
    runtime, config = setup
    entered = asyncio.Event()
    async def delayed(*args):
        entered.set()
        await asyncio.sleep(30)
    runtime.run_backend = delayed
    task = asyncio.create_task(runtime.realize_change('early', 'slice', 'EDIT'))
    await entered.wait()
    other = Runtime(config)
    assert (await other.cancel_change('early'))['control_status'] == 'unavailable'
    assert (await runtime.cancel_change('early'))['writer_stopped'] is False
    result = await task
    assert result['mutation'] == 'unchanged'
    settled = await runtime.cancel_change('early')
    assert settled['writer_stopped'] and not settled['context_resumable']
    with pytest.raises(ValueError, match='durable backend identity'):
        await runtime.realize_change('resume', 'slice', 'EDIT', context_id=result['context_id'])
    assert not (config.repository.parent / 'calls').exists()


async def test_completion_wins_cancel_race(setup):
    runtime, _ = setup
    result = await runtime.realize_change('done', 'slice', 'EDIT')
    cancelled = await runtime.cancel_change('done')
    assert cancelled['control_status'] == 'settled'
    assert cancelled['result'] == result and result['status'] == 'APPLIED'


async def test_repeated_caller_cancel_keeps_lock_through_cleanup(setup):
    runtime, _ = setup
    entered, cleaning, release = asyncio.Event(), asyncio.Event(), asyncio.Event()
    async def backend(*args):
        entered.set()
        try:
            await asyncio.sleep(30)
        finally:
            cleaning.set()
            await release.wait()
    runtime.run_backend = backend
    task = asyncio.create_task(runtime.realize_change('cleanup', 'slice', 'EDIT'))
    await entered.wait()
    task.cancel()
    await cleaning.wait()
    task.cancel()
    await asyncio.sleep(0)
    assert not task.done()
    with pytest.raises(ValueError, match='busy'):
        with runtime.locked():
            pass
    release.set()
    with pytest.raises(asyncio.CancelledError):
        await task
    assert runtime.operation_status('cleanup')['status'] == 'FAILED'


async def test_cancel_during_spawn_reaps_process(setup, monkeypatch):
    from semantic_edit_mcp.runtime import spawn_owned
    runtime, _ = setup
    created, release = asyncio.Event(), asyncio.Event()
    actual = asyncio.create_subprocess_exec
    processes = []
    async def delayed(*args, **kwargs):
        process = await actual(*args, **kwargs)
        processes.append(process)
        created.set()
        await release.wait()
        return process
    monkeypatch.setattr(asyncio, 'create_subprocess_exec', delayed)
    with runtime.locked():
        task = asyncio.create_task(spawn_owned(sys.executable, '-c', 'import time; time.sleep(30)',
            start_new_session=True, pass_fds=(runtime.lock_fd,)))
        await created.wait()
        task.cancel()
        release.set()
        with pytest.raises(asyncio.CancelledError):
            await task
        assert processes[0].returncode is not None


async def test_semantic_inspection_fresh_readonly_and_state(setup):
    runtime, config = setup
    edited = await runtime.realize_change('edit', 'slice', 'EDIT')
    result = await runtime.inspect_semantics('What behavior is present?', edited['result_state'])
    assert result['mutation'] == 'unchanged' and result['inspected_state'] == edited['result_state']
    assert result['facts'][0]['sources'] and result['uncertainty']
    args = json.loads((config.repository.parent / 'calls').read_text().splitlines()[-1])
    assert 'sandbox_mode="read-only"' in args and '--ephemeral' in args and 'resume' not in args
    assert runtime.db.execute('SELECT count(*) FROM contexts').fetchone()[0] == 1
    with pytest.raises(ValueError, match='stale'):
        await runtime.inspect_semantics('What behavior?', 'stale')
    with runtime.locked():
        with pytest.raises(ValueError, match='busy'):
            await runtime.inspect_semantics('What behavior?')
    with pytest.raises(ValueError, match='changed during read-only'):
        await runtime.inspect_semantics('INSPECT_MUTATE')
    with pytest.raises(ValueError):
        await runtime.inspect_semantics('MALFORMED')


async def test_stdio_active_control_and_inspection(setup):
    _, config = setup
    params = StdioServerParameters(command=sys.executable, args=['-m', 'semantic_edit_mcp.server',
        '--repository', str(config.repository), '--state-dir', str(config.state_dir), '--codex', config.codex])
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as client:
            await client.initialize()
            pending = asyncio.create_task(client.call_tool('realize_change',
                {'request_id': 'wire-active', 'slice_id': 's', 'specification': 'PARTIAL_SLEEP'}))
            await wait_until(lambda: (config.repository / 'partial.txt').exists())
            cancelled = await client.call_tool('cancel_change', {'request_id': 'wire-active'})
            assert not cancelled.isError
            finished = await pending
            result = json.loads(finished.content[0].text)
            assert result['status'] == 'FAILED' and result['mutation'] == 'partial'
            inspection = await client.call_tool('inspect_semantics',
                {'question': 'Which partial state remains?', 'expected_state': result['result_state']})
            assert not inspection.isError
            assert json.loads(inspection.content[0].text)['mutation'] == 'unchanged'


async def test_inspection_repeated_cancel_keeps_lock_through_cleanup(setup):
    runtime, _ = setup
    entered, cleaning, release = asyncio.Event(), asyncio.Event(), asyncio.Event()
    async def backend(*args, **kwargs):
        entered.set()
        try:
            await asyncio.sleep(30)
        finally:
            cleaning.set()
            await release.wait()
    runtime.run_backend = backend
    task = asyncio.create_task(runtime.inspect_semantics('Which owner?'))
    await entered.wait()
    task.cancel()
    await cleaning.wait()
    task.cancel()
    await asyncio.sleep(0)
    assert not task.done()
    with pytest.raises(ValueError, match='busy'):
        with runtime.locked():
            pass
    release.set()
    with pytest.raises(asyncio.CancelledError):
        await task
    with runtime.locked():
        pass


async def test_inspection_cancel_during_spawn(setup, monkeypatch):
    runtime, _ = setup
    actual = asyncio.create_subprocess_exec
    created, release = asyncio.Event(), asyncio.Event()
    processes = []
    async def delayed(*args, **kwargs):
        process = await actual(sys.executable, '-c', 'import time; time.sleep(30)',
            start_new_session=True, pass_fds=(runtime.lock_fd,))
        processes.append(process)
        created.set()
        await release.wait()
        return process
    monkeypatch.setattr(asyncio, 'create_subprocess_exec', delayed)
    task = asyncio.create_task(runtime.inspect_semantics('Which owner?'))
    await created.wait()
    task.cancel()
    await asyncio.sleep(0)
    task.cancel()
    await asyncio.sleep(0)
    assert not task.done()
    with pytest.raises(ValueError, match='busy'):
        with runtime.locked():
            pass
    release.set()
    with pytest.raises(asyncio.CancelledError):
        await task
    assert processes[0].returncode is not None

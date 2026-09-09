# Semantic implementation MCP

The B workflow lets the parent specify a program change, call an MCP tool, and
rely on its summary until independent slice acceptance. The backend runs local
Codex realization in a persisted thread. Compiler errors, test fixtures, source
reads, and routine repairs stay inside that thread.

[Plugin variants](plugin-variants.md) explains packaging and selecting A or B.
The [proposal](improvement-semantic-edit-tool.md) describes the behavioral target
and deferred clojure-wasm A/B experiment. Selecting that task and measuring
savings remain future work.

## Run the server

Install `uv` and a supported Codex CLI with working local authentication. The
backend was developed against Codex CLI 0.153.4. It uses `exec --json`, a final
JSON output schema, and exact thread-ID `exec resume`. The checked-in `uv.lock`
pins the Python dependencies.

From a checkout or exported B package, launch:

```sh
uv run --frozen semantic-edit-mcp --repository /absolute/project --state-dir /absolute/external-state
```

The repository must be the exact root of a Git worktree. State must live outside
that worktree and belongs to its repository/backend configuration. The server
creates it with owner-only permissions; an existing state directory must be
owned by the current user with mode `0700`. A separate
worktree and state directory are appropriate for each A/B run. The first
operation binds the worktree lock to its state directory; use that same directory
for restarts. Switching state directories cannot bypass an unresolved operation.

The equivalent environment configuration is:

| Variable | Purpose |
| --- | --- |
| `SEMANTIC_EDIT_REPOSITORY` | Required exact target worktree root |
| `SEMANTIC_EDIT_STATE_DIR` | Required external durable state/evidence directory |
| `SEMANTIC_EDIT_CODEX` | Backend executable, default `codex` on PATH |
| `SEMANTIC_EDIT_MODEL` | Backend model, default `gpt-5.6-luna` |
| `SEMANTIC_EDIT_REASONING_EFFORT` | Reasoning effort, default `high` |
| `SEMANTIC_EDIT_TIMEOUT_SECONDS` | Operation timeout, default `1800` seconds |

Command-line flags override these values. Set the model and effort to the
user-selected configuration. The server does not silently substitute an
unavailable model. The backend uses normal execution, workspace-write sandboxing,
no approval escalation, and no shell network access. MCP calls cannot change
that host configuration or broaden the bound repository.

The backend disables plugins, apps, subagent delegation, memories, and web
search. Before execution it enumerates configured MCP server names and disables
each explicitly, including project registrations. Failure to enumerate prevents
execution; raw configuration and credentials are not retained in evidence.
It reuses local Codex authentication. Ordinary user configuration is not loaded;
project instructions and applicable command safety rules remain relevant.
Provider-specific configuration requiring a different backend is not silently
inherited. No commit, push, deployment, or publication is authorized by the
realizer role.

## Compose operations

The parent implements and integrates the slice by choosing one specific edit
per call. Each request states an owner, behavior, constraints, and local completion
condition. Complete slice context is background, not authority to finish remaining
work. The backend returns `BLOCKED` for necessary scope expansion.

The first request establishes an implementation context:

```json
{
  "request_id": "cancellation-1",
  "slice_id": "cancellation",
  "specification": "Worker owns pre-dispatch cancellation observation. Reuse the repository and transaction boundary. Add the observation and return the existing cancelled result. Block if this changes the public dispatch contract.",
  "acceptance": "Observed cancellation prevents executor invocation; ordinary dispatch remains unchanged."
}
```

Pass this to `realize_change`. Subsequent requests use a new request ID and the
returned `context_id` and `result_state` as `expected_state`. The specification
can be a concise delta. A successful operation is complete locally, while the
slice remains unaccepted. Rely on its summary to compose the next operation;
avoid routinely inspecting its patch or rerunning its checks between calls.
Targeted direct reads remain available when needed; semantic inspection is preferred.

A result separates `APPLIED`, `BLOCKED`, or `FAILED` from the mutation disposition
(`unchanged`, `partial`, or `complete`). Verification records contain commands
and outcomes. The server measures the actual repository delta and retains
request, snapshots, CLI events, and final output in its evidence directory.
Snapshot content is retained in a deduplicated blob store so before/after
deltas remain reconstructable without relying on the current worktree.
A malformed backend result or missing passing checks cannot become `APPLIED`.

For a blocker, resolve the stated assumption or authority question and send the
accepted semantic delta in the same context. For acceptance corrections, use
the same procedure. Exact Codex thread reuse retains implementation discoveries;
normal harness compaction preserves thread identity. Automatic replacement of
a lost thread is not implemented. Such a loss is an explicit execution failure
requiring a recovery decision.

## Inspect semantic facts

Call `inspect_semantics(question, expected_state?)` for a bounded question about
existing behavior, interfaces, ownership, state, ordering, or failure boundaries.
For example: “Can failed publication expose a callable before rollback, and which
owner establishes that ordering?” The runtime uses a fresh, ephemeral read-only
context, with the same host-selected model and reasoning configuration. It does
not reuse or alter the editing thread.

The response carries a summary, facts with source-location references and an
observed/inferred distinction, explicit uncertainty, `inspected_state`, and a
private evidence reference. The runtime excludes active writers and checks source
state before and after inspection. A changed worktree invalidates the result;
there is no automatic rollback. Required independent review and the parent's
acceptance decision remain separate. A fresh inspection is not automatically a
whole-slice review, and source references do not independently prove each claim.

## Cancel and steer an edit

`cancel_change(request_id)` targets execution owned by this server. A `requested`
response means cancellation was requested, not that the writer stopped. Await
`realize_change` or retrieve `operation_status` for the settled result and exact
state. The runtime stops the backend process group before recording settlement
and preserves partial edits, evidence, and context identity. Repeated cancellation
requests do not interrupt cleanup or start another writer. If completion wins the
race, the recorded completion remains authoritative.

Once settled, `cancel_change` returns `settled`, the result, and
`context_resumable`. Cancellation before `thread.started` preserves the opaque
context but cannot resume a thread that never became durable; explicitly select
a fresh context in that case. An execution owned by another server instance
returns `unavailable`; the tool does not kill a process from a journal PID.

`steer_change(control_id, request_id, correction)` records one bounded correction
separately from the immutable original request. Identical control retries return
the recorded disposition; changing a control ID's payload is rejected. This CLI
backend has no in-flight steering channel, so active steering returns
`requires_stop_and_resume`, with `delivered: false` and `applied: false`. A settled
target returns `rejected`. It does not silently launch a second edit.

After `requires_stop_and_resume`, cancel the active request, establish settlement,
and send the correction through `realize_change` with a new request ID, recovered
state, and the same durable context when available. Stopping the outer caller wait
alone still does not prove backend cancellation. These tools provide exceptional
control, not a routine supervision loop.

## Recover an interrupted request

A request ID identifies one immutable invocation. Retrying the same ID and
arguments returns its recorded outcome rather than applying the change again.
Reusing the ID with different arguments is rejected.

Use `operation_status(request_id)` after a lost response. When no writer holds
the lock, its `observed_state` supplies the token for explicit recovery. `UNKNOWN`
means the
operation is still running or interruption left its completion unresolved. It
does not mean the tree is unchanged. New work is refused while unresolved
execution may still own the worktree.

The recovery tool `acknowledge_interruption(request_id, expected_state)` records
an interrupted operation as failed only after exclusion of a live writer and
validation of the supplied current state. It never replays the request or resets
the worktree. Preserve useful partial changes; a subsequent correction is a new
request in the existing context when that identity remains available.

The parent should obtain current state from the runtime's status/acceptance
interface or explicit recovery inspection, not guess a token or replace a stale
one automatically. Parent-authorized commits and other known external edits
require deliberate state reconciliation before continuing.

## Accept the slice

Call `slice_summary(context_id, slice_id)` at the completed slice boundary.
The packet aggregates operation outcomes and evidence references for independent
source and behavioral checks. Historical blockers and failures remain visible;
later operations can correct them. Evaluate the final contract, not whether
every historical request succeeded.

The packet is not an approval tool. The parent records slice acceptance in the
owning workflow after independently checking consequential boundaries and
applicable assertions. Send any correction through `realize_change` and accept
the corrected aggregate. An outer Tick or exact-revision gate remains separate
when required by the work package.

## State and evidence limits

Use the worktree exclusively during realization. The runtime serializes its
writers and fingerprints tracked files, nonignored untracked files, the index,
and HEAD. Ignored build outputs are not source-state evidence. Worktrees containing
tracked submodules are rejected because their nested state is not modeled. Concurrent edits by unrelated
processes cannot be reliably attributed, especially when they affect the same
file; a file hash is not a transactional filesystem. Do not run two experiments
against one shared worktree.

The server does not provide rollback or accept a slice automatically. Scope and
semantic conformance are checked at slice acceptance; sandboxing enforces the
host filesystem boundary and does not prove that a design is correct. Evidence
and raw logs stay in the external state directory and may contain repository
content. Keep that directory local to the authorized workflow.

## Verification

Run the deterministic suite from the source checkout (tests are not bundled
in an exported plugin):

```sh
uv run --frozen pytest
```

Tests exercise the MCP transport and a controlled Codex subprocess to establish
context reuse, retry behavior, blockers, partial failures, and state boundaries.
The cancellation/inspection regressions also cover duplicate controls, partial
mutation, completion races, repeated caller cancellation, and subprocess creation.
Run `uv run python scripts/smoke_semantic_inspection.py` for a disposable live
read-only inspection compatibility probe.

The optional live fixture can be run from the source checkout with
`uv run --frozen python scripts/smoke_semantic_mcp.py`. It uses the configured
local Codex authentication and temporary repository/evidence directories.
A live Codex run establishes backend compatibility separately; neither test class
measures savings on the still-unselected clojure-wasm task.

Sources: [Codex non-interactive execution](https://learn.chatgpt.com/docs/non-interactive-mode),
[Agent Plugins MCP configuration](https://agent-plugins.org/plugin-authors/mcp-servers),
and [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk).

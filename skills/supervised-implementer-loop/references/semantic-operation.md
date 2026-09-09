# Semantic Operation Contract

Use the semantic-edit MCP to realize a design in its host-bound Git worktree.
The host selects repository, external state directory, model, and reasoning
configuration. Portable skills contain no host paths or credentials. The runtime
and deployment instructions are described in the plugin's runtime documentation.

## Bound One Edit

The parent implements and integrates the slice. Each `realize_change` request
selects one specific change and states its owner, behavior, constraints, and
local completion condition. Distinguish slice background and acceptance
scenarios from the edit authorized now, including on a short continuation in
an existing context. The tool may adapt source and repair local errors for
that edit; a necessary scope expansion or design contradiction returns to the
parent as `BLOCKED` rather than authorizing subsequent slice work.

For example, adding a typed diagnostic operation using the existing text-value
representation is one edit, even if source, fixtures, and tests span files.
Finishing named types, dispatch, rollback, rotation, tests, and documentation
delegates a package. Judge the selected behavior, not prompt length, file count,
line count, or an obligatory one-function limit. A naturally small slice may
coincide with one edit, but slice readiness is not a substitute for an edit's
local completion condition.

## Execute And Compose

Call `realize_change(request_id, slice_id, specification, context_id?,
expected_state?, acceptance?)`. Use a unique request ID for a new operation.
After a lost response, retrieve status under the recovery section first. If
documented recovery permits resubmitting the original request, preserve its ID
and identical arguments; this is not permission to replay an unresolved writer.
Reusing an ID with different content is an error. Keep the returned context and state
IDs for later operations. Pass acceptance scenarios once or update them when
the accepted contract changes.

The realizer searches, edits, compiles, tests, and repairs failures within the
selected edit. Its compact result supplies changed behavior, relevant interfaces,
checks, and unresolved questions. The parent uses it to update its abstract
understanding of the program and choose the next edit:

- `APPLIED`: operation complete with the stated local checks; independent slice
  acceptance remains pending.
- `BLOCKED`: a semantic decision or authority is needed. Resolve the supplied
  contradiction and issue the accepted delta in the same context.
- `FAILED`: execution did not complete. Inspect recorded status and recover
  partial state rather than assuming no edits occurred.

Mutation state is separate from semantic status. Evidence references identify
private logs and recorded deltas. Prefer semantic facts over fetching raw code, patches, or code-bearing logs,
including for design, recovery, and acceptance. Use the inspection guidance below
to avoid unnecessary implementation detail in the parent context.

## Obtain Semantic Facts

Before a design decision, recovery decision, or acceptance challenge needs code
facts, ask an available read-only semantic inspection capability a bounded
question about behavior, interfaces, ownership, state, ordering, or failure
boundaries. State the decision the answer must support and the relevant scope.
For example: “Can failed publication expose a callable before rollback, and
which owner establishes that ordering?” Prefer a focused answer to a source dump.

Require compact source-grounded facts, source-location references for traceability,
the inspected revision or worktree state, and explicit uncertainty or missing
coverage. Keep observed behavior distinct from inference and proposed changes.
Prefer responses without raw code, diffs, or code-bearing logs. Include a bounded
excerpt when it materially helps resolve the question.
Inspection authorizes no mutation, repair, acceptance, or second writer. Evidence
from a changing or unresolved worktree cannot establish settled current state.

An independent reviewer may inspect code and answer these questions under its
read-only authority. At acceptance, use evidence independent of the editing
context; another self-report from that context is insufficient. The parent
retains the design and acceptance decisions and requests further evidence when
claims conflict or required coverage is unknown. A bounded inspection question
during implementation does not create a new slice gate or outer Tick.

Check actual capability availability. This contract does not introduce a tool
name or claim that the installed MCP offers semantic inspection. If neither an
appropriate inspection tool nor an authorized independent reviewer is available,
report the capability gap and use a targeted direct read when needed to progress.
Direct parent code reads are permitted, including when semantic evidence is
insufficient or a precise detail matters; keep them bounded to the decision and
avoid routine replay of successful edits. Missing inspection capability alone is
not a blocker. Preserve uncertainty when evidence remains insufficient, and keep
required reviewer independence. An edit call is not a read-only inspection path.

## Accept A Slice

Call `slice_summary(context_id, slice_id)` when the accumulated slice is ready.
It returns the operation summaries and evidence references bound to the resulting
state. This is a read-only aggregate packet, not self-approval. An independent
reviewer checks behavior, source boundaries, and applicable assertions and returns
semantic evidence, normally without raw code. The parent evaluates that evidence and can
challenge specific claims through further inspection questions.
Send any resulting semantic correction through the same context; review the
corrected aggregate at acceptance rather than every corrective tool call.

Parent-authorized commits or unrelated external edits can change the expected
state. Reconcile that explicit boundary before issuing more work; do not blindly
replace a stale state token just to force an operation through.

## Control An Active Edit

When the user changes direction or the parent detects incorrect scope, stop
issuing dependent edits and inspect the available control capabilities. If
steering is supported, address a bounded correction to the active request in
the same context and require a result saying whether and when it took effect.
Sending another realization request is not steering, and changing a recorded
request's immutable payload is not an allowed retry.

If steering is rejected or requires stop-and-resume, use supported cancellation
for that request. Distinguish cancellation requested from writer stopped;
require settlement evidence and exact current state before recovery and a new
bounded request. Preserve partial work, context identity, evidence, and writer
exclusion. Cancellation does not imply rollback. If completion wins the race,
use the recorded completion result rather than claiming cancellation.

These instructions do not assert that the installed runtime provides either
capability. If the needed control is unavailable, report the limitation, avoid
claims of successful steering or cancellation, and use the documented status
and recovery path once the writer settles. Terminating an outer wait does not
establish backend cancellation. `UNKNOWN`, unknown mutation, a missing state,
or a busy worktree leaves settlement unresolved; do not acknowledge interruption,
start a second writer, or bypass its lock. Interruption acknowledgment records
recovery after the writer stops; it does not stop the writer.

Control and status recovery are exceptional paths, not a per-edit supervision
or polling loop. Resume with a new request ID and the recovered state only after
the previous writer is known to have stopped.

## Recover Without Replaying

Use `operation_status(request_id)` after a lost response to retrieve the known
outcome. A completed request returns its stored result without reapplying edits.
An in-flight or interrupted request is not permission for a second writer.
Follow the runtime's recovery tool only after it establishes that the previous
writer is stopped and the current state matches the recovery decision.

Use the worktree exclusively while realization is active. The runtime excludes
its own concurrent writers and checks repository state; it cannot reliably
attribute arbitrary edits by another process in the same files. It preserves
partial changes and does not automatically reset the tree. No operation grants
commit, push, deployment, or broader filesystem authority.

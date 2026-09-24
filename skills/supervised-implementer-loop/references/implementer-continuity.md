# Implementer Continuity

Use this reference with the
[delivery-package authority](contract-and-scenario-package.md) when an
implementation work package may outlive one useful context. It defines
selection, context lifetime, and renewal; it does not define another contract
matrix, delivery-package record, review phase, or fixed-point result.

Read [selection](#select-the-implementer) at setup. Use the
[continuity sequence](#executable-continuity-sequence) when crossing packages or
reliability is in doubt, [missed events](#handle-a-missed-event) after the agreed
stall deadline, and [exceptional recovery](#exceptional-stop-and-rebaseline)
when the active course must stop.

## Local terms and authority

Carry the record selected by [admission depth](contract-and-scenario-package.md#choose-admission-depth):
for bounded delivery, use the accepted brief, its revision, and established
outcomes wherever the formal route carries map, plan, and contract identities.
Renewal does not require upgrading a bounded brief into formal plan review.

- A **continuity mode** records whether the caller explicitly requires an
  identity or only a role and exact runtime configuration. `identity-persistent`
  means that the required identity may not be replaced without explicit
  permission; an agent name alone does not select this mode.
  `role/model-persistent` is the default: a fresh context may be used at an
  authorized boundary while preserving the selected role, model, reasoning
  effort, and normal or fast mode.
- A **persistence interval** is the lifetime of one active implementation
  context through one admitted delivery package, its corrections, and parent
  acceptance. At that boundary the parent may begin another interval with the
  same context or authorize a fresh one; renewal is considered only after the
  accepted boundary.
- A **turnover envelope** is a compact, parent-verified view over existing
  package, plan, goal, tree, configuration, and evidence records. It is a
  handoff reference, not a second package or contract ledger.
- A **context-health disposition** is one of `continue`,
  `renew-at-boundary`, or `stop-and-rebaseline`. It is a capability-aware
  workflow decision, not a numeric context or compaction threshold.

The delivery-package reference remains authoritative for package identity,
contract mapping, useful stopping points, admission, closure, and acceptance.
Only parent acceptance of an admitted delivery package is an ordinary renewal
boundary. A generic owner checkpoint, design checkpoint, or internal step is
not eligible unless the reviewed delivery map admits it as a delivery package.

There is exactly one active implementation writer. A renewal retires the old
context before starting one fresh context; it never overlaps implementation,
review, or Git writes. The parent remains responsible for admission,
independent inspection, correction, acceptance, and authorization.

## Executable continuity sequence

### 1. Establish the caller's continuity policy

At package setup, apply explicit caller requirements and otherwise use the
configured implementer with `role/model-persistent` continuity. This supplies
standing authority for initial spawning and same-configuration respawning
within the authorized work; do not ask the user to confirm routine lifecycle
actions. Record:

- implementer identity, when the caller explicitly requires preserving it;
- model, reasoning effort, and normal or fast execution mode;
- continuity mode and who may authorize replacement;
- the admitted delivery-package map, plan identity, and goal identity;
- the next safe turnover boundary; and
- the shared artifact location for evidence that must survive renewal.

When the caller has not required a particular identity, a fresh context is
permitted only if the runtime can actually preserve the selected model,
reasoning effort, and execution mode. Do not silently substitute any of them.
If the runtime cannot provide the authorized configuration, renewal is
unavailable: continue in the current context when it remains trustworthy, or
stop and ask for the required rebaseline or replacement authority.

At a parent-accepted delivery-package boundary, exercise that standing authority
by recreating the implementer with the exact recorded configuration. The same
authority covers exceptional recovery after writer settlement and parent
rebaseline below. Ask only when an explicit identity restriction, configuration
change, or scope expansion needs new authority. Lifecycle authority does not
expand permission to edit, commit, publish, or perform external actions.

Do not add turnover ceremony to a small package expected to finish in one
coherent context.

### 2. Run one package in one active context

Give one active implementer the complete admitted delivery-package assignment
once. Keep it active through the package's internal steps, focused checks,
handoff, parent corrections, and acceptance. Corrections remain delta-only;
the parent does not resend the package map or create a replacement for an
ordinary correction.

Carry the complete delivery-package map only as sequencing context. Assign one
current parent-acceptable package; do not ask the implementer to complete later
unaccepted packages in the same assignment. Admit the next package only after
the parent accepts the current one.

Queue a delta to an active turn. Trigger a new turn only when the implementer
is idle and a substantive correction or accepted boundary is ready. Do not use
status-only turns as a substitute for a continuity decision. No other
implementation writer edits the shared tree, and Git writes remain serialized.

### 3. Observe and choose a disposition

Use available runtime observations together with behavior and current-tree
evidence. Useful observations include compaction or retained-prefix behavior,
repeated broad reinspection, reconstructing already supplied context, or
omitting accepted adjacent contracts. These observations are diagnostic only:
compaction alone does not fail a package, and no invented number establishes a
renewal or failure decision.

Choose exactly one disposition:

- **`continue`** — the current context remains coherent and trustworthy enough
  to finish the admitted package and its ordinary corrections.
- **`renew-at-boundary`** — pressure is material, but accepted state remains
  trustworthy. Finish the current admitted delivery package, obtain parent
  acceptance, and prepare renewal before starting the next package.
- **`stop-and-rebaseline`** — accepted state is contradicted or no longer
  carried reliably, or the current course is otherwise invalidated. Stop
  implementation deltas and use the recovery procedure below. This is not an
  ordinary mid-package renewal.

Correctness must remain decidable when the runtime exposes no telemetry. In
that case, use behavioral evidence, accepted package records, and bounded tree
inspection; do not invent a timer, size limit, or savings claim.

### 4. Finish and accept before ordinary renewal

For `renew-at-boundary`, finish the current admitted delivery package. The
parent independently verifies the ordinary acceptance packet, current
realization dispositions, changed owners, focused checks, and remaining risks.
A context-health observation does not waive any package closure requirement;
SIL does not select or redivide delivery boundaries locally.

Do not begin the next delivery package in the context selected for retirement.
If parent acceptance fails, send a delta correction to that same context while
it remains active, or use `stop-and-rebaseline` if its continuity is no longer
trustworthy.

### 5. Externalize evidence and verify the turnover envelope

Before retiring the old context, ensure every fact needed after renewal is in a
shared, accessible artifact or existing accepted record. Successful raw logs
need not be copied; a bounded result and durable evidence location are enough.
Evidence that exists only in the retiring context must be externalized before
renewal can proceed.

The parent verifies this compact envelope against the current tree and the
existing authoritative records:

```text
Turnover envelope
  goal ID and direct-scenario status
  plan identity and current accepted delivery-package map
  last parent-accepted delivery package and established contract IDs
  exact revision, or base revision plus bounded dirty-tree state
  continuity mode, required identity, role/model/reasoning/execution config,
  replacement authority
  next admitted delivery package and its accepted prerequisites
  material decisions or rejected approaches not represented elsewhere
  unresolved risks, blockers, and shared evidence locations
```

The envelope references the accepted delivery-package packet and map rather
than copying their contract or closure fields. The outgoing implementer may
provide deltas or point to evidence, but its summary is not authoritative.
The parent verifies material claims, reachability of shared evidence, and the
absence of an overlapping writer before retiring the context.

### 6. Renew once, without replay

For an authorized `role/model-persistent` renewal, retire the old context and
start exactly one fresh implementer with the same selected role, model,
reasoning effort, and execution mode, without asking again. In Codex, use
`agent_type: "implementer"` and `fork_turns: "none"` for the default role.
Give it the verified turnover envelope, the current accepted package map,
and the next admitted package as one
complete bounded assignment. Later communication is delta-only.

The old context is historical evidence, not a fallback or comparison path. Do
not reactivate it, ask both contexts to implement, or have either context
rework the same package. Renewal does not add a reviewer phase or a Tick.

For `identity-persistent` continuity, report the evidence and obtain the
required explicit authorization before replacing the named identity, including
when the context has become unsafe or unavailable. No context-health signal
silently broadens that authority.

## Exceptional stop and rebaseline

When `stop-and-rebaseline` is selected, stop issuing implementation deltas.
Request interruption when the active course must stop, then obtain lifecycle
evidence that the active turn and writer-owned subprocesses or cleanup have
settled. A timeout or interrupt acknowledgement alone does not prove settlement.
Do not inspect/replay the mutable handoff state or start a replacement writer
until settlement is established. If settlement cannot be established, preserve
the known state and do not overlap writers.

The parent inspects the bounded dirty tree and shared evidence without relying
on an untrustworthy outgoing summary. Starting from the last parent-accepted
delivery package, classify observable work as:

- **accepted** — already covered by parent acceptance;
- **complete-but-unaccepted** — plausibly complete but not yet accepted;
- **partial** — edits or evidence that do not close the current package; or
- **obsolete** — invalidated by an accepted decision or the rebaseline.

Preserve useful edits and evidence. Do not discard them merely to obtain a
clean conversational restart, and do not treat complete-but-unaccepted work
as accepted. The parent records the invalidated assumption and selects the
smallest recovery boundary. For the default continuity mode, the parent may
respawn with the same configuration and scope without another user approval;
obtain new authority only for an explicit identity restriction or a required
configuration or scope change. A fresh context receives a new complete bounded
assignment only after that rebaseline and any applicable package admission
remain valid.

## Acceptance backstops

Before ordinary renewal, verify all of the following:

- the current delivery package is parent-accepted, not merely at a checkpoint
  or internal step;
- exactly one writer was active and all Git writes were serialized;
- required configuration and continuity authority are explicit and preserved;
- the turnover envelope is a verified composition of existing records rather
  than a second ledger;
- required post-renewal evidence is reachable outside the retiring context;
- the fresh context will receive one complete assignment followed by deltas,
  with no parent conversation history; and
- no reviewer lifecycle, Tick/Tock, or independent-review authority changed.

For exceptional recovery, also verify that the dirty-tree classification,
invalidated assumptions, preserved edits, and rebaseline authority are recorded
before any new implementation delta.

## Select the implementer

Use the installed `implementer` role: `gpt-5.6-luna` with `max` reasoning.
Its [role file](../assets/implementer.toml) owns the child's execution process.
Explicit task or repository choices override this default; honor applicable
memory instructions without reopening an already resolved selection. Use normal
execution unless fast mode is explicitly requested.

In Codex, explicitly pass `agent_type: "implementer"` and `fork_turns: "none"`
on the initial spawn and every respawn. The role fixes model and reasoning, so
do not pass conflicting model overrides. For an explicitly different configured
role, select that role with the same history-free spawn. An explicit configuration
without a matching role uses the runtime's model and reasoning fields and the
bundled execution instructions instead of a conflicting named role. The complete assignment
supplies task context; configuration, repository instructions, and the available
skill catalog still apply. Keep subsequent messages delta-only in the same child.

Register the bundled regular file through `agents.implementer.config_file`;
use the repository's [role registration procedure](../../../README.md#codex-implementer-role).
The plugin supplies the role contents; the configuration entry makes it
discoverable without a separate copy or symlink.
If the role is unavailable in the current tool catalog, do not send an undeclared
parameter. For this same authorized configuration, start a history-free child
with explicit Luna Max settings and instruct it to read the bundled role's
execution process once. If the runtime cannot provide the required configuration,
report that concrete blocker instead of silently changing models.

Other harnesses use their named-role and clean-context equivalents, or the same
explicit configuration and bundled execution instructions. Apply the default
[continuity policy](#1-establish-the-callers-continuity-policy) without a separate
approval prompt. Read recovery details only when crossing packages or context
reliability requires a decision.

## Handle a missed event

Use this procedure after a promised event misses the agreed stall deadline, or
when concrete safety, scope, or lifecycle evidence warrants intervention.

### Bound recovery attempts

A missed event does not by itself invalidate the implementer or its edits. After
the first missed milestone, allow at most one recovery turn when the narrow
check below still supports `continue`. Bound that turn to restoring the promised
checkpoint or handoff; it is not another open-ended correction cycle.

Select `stop-and-rebaseline` if that recovery:

- misses its promised event;
- leaves source that does not parse or compile;
- broadens failures outside the assigned owner;
- omits acceptance evidence it claims to have completed; or
- requires the parent to repair implementation before acceptance.

Do not send another correction to that context. Settle the writer and its
subprocesses, classify the preserved dirty tree, and choose the smaller capable
completion route: finish locally when the remaining correction is small and
bounded, or respawn the same authorized configuration with `fork_turns: "none"`
from the verified rebaseline envelope.

Exhausting this recovery budget invalidates the supervised communication
channel, not the correctness or usefulness of the preserved edits. A timeout or
its count still does not establish an implementation defect.

1. Make one narrow check that can change the decision. A timeout or its count
   alone is not evidence of a stall.
2. After that check, send at most one status request. Queue substantive deltas
   to an active turn; trigger a new turn only when it is idle and work is ready.
3. Interrupt at most once when the course is unsafe, invalidated, or credibly
   stalled. Establish writer and subprocess settlement before inspecting stable
   partial edits or resuming work; an interrupt acknowledgement is insufficient.
4. Resume with a delta when disposition remains `continue`, or when
   `renew-at-boundary` still permits safe completion of the current package.
   Otherwise follow [exceptional stop and rebaseline](#exceptional-stop-and-rebaseline).
   Avoid repeated status-only turns.

When telemetry is available, distinguish raw input, cached reads/writes, and
newly appended context. Do not infer savings from a timeout duration or invent
runtime behavior when telemetry is absent.

# Implementer Continuity

Use this reference with the
[delivery-package authority](contract-and-scenario-package.md) when an
implementation work package may outlive one useful context. It defines
context lifetime and renewal; it does not define another contract matrix,
delivery-package record, review phase, or fixed-point result.

## Local terms and authority

- A **continuity mode** records whether the caller requires a particular
  identity or only a role and exact runtime configuration. `identity-persistent`
  means that a named implementer may not be replaced without explicit
  permission. `role/model-persistent` means that a fresh context may be used at
  an authorized boundary, but it must preserve the selected role, model,
  reasoning effort, and normal or fast mode.
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

At package setup, record the caller's exact requirements for:

- implementer identity, when one is named;
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

Recording `role/model-persistent` continuity is standing renewal authority for
the recorded work-package scope unless the caller explicitly limits it. At a
later parent-accepted delivery-package boundary, exercise that existing
authority by recreating the implementer with the exact recorded configuration;
do not stop to request the same permission again. Ask only when identity,
configuration, or authorized scope must change.

Do not add turnover ceremony to a small package expected to finish in one
coherent context.

### 2. Run one package in one active context

Give one active implementer the complete admitted delivery-package assignment
once. Keep it active through the package's internal steps, focused checks,
handoff, parent corrections, and acceptance. Corrections remain delta-only;
the parent does not resend the package map or create a replacement for an
ordinary correction.

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
reasoning effort, and execution mode. Give it the verified turnover envelope,
the current accepted package map, and the next admitted package as one
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
The parent inspects the bounded dirty tree and shared evidence without relying
on an untrustworthy outgoing summary. Starting from the last parent-accepted
delivery package, classify observable work as:

- **accepted** — already covered by parent acceptance;
- **complete-but-unaccepted** — plausibly complete but not yet accepted;
- **partial** — edits or evidence that do not close the current package; or
- **obsolete** — invalidated by an accepted decision or the rebaseline.

Preserve useful edits and evidence. Do not discard them merely to obtain a
clean conversational restart, and do not treat complete-but-unaccepted work
as accepted. The parent records the invalidated assumption, selects the
smallest recovery boundary, and obtains any required identity or configuration
authority before resuming. A fresh context receives a new complete bounded
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
- the fresh context will receive one complete assignment followed by deltas;
  and
- no reviewer lifecycle, Tick/Tock, or independent-review authority changed.

For exceptional recovery, also verify that the dirty-tree classification,
invalidated assumptions, preserved edits, and rebaseline authority are recorded
before any new implementation delta.

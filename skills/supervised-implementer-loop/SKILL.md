---
name: supervised-implementer-loop
description: >-
  Implement one non-trivial work package through ordered, dependent slices
  composed of specific semantic edits, using one active implementation context
  at a time while the main agent independently reviews, corrects, validates,
  and accepts each slice. Reuse that context through an admitted delivery
  package and its corrections; an authorized renewal may start the next
  package with the same configuration.
  Use when the user asks to reuse one implementer, review every implementation
  slice, make later work rely on accepted earlier fixes, or keep implementation
  token-efficient. Do not use for review-only work, small direct edits, or
  genuinely independent parallel packages.
---

# Supervised Implementer Loop

Complete one bounded work package through a repeated implement-review-correct
loop. The main agent is the acceptance authority; one active implementation
context owns the edits and first-pass validation at a time.

This skill returns when its assigned work package is implemented and accepted.
The primary follows [request completion and runtime goals](references/request-completion.md)
at establishment and acceptance boundaries: a completed edit or leaf package
does not end a larger authorized request. This skill does not initiate broader
reviews, invent adjacent work, or take completion authority from an outer owner.

When an outer fixpoint workflow invokes this skill for remediation, return the
accepted package to that orchestrator. Delivery-package acceptance proves the
Tock package, not an independent whole-scope Tick; do not reuse the implementer
as the fixed-point reviewer.

## Establish The Work Package

Read
[references/contract-and-scenario-package.md](references/contract-and-scenario-package.md)
before routing admitted delivery packages. Build its contract-first package
matrix from stable contract IDs and keep it as the package's requirement
authority.

Use that reference's delivery-package record and map-admission sequence before
implementation work. The reference owns package fields, bidirectional contract
mapping, useful stopping points, closure, split/combine decisions, and
internal-step treatment. This entrypoint only establishes the caller-authorized
work package, consumes the reviewed plan decision, and routes admission and
execution.

When the work package may cross an accepted delivery-package boundary, also
read [references/implementer-continuity.md](references/implementer-continuity.md).
It owns continuity mode, context-health dispositions, turnover-envelope
verification, fresh-context assignment, and exceptional recovery. It does not
replace the delivery-package record or add a review phase.

Consume the durable result and plan identity from the
[review-fixpoint contract boundary](../review-fixpoint/references/contract-and-evidence-boundary.md).
Before spawning or allowing production edits, require a current
`implementation-plan-fixed-point` for unchanged plan-owning content and
dependencies, with every plan cell cleared. A missing, contract-only, stale,
invalidated, changed, or unknown plan result stops admission; checkpoints do
not establish plan readiness and this entrypoint does not invent unresolved
package boundaries.

Apply the shared
[behavioral design trace and rebaseline authority](../evidence-efficient-review/references/behavioral-design-trace.md)
through that package reference. Carry its stable package-level goal record from
establishment through slice and package acceptance.

At the existing pre-edit, handoff, and parent-acceptance boundaries, consume
the reference's realization disposition for each contract in the admitted
delivery package. The reference owns its dimensions and closure rules. Before
production edits, require a concrete feasible plan for every applicable
capability, information, transaction, scenario/assertion, and design-
dependency cell; at handoff, require actual source and assertion evidence in
place of the plan. Missing, unproved, or stale coverage blocks the current
decision. Affected design dependencies must be reconciled before continuation,
and plan-owning changes follow the existing review-fixpoint invalidation rule.

Before spawning, resolve glossary state through the
[project-glossary authority](../clear-technical-writing/references/project-glossaries.md).
Record either the explicit opt-out marker alone or, for a selected glossary,
its source, declared-scope fit when applicable, and only the material term-to-
semantic-source relationships and unresolved candidates in the work package.
Glossary wording is explanatory input; package contracts and technical owners
retain semantics.

1. Inspect the current tree, user-supplied requirements, repository guidance,
   and existing changes. Begin at the first unmet requirement and preserve
   unrelated user work.
2. State the package outcome, complete matrix rows, admitted delivery-package
   map and plan identity, explicit non-goals, evidence lanes, and authorization
   or commit boundaries.
3. Put private representation, fields, plumbing, and numeric defaults in the
   conditional implementation appendix unless a row states why correctness
   requires them.
4. Validate and consume the admitted, independently reviewed, ordered
   delivery-package map. Do not divide matrix rows, regroup contracts, or
   create package boundaries locally after admission. Keep grouping,
   split/combine decisions, and dependency order in the reviewed plan. If a
   boundary is missing, invalid, or no longer closes a useful behavior, return
   to the plan-review owner instead of inventing one locally. Apply the
   reference's structural profile to each admitted delivery package and
   preserve the invariants on which later packages rely.
5. Keep uncertain decisions local and reversible. Ask only when a missing
   choice would materially change behavior, architecture, risk, or scope.

When the package explicitly includes modularization or physical decomposition,
apply the reference's residual-topology inventory to every affected root. Carry
the initial inventory through slice planning and compare it with the final root
before package acceptance. Batch related state, operations, transaction
handling, ABI adaptation, and tests at meaningful owner boundaries. Include the
requested stateful and transactional architecture work in those boundaries
rather than using easy stateless extractions as a proxy for package completion.

## Select The Implementer

Before spawning an implementer:

1. Consult available memory according to the environment's memory instructions
   for repository-, task-, and user-specific model and reasoning preferences.
   Keep the lookup narrow. Current user instructions override memory.
2. Confirm that the remembered or explicitly requested model is currently
   available and appropriate for the package. Do not silently substitute a
   different model.
3. If model or reasoning selection remains unclear, conflicting, stale, or
   unavailable, explicitly ask the user what configuration to use before
   spawning. Do not guess.
4. Prefer the leanest capable implementation model consistent with the clear
   selection, paired with enough reasoning effort for principled owner-level
   work. A lean model such as Luna with high or maximum reasoning can be an
   effective implementation choice when current availability and remembered or
   explicit preferences support it.
   When the user supplies or current capabilities establish a material cost
   asymmetry, record it without inventing prices and prefer the cheaper capable
   implementation owner for exhaustive mechanical and evidence-producing work.
5. Use normal, non-fast execution by default. Enable fast mode only when the
   user explicitly requests fast mode for the current task; never infer it from
   memory, model choice, urgency, or token-economy instructions.

Select exactly one active implementation context at a time. Apply
[implementer-continuity.md](references/implementer-continuity.md): retain the
context through the current admitted delivery package and its corrections, and
consider renewal only after parent acceptance of that package. If continuity
is `identity-persistent`, report loss and ask before replacing the named
implementer. If it is `role/model-persistent`, renew only through the verified
envelope and only when the runtime preserves the required configuration.
Treat that mode's caller authorization as standing authority for the recorded
work-package scope: recreate the implementer with the same role, model,
reasoning effort, and execution mode at later accepted boundaries without
asking again. Ask only if the caller limited the authorization or identity,
configuration, or scope must change.

## Give The Initial Assignment

Give the implementer enough context once:

- the work-package outcome and complete accepted delivery-package map with its
  current plan identity, provided once;
- the stable behavioral goal record and current direct scenario status;
- the current delivery package's contract IDs and scenario-portfolio entries;
- the complete realization disposition for those contract IDs, carried once as
  defined by the package reference;
- architectural owners, invariants, and dependency direction;
- any applicable structural baseline and the current delivery package's
  intended source destination;
- the current residual-topology inventory when the package includes physical
  decomposition;
- accepted existing behavior that must not regress;
- explicit non-goals and prohibited plastering fixes;
- evidence class, shared capture helpers, localization signals, external
  evidence status when applicable, and reporting format;
- known architectural follow-up IDs and the authority boundary for any ledger
  mutation;
- the explicit glossary opt-out marker alone or, for a selected glossary, its
  source, declared-scope fit, and the material term-to-semantic-source
  relationships and unresolved candidates, without copying the glossary; and
- the continuity mode, required identity when applicable, exact model,
  reasoning effort, execution mode, replacement authority, context-health
  disposition, and shared evidence location; and
- the progress envelope: expected duration class, milestones the implementer
  reports without prompting, immediate blocker conditions, the first credible
  stall threshold, and any intermediate decision the parent must make; and
- whether the implementer may commit.

Under an explicit opt-out, instruct the implementer not to ask another
placement question, access a glossary, calculate or carry scope fit or glossary
candidates, or persist a term later in the package. Keep needed concept
explanations local to the artifact.

Explicitly instruct the implementer to use tokens economically without
weakening correctness: inspect only relevant owners and adjacent consumers,
avoid repeating supplied context, communicate concise deltas, run focused
checks during iteration, and report only changed files, verification, and
material unresolved concerns.

Keep verbose logs, normalized comparisons, symbol inventories, and
intermediate evidence with the implementer or in a temporary or explicitly
authorized evidence artifact. The implementer's handoff should reference that
artifact instead of pasting successful logs or complete files.

Use the smallest context fork that still carries the requirements and current
repository state. Do not repopulate the active context on later slices. A fresh
context, when authorized at an accepted boundary, receives the verified
turnover envelope and next admitted package once rather than a transcript or
raw-log replay.

## Compose Specific Semantic Edits

The complete delivery-package map supplied to the implementer is context and
an authority boundary. It does not authorize the implementer to execute every
edit in that map. The parent selects the currently named edit inside the
admitted delivery package. Each assignment names:

- the semantic owner and the required behavior or interface result;
- accepted prerequisites and the current state on which the edit may rely;
- constraints, dependencies, ordering, transaction or recovery guarantees,
  and permitted implementation freedoms;
- explicit exclusions, including later edits, unrelated cleanup, and package
  or design decisions that remain with the parent; and
- local completion evidence: the owner-level invariant, focused scenarios or
  assertions, and checks that must pass for this edit.

One semantic edit may span several files when they jointly realize that
behavior. Choose the boundary by responsibility, behavior, and local evidence;
do not impose a numeric size, line-count, file-count, or duration limit. The
implementer resolves source details and performs source, fixture, import, and
compiler adaptation plus repairs directly caused by the assigned edit. It does
not choose later edits, reorder the admitted package, or expand the package
contract.

Require a compact result for every edit: outcome; attributed changed paths and
owner or interface delta; local checks and scenarios; the evidence phase for
each check (expected reproduction or final verification); and unresolved
questions or risks. Establish the assignment baseline before editing so
inherited dirty state, same-file edits, and concurrent or ambiguous attribution
are reported rather than credited automatically. Local completion is separate
from delivery-package acceptance: zero selected tests, stale passes, adjacent
success, or missing required assertions do not establish it. Any out-of-scope
change is never credited to the edit or package; classify it explicitly and
have its authorized owner resolve it before acceptance.

After a successful edit, use that result as the parent's working premise for
selecting the next edit. Do not routinely reread its implementation, patch, or
successful logs between edits. A targeted parent read remains allowed when it
answers a concrete design or acceptance question, resolves contradictory
evidence, or investigates attribution or scope.

## Design Tests To Survive Simplification

Use the reference's scenario portfolio, evidence lanes, and test-stability
rules. Each slice should use a small set of observable scenarios, not an
assertion inventory. Reuse capture helpers without promoting their private
fields into the contract. Keep deterministic acceptance independent from
credential availability and report external capability and composition
statuses separately.

## Reconcile Specification And Complexity

Use the shared behavioral-design authority when literal specification choices
or cumulative slice evidence trigger its aggregate comparison. The implementer
supplies the goal trace, mechanism derivations, and comparison with the smallest
faithful alternative. The parent may accept a mechanism-only constructive
rebaseline within package authority. A behavioral contract change requires
acceptance by the named product authority. After the applicable acceptance,
update the owning contract once and resume design-sensitive work at the
corrected boundary, carrying forward unaffected evidence.

Apply the
[economic actionability authority](../evidence-efficient-review/references/economic-actionability.md)
only when a defensive requirement would add or preserve product machinery or
lasting mechanism-coupled tests. Use the package reference for exact-limit
justification.

## Route Architectural Scope Decisions

When implementation or parent review exposes non-local impact, uncertain
ownership, mechanism-coupled tests, physical source structure that may hide
distinct responsibilities, or a local fix that may preserve an architectural
problem, read
[references/architectural-scope-decision.md](references/architectural-scope-decision.md)
completely. Do not infer an architecture defect from effort or file count.

The primary supervisor qualifies the signal, bounds the proper correction, and
accepts one of the reference's four branches within the caller-approved
package. The implementer supplies evidence and a proposal but has no acceptance
or scope-expansion authority. If no bounded non-worsening route fits, stop for
the caller's scope decision before production changes.

Record a repeated architectural-mismatch trigger when the same accepted owner
or design assumption fails again; no numeric threshold is required. Pause
further design-sensitive edits and require a concrete design checkpoint before
resuming: the intended owner, producer and consumer information flow, state and
lifetime, ordering or transaction boundary, failure and recovery path, and
decisive source or behavior evidence. If that checkpoint cannot be accepted
within the current authority, return to the architecture or package owner
instead of dispatching another local correction.

Do not accept a safe-deferral branch until the current contract passes, every
applicable non-worsening disposition is proved, and the authorized durable
follow-up is read back. External or otherwise separately controlled ledger
writes require their own authorization. Preserve the resulting decision record
and follow-up delta for slice and package handoff.

## Run Each Delivery Package

For every admitted delivery package:

The package reference owns the realization-disposition schema. At the existing
pre-edit boundary, this entrypoint consumes the complete relation and refuses
production edits when an applicable row lacks a concrete feasible plan or is
missing, unproved, or stale. The initial assignment carries the relation once;
later handoffs and corrections carry only changed dispositions and affected
contract IDs. The acceptance packet replaces planned entries with actual
source and assertion evidence, and parent acceptance consumes the current
relation before deciding the package. Adjacent success, a broad gate, names,
or an implementer summary cannot satisfy an unresolved row.

1. Send the delivery package to the active implementation context. After the
   initial assignment, use follow-up messages containing only new requirements,
   evidence, and corrections. Do not replace that context for an ordinary
   correction.
2. Let the implementer perform the assigned semantic edit and run focused
   validation. Do not perform
   overlapping writes or Git operations in the shared workspace. Non-mutating
   preparation may continue, but formally review only a completed delivery
   package. At handoff, planned realization entries are replaced with actual
   source and assertion evidence; a design change marks dependent entries
   stale before continued work or acceptance. The result must distinguish
   expected pre-fix failures from final checks and must attribute changes
   against the assignment baseline.
3. Require a compact delivery-package acceptance packet: changed paths and
   resulting owner boundary; contract IDs established; intended behavior or
   interface changes, or an explicit statement that none were intended;
   exceptions from mechanical equivalence; material structural delta when a
   profile applies; the goal ID and direct scenario's behavioral status;
   mechanism progress stated separately; checks and scenario results with
   pass/fail status; unresolved risks or blockers; and the detailed-evidence
   location. For a modularization package, include the residual-topology delta
   and disposition of every affected material cluster. Include the current
   realization disposition, or only its changed entries after the initial
   assignment, and identify any unresolved row. Include affected-test,
   external-evidence, architectural-decision, and follow-up dispositions only
   when they apply. For a selected glossary, also include changed or still-
   material scope-fit and candidate dispositions; under opt-out, include only
   the marker. Preserve the original failure and any cleanup failure as
   separate evidence. Label observed facts, hypotheses, and runtime witnesses
   separately; a plausible explanation is not an execution witness. The
   implementer does not approve its own work.
4. Independently inspect the packet, changed owner topology, and the few
   boundaries where defects would be consequential. For a modularization
   package, verify that each extracted module is cohesive, the root lost the
   corresponding responsibility rather than retaining an operational copy,
   every material residual cluster has an explicit disposition, and central
   state, transaction, lifecycle, or ABI work was designed rather than skipped
   as non-mechanical. Prefer normalized
   extraction comparisons, symbol and visibility inventories, forbidden-
   dependency searches, narrow changed ranges, and focused witnesses selected
   independently from the implementer's checks over complete moved-body or log
   rereads. Expand inspection when evidence is contradictory, incomplete, or
   implausible. For a routed architectural
   decision, verify its causal evidence, correction bound, branch, and durable
   follow-up read-back. At parent acceptance, select a few high-risk probes
   independently at those consequential boundaries. Do not accept the
   implementer's summary as evidence by itself.
   Before dispatching corrections aimed at package acceptance, consolidate one
   bounded inspection of every changed owner, affected consumer, and material
   residual-topology cluster. Sequence the corrections from that complete
   finding set and its dependencies instead of dispatching a new correction
   after each isolated discovery.
5. When the review finds a defect, send corrective guidance to the active
   implementation context. State:
   - the concrete evidence;
   - the violated invariant;
   - the owning boundary and required result;
   - the state or public behavior that must be proved; and
   - any tempting but invalid workaround to avoid.
   Before requiring rollback or recovery, identify the mutation boundary, the
   failure point, the transaction owner, and the commit or publication
   boundary. Keep a failure inside an uncommitted transaction distinct from
   cleanup after an earlier commit; do not infer rollback requirements from a
   cleanup symptom alone.
6. Repeat implementation and parent review until the delivery package is
   correct. Confirm that parent acceptance has a current, complete realization
   disposition for every contract ID; do not advance because one narrow test
   passes.
7. Run independent validation proportional to the delivery package. A verified
   milestone commit before package acceptance is permitted only when existing
   caller or repository policy grants commit authority. The main agent
   serializes that write and stages only attributable, coherent, locally
   checked state. Preserve the original review and package base and map across
   the checkpoint. Record the commit as verified-but-unaccepted in the handoff
   and acceptance packet; it does not establish slice or package acceptance,
   plan readiness, or a fixed point.
   Interrupted, partial, unverified, or ambiguous work is not checkpointed.
   Without existing commit authority, preserve the verified work as dirty
   state.
8. Only then begin the next reviewed delivery package. Treat accepted earlier
   invariants as stable; do not rediscover or restate them unless new evidence
   challenges them. At this accepted boundary, apply the continuity
   disposition: continue with the active context, or renew only after the
   parent verifies the turnover envelope and retires the old context. A
   checkpoint or internal step is not an ordinary renewal boundary.

## Manage Context Continuity

Follow [implementer-continuity.md](references/implementer-continuity.md) when
the active context may cross delivery packages or its reliability is in doubt.
The positive path is:

1. Keep exactly one active implementation writer through the admitted package,
   focused checks, parent corrections, and acceptance.
2. Observe context pressure together with behavioral and current-tree evidence
   and select `continue`, `renew-at-boundary`, or `stop-and-rebaseline` without
   a numeric threshold. Correctness must also work when telemetry is absent.
3. For `renew-at-boundary`, externalize required evidence, have the parent
   verify a turnover envelope that references existing package and plan records,
   retire the old context, and start exactly one fresh context with the same
   authorized configuration and one complete next-package assignment.
4. For `stop-and-rebaseline`, stop implementation deltas. The parent classifies
   the bounded dirty tree from the last accepted package as accepted,
   complete-but-unaccepted, partial, or obsolete, preserves useful edits, and
   records the rebaseline before any new assignment.

The implementer may contribute turnover deltas, but the parent verifies them;
the envelope is not a second contract or package ledger. Renewal does not add a
Tick, change reviewer independence, or reactivate the retired context.

Across assignments, corrections, slice handoffs, and parent review, verify that
preferred terms and their semantic-source relationships remain continuous and
that technical owners outrank glossary wording. For a selected glossary, carry
only changed or still-material declared-scope fit and unresolved candidate
dispositions after the initial assignment. They remain current only while
glossary selection, active scope, semantic source, and materiality remain
unchanged. Missing or stale selected-source state blocks the affected correction
or handoff; recover there through the shared authority and recheck only material
terms, without a ledger or repository audit. Treat a new term as a candidate
unless its meaning, glossary location, and edit scope are authorized for a
bounded write. Never translate a glossary label into a new field, state, limit,
component, or other mechanism without its own semantic owner.

## Keep The Loop Economical

- Reuse the active implementation context for ordinary corrections and later
  internal slices in the admitted package. Do not renew before parent accepts
  that package.
- Prefer concise follow-up tasks over full rewritten briefs.
- Keep detailed working evidence in the implementer's context or referenced
  artifact; import it into the parent only to answer a concrete acceptance
  question.
- Read and test the smallest relevant surface during iteration.
- Run focused checks first and defer expensive complete gates to meaningful
  package checkpoints unless risk requires them earlier. When a repository
  requires a clean-revision gate, run it once on the accepted exact checkpoint
  instead of duplicating the same full suite before and after commit.
- Omit routine narration, unchanged-code summaries, generic reassurance, and
  repeated architectural background.
- Do not repeat a successful implementer check in the parent unless it supplies
  distinct independence or risk coverage.
- Preserve required facts, evidence, constraints, and design reasoning before
  trimming explanation.
- Do not interpret token efficiency as permission to skip owner analysis,
  tests, cleanup, documentation, or independent review.

### Event-Driven Progress And Stall Protocol

Establish the progress envelope in the initial assignment, then wait for a
completion, checkpoint, blocker, or decision request instead of asking for
reassurance. Use the longest useful bounded mailbox wait permitted by the next
real checkpoint, user-communication policy, and active platform. A longer wait
must return early when an event arrives, so it does not delay a prompt handoff.

Treat a wait timeout only as absence of a message during that interval. Wait
again while the work remains inside its progress envelope. Inspect the shared
tree or process state only after a promised milestone is missing, the stall
threshold is crossed, a dependent decision needs current evidence, or another
credible safety or scope signal appears. Batch one narrow probe around the
decision it can change; ordinary dirty state while the writer is active is not
progress-quality evidence.

An event-driven wait completes only when a completion, checkpoint, blocker, or
decision event is delivered. A timeout, caller-side wait interruption, or
missing event says nothing about whether the writer has stopped or whether the
edit changed the tree. Do not create repeated reassurance turns or treat a
completion result as package acceptance; use the result to resume the parent's
assignment and acceptance flow.

Use the interaction capability that matches the state:

- queue a delta or correction to an active implementer without restarting its
  work or resending package context;
- trigger a new turn for an idle active implementer only when real follow-up
  work is ready;
- wait on mailbox events for completion and checkpoints;
- inspect agent topology only when lifecycle state is uncertain; and
- interrupt only when the active course should stop because it is unsafe,
  invalidated, or credibly stalled.

If the active runtime publishes a reusable-prefix lifetime, a bounded wait may
be selected slightly below it when no earlier checkpoint applies. Treat this as
a runtime profile, not a permanent duration: a 25-minute bound is longer than a
5-minute bound, but neither alone proves cache savings. When telemetry exists,
separate raw input, cached reads and writes, and newly appended context. When
cache behavior is unknown, use event-driven waiting without inventing a timer
or savings claim.

The implementer does not start a broad or complete suite until the parent has
accepted the focused delivery package unless its contract requires otherwise.
Let a completion handoff finish, then perform parent review. After a justified
stall probe, send at most one status request and make at most one interrupt;
inspect stable edits and resume the active context with a delta-only assignment
when its disposition remains `continue`, or when `renew-at-boundary` still
permits safe completion of the current admitted package. Otherwise use the
bounded stop-and-rebaseline procedure. Do not create repeated status-only
turns.

When the current direction is invalidated, stop dependent assignments and
interrupt the active writer. Wait for explicit settlement or stopped-writer
evidence, then inspect the resulting state and classify it as accepted,
complete-but-unaccepted, partial, or obsolete before issuing a replacement
assignment. Interruption does not imply rollback, no mutation, or a reusable
clean state; preserve partial work and evidence, and never replay an unresolved
edit or overlap writers.

Stopped-writer evidence means harness lifecycle evidence showing no active turn,
plus settlement of any writer-owned subprocess or cleanup. A timeout or caller
interruption alone does not establish that evidence.

## Accept The Package

After the final delivery package:

1. Map the resulting tree back to every package-matrix row and its named
   scenario status.
2. Verify the stable goal record's direct public scenario and report its
   behavioral status separately from mechanism completion. Mechanism evidence
   cannot establish behavioral acceptance.
3. Compare every applicable structural profile with the accepted result and
   resolve any qualified worsening through the architectural-scope authority.
   For a modularization package, also confirm that every material residual
   cluster is `extracted`, `retained-with-proof`, or justified
   `not-applicable`; required `unknown` coverage blocks package acceptance.
4. Run the package-level verification required by the repository and the risk
   of the changes.
5. Confirm no partial implementer work, unresolved feedback, overlapping write,
   or unintended dirty state remains.
6. Confirm every architectural-scope decision has an accepted branch and that
   no unauthorized or unverified ledger mutation is credited as durable.
7. Report the explicit glossary opt-out marker alone or, for a selected
   glossary, its source, declared-scope fit, material access or authorized
   changes, changed or still-material unresolved term candidates, and
   terminology continuity alongside the accepted delivery packages, important
   review corrections, verification, follow-up ledger delta, commits or pending
   changes, and any genuine remaining limitation.
8. After contract IDs, package scope, and evidence results are accepted, apply
   one compact
   [clear technical writing pass](../clear-technical-writing/SKILL.md) to the
   final package handoff without changing those decisions. Route a later
   material edit through that skill's revision-after-change behavior rather
   than applying a second outer prose pass.

Return an accepted package to its caller. Before ending the user-facing turn,
apply the linked request-completion decision: continue any remaining work in the
authorized outer request, or stop when the requested outcome is accepted, the
user directs a different boundary, or a concrete blocker requires input. Do not
continue into unrelated cleanup or an unrequested broader review.

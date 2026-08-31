---
name: supervised-implementer-loop
description: >-
  Implement one non-trivial work package through ordered, dependent slices
  using one persistent subagent while the main agent independently reviews,
  corrects, validates, and accepts each slice. Use when the user asks to reuse
  one implementer, review every implementation slice, make later work rely on
  accepted earlier fixes, or keep implementation token-efficient. Do not use
  for review-only work, small direct edits, or genuinely independent parallel
  packages.
---

# Supervised Implementer Loop

Complete one bounded work package through a repeated implement-review-correct
loop. The main agent is the acceptance authority; one persistent implementer
owns the edits and first-pass validation.

This skill ends when the requested work package is implemented and accepted.
It does not initiate broader reviews, invent adjacent work, or define an outer
project-completion process.

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

Before spawning, resolve glossary state through the
[project-glossary authority](../clear-technical-writing/references/project-glossaries.md).
Record the selected source or explicit opt-out and only the material
term-to-semantic-source relationships in the work package. Glossary wording is
explanatory input; package contracts and technical owners retain semantics.

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
   persistent implementer for exhaustive mechanical and evidence-producing
   work.
5. Use normal, non-fast execution by default. Enable fast mode only when the
   user explicitly requests fast mode for the current task; never infer it from
   memory, model choice, urgency, or token-economy instructions.

Spawn exactly one implementation subagent and reuse it for every delivery
package and correction in the work package. If that agent becomes unavailable,
report the loss of continuity and ask before replacing it.

## Give The Initial Assignment

Give the implementer enough context once:

- the work-package outcome and complete accepted delivery-package map with its
  current plan identity, provided once;
- the stable behavioral goal record and current direct scenario status;
- the current delivery package's contract IDs and scenario-portfolio entries;
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
- the selected glossary source or explicit opt-out and the material
  term-to-semantic-source relationships, without copying the glossary; and
- the progress envelope: expected duration class, milestones the implementer
  reports without prompting, immediate blocker conditions, the first credible
  stall threshold, and any intermediate decision the parent must make; and
- whether the implementer may commit.

Under an explicit opt-out, instruct the implementer not to ask another
placement question, access a glossary, or persist a term later in the package.

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
repository state. Do not repopulate the agent's context on later slices.

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

Do not accept a safe-deferral branch until the current contract passes, every
applicable non-worsening disposition is proved, and the authorized durable
follow-up is read back. External or otherwise separately controlled ledger
writes require their own authorization. Preserve the resulting decision record
and follow-up delta for slice and package handoff.

## Run Each Delivery Package

For every admitted delivery package:

1. Send the delivery package to the existing implementer. After the initial
   assignment, use follow-up messages containing only new requirements,
   evidence, and corrections.
2. Let the implementer edit and run focused validation. Do not perform
   overlapping writes or Git operations in the shared workspace. Non-mutating
   preparation may continue, but formally review only a completed delivery
   package.
3. Require a compact delivery-package acceptance packet: changed paths and
   resulting owner boundary; contract IDs established; intended behavior or
   interface changes, or an explicit statement that none were intended;
   exceptions from mechanical equivalence; material structural delta when a
   profile applies; the goal ID and direct scenario's behavioral status;
   mechanism progress stated separately; checks and scenario results with
   pass/fail status; unresolved risks or blockers; and the detailed-evidence
   location. For a modularization package, include the residual-topology delta
   and disposition of every affected material cluster. Include affected-test,
   external-evidence, architectural-decision, and follow-up dispositions only
   when they apply. The implementer does not approve its own work.
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
   follow-up read-back. Do not accept the implementer's summary as evidence by
   itself.
5. When the review finds a defect, send corrective guidance to the same
   implementer. State:
   - the concrete evidence;
   - the violated invariant;
   - the owning boundary and required result;
   - the state or public behavior that must be proved; and
   - any tempting but invalid workaround to avoid.
6. Repeat implementation and parent review until the delivery package is
   correct. Do not advance because one narrow test passes.
7. Run independent validation proportional to the delivery package. Checkpoint
   accepted work according to user and repository policy, with all Git writes
   serialized by the main agent unless explicitly delegated.
8. Only then begin the next reviewed delivery package. Treat accepted earlier
   invariants as stable; do not rediscover or restate them unless new evidence
   challenges them.

Across assignments, corrections, slice handoffs, and parent review, verify that
preferred terms and their semantic-source relationships remain continuous and
that technical owners outrank glossary wording. Treat a new term as a candidate
unless its meaning, glossary location, and edit scope are authorized for a
bounded write. Never translate a glossary label into a new field, state, limit,
component, or other mechanism without its own semantic owner.

## Keep The Loop Economical

- Reuse the same implementer; do not spawn a replacement for ordinary
  corrections or subsequent slices.
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

Use the interaction capability that matches the state:

- queue a delta or correction to an active implementer without restarting its
  work or resending package context;
- trigger a new turn for an idle persistent implementer only when real
  follow-up work is ready;
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
inspect stable edits and resume the same implementer with a delta-only
assignment. Do not create repeated status-only turns.

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
7. Report the glossary source or explicit opt-out, material access or authorized
   changes, unresolved term candidates, and terminology continuity alongside
   the accepted delivery packages, important review corrections, verification, follow-up
   ledger delta, commits or pending changes, and any genuine remaining
   limitation.
8. After contract IDs, package scope, and evidence results are accepted, apply
   one compact
   [clear technical writing pass](../clear-technical-writing/SKILL.md) to the
   final package handoff without changing those decisions. Route a later
   material edit through that skill's revision-after-change behavior rather
   than applying a second outer prose pass.

Stop when this package is accepted. Do not continue into unrelated cleanup or
a broader review unless the user separately requests it.

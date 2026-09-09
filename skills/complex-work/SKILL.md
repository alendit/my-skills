---
name: complex-work
description: >-
  Orchestrate a mixed, non-trivial work package spanning multiple artifact
  types, capability boundaries, or specialized skills when no single skill
  owns the outcome end to end. Use for work that combines implementation,
  review, documentation, research, or external validation. Do not use for a
  small bounded edit or a request fully owned by one specialized skill.
---

# Complex Work

Coordinate one mixed work package without taking substantive ownership away
from its leaf owners. Keep the primary agent responsible for the package
outcome, scope, cross-unit ordering, shared constraints, authorization
boundaries, integration, acceptance, and final handoff.

## Establish The Package

1. Read the user request, applicable repository guidance, current state, and
   relevant primary evidence. Inspect the available skills before assigning
   owners.
2. State the outcome, scope, explicit non-goals, material unknowns or
   assumptions, and the evidence that will demonstrate acceptance.
3. Instantiate the stable package-level goal record from the
   [behavioral design trace and rebaseline authority](../evidence-efficient-review/references/behavioral-design-trace.md)
   and carry its identity through leaf routing and acceptance. Update its
   status only from accepted evidence.
4. Discover and carry user and repository policy for commits, external writes,
   publication, destructive actions, and unrelated worktree state.
5. Record an execution-cost profile only when the user supplies one or current
   capabilities establish a material difference between capable owners. Name
   the selected cheaper capable implementation owner/configuration; include
   parent continuations spent waiting, polling, and interpreting coordination
   probes when they are material.
   Distinguish raw input, cache effects, and newly appended context when
   current telemetry supports that distinction; do not invent prices, cache
   behavior, or savings, and do not weaken authority to save context.
6. Carry the semantic MCP's repository binding and caller-selected implementer
   configuration when routing implementation. The MCP owns context continuity;
   the coordinator does not select a model, operate a mailbox, or manage renewal.
7. Decompose the outcome into ordered units only as far as observable
   acceptance requires. Record each unit's owner, dependencies, shared
   constraints, and exit evidence. Group related mechanical work at the
   smallest meaningful acceptance boundary, but keep a boundary separate when
   later work depends on a semantic or architectural decision there. Keep
   uncertain choices local and reversible.
8. Bypass this skill when the result is a small bounded edit or one specialized
   skill owns it end to end.

At package establishment, resolve or consume glossary state through the shared
[project-glossary authority](../clear-technical-writing/references/project-glossaries.md).
Under explicit opt-out, carry only the opt-out marker: do not access a glossary
or calculate, request, transfer, recover, or report scope fit or candidates;
affected leaves explain concepts locally. For a selected glossary, record its
identity, declared-scope fit when applicable, and only material unresolved
candidates with their semantic sources, project distinctions or ambiguities,
and unresolved aliases. Selected-source state remains current only while its
selection, active scope, semantic sources, and materiality remain unchanged.
Missing or stale selected-source state blocks the affected routing or handoff;
recover at that existing boundary through the shared authority and recheck only
material terms, without a ledger or repository audit. Do not copy the coverage
procedure into this coordinator.

For every design-sensitive unit, the coordinator carries the repository's
[architecture-guidance authority](../add-architectural-guidances/references/guidance-contract.md)
and its semantic-authority/physical-decomposition orthogonality rule as shared
constraints. For each new or materially changed responsibility, the coordinator
asks the leaf to report a lightweight physical-boundary disposition: the
semantic owner, the selected source boundary, and a cohesion reason—one primary
reason to change without unrelated context. This ordinary disposition does not
require a whole-root residual-topology inventory or a complete-boundary
challenge for unrelated clusters.

When the user-selected contract explicitly includes modularization or physical
decomposition, or when source/dependency/state/test evidence qualifies a
physical-decomposition defect under the
[architectural-scope authority](../supervised-implementer-loop/references/architectural-scope-decision.md),
the coordinator routes the affected unit through that authority and the
existing leaf mechanics. For the activated scope, the implementation or review
leaf must report the activated-scope result, residual-topology coverage,
separate preservation and locality evidence, and fixed-point eligibility.
Several units touching the same source owner are a signal for the coordinator
to check the lightweight disposition; overlap alone does not activate the full
topology mechanics. Existing leaf owners retain activation, inventory,
qualification, and fixed-point rules.

## Assign Leaf Owners

Route a unit to the applicable specialized skill, then follow that skill's
interface and acceptance rules without restating or replacing its mechanics:

During package establishment and routing, consume the current reviewed result
level and plan identity for every unit that can produce production edits. If
implementation-plan coverage is missing, contract-only, stale, invalidated,
changed, or has any unknown plan cell, route plan or specification review to
`$evidence-efficient-review` or `$review-fixpoint` and do not route production
implementation. Route an accepted, current implementation plan to
`$supervised-implementer-loop`, carrying its result level and plan identity in
the leaf assignment and acceptance packet. Carry only those routing facts here:
EER owns contract and plan cells; review-fixpoint owns result effects and
fixed-point phase mechanics; SIL owns delivery-package schema, admission, and
execution. Do not copy those leaf schemas or mechanics into this coordinator.

When routing a unit to `$supervised-implementer-loop`, carry material host
binding and configuration constraints. The parent acting through the leaf
implements and integrates the slice by selecting specific semantic edits;
the MCP realizes each selected edit. Trust its summaries until independent
slice acceptance. The semantic parent does not read or emit implementation code;
route code-fact questions, including recovery and acceptance, through SIL’s
semantic inspection contract. Source inspection in other leaf procedures belongs
behind tools or with the independent reviewer. Runtime context
continuation does not change the admitted dependency map or accept an outer unit.

- route review-only work to `$evidence-efficient-review`;
- route repeated review and remediation to `$review-fixpoint`;
- route dependent implementation requiring the supervised implementation
  workflow to `$supervised-implementer-loop`;
- route an educational technical-note series to `$technical-note-series`;
- route repository architecture documentation to
  `$project-architecture-doc`;
- route reusable architecture policy to `$add-architectural-guidances`; and
- route final engineering prose to `$clear-technical-writing`.

When no available specialized skill owns a unit's complete outcome, keep the
primary agent as that unit's leaf owner under the carried repository and
authorization policy. Do not invent a leaf, force delegation, or bypass an
applicable specialized owner.

## Execute And Integrate Units

For each unit, give its leaf owner the package goal record, outcome, unit
boundary, dependencies, accepted prior evidence, shared constraints,
authorization limits, and observable exit. Let the leaf owner make its
substantive decisions and choose its validation mechanics. The primary agent
verifies the result, integrates it with accepted units, and retains final
acceptance authority.

Give an affected leaf the opt-out marker or current selected-source state once.
For a selected glossary, carry only changed or still-material scope-fit and
candidate dispositions in later assignments, corrections, and handoffs.
Technical owners retain meaning, and no disposition authorizes a glossary write
or a new mechanism.

When source-owner overlap applies, require the implementation leaf's accepted
baseline-to-result structural decision before package acceptance. Integrate
that evidence without copying the leaf's scanning or architecture-scope
mechanics.

Delegate only when the user requests delegation, the selected leaf requires
it, an active execution-cost profile identifies a cheaper capable implementation
owner/configuration for suitable mechanical or evidence-producing work, or packages are
genuinely independent. Do not fan out or delegate all work merely because the
package is large.

When the execution-cost profile identifies a cheaper capable implementation
owner/configuration, keep exhaustive mechanical work, iteration, and verbose
evidence with that owner. Give the primary a bounded acceptance packet and
independently selected risk probes sufficient for its package decisions;
context savings do not transfer scope, architecture, authorization,
acceptance, or independent-review authority.

For semantic implementation, the parent retains the edit sequence and integration
reasoning. Let the MCP own source adaptation, local checks, repairs, and execution
within the selected edit, plus context reuse. The parent uses each summary to
choose the next specific edit without inspecting patches or rerunning checks.
Complete package context does not delegate completion of the package. Independent
probes belong at the completed slice boundary. Necessary scope expansion returns
to the parent. For changed direction during execution, use SIL's active-edit
control and recovery contract; an ended wait does not establish writer settlement.
Do not wrap the tool in the previous implementer supervision loop.

For other long delegated leaves, use their progress interface and bounded
notifications rather than status-only parent turns. The semantic MCP requires
no implementation-agent mailbox management by this coordinator.

Treat every mutation as bounded by existing authority. A reviewable unit does
not authorize a commit, push, publication, deployment, message, destructive
action, or other external write. Checkpoint only when user and repository
policy authorize it, and preserve unrelated worktree changes.

When an authorized unit changes an installed skill source, inventory the exact
destination first, preserve the previous standalone source recoverably until
read-back succeeds, link the installed entry to the accepted repository
package, and verify both the resolved target and readable `SKILL.md`.

## Replan At The Broken Boundary

When new evidence contradicts the route, identify the invalidated assumption,
unit, or ordering decision. Return to the latest broken boundary and replan
that unit and its dependents. Preserve accepted units whose dependencies and
evidence remain valid. Do not continue a disproved route or restart unaffected
work.

When a leaf proposes a behavioral contract change, return it to the product
authority named by the shared record. After acceptance, update the owning
contract once. Resume affected units from the accepted rebaseline boundary;
leave the comparison and test-disposition process with the leaf authority.

Treat cumulatively harmful placement that invalidates the assumed source owner
as such a contradiction; size alone does not invalidate the route.

Also replan when primary-context growth is dominated by source, diffs, logs, or
checks already processed by a capable delegated owner without supporting a new
primary decision. Expand primary inspection only around consequential risk,
contradictory evidence, or an authority the primary must exercise.

When semantic realization returns a design blocker, replan the affected unit
and dependencies. An execution failure instead follows the MCP's recorded
operation recovery; do not silently switch to native-agent implementation or
replay an uncertain mutation. Preserve accepted slices and partial useful work.
Runtime continuation or compaction does not accept a slice or an outer unit.

## Verify And Finish

Let the semantic MCP run focused implementation checks while a slice is unstable.
The parent evaluates independent semantic evidence at slice acceptance; code
inspection belongs to tools or an independent reviewer, not the parent.
Run expensive complete gates at meaningful package checkpoints, according to
repository policy and the selected leaf owner's acceptance rules. Do not defer
all validation until the end.

Apply a final `$clear-technical-writing` pass exactly once after substantive
decisions stabilize. If a leaf owner already applied that pass to its artifact,
verify that it occurred and do not repeat it in the outer workflow.

Finish with one integrated handoff that reports:

- accepted units and their owners;
- the goal ID and direct scenario's behavioral status, reported separately from
  mechanism progress;
- evidence and package-level verification;
- unresolved unknowns or capability status;
- the explicit opt-out marker alone, or the selected glossary identity,
  declared-scope fit, and changed or still-material unresolved candidates; and
- pending actions that still require authorization.

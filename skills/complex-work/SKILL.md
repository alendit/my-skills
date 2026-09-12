---
name: complex-work
description: >-
  Coordinate a mixed, non-trivial work package spanning artifact types,
  capability boundaries, or specialized skills when no single skill owns the
  outcome end to end. Not for a small bounded edit or a task fully owned by
  one specialized skill.
---

# Complex Work

The primary owns the complete request, scope, ordering, integration, and final
acceptance. Specialized skills own their substantive work and validation.
Following a skill does not itself require spawning an agent.

## 1. Establish The Outcome

Read the request, repository guidance, current state, and relevant primary
evidence. State the outcome, non-goals, material unknowns, acceptance evidence,
and authorization boundaries, including commit policy and unrelated changes.
Bypass this coordinator when one leaf skill can own the entire result.

Carry one [behavioral goal record](../evidence-efficient-review/references/behavioral-design-trace.md#establish-the-behavioral-trace)
and resolve or consume [glossary state](../clear-technical-writing/references/project-glossaries.md#resolve-glossary-state-in-order).
Reference existing authorities; update status from accepted evidence.

## 2. Divide And Route The Work

Create ordered units only where observable acceptance or a dependency decision
needs a boundary. Record each unit's owner, prerequisites, shared constraints,
and exit evidence. Keep related mechanical work together.

| Unit | Owner |
|---|---|
| Prose-heavy specification, plan, skill, or design proposal | Primary, with the applicable writing skill |
| Admitted code package benefiting from delegated execution | `supervised-implementer-loop` |
| Review-only work | `evidence-efficient-review` |
| Repeated review and remediation | `review-fixpoint` |
| Educational note series | `technical-note-series` |
| Repository architecture document | `project-architecture-doc` |
| Reusable architecture policy | `add-architectural-guidances` |
| Final engineering prose | `clear-technical-writing`, applied by the artifact owner |

For mixed work, the primary owns design/specification decisions and the
implementer owns admitted code and its directly supporting artifacts. Honor
explicit user delegation. If no specialized skill owns a unit, keep the primary
as its owner; do not invent a team because the package is large.

Before routing production edits, consume the current
`implementation-plan-fixed-point` and plan identity. Missing, contract-only,
stale, changed, or unknown plan coverage returns to plan review; SIL performs
final edit admission. Use the [conditional routing interfaces](references/routing-and-integration.md)
for cost-based delegation, continuity, terminology, or design-sensitive units.

## 3. Execute And Integrate

Give each leaf its outcome, boundary, accepted prerequisites, shared constraints,
authorization, and observable exit once. Carry later changes as deltas. Let the
leaf choose its substantive methods and validation; verify its result and its
joins with accepted units before advancing dependent work.

For supervised code, consume SIL's progress envelope and event-driven waiting
process. Empty timeouts do not change routing or justify source, diff, or status
inspection. Keep verbose evidence with the implementer; inspect only what a
concrete integration, risk, or acceptance decision requires.

Run focused checks while a unit is unstable and required complete gates at
meaningful checkpoints. A reviewable unit does not expand authorization for
commits, external writes, or publication. If the request includes updating an
installed skill, use the [distribution update procedure](references/routing-and-integration.md#update-an-installed-skill).

## 4. Replan The Invalidated Boundary

When evidence contradicts a route, identify the failed assumption and replan
the affected unit and dependents. Preserve accepted units whose evidence still
holds. Route behavioral contract changes to the named product authority and
update the owning contract once after acceptance.

When parent work is dominated by repeated reads or status probes with no new
decision, correct the coordination pattern while preserving the delegated
unit: return to bounded handoffs, milestone events, and risk-driven inspection.

Consume SIL's `renew-at-boundary` or `stop-and-rebaseline` result through the
continuity interface. An accepted inner delivery package is not automatically
an accepted outer unit; SIL owns turnover and writer settlement.

## 5. Verify The Complete Request

Confirm all requested units and their joins are accepted, required evidence is
current, and remaining unknowns or capability limitations are explicit. Report
the direct scenario's behavior separately from mechanism progress.

Give one integrated handoff: accepted units and owners, verification, material
terminology changes, unresolved limitations, and pending authorized work or
actions requiring authorization. Let each artifact owner apply one final
clear-writing pass; do not rewrite an already completed leaf artifact again.

Continue the next unmet unit before ending. Finish at the full accepted outcome,
a user-directed boundary, or a concrete blocker requiring input.

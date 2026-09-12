---
name: review-fixpoint
description: >-
  Alternate independent reviews and remediation until a selected repository
  work package reaches a functional and architectural fixed point. Use when
  asked to address review findings, review remediations, run another round,
  or iterate until no actionable defects remain.
---

# Review Fixpoint

This skill owns phase selection, phase commits, reviewer continuity, and the
fixed-point decision. Repository guidance owns scope-specific policies and
canonical gates. EER owns review mechanics; SIL owns delegated code execution.

## 1. Recover Scope And Select The Phase

Read the request, repository guidance, status, history, and latest applicable
review artifact completely. Keep the selected work-package scope and preserve
unrelated changes. Recover the review-artifact convention and required gates.

Choose **Tock** when findings remain unimplemented, or **Tick** when remediation
is present or another review is requested. If ambiguous, inspect the relevant
diff, owners, tests, and history before asking. Preserve historical findings:
use numbered immutable reviews or the repository's declared ledger convention.

Read the [contract and evidence boundary](references/contract-and-evidence-boundary.md#preserve-one-contract-authority)
through “Carry result levels and plan identity.” Carry the existing contract
matrix, goal record, and current [glossary state](../clear-technical-writing/references/project-glossaries.md#resolve-glossary-state-in-order)
into each leaf; later inputs carry material deltas only.

For specification scope, retain the selected review level. A contract-level
result routes to delivery-plan review. Production implementation requires a
current `implementation-plan-fixed-point` for unchanged plan-owning content
and dependencies; a changed or unknown plan returns to review before editing.

## 2. Establish Independent Review

Select exactly one persistent read-only reviewer independent of remediation
and reuse it for every Tick. Give it a neutral dossier and current source,
without the author's expected findings or remediation reasoning. The primary
verifies material candidates rather than repeating the complete review.

Use [reviewer selection and independence](references/phase-mechanics.md#preserve-review-independence)
for configuration, an unresolved dispute, or reviewer loss. Ask before replacing
a required persistent reviewer; ordinary rounds do not need new reviewers.

## 3. Tock: Remediate And Validate

1. Map each finding to its owning contract and prove the defect at that boundary.
   Build one coherent remediation package when findings share a target and
   dependent work. Use the [finding-remediation procedure](references/phase-mechanics.md#remediate-findings)
   for history, regression evidence, compatibility, and authority updates.
2. Keep prose-heavy remediation with the primary. Route non-trivial admitted
   code packages through SIL with the current plan identity and accepted map;
   handle small fixes directly. Parent acceptance of SIL packages completes
   remediation, not independent review.
3. When the proposed fix changes supporting design or adds a defense, apply the
   [behavioral rebaseline](../evidence-efficient-review/references/behavioral-design-trace.md)
   or [economic actionability](../evidence-efficient-review/references/economic-actionability.md)
   procedure as applicable. For non-local impact, uncertain ownership, or a
   local repair preserving an architectural defect, use the [architectural-scope decision](../supervised-implementer-loop/references/architectural-scope-decision.md).
   The primary accepts the branch; product authority accepts behavioral changes.
4. Resolve every finding and required unknown, finish focused verification, and
   obtain parent acceptance. Reuse an eligible coherent handoff commit covering
   exactly the phase, or create the remediation commit. Run the [canonical gate](references/phase-mechanics.md#verify-each-tock)
   on that exact clean revision. A failure returns to remediation before Tick.

Commit each completed phase under the phase-mechanics policy; an explicit
no-commit request leaves the pending phase clearly uncommitted. Serialize Git
writes and preserve unrelated work. Never create an empty acceptance commit or
repeat equivalent complete suites solely to show the same result twice.

## 4. Tick: Review The Accepted Revision

Use EER to independently review the exact accepted revision. Supply the scope,
contract matrix and selected result level, previous findings and baseline,
architecture authorities, canonical gates, and repository artifact destination.
Use the [Tick brief and artifact fields](references/phase-mechanics.md#prepare-and-record-a-tick)
for applicable structural, terminology, follow-up, and external evidence.

Review promised closure and the complete selected goal. Use incremental mode
when prior coverage is trustworthy and impact is bounded; otherwise rebaseline.
A correction invalidates only affected evidence when dependencies remain clear.
The reviewer independently audits architectural classifications and deferrals;
it reports ledger changes but never makes them.

Verify material findings and evidence, preserve the durable review artifact even
when it has zero findings, and commit the completed review phase. The leaf owns
its final clear-writing pass; the orchestrator does not rewrite it again.

## 5. Repeat Or Establish Fixed Point

If Tick finds defects, return to Tock. Reuse the implementer with a delta while
SIL's disposition is `continue`; otherwise follow SIL's authorized renewal or
rebaseline path. A turnover, checkpoint, or accepted internal slice is not a
Tick. Review only settled, completed remediation.

Declare `deterministic-fixed-point` only when the independent Tick establishes:

- all previous findings are closed and no P0–P3 functional or architectural
  finding or required unknown remains;
- current contract evidence proves owner behavior and realistic public
  compositions, with behavior reported separately from mechanism completion;
- required deterministic gates pass on the exact reviewed revision; and
- the [applicable completion checks](references/phase-mechanics.md#check-fixed-point-eligibility)
  clear architecture, compatibility, resource bounds, documentation, economic
  actionability, and any activated decomposition or follow-up scope.

Do not declare fixed point after Tock or from green tests alone. A valid external
`product-contract-failure` blocks it. When external evidence is required, use the
[external acceptance sequence](references/contract-and-evidence-boundary.md#sequence-external-diagnostics-and-acceptance)
and report capability status separately. Unavailable evidence leaves capability
unconfirmed; do not claim that capability or `Done` until it is confirmed.

Return the durable review decision, reviewed revision, verification, material
terminology state, legitimate follow-ups, and remaining limitations. Continue
any remaining unit in the authorized request; finish at the accepted requested
outcome, a user-directed boundary, or a concrete blocker requiring input.

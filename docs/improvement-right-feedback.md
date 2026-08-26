# Improvement Plan: Architectural Feedback Without Unbounded Scope

## Purpose and authority

Improve the development and review skills so concrete implementation friction
can correct architecture without expanding every package indefinitely or
entrenching a defect through a convenient local patch.

The matrix below is the single normative authority for this package. Ordered
slices and validation scenarios reference its stable IDs; they do not restate
its requirements. The
[contract-centered improvement plan](improvement_avoid_repetition.md) remains
authoritative for contract normalization, evidence classes, scenario
portfolios, exact-limit justification, workflow/product-document separation,
and fixed-point evidence. This plan adds only the missing architectural-scope
decision and follow-up lifecycle.

## Scope and non-goals

The behavior owners in scope are:

- `supervised-implementer-loop`;
- `review-fixpoint`;
- `evidence-efficient-review`; and
- `add-architectural-guidances`.

`project-architecture-doc` and `technical-note-series` are inspected consumers,
not presumed change targets. Their explicit dispositions are in AF8.

This package does not make file count an architecture metric, require a
follow-up for every possible refactor, turn a follow-up ledger into an automatic
gate or roadmap, permit a worsening patch for scope control, require a
full-system redesign, or duplicate the contract, evidence, test, and fixpoint
rules owned by the preceding plan. It does not rewrite the Feature 88 addendum.

## Current evidence and gap

The current skills already reject local repairs that preserve faulty ownership,
distinguish stable contracts from private mechanisms, and keep feature
requirements separate from fixpoint mechanics. The Feature 88 review exposes a
remaining gap: a roughly 400-line live E2E addition and a credentialed 301-second
scenario create change and diagnosis friction, but friction alone cannot say
whether the cause is product architecture, inherently end-to-end composition,
test infrastructure, or an implementation choice.

There is no shared rule that qualifies that signal, bounds the proper
correction, distinguishes safe deferral from worsening deferral, assigns the
branch decision to an exact authority, or preserves legitimate deferred work
without laundering a current finding. AF1-AF8 define that missing rule.

## Authoritative contract-and-evidence matrix

| ID | Normative outcome | Decision authority | Owning skill and slice | Named evidence |
|---|---|---|---|---|
| AF1 | **Qualify an architecture signal from causal evidence, not effort or file count.** The decision record names the triggering change and stable contract IDs; expected semantic owner; actual owners, consumers, dependency edges, state/lifetime boundaries, and tests affected; the causal path forcing non-local work; the desired owner or dependency direction; and why a local patch preserves the problem. It must show at least one architecture property: duplicated semantic authority, dependency inversion, split or misplaced state/lifetime ownership, a public or compatibility surface forced by the wrong owner, or tests that reject an independently designed correct implementation because they freeze decomposition. Ordinary adapter propagation, serialization at a real boundary, cohesive multi-file owner changes, inherently end-to-end contract composition, unfamiliarity, slow tooling, and difficult test editing are insufficient without that causal property. | The primary supervisor qualifies during a supervised package; Tock qualifies before remediation; the independent Tick audits the classification. A reviewer may raise AF1 as a candidate but does not choose remediation. | `supervised-implementer-loop`, `review-fixpoint`, and `evidence-efficient-review`; S2-S4 | G1 Signal-classification fixture |
| AF2 | **Bound the smallest proper correction before choosing a branch.** Record affected semantic owners, representative consumers, stable public contracts, dependency changes, state migration/lifetime, compatibility obligations, tests, documentation, and removal work. The bound follows the causal owner and required compositions; it is neither the current diff nor permission for a full-system rewrite. | The primary supervisor owns the bound for a supervised package. During Tock, the workflow owner proposes the bound and the primary accepts it. Tick audits whether excluded impact invalidates it. | `supervised-implementer-loop` and `review-fixpoint`; S2-S3 | G2 Correction-bound fixture |
| AF3 | **Correct the architecture now when AF2 fits the accepted package and does not endanger its useful fixed point.** Revise the owning contract or plan once when needed, reclassify affected tests, implement at the architectural boundary, remove the obsolete path, and resume the package. Non-locality alone is not a reason to defer a bounded owner correction. | The primary supervisor may select this branch within the caller-approved outcome and scope. Tock may select it under the same boundary; Tick only audits it. Material expansion beyond that authority goes to AF5. | `supervised-implementer-loop` and `review-fixpoint`; S2-S3 | G3 Bounded-correction scenario |
| AF4 | **Defer only a current-contract-satisfying, non-worsening correction.** A containment fix is eligible only when every applicable dimension is unchanged or improved: dependency direction; number of semantic owners or policy copies; durable state, state lifetime, and synchronization; public, persisted, wire, and compatibility surfaces; fallback, shim, dual-path, and temporary-abstraction burden; mechanism coupling in durable tests; number of consumers exposed; observable failure visibility; and migration, removal, or future remediation cost. Record a short evidence-backed disposition per applicable dimension and explain `not-applicable`; never replace this with a numeric score. Create or update the AF6 follow-up and continue. | The primary supervisor accepts this branch. Tock proposes and records it; Tick independently audits AF1, the current contract, every AF4 disposition, and AF6 identity. A reviewer cannot downgrade a current finding merely by recommending deferral. | `supervised-implementer-loop`, `review-fixpoint`, and `evidence-efficient-review`; S2-S4 | G4 Non-worsening table; G5 Safe-deferral scenario |
| AF5 | **Reevaluate before accepting any worsening minimal fix.** If an AF4 dimension worsens, reject ordinary deferral and search within AF2 for the smallest architecture-preserving intermediate correction: one that satisfies the current contract, prevents new dependence on the defect, and reduces or does not increase later removal cost. If that correction fits existing authority, take AF3. If no bounded non-worsening route exists, stop before production changes and request an explicit scope decision; record the rejected option and the smallest known proper correction. | The primary supervisor performs reevaluation. Only the caller or other explicit package-scope authority may authorize a material outcome/scope expansion at the stop. Tock and Tick must surface the stop and cannot self-authorize expansion. | `supervised-implementer-loop` and `review-fixpoint`; S2-S3 | G6 Worsening-shim and scope-stop scenarios |
| AF6 | **Maintain one durable architectural follow-up ledger.** Reuse the project's existing issue, architecture-debt, or feature ledger; create no competing TODO list. If none exists, the caller selects one durable project authority before deferral; without authority to write such a record, AF4 deferral is unavailable and AF5 applies. Each record has a ledger-issued stable ID and a dedupe identity of affected contract or semantic owner plus the undesired dependency/state relation and desired owner/direction. It records status, AF1 evidence, concise problem and remediation direction, why it is outside the package, current containment fix, AF4 dispositions, affected areas/scope drivers, revisit trigger or prerequisite, and originating finding/decision links. Create only after AF4 passes; update the same identity when evidence, containment, scope, or trigger changes; dedupe overlapping observations into that record; close only with source/evidence that the desired boundary now holds and obsolete containment is removed; mark `stale` when its contract, owner, evidence, or prerequisite is invalidated, then revalidate, supersede with a link, or close rather than silently dropping it. Every package and Tick handoff reports created, updated, closed, stale, and unchanged-relevant IDs. Records are non-gating by default and become gates only when an accepted contract or explicit work package activates them. | The primary supervisor owns create/update/close proposals during implementation; the project's existing ledger authority owns record identity. Tock records authorized deltas. Tick audits identity, lifecycle disposition, and handoff visibility without mutating the ledger. External ledger writes require their own authorization. | Shared detailed authority in `supervised-implementer-loop`; consumers in `review-fixpoint` and `evidence-efficient-review`; S2-S4 | G7 Ledger-lifecycle fixture |
| AF7 | **Never launder a finding into AF6.** A current contract violation, unresolved P0-P3 defect, required coverage still `unknown`, worsening fix under AF4, or valid external product-contract failure remains gating under the existing fixpoint authority. A non-gating follow-up may coexist with deterministic fixed point only when the current contract is satisfied, deterministic required cells are cleared, the accepted change passes AF4, deferral is explicit and durable under AF6, and no activated follow-up requirement remains open. A zero-finding Tick reports relevant follow-up IDs but does not call them findings or silently call them closed. | Tock must not propose laundering; the independent Tick is the final authority on finding classification and deterministic fixed-point eligibility. The caller remains authority for activating a follow-up as new scope. | `review-fixpoint` and `evidence-efficient-review`; S3-S4 | G8 Finding-laundering fixture |
| AF8 | **Keep responsibilities narrow and explicit.** `supervised-implementer-loop` owns AF1-AF6 decisions during slice supervision, uses one shared detailed decision/ledger reference, and exposes follow-up deltas in handoff. `review-fixpoint` consumes that authority in Tock, independently audits AF1-AF7 in Tick, and preserves the existing fixed-point meanings. `evidence-efficient-review` distinguishes actionable current findings, unknowns, and evidenced non-gating improvements; audits AF1/AF4/AF6; reports ledger deltas; and never remediates. `add-architectural-guidances` adds only compact change-locality, smallest-correction, non-worsening, and scope-stop guidance plus one design self-check, linking rather than copying the detailed workflow. `project-architecture-doc` is **not applicable** as a behavior owner: it may link a known architectural delta to the existing ledger but must not create a second task ledger or decide deferral. `technical-note-series` is **not applicable**: educational publication has no decision or ledger responsibility and receives no change unless implementation reveals duplicated authority. | Each skill owns only its listed behavior. The package primary verifies both changed owners and not-applicable consumer dispositions before acceptance. | S2-S5 | G9 Responsibility-routing and consumer-disposition check |

## Ordered implementation slices

### S1 — Normalize this specification

Replace the handover with this matrix, reconcile it with the existing
contract-centered authority, and validate AF1-AF8 against the six scenarios
below. Change no skill behavior in this slice.

### S2 — Establish supervised decision ownership

Implement AF1-AF6 and AF8 in `supervised-implementer-loop`. Put the detailed
decision record, AF4 disposition table, and AF6 schema/lifecycle in one directly
linked reference. Keep the entrypoint focused on detection, authority, branch
selection, slice acceptance, and handoff.

### S3 — Integrate the decision with Tick/Tock

Implement AF2-AF8 in `review-fixpoint`. Reference the S2 authority instead of
copying its decision table or ledger schema. Preserve existing review
independence, contract/evidence classes, phase ownership, and fixed-point result
vocabulary.

### S4 — Make review classification evidence-based

Implement AF1, AF4, AF6-AF8 in `evidence-efficient-review`. Add the minimum
coverage-ledger fields needed to distinguish a current finding, unknown, and
non-gating architectural improvement. Keep the skill read-only and keep
remediation authority outside it.

### S5 — Add compact reusable architecture guidance

Implement AF8 in `add-architectural-guidances` without copying the branch table
or ledger lifecycle. Inspect the two not-applicable consumers and change them
only if their current text contradicts AF8.

### S6 — Validate the composed workflow

Run G1-G9, skill structural validators, reference/link checks, and
`git diff --check`. Review the finished package against AF1-AF8 and the imported
authority before declaring fixed point.

## Scenario-level validation

These scenarios preserve the six concrete cases from the handover. They are
behavioral fixtures, not assertion inventories.

1. **Cohesive owner correction (AF1-AF3):** a proper correction spans several
   files under one causal owner and fits the accepted package. Expected branch:
   G3 confirms correction now rather than file-count-based deferral.
2. **Neutral containment (AF1, AF4, AF6):** a larger cleanup is unnecessary for
   current correctness; the containment fix adds no coupling or compatibility
   surface. Expected branch: G5 accepts it with one durable follow-up.
3. **Worsening public shim (AF4-AF5):** a proposed local shim adds a public path
   and mechanism-coupled tests. Expected branch: G6 rejects ordinary deferral
   and chooses a bounded architecture-preserving correction or scope stop.
4. **Unrelated attractive improvement (AF1, AF6-AF7):** review finds a useful
   improvement unrelated to the current contract. Expected result: G8 records
   a non-gating follow-up without inventing a P2 finding.
5. **Finding laundering (AF7):** a current architectural defect is relabeled as
   follow-up to obtain fixed point. Expected result: G8 keeps the finding open
   and rejects fixed point.
6. **Difficult nested test (AF1-AF5):** repeated editing difficulty triggers an
   evidence check. Expected result: G1 does not infer product-architecture debt
   from friction alone; when causal evidence instead shows frozen test
   decomposition, G2-G6 choose bounded reusable infrastructure now, safe
   follow-up, or explicit scope stop.

## Named validation gates

- **G1 Signal-classification fixture:** exercise inherent composition,
  implementation friction, and each qualifying causal architecture property;
  verify distinct dispositions and an evidence-complete AF1 record.
- **G2 Correction-bound fixture:** verify the bound follows owners, consumers,
  contracts, state, compatibility, evidence, docs, and removal work without
  expanding to an unrelated redesign.
- **G3 Bounded-correction scenario:** verify a cohesive multi-file correction
  within accepted scope selects AF3.
- **G4 Non-worsening table:** exercise every AF4 dimension with unchanged,
  improved, worsened, and reasoned-not-applicable dispositions; any worsened
  dimension routes to AF5.
- **G5 Safe-deferral scenario:** verify current-contract satisfaction,
  non-worsening containment, AF6 creation/dedupe, and handoff visibility.
- **G6 Worsening-shim and scope-stop scenarios:** verify a public shim cannot be
  deferred normally, an architecture-preserving intermediate correction is
  preferred when bounded, and absent such a route no production change occurs
  without explicit scope authority.
- **G7 Ledger-lifecycle fixture:** exercise reuse, stable identity, dedupe,
  create, update, close, stale, supersede, handoff delta, and default non-gating
  behavior.
- **G8 Finding-laundering fixture:** exercise current P0-P3, unknown coverage,
  external product-contract failure, legitimate follow-up, and activated
  follow-up states against fixed-point eligibility.
- **G9 Responsibility-routing and consumer-disposition check:** verify the four
  behavior owners implement only AF8 responsibilities and both inspected
  consumers remain not applicable unless concrete contradictory behavior is
  found.

## Validation and handoff

Each slice handoff reports only changed files, addressed AF IDs, named gate
results, and unresolved concerns. S6 additionally validates relative links,
stable-ID references, scenario coverage, reference discoverability, and the
complete diff for duplicated authority. Completion requires AF1-AF8 cleared,
G1-G9 passing, no required unknown, and a fresh independent Tick under the
existing fixed-point authority.

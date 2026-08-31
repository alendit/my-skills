# Contract Loss During Implementation: Review 01

**Changes requested. Neither `contract-fixed-point` nor
`implementation-plan-fixed-point` is reached.**

The raw note is a useful diagnostic, but it deliberately supplies no normative
CL contract, result level, owner assignment, or delivery plan. This review
rebaselines it into a complete **candidate** CL1-CL8 matrix and a complete
two-package plan. Those reviewer-authored candidates are not accepted product
authority. The main agent may explicitly accept them as a mechanism-only
normalization of CL-G1; any behavioral expansion must return to the user.
Implementation remains blocked until that authority decision is durable and a
fresh plan review binds the accepted content to an unchanged plan identity.

## Review identity and contract

- Baseline `HEAD`: `0f078a6488dab0fe1df2f1cbdf5dfbd7ce5fadb3`.
- Reviewed [proposal](improvement-contract-loss-during-implementation.md):
  `aec5aa6eb85c03d18794405d4436365352ae99df`.
- Scope: the proposal and the current generic owners in SIL, EER, and
  review-fixpoint. Target-repository Review 98 and Slice 7 remediation are not
  in scope and were not accessed.
- Evidence: deterministic repository source/contract review only. External
  capability and telemetry are not applicable.
- Glossary: explicit opt-out. Terms introduced below are defined locally.

```text
Goal ID: CL-G1
Behavioral goal: Every accepted ownership, information, transaction, and
  evidence requirement remains decision-active from reviewed plan through
  concrete owner operations, state, and assertions; a design change invalidates
  dependent authority and evidence so missing coverage is rejected before the
  canonical gate.
Direct scenario: Given a package containing foreign-ownership, provenance,
  atomic-publication, and negative-authority requirements, each stable contract
  maps to a concrete implementation capability and assertion. Missing or stale
  mapping blocks pre-edit completeness or parent acceptance, while the final
  independent Tick remains the backstop.
Product authority: The user-selected proposal and this request. The main agent
  may accept mechanism-only normalization; behavioral changes return to the
  user.
Owning contract: candidate CL1
Behavioral status: partial; current skills carry contracts, scenarios, and a
  final independent review, but do not keep a complete contract-to-operation,
  state, transaction, and assertion mapping decision-active through SIL
  handoffs and parent acceptance.
Mechanism status: not-started
```

The preserved non-goals are: no new review phase; no earlier or repeated
canonical gate; no target-repository architecture or remediation; no exclusive
blame assignment; and no weakening of persistent independent review.

## Findings and required unknowns

| ID | Severity | Raw-note defect and effect |
|---|---|---|
| CL-R1 | P2 | The status says the note does not select skill changes, and the document has questions rather than one stable goal/matrix or a review level. No contract decision can be returned from it. |
| CL-R2 | P2 | The interception-stage table is diagnostic only. It supplies no bidirectional contract/package map, useful stopping points, package records, dependency order, or acceptance-cost decision. |
| CL-R3 | P2 | The note lists four workflow surfaces to examine without assigning schema, admission, acceptance, audit, invalidation, or fixed-point effects to one owner each. A literal implementation could duplicate checks or create a new phase. |
| CL-R4 | P3 | The `Source Evidence` section names target-repository artifacts unavailable here and presents their conclusions without a local evidence class. They may motivate CL-D2 through CL-D6 but cannot prove this skill contract. |
| CL-U1 | Required authority unknown | Will the main agent accept CL1-CL8 below as a mechanism-only normalization of CL-G1? If any row changes behavior rather than preserving the supplied goal, user acceptance is required. |
| CL-U2 | Required plan-identity unknown | After the proposal adopts or references the accepted matrix and CL-P1/CL-P2 records, what exact plan-owning content and dependency blobs receive the next independent `implementation-plan-fixed-point` decision? |

There is no required target-repository evidence unknown: that evidence is an
explicit non-goal and is not needed to decide the user-authorized workflow
contract. No implementation package may start while CL-U1 or CL-U2 remains.

## Candidate sole CL contract authority

These terms are local to the candidate:

- A **realization disposition** is the current evidence that one accepted
  contract ID is implemented by an adequate owner capability, required
  information/state, transaction behavior, and assertion-level scenario. It is
  a logical relation and does not require a new file or private data shape.
- **Decision-active** means the current workflow decision must disposition the
  contract itself; adjacent success, a broad gate, or an implementer summary
  cannot silently stand in for it.
- A **dependent authority or evidence claim** is a plan, owner-map,
  architecture, scenario, or test claim whose truth relies on a selected design
  decision.

If product authority accepts this normalization, CL1-CL8 become the sole
normative outcomes. The incident narrative, stage table, plan records, and
fixtures then reference these IDs and do not redefine them.

| ID | Candidate observable contract | Semantic owner | Public composition | Deterministic evidence | External | Telemetry | Status |
|---|---|---|---|---|---|---|---|
| CL1 | Every accepted contract ID in an admitted delivery package has one current realization disposition from pre-edit completeness through implementation handoff and parent acceptance. Missing, unproved, or stale parts remain visible and block the current decision. | SIL contract-and-scenario lifecycle; independently audited by EER | Accepted plan → SIL establishment and assignment → handoff → parent acceptance | CL-D1 and CL-D7 | Not applicable: repository workflow | Not applicable: no metric decides it | Candidate; CL-U1 pending |
| CL2 | An ownership requirement maps to a concrete owner capability or operation that can observe and enforce every required ownership partition. Convenient lookup or mutation that cannot distinguish those partitions is insufficient; absence of a feasible capability blocks implementation and returns to the owning design decision. | SIL realization schema and pre-edit admission | Contract row → selected owner capability → composed ownership scenarios | CL-D1 and CL-D2 | Not applicable | Not applicable | Candidate; CL-U1 pending |
| CL3 | Required identity, provenance, or other immutable information maps to concrete produced or persisted state and its consumer path. Conditional private layout does not make accepted information optional. | SIL realization schema and pre-edit admission | Contract row → state producer/lifetime → consuming behavior and assertion | CL-D1 and CL-D3 | Not applicable | Not applicable | Candidate; CL-U1 pending |
| CL4 | Every accepted transaction requirement maps to concrete ordered admission, mutation, publication/commit, abort, retry, and recovery operations plus assertions for the applicable success and failure partitions. | SIL realization schema and pre-edit admission | Contract row → ordered owner operations → focused transaction scenarios | CL-D1 and CL-D4 | Not applicable | Not applicable | Candidate; CL-U1 pending |
| CL5 | Each required evidence scenario maps to its observable invariant, adversarial partitions, and assertions. Renaming or substituting a test is accepted only when its assertions retain the same positive and negative decision power. | SIL scenario lifecycle; EER owns independent assertion audit | Scenario claim → concrete assertions → owner/public behavior | CL-D1 and CL-D5 | Not applicable | Not applicable | Candidate; CL-U1 pending |
| CL6 | A design change identifies every dependent authority and evidence claim and makes affected realization dispositions stale until each is retained with dependency proof, strengthened, replaced, or deleted. A changed contract or plan-owning dependency also triggers the existing review-fixpoint invalidation boundary. | SIL package reconciliation; existing review-fixpoint boundary for plan identity | Selected design change → dependency impact → updated package/evidence dispositions | CL-D6 | Not applicable | Not applicable | Candidate; CL-U1 pending |
| CL7 | Existing SIL pre-edit and parent-acceptance decisions reject incomplete or stale realization coverage using focused evidence before the one canonical gate. No new phase or repeated full gate is added, and package acceptance never replaces the final independent Tick. | SIL entrypoint admission and parent acceptance; existing review-fixpoint gate topology | Package establishment/handoff → parent decision → existing canonical gate → Tick | CL-D2 through CL-D7 | Not applicable | Not applicable | Candidate; CL-U1 pending |
| CL8 | Independent implementation review traces every accepted contract through the actual owner operation, state/information, transaction order, and assertion, and audits design-change invalidation. A green canonical gate cannot clear missing or stale contract evidence. | EER implementation-review mechanics; consumed by review-fixpoint Tick | Exact implementation and accepted baseline → EER contract-cell review → fixpoint decision | CL-D7 plus CL-D2 through CL-D6 as adversarial cases | Not applicable | Not applicable | Candidate; CL-U1 pending |

### Candidate deterministic scenario portfolio

| Fixture | Contracts | Observable result and localization |
|---|---|---|
| CL-D1 — complete realization | CL1-CL7 | A package maps ownership, information, transaction, and evidence rows to adequate concrete capabilities/state/assertions; SIL may proceed through parent acceptance. A failure localizes to the first incomplete row, not to a broad gate. |
| CL-D2 — ownership capability absent | CL1, CL2, CL7, CL8 | A generic lookup/mutation path cannot distinguish absent, predeclared, same-owned-group, and foreign ownership. Pre-edit completeness blocks and EER would report the owner-operation gap. |
| CL-D3 — required information absent | CL1, CL3, CL7, CL8 | The selected representation cannot produce or retain required identity/provenance. Conditional layout does not waive the information row; pre-edit or parent acceptance blocks. |
| CL-D4 — transaction only partly proved | CL1, CL4, CL7, CL8 | Successful publication or rollback does not prove admission-before-mutation, atomic group commit, retry, and recovery partitions. The transaction row remains unresolved. |
| CL-D5 — weaker evidence substitute | CL1, CL5, CL7, CL8 | A renamed test lacks the negative-authority assertion of the accepted scenario. Name or broad pass status cannot establish assertion parity, so acceptance blocks. |
| CL-D6 — design dependency changed | CL1, CL6, CL7, CL8 | A representation change leaves old owner-map, architecture, or evidence claims active. Affected dispositions become stale until dependency-aware retain/strengthen/replace/delete decisions complete. |
| CL-D7 — green gate with missing row | CL1, CL7, CL8 | Focused or canonical checks pass while one realization row or assertion is absent. Parent acceptance rejects it when visible; otherwise the independent Tick reports a finding or required unknown. The gate is neither moved nor repeated. |

These are deterministic source/contract fixtures. They can establish instruction
and owner conformance after implementation; they cannot prove model efficacy.

## Smallest faithful mechanism and owner boundaries

The smallest faithful mechanism is to extend the existing contract-first
package matrix and acceptance packet with a compact realization disposition per
accepted contract ID, carry only its current delta through existing SIL
handoffs, and make incomplete or stale dispositions decision-bearing at the
existing pre-edit and parent-acceptance boundaries. It reuses stable IDs,
scenario records, package handoffs, and existing plan invalidation. A new
ledger, checklist artifact, reviewer role, review phase, or canonical gate is
unnecessary.

| Concern | One owner and required effect |
|---|---|
| Stable CL behavior | The accepted proposal matrix owns CL1-CL8 once. Rationale and plan text use ID references. |
| Realization schema, scenario lifecycle, and design-dependency disposition | `supervised-implementer-loop/references/contract-and-scenario-package.md`. It defines the generic relation and when it is complete, blocked, or stale without prescribing storage. |
| Pre-edit assignment, compact handoff, and parent acceptance | `supervised-implementer-loop/SKILL.md`. It consumes the relation at existing boundaries and rejects missing coverage; it does not create review vocabulary. |
| Independent source/state/assertion audit | `evidence-efficient-review/references/implementation-review.md`. It verifies rather than authors the realization disposition and reports findings/unknowns. The EER entrypoint already routes implementation review and needs no duplicate schema. |
| Result levels, plan invalidation, one canonical gate, and final Tick | Existing review-fixpoint sources. No review-fixpoint change is proposed. When a design change reaches plan-owning content, the existing invalidation rule applies; otherwise SIL/EER reconcile the package-local dependency evidence. |

Current source has the right anchors but not their complete composition: SIL
already carries a contract matrix, plan identity, scenarios, and a compact
acceptance packet; EER already challenges identity/provenance and compares test
names with assertions; review-fixpoint already invalidates changed plan
dependencies. None requires a per-contract mapping from the accepted row to
concrete operations, information/state, transaction order, and assertions
through pre-edit and parent acceptance. This is the source-grounded gap.

## Candidate ordered delivery plan

Proposal normalization and acceptance are a specification checkpoint, not a
delivery package. After CL-U1 is resolved and a fresh independent plan review
binds CL-U2, the production plan has exactly two useful delivery packages:

| Package | Establishing contracts | Order | Candidate status |
|---|---|---|---|
| CL-P1 — SIL realization continuity | CL1, CL2, CL3, CL4, CL5, CL6, CL7 | First | Complete candidate; authority pending |
| CL-P2 — independent realization audit | CL8 | Second; consumes accepted CL-P1 semantics | Complete candidate; authority pending |

Every CL ID appears in exactly one package and each package establishes at least
one complete ID. Diagnostic stages and internal edits are not additional
packages.

### CL-P1 — SIL realization continuity

- **Useful outcome:** If work stops after CL-P1, SIL keeps every accepted
  owner, information, transaction, and evidence row current from pre-edit
  completeness through handoff and parent acceptance. Missing capability,
  state, assertion, or stale design dependency blocks before the canonical
  gate; the existing final Tick remains available.
- **Semantic and physical owner:** the SIL package reference owns the generic
  realization relation and scenario/dependency lifecycle; the SIL entrypoint
  owns its use at establishment, assignment, handoff, and parent acceptance.
  Exact headings or private record shape are conditional implementation detail.
- **Prerequisites and order:** accepted CL1-CL8 authority and a durable
  `implementation-plan-fixed-point` for the unchanged CL-P1/CL-P2 plan. It is
  the first production package.
- **State and lifetime:** one logical disposition keyed by each existing stable
  contract ID lives for the admitted work package and is carried by delta after
  initial assignment. No new durable global registry is required.
- **Transaction and recovery closure:** completeness is established before
  production edits; design changes mark dependent rows stale before continued
  work or acceptance; unresolved rows return to the owning contract, design, or
  plan decision. Unaffected rows carry forward only when dependencies remain
  unchanged.
- **Public skill surface:** the existing package matrix, scenario portfolio,
  initial assignment, delivery-package acceptance packet, and parent
  acceptance decision.
- **Focused evidence:** CL-D1 through CL-D6, SIL package validation, relative
  links, and source checks that the reference owns schema while the entrypoint
  only consumes it.
- **Safe deferred work:** CL-P2's independent reviewer audit. CL-P1 does not
  claim fixed point or remove the existing Tick backstop.
- **Split/combine decision:** keep CL1-CL7 together because partial lifecycle
  enforcement would recreate the loss between pre-edit, handoff, invalidation,
  and parent acceptance. Keep CL-P2 separate because it has an independent
  reviewer owner and CL-P1 is already a useful pre-gate stopping point.
- **Acceptance-cost topology:** use focused row completeness and adversarial
  fixtures at existing SIL decisions, then parent acceptance. Do not run the
  canonical gate yet and do not add another review phase.

### CL-P2 — independent realization audit

- **Useful outcome:** If work stops after CL-P2, EER independently traces every
  accepted row through actual owner operations, information/state,
  transactions, and assertions; missing or stale coverage remains a finding or
  required unknown even after green broad checks.
- **Semantic and physical owner:** EER implementation-review mechanics. The
  entrypoint already routes this review and needs no copied trace schema.
- **Prerequisites and order:** accepted CL-P1 and its stable realization
  semantics. CL-P2 is second.
- **State and lifetime:** the reviewer consumes the accepted matrix and SIL
  disposition as navigation evidence, then verifies current source directly.
  It creates no implementation state and never authors remediation evidence.
- **Transaction and recovery closure:** review is read-only. Any incomplete or
  stale row blocks the review result and returns to remediation; it is not
  cleared by adjacent success or by the canonical gate.
- **Public skill surface:**
  `evidence-efficient-review/references/implementation-review.md` only.
- **Focused evidence:** CL-D2 through CL-D7, EER package validation, owner/source
  searches, and a composed scenario showing that implementation review reports
  the missing row.
- **Safe deferred work:** no skill mechanism. After parent acceptance, the
  existing workflow creates one coherent Tock commit, runs the canonical gate
  once on that exact revision, and invokes the persistent independent Tick.
- **Split/combine decision:** do not combine with CL-P1 because SIL authors and
  consumes package evidence while EER independently verifies it; merging them
  would blur authority and independence. Do not split CL-P2 by requirement type
  because one contract-cell review already covers the four dimensions.
- **Acceptance-cost topology:** focused EER validation and parent acceptance,
  followed by one existing exact-revision canonical gate for the completed
  Tock and one final independent Tick. No repeated full review or earlier gate.

### Candidate plan identity

The identity-bearing scope is the accepted CL1-CL8 rows, CL-D1-CL-D7 fixtures,
CL-P1/CL-P2 map and records, and the dependency contracts represented at this
baseline by:

- SIL entrypoint `0c5c73258e43166e1d38f98e054079144e39725d`;
- SIL package reference `bd31cd7f5eab1e79d974006266123ac12f1230ac`;
- EER implementation-review reference
  `a1a4a520dbb31cee859802ca3cc5687b78edfe19`; and
- review-fixpoint contract boundary
  `b93565b492593b712a245b37adf6f4ff33d452cf`.

This is a candidate identity description, not a current plan result. The next
review must record the exact adopted proposal/review content and recheck any
dependency whose blob changed.

## Required specification-cell dispositions

| Cell | Raw note | Candidate normalization/plan |
|---|---|---|
| Single normative authority | **Not cleared — CL-R1.** | Structurally complete CL1-CL8 authority; CL-U1 must accept it before it is normative. |
| Behavioral design trace | **Not cleared.** No stable goal record or separate status lanes. | CL-G1 record is complete; behavioral partial and mechanism not-started remain separate; CL-U1 pending. |
| Durable contract boundary | Partial semantic narrative only. | **Cleared as candidate.** Rows require outcomes and mappings, not a private representation or new artifact. |
| Scenario diagnosability | Incident examples exist but are not a repository-local portfolio. | **Cleared as candidate.** CL-D1-CL-D7 name outcomes and localization. |
| Evidence topology | **Not cleared — CL-R4.** Target reports are unclassified and unavailable. | **Cleared as candidate.** Fixtures are deterministic source/contract evidence; target reports are motivation only. |
| External freshness | Not applicable. | Not applicable: no external capability. |
| Telemetry decision power | Not applicable. | Not applicable: no telemetry. |
| Exact-limit justification | Not applicable. | Not applicable: no numeric limit. |
| Defensive actionability | No product defense proposed. | **Cleared.** The user-authorized direct scenario requires the workflow decision; the smallest response reuses existing records and gates without product machinery. |
| Change locality | Surfaces are listed without one owner per effect. | **Cleared as candidate** by the owner table; exact private placement remains conditional. |
| Workflow boundary | Non-goals reject a new phase/gate. | **Cleared as candidate.** Existing SIL decisions, EER review, and review-fixpoint phases remain. |
| Decision level and plan disposition | **Not cleared — CL-R1.** | Contract and plan decisions are separate; neither result is returned while CL-U1/CL-U2 remain. |
| Contract-to-package coverage | **Not cleared — CL-R2.** | **Cleared as candidate.** CL1-CL7 map once to CL-P1 and CL8 once to CL-P2; both packages are nonempty. |
| Useful stopping point | Interception stages are checkpoints, not packages. | **Cleared as candidate.** CL-P1 supplies pre-gate continuity; CL-P2 supplies independent audit. |
| Cohesion and transaction closure | Unknown. | **Cleared as candidate.** CL-P1 closes one SIL lifecycle; CL-P2 is one read-only review transaction. |
| Dependency order | Unknown. | **Cleared as candidate.** Accepted authority → CL-P1 → CL-P2 → existing canonical gate → Tick. |
| Package-size tradeoff | Unknown. | **Cleared as candidate.** SIL lifecycle effects stay together; independent reviewer ownership stays separate. |
| Acceptance-cost topology | **Not cleared — CL-R2/R3.** | **Cleared as candidate.** Focused checks at existing decisions, one final canonical gate, one independent Tick. |
| Checkpoint/package distinction | The stage table explicitly contains interception points only. | **Cleared as candidate.** Proposal adoption is a checkpoint; only CL-P1 and CL-P2 are delivery packages. |

No plan-content cell remains semantically unspecified in the candidate. The
plan result is blocked by authority and durable identity, not by an invitation
to invent implementation details.

## Exact owning corrections

### CL-R1 — replace diagnostic-only status with a candidate authority

Replace the opening status and the `Questions For A Later Improvement Design`
section with this text, followed by the accepted form of the matrix above:

> Status: candidate CL-G1 contract and implementation plan; not implementation-
> ready until an independent review records the accepted result level and plan
> identity.
>
> CL-G1 and CL1 through CL8 in the contract-and-evidence matrix are the sole
> normative outcomes. The observation and interception-stage sections are
> rationale indexed by CL IDs; they do not redefine those outcomes. Behavioral
> changes require user acceptance. Mechanism-only normalization requires an
> explicit main-agent disposition.

### CL-R2 — add the complete plan, not packages named after stages

Insert the CL-P1/CL-P2 map and complete records from this review after the
accepted matrix. Do not count specification adoption, preflight, handoff,
parent acceptance, the canonical gate, or Tick as separate delivery packages.

### CL-R3 — route one concern to one existing owner

Replace `Existing Workflow Surfaces To Examine` with the owner-boundary table
above. The concrete correction changes only the SIL package reference and
entrypoint in CL-P1 and the EER implementation-review reference in CL-P2.
Review-fixpoint is an unchanged dependency, not a third implementation owner.

### CL-R4 — classify unavailable source reports as motivation

Replace the `Source Evidence` introduction with:

> ## Motivating Target-Repository Report
>
> The following artifacts are not present in this repository and are not
> acceptance evidence for the CL workflow contract. Their reported cases
> motivate CL-D2 through CL-D6. Deterministic acceptance comes from
> repository-local source/contract fixtures that exercise the generic owner
> boundaries without claiming the target findings were independently verified
> here.

The existing artifact names may remain beneath that paragraph as provenance.

## Result, architecture, and validation status

- **Raw-proposal decision:** changes requested.
- **Contract-level decision:** no `contract-fixed-point`; CL-U1 is an unresolved
  authority disposition. The candidate stable cells are otherwise complete.
- **Plan-level decision:** no `implementation-plan-fixed-point`; the candidate
  plan cells are complete, but CL-U1 and CL-U2 prevent a durable plan identity.
- **Implementation admission:** blocked. This review selects no Tock and
  authorizes no production edit.
- **Behavioral status:** partial at the current source baseline.
- **Mechanism status:** not-started.
- **Architecture self-check:** the smallest faithful mechanism reuses the
  existing SIL matrix/handoff and EER review. It adds no new role, phase,
  canonical gate, fixed-point vocabulary, target architecture, or mandatory
  artifact. Review-fixpoint remains unchanged and authoritative for its
  existing concerns.
- **External capability and telemetry:** not applicable.
- **Economic actionability:** satisfied by the accepted direct workflow
  scenario and low-burden reuse of existing decisions; no lasting product
  defense is proposed.

Validation evidence:

- Read the complete proposal and exact-baseline EER specification and
  implementation review authorities, SIL entrypoint and package reference, and
  review-fixpoint result boundary.
- Verified the exact baseline and all identity-bearing source blobs listed
  above.
- Source searches confirmed existing matrix, assertion-review, provenance seam,
  and plan-invalidation anchors, but no complete per-contract realization
  mapping through SIL pre-edit, handoff, and parent acceptance.
- All proposal relative links resolve.
- `quick_validate.py` passed for EER, SIL, and review-fixpoint. These results
  establish current skill-package conformance only; they do not prove the
  proposed behavior or model efficacy.
- `git diff --check` passed before this artifact was written.

Glossary handling remains the explicit opt-out: no glossary was accessed,
created, updated, or proposed. The final clear-technical-writing pass preserves
the distinction between motivating incident claims, candidate behavioral
authority, complete-but-unaccepted plan content, and current source evidence.

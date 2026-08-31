# Improvement Note: Contract Loss During Implementation

Status: [Review 02](improvement-contract-loss-during-implementation-review-02.md)
supplied `contract-fixed-point` and `implementation-plan-fixed-point` for the
exact plan identity. CL-P1 and CL-P2 are implemented and parent-accepted in the
current working tree. Behavioral status remains partial/unproved; exact-
revision/canonical-gate evidence and the independent whole-scope Tick remain
pending. This uncommitted tree is not `deterministic-fixed-point`, and
commit/push remain unauthorized for this package.

## Scope and authority

This note adopts the [Review 01 normalization](improvement-contract-loss-during-implementation-review-01.md)
as a mechanism-only clarification of the supplied workflow goal. [Review
02](improvement-contract-loss-during-implementation-review-02.md) supplied the
two result levels for its unchanged exact identity. CL-G1 and CL1 through CL8
below are the sole
normative authority. The observation, interception stages, deterministic
fixtures, owner boundaries, and delivery records reference those IDs; they do
not redefine them. Any behavioral expansion returns to the user-selected
product authority.

The Review 02 results are current for the unchanged identity; CL-P1 and CL-P2
were subsequently admitted, implemented, and parent-accepted in this working
tree. No `deterministic-fixed-point` is claimed for the uncommitted tree.
Exact-revision/canonical-gate evidence and the independent whole-scope Tick
remain pending. Evidence is deterministic repository source/contract evidence
only; external capability and telemetry are not applicable. Glossary handling
is an explicit opt-out, and terms are defined locally below.

The goal record below carries the normalized CL-G1 identity and direct scenario;
its original status snapshot remains with that record, while current progress
is reported in the current status lane below.

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
  accepted mechanism-only normalization; behavioral changes return to the
  user.
Owning contract: CL1
Behavioral status: partial; current skills carry contracts, scenarios, and a
  final independent review, but do not keep a complete contract-to-operation,
  state, transaction, and assertion mapping decision-active through SIL
  handoffs and parent acceptance.
Mechanism status: not-started; this proposal establishes authority and plan
  content only and does not edit or admit a production skill mechanism.
```

The preserved non-goals are: no new review phase; no earlier or repeated
canonical gate; no target-repository architecture or remediation; no exclusive
blame assignment; and no weakening of persistent independent review.

## Observation

The incident narrative below is preserved as motivation. The target repository
and its reports are unavailable in this repository, so those reports are not
acceptance evidence for the CL workflow contract; the repository-local fixtures
below provide the deterministic source/contract evidence boundary.

The first Slice 7.1 implementation reached its independent Tick with a compact,
mostly coherent protocol kernel and passing canonical gates, but it had lost
several already accepted requirements between specification, design,
implementation, and evidence.

Review 98 inspected exact clean revision
`290e554b495e6391eff752574e17951a34f930c4`, using the accepted design revision
`13665a2c18b301127f16774a684c2ab0688d0b2e` as its baseline. It found two P2
functional and architectural defects and two P3 authority or evidence defects:

1. protocol definition reused arbitrary same-namespace Vars and overwrote their
   roots instead of admitting one complete owned generated group;
2. protocol descriptors and generated Vars omitted required canonical identity
   and definition provenance, publishing zero provenance instead;
3. active owner-map, architecture, and evidence text still required a discarded
   global cache representation after the implementation selected descriptor-
   local packed cells; and
4. an exact required negative-authority scenario was replaced by a differently
   named, weaker test whose assertions could not exclude host protocol
   authority.

The independent Tick caught the failure. The improvement opportunity is to
catch these defects before the expensive exact-revision gate and final review,
without adding repeated full reviews during implementation.

## Why This Was Not Primarily Underspecification

The stable semantic requirements were already explicit:

- `S7-PROTOCOL` required canonical name and provenance, complete generated-Var
  ownership, binding admission before mutation, and atomic group publication;
- the owner map required absent, matching-predeclared, same-owned-group, and
  foreign or colliding binding distinctions;
- the 7.1 design called for a narrow protocol-method-group operation rather
  than direct access to Var or publication records; and
- the evidence portfolio named both the stable protocol-group scenario and the
  negative-authority scenario, with assertion-level behavior rather than names
  alone.

Private storage remained deliberately conditional, but the observable owner,
information, transaction, and evidence requirements did not. The implementation
was therefore free to choose compact descriptor and cache storage; it was not
free to omit binding ownership or provenance.

The primary failure was loss of contract traceability during implementation.
Convenient existing operations were treated as sufficient even though they
could not observe group ownership, and a compact descriptor representation was
accepted without accounting for all immutable identity facts. The focused
tests exercised successful definition, redeclaration, rollback, dispatch, and
cache behavior, but did not challenge foreign ownership, cross-protocol reuse,
same-name collision, matching predeclaration, or provenance.

The remaining two findings show related trace failures. A design change did not
invalidate every active authority and evidence row that depended on the old
cache representation, and a required scenario name was treated as replaceable
without proving that the substitute assertions carried the same negative
power.

This is not usefully classified as implementer error alone. The implementer
made unsound local choices, but the package also passed through design
settlement, focused verification, parent acceptance, documentation settlement,
and a canonical gate without those choices being rejected. The workflow
retained the requirements but did not keep them decision-active at each
handoff.

## Diagnostic interception stages

The table preserves the incident rationale. Each stage is indexed by the
normative CL IDs and fixtures below; no stage is a contract, delivery package,
role, phase, gate, or artifact requirement.

| Stage | Evidence already available | Failure signal that could have been noticed |
| --- | --- | --- |
| Specification review | The owner, immutable information, transaction, and named scenarios were explicit. | No defect for F98.1 or F98.2: this stage had already supplied the required semantics. Treating conditional layout as conditional behavior would have been a downstream misread. |
| Package and checkpoint design | The package map assigned generated-group ownership and provenance to 7.1; the design named a new narrow group-publication seam. | An exit check on the checkpoint could have asked whether the selected calls could distinguish foreign, predeclared, and same-group bindings and could carry real provenance. Ordinary name lookup and root staging plainly could not. |
| Implementer preflight | The implementer had the complete package, current owner operations, and named evidence portfolio. | A contract-to-operation and contract-to-persisted-information comparison would have exposed the missing ownership observation and absent provenance fields before production edits accumulated. |
| Focused scenario design | Collision classes, atomic retry, provenance, and negative host authority were stable observable partitions. | The planned assertions omitted the cases most likely to falsify the shortcut. Comparing scenario claims with assertions would also have rejected the weaker renamed negative test. |
| Implementation handoff | Changed owners, non-mechanical decisions, focused results, and unresolved risks were available for a compact handoff. | A package could not show how the group-ownership and provenance cells were satisfied. Successful rollback and broad checks were adjacent evidence, not proof of those cells. |
| Parent slice acceptance | The parent could inspect concise diffs, symbol and state inventories, forbidden-dependency searches, and a few independently selected probes. | A foreign-Var protocol definition probe exposed F98.1 immediately. A search for zero provenance at generated publication exposed F98.2. A search for the exact required scenario name exposed F98.4. |
| Design-change reconciliation | The descriptor-local cache decision named the superseded global-table mechanism. | Searching all active authorities and evidence rows for the removed capacity, insertion, revision, and reclamation model would have exposed F98.3 before the package gate. |
| Canonical deterministic gate | Formatting, builds, prior regressions, release checks, and the supplied focused tests all passed. | This gate could not prove assertions that did not exist. It correctly established broad preservation, not contract completeness; making it earlier or running it again would not have found the omissions. |
| Independent Tick | The exact clean revision and complete contract baseline were available to an independent reviewer. | Review 98 found all four defects. This stage worked, but only after the package incurred late rework and a canonical-gate cycle. |

The earliest practical detection point differed by finding. F98.1 and F98.2
could have been blocked when the just-in-time design was connected to concrete
owner operations, or by focused negative tests before implementation
acceptance. F98.3 belonged to dependency invalidation when the cache design
changed. F98.4 belonged to assertion-level evidence comparison as soon as the
required scenario was implemented under another name.

The normalized delivery map and package records below remain identity-bearing
plan content; their current result and implementation status are recorded in
the current status section without changing assignment or closure fields.

## Sole CL contract authority

These terms are local to this proposal:

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

CL-G1 and CL1 through CL8 are the sole normative outcomes. The incident
narrative, diagnostic stages, delivery records, and fixtures reference these
IDs and do not redefine them.

The matrix status cells below preserve the normalized contract snapshot; the
current Review 02 result and implementation status are recorded in the current
status section below without changing the contract cells.

| ID | Accepted observable contract | Semantic owner | Public composition | Deterministic evidence | External | Telemetry | Status |
|---|---|---|---|---|---|---|---|
| CL1 | Every accepted contract ID in an admitted delivery package has one current realization disposition from pre-edit completeness through implementation handoff and parent acceptance. Missing, unproved, or stale parts remain visible and block the current decision. | SIL contract-and-scenario lifecycle; independently audited by EER | Accepted plan → SIL establishment and assignment → handoff → parent acceptance | CL-D1 and CL-D7 | Not applicable: repository workflow | Not applicable: no metric decides it | Accepted mechanism-only normalization; no fixed-point result; plan review pending |
| CL2 | An ownership requirement maps to a concrete owner capability or operation that can observe and enforce every required ownership partition. Convenient lookup or mutation that cannot distinguish those partitions is insufficient; absence of a feasible capability blocks implementation and returns to the owning design decision. | SIL realization schema and pre-edit admission | Contract row → selected owner capability → composed ownership scenarios | CL-D1 and CL-D2 | Not applicable | Not applicable | Accepted mechanism-only normalization; no fixed-point result; plan review pending |
| CL3 | Required identity, provenance, or other immutable information maps to concrete produced or persisted state and its consumer path. Conditional private layout does not make accepted information optional. | SIL realization schema and pre-edit admission | Contract row → state producer/lifetime → consuming behavior and assertion | CL-D1 and CL-D3 | Not applicable | Not applicable | Accepted mechanism-only normalization; no fixed-point result; plan review pending |
| CL4 | Every accepted transaction requirement maps to concrete ordered admission, mutation, publication/commit, abort, retry, and recovery operations plus assertions for the applicable success and failure partitions. | SIL realization schema and pre-edit admission | Contract row → ordered owner operations → focused transaction scenarios | CL-D1 and CL-D4 | Not applicable | Not applicable | Accepted mechanism-only normalization; no fixed-point result; plan review pending |
| CL5 | Each required evidence scenario maps to its observable invariant, adversarial partitions, and assertions. Renaming or substituting a test is accepted only when its assertions retain the same positive and negative decision power. | SIL scenario lifecycle; EER owns independent assertion audit | Scenario claim → concrete assertions → owner/public behavior | CL-D1 and CL-D5 | Not applicable | Not applicable | Accepted mechanism-only normalization; no fixed-point result; plan review pending |
| CL6 | A design change identifies every dependent authority and evidence claim and makes affected realization dispositions stale until each is retained with dependency proof, strengthened, replaced, or deleted. A changed contract or plan-owning dependency also triggers the existing review-fixpoint invalidation boundary. | SIL package reconciliation; existing review-fixpoint boundary for plan identity | Selected design change → dependency impact → updated package/evidence dispositions | CL-D6 | Not applicable | Not applicable | Accepted mechanism-only normalization; no fixed-point result; plan review pending |
| CL7 | Existing SIL pre-edit and parent-acceptance decisions reject incomplete or stale realization coverage using focused evidence before the one canonical gate. No new phase or repeated full gate is added, and package acceptance never replaces the final independent Tick. | SIL entrypoint admission and parent acceptance; existing review-fixpoint gate topology | Package establishment/handoff → parent decision → existing canonical gate → Tick | CL-D2 through CL-D7 | Not applicable | Not applicable | Accepted mechanism-only normalization; no fixed-point result; plan review pending |
| CL8 | Independent implementation review traces every accepted contract through the actual owner operation, state/information, transaction order, and assertion, and audits design-change invalidation. A green canonical gate cannot clear missing or stale contract evidence. | EER implementation-review mechanics; consumed by review-fixpoint Tick | Exact implementation and accepted baseline → EER contract-cell review → fixpoint decision | CL-D7 plus CL-D2 through CL-D6 as adversarial cases | Not applicable | Not applicable | Accepted mechanism-only normalization; no fixed-point result; plan review pending |

### Deterministic source/contract fixtures

| Fixture | Contracts | Observable result and localization |
|---|---|---|
| CL-D1 — complete realization | CL1-CL7 | A package maps ownership, information, transaction, and evidence rows to adequate concrete capabilities/state/assertions; SIL may proceed through parent acceptance. A failure localizes to the first incomplete row, not to a broad gate. |
| CL-D2 — ownership capability absent | CL1, CL2, CL7, CL8 | A generic lookup/mutation path cannot distinguish absent, predeclared, same-owned-group, and foreign ownership. Pre-edit completeness blocks and EER would report the owner-operation gap. |
| CL-D3 — required information absent | CL1, CL3, CL7, CL8 | The selected representation cannot produce or retain required identity/provenance. Conditional layout does not waive the information row; pre-edit or parent acceptance blocks. |
| CL-D4 — transaction only partly proved | CL1, CL4, CL7, CL8 | Successful publication or rollback does not prove admission-before-mutation, atomic group commit, retry, and recovery partitions. The transaction row remains unresolved. |
| CL-D5 — weaker evidence substitute | CL1, CL5, CL7, CL8 | A renamed test lacks the negative-authority assertion of the accepted scenario. Name or broad pass status cannot establish assertion parity, so acceptance blocks. |
| CL-D6 — design dependency changed | CL1, CL6, CL7, CL8 | A representation change leaves old owner-map, architecture, or evidence claims active. Affected dispositions become stale until dependency-aware retain/strengthen/replace/delete decisions complete. |
| CL-D7 — green gate with missing row | CL1, CL7, CL8 | Focused or canonical checks pass while one realization row or assertion is absent. Parent acceptance rejects it when visible; otherwise the independent Tick reports a finding or required unknown. The gate is neither moved nor repeated. |

These are deterministic source/contract fixtures. Source/package validators
establish structure and owner conformance only; they do not prove model
efficacy, external capability, telemetry, or the unavailable target reports.

## One-owner boundaries

| Concern | One owner and required effect |
|---|---|
| Stable CL behavior | The accepted proposal matrix owns CL1-CL8 once. Rationale and plan text use ID references. |
| Realization schema, scenario lifecycle, and design-dependency disposition | [`supervised-implementer-loop` package reference](../skills/supervised-implementer-loop/references/contract-and-scenario-package.md). It defines the generic relation and when it is complete, blocked, or stale without prescribing storage. |
| Pre-edit assignment, compact handoff, and parent acceptance | [`supervised-implementer-loop` entrypoint](../skills/supervised-implementer-loop/SKILL.md). It consumes the relation at existing boundaries and rejects missing coverage; it does not create review vocabulary. |
| Independent source/state/assertion audit | [`evidence-efficient-review` implementation-review reference](../skills/evidence-efficient-review/references/implementation-review.md). It verifies rather than authors the realization disposition and reports findings/unknowns. The EER entrypoint already routes implementation review and needs no duplicate schema. |
| Result levels, plan invalidation, one canonical gate, and final Tick | Existing [`review-fixpoint` sources](../skills/review-fixpoint/SKILL.md). No review-fixpoint change is proposed. When a design change reaches plan-owning content, the existing invalidation rule applies; otherwise SIL/EER reconcile the package-local dependency evidence. |

The smallest faithful mechanism is to extend the existing contract-first
package matrix and acceptance packet with a compact realization disposition per
accepted contract ID, carry only its current delta through existing SIL
handoffs, and make incomplete or stale dispositions decision-bearing at the
existing pre-edit and parent-acceptance boundaries. It reuses stable IDs,
scenario records, package handoffs, and existing plan invalidation. A new
ledger, checklist artifact, reviewer role, review phase, or canonical gate is
unnecessary.

## Ordered delivery plan

Normalization and proposal acceptance are a specification checkpoint, not a
delivery package. After the accepted authority is independently bound to the
unchanged plan identity, the production plan has exactly two useful delivery
packages:

| Package | Establishing contracts | Order | Status |
|---|---|---|---|
| CL-P1 — SIL realization continuity | CL1, CL2, CL3, CL4, CL5, CL6, CL7 | First | Complete normalized record; independent plan review pending |
| CL-P2 — independent realization audit | CL8 | Second; consumes accepted CL-P1 semantics | Complete normalized record; independent plan review pending |

Every CL ID appears in exactly one package and each package establishes at least
one complete ID. Diagnostic stages and internal edits are not additional
packages. No implementation package is admitted from this proposal alone.

### CL-P1 — SIL realization continuity

- **Useful outcome:** If work stops after CL-P1, SIL keeps every accepted
  owner, information, transaction, and evidence row current from pre-edit
  completeness through handoff and parent acceptance. Missing capability,
  state, assertion, or stale design dependency blocks before the canonical
  gate; the existing final Tick remains available.
- **Semantic and physical owner:** The
  [`SIL package reference`](../skills/supervised-implementer-loop/references/contract-and-scenario-package.md)
  owns the generic realization relation and scenario/dependency lifecycle; the
  [`SIL entrypoint`](../skills/supervised-implementer-loop/SKILL.md) owns its
  use at establishment, assignment, handoff, and parent acceptance. Exact
  headings or private record shape are conditional implementation detail.
- **Prerequisites and order:** Accepted CL1-CL8 authority and an independent
  `implementation-plan-fixed-point` for the unchanged CL-P1/CL-P2 plan. It is
  the first production package; no such result is claimed here.
- **State and lifetime:** One logical disposition keyed by each existing stable
  contract ID lives for the admitted work package and is carried by delta
  after initial assignment. No new durable global registry is required.
- **Transaction and recovery closure:** Completeness is established before
  production edits; design changes mark dependent rows stale before continued
  work or acceptance; unresolved rows return to the owning contract, design,
  or plan decision. Unaffected rows carry forward only when dependencies remain
  unchanged.
- **Public/ABI skill surface:** The existing package matrix, scenario
  portfolio, initial assignment, delivery-package acceptance packet, and parent
  acceptance decision.
- **Focused evidence:** CL-D1 through CL-D6, SIL package validation, relative
  links, and source checks that the reference owns schema while the entrypoint
  only consumes it.
- **Safe deferred work:** CL-P2's independent reviewer audit. CL-P1 does not
  claim fixed point or remove the existing Tick backstop.
- **Split/combine decision:** Keep CL1-CL7 together because partial lifecycle
  enforcement would recreate the loss between pre-edit, handoff, invalidation,
  and parent acceptance. Keep CL-P2 separate because it has an independent
  reviewer owner and CL-P1 is already a useful pre-gate stopping point.
- **Acceptance-cost topology:** Use focused row completeness and adversarial
  fixtures at existing SIL decisions, then parent acceptance. Do not run the
  canonical gate yet and do not add another review phase.

### CL-P2 — independent realization audit

- **Useful outcome:** If work stops after CL-P2, EER independently traces every
  accepted row through actual owner operations, information/state,
  transactions, and assertions; missing or stale coverage remains a finding or
  required unknown even after green broad checks.
- **Semantic and physical owner:** The
  [`EER implementation-review reference`](../skills/evidence-efficient-review/references/implementation-review.md)
  owns implementation-review mechanics. The entrypoint already routes this
  review and needs no copied trace schema.
- **Prerequisites and order:** Accepted CL-P1 and its stable realization
  semantics. CL-P2 is second.
- **State and lifetime:** The reviewer consumes the accepted matrix and SIL
  disposition as navigation evidence, then verifies current source directly.
  It creates no implementation state and never authors remediation evidence.
- **Transaction and recovery closure:** Review is read-only. Any incomplete or
  stale row blocks the review result and returns to remediation; it is not
  cleared by adjacent success or by the canonical gate.
- **Public/ABI skill surface:** The
  [`EER implementation-review reference`](../skills/evidence-efficient-review/references/implementation-review.md)
  only.
- **Focused evidence:** CL-D2 through CL-D7, EER package validation,
  owner/source searches, and a composed scenario showing that implementation
  review reports the missing row.
- **Safe deferred work:** No skill mechanism is admitted by this proposal.
  After parent acceptance, the existing workflow creates one coherent Tock
  commit, runs the canonical gate once on that exact revision, and invokes the
  persistent independent Tick.
- **Split/combine decision:** Do not combine with CL-P1 because SIL authors
  and consumes package evidence while EER independently verifies it; merging
  them would blur authority and independence. Do not split CL-P2 by requirement
  type because one contract-cell review already covers the four dimensions.
- **Acceptance-cost topology:** Focused EER validation and parent acceptance,
  followed by one existing exact-revision canonical gate for the completed
  Tock and one final independent Tick. No repeated full review or earlier gate.

### Plan identity boundary

The identity-bearing scope is the accepted CL1-CL8 rows, CL-D1-CL-D7 fixtures,
CL-P1/CL-P2 map and records, and the dependency contracts represented at this
baseline by:

- SIL entrypoint `0c5c73258e43166e1d38f98e054079144e39725d`;
- SIL package reference `bd31cd7f5eab1e79d974006266123ac12f1230ac`;
- EER implementation-review reference
  `a1a4a520dbb31cee859802ca3cc5687b78edfe19`; and
- review-fixpoint contract boundary
  `b93565b492593b712a245b37adf6f4ff33d452cf`.

This is the identity description for Review 02's pre-implementation plan
result. Review 02 bound the listed dependency blobs at that baseline. Accepted
CL-P1 and CL-P2 intentionally changed the three implementing owner surfaces
(the SIL entrypoint, SIL package reference, and EER implementation-review
reference) under that plan; only the review-fixpoint boundary remains unchanged.
The accepted CL rows, fixtures, package records/order, and owner routing remain
unchanged. Current implementation blobs belong to the pending whole-scope
review and exact-revision/canonical-gate evidence. No
`deterministic-fixed-point` is claimed for the uncommitted working tree.
Exact-revision/canonical-gate evidence and the independent whole-scope Tick
remain pending.

## Current status after Review 02 and CL-P1/CL-P2

[Review 02](improvement-contract-loss-during-implementation-review-02.md)
supplied `contract-fixed-point` and `implementation-plan-fixed-point` for the
exact identity above, with no findings or required unknowns. SIL admitted both
packages; CL-P1 and CL-P2 were implemented and parent-accepted in the current
working tree. This records mechanism progress only; it does not establish model
adherence or efficacy.

The current working tree has not passed the exact-revision/canonical-gate
evidence or the independent whole-scope implementation Tick. It is uncommitted,
so no `deterministic-fixed-point` can be claimed and commit/push remain
unauthorized for this package. External capability and telemetry remain not
applicable. Glossary handling remains the explicit opt-out.

## Review 01 dispositions

| ID | Disposition |
|---|---|
| CL-R1 | Resolved by the CL-G1 goal record and sole CL1-CL8 authority. The status distinguishes accepted normalization from review results and implementation admission. |
| CL-R2 | Resolved by the bidirectional CL ID/package map, useful stopping points, complete package records, dependency order, split/combine choices, and acceptance-cost topology. |
| CL-R3 | Resolved by the one-owner table. Existing SIL, EER, and review-fixpoint authorities remain local to their concerns; no duplicate phase or mechanics are introduced. |
| CL-R4 | Resolved by classifying unavailable target-repository reports as motivation only and using CL-D1-CL-D7 as repository-local deterministic source/contract fixtures. |
| CL-U1 | Resolved: the main agent accepted CL-G1 and CL1-CL8 as mechanism-only normalization. Any behavioral expansion remains user-owned. |
| CL-U2 | Resolved by [Review 02](improvement-contract-loss-during-implementation-review-02.md): the exact unchanged CL-P1/CL-P2 plan and its dependency blobs are bound to `implementation-plan-fixed-point`. |

Current status lanes are deliberately separate:

- **Contract authority:** CL-G1 and CL1-CL8 remain the sole accepted
  mechanism-only normalized authority. Review 02 supplied
  `contract-fixed-point` for the exact unchanged identity; this is not a
  behavioral expansion.
- **Plan:** CL-P1 and CL-P2 remain the complete normalized records with exact
  cardinality and closure. Review 02 supplied
  `implementation-plan-fixed-point` for that unchanged identity.
- **Implementation admission:** CL-P1 and CL-P2 were admitted, implemented,
  and parent-accepted in the current working tree; the exact-revision/canonical
  gate and independent whole-scope Tick remain pending.
- **Behavioral:** partial/unproved. CL-P1/P2 mechanism evidence does not
  establish model adherence or efficacy.
- **Mechanism:** CL-P1 and CL-P2 are implemented and parent-accepted in the
  current working tree. No `deterministic-fixed-point` can be claimed before
  the authorized commit and exact-revision evidence.
- **Evidence:** CL-D1-CL-D7 and proposal validators are deterministic
  source/contract evidence for structure, links, ownership, and localization
  only. They do not establish model adherence, model capability, telemetry, or
  external target findings.
- **External and telemetry:** not applicable.
- **Glossary:** explicit opt-out; no glossary was accessed, created, updated,
  or proposed.

## Non-Goals

- This note does not propose exact skill wording, new mandatory artifacts, or a
  new review phase.
- It does not prescribe the Slice 7 remediation or change the target
  repository's architecture.
- It does not assign the failure exclusively to the implementer, parent, spec
  author, or reviewer.
- It does not recommend earlier or repeated canonical gates; the observed gate
  lacked the missing assertions and could not decide these findings.
- It does not weaken reviewer independence. The final Tick remains the
  backstop that established the failure on an exact clean revision.

## Motivating Target-Repository Report

The following artifacts are not present in this repository and are not
acceptance evidence for the CL workflow contract. Their reported cases
motivate CL-D2 through CL-D6. Deterministic acceptance comes from
repository-local source/contract fixtures that exercise the generic owner
boundaries without claiming the target findings were independently verified
here.

- `clojure-wasm/docs/stage2/review98.md`, especially F98.1-F98.4 and its
  contract ledger;
- `clojure-wasm/docs/stage2/07-user-types-and-protocols.md`, S7-PROTOCOL,
  identity rationale, and the required scenario portfolio;
- `clojure-wasm/docs/stage2/07-user-types-and-protocols-owner-map.md`, the 7.1
  owner map and evidence lifecycle; and
- `clojure-wasm/docs/stage2/07-1-protocol-kernel-design.md`, the selected
  cross-owner operations and checkpoint decisions.

## Proposal validation boundary

Review 02 established the exact `contract-fixed-point` and
`implementation-plan-fixed-point` results for the unchanged proposal identity,
and CL-P1/CL-P2 mechanism validation was parent-accepted in the current working
tree. Proposal and mechanism checks remain repository-local structure and
source/contract evidence: relative-link resolution, CL ID/package cardinality,
fixture and package-record completeness, and whitespace checks. They cannot
prove model adherence or efficacy, external capability, telemetry, or the
unavailable target-repository reports. The uncommitted tree has no
`deterministic-fixed-point`; exact-revision/canonical-gate evidence and the
independent whole-scope Tick remain required, and commit/push are unauthorized.

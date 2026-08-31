# Improvement: Even Better Implementation Slicing

## Outcome

`EBS-G1` and `EBS1` through `EBS8` in the contract-and-evidence matrix are the
sole normative behavior authority for this proposal. Delivery-package
assignments reference EBS IDs and are not part of those stable outcomes. They
may be represented as level-scoped matrix fields or a separate plan, and may
change without rewriting observable contract rows.

A review may deliberately stop at `contract-fixed-point`; unresolved
delivery-plan fields remain explicit and block `implementation-plan-fixed-point`
and implementation admission. The remaining sections provide rationale,
plan-record schema, owner routing, and validation cases. They reference EBS IDs
and do not redefine their outcomes.

## Behavioral Goal And Contract Authority

```text
Goal ID: EBS-G1
Behavioral goal: A repository workflow distinguishes a stable contract from an
  implementation-ready package plan and completed implementation, and never
  begins production implementation while delivery-package boundaries remain
  unresolved.
Direct scenario: Given complete semantic contracts and design checkpoints but
  no reviewed delivery-package map, contract review may accept only a
  contract-fixed-point; implementation-plan review reports required plan
  unknowns; and supervised implementation refuses production edits until every
  contract maps to an ordered cohesive delivery package.
Product authority: User-selected proposal; main agent accepts Review 01
  normalization as mechanism-only, with EBS1-EBS8 as the sole normalized
  contract rows.
Owning contract: EBS1
Behavioral status: repository-controlled source composition and deterministic
  contract scenarios pass in the working tree under the accepted integrated Tick;
  external/model capability is not applicable
Mechanism status: all EBS-P1-EBS-P3 mechanisms implemented and integrated
  parent-accepted in the working tree; commit/canonical exact-revision gate and
  any required final exact-revision Tick remain pending
```

The normalized contract-and-evidence matrix is:

| ID | Observable contract | Semantic owner | Public composition | Deterministic evidence | External compatibility | Telemetry | Current status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EBS1 | A decision that could authorize implementation names its level. `contract-fixed-point` clears only contract-required cells and exposes downstream plan unknowns; `implementation-plan-fixed-point` additionally clears the delivery plan and alone authorizes the first delivery package; neither implies completed implementation. | `review-fixpoint` result and fixed-point boundary | Specification review result consumed by a fixpoint caller | D1 and D6 decision cases plus source ownership check | Not applicable: repository-local workflow contract | Not applicable: no metric decides this outcome | Accepted contract; EBS-P1 mechanism parent-accepted in working tree; commit/canonical exact-revision pending |
| EBS2 | Stable semantic contract fields and delivery-package assignments have distinct authority and decision power. The plan references stable contract IDs and may change without rewriting observable contract rows; one ledger may represent both when that distinction remains explicit. | `evidence-efficient-review` specification normalization | Contract review followed by implementation-plan review | D1 and D6 source/structure cases | Not applicable | Not applicable | Accepted contract; EBS-P1 mechanism parent-accepted in working tree; commit/canonical exact-revision pending |
| EBS3 | An `implementation-plan-fixed-point` has a bidirectionally complete relation: each contract has exactly one establishing delivery package, each delivery package establishes at least one complete contract, and neither a design checkpoint nor an internal step counts as a delivery package. | `evidence-efficient-review` specification cells | Package-plan review | D1, D2, and D6 decision cases | Not applicable | Not applicable | Accepted contract; EBS-P1 mechanism parent-accepted in working tree; commit/canonical exact-revision pending |
| EBS4 | Each delivery package leaves a correct and useful public or owner-level behavior if later packages never arrive and records closed ownership, state/lifetime, transaction/recovery, surface, evidence, and safe deferred-work boundaries. | `supervised-implementer-loop` package authority; independently audited by `evidence-efficient-review` | Accepted delivery slice and its realistic composition | D2, D3, D4, D5, and D6 decision cases | Not applicable | Not applicable | Accepted contract; EBS-P2 mechanism parent-accepted in working tree; commit/canonical exact-revision pending |
| EBS5 | Delivery packages are dependency ordered and include a causal split/combine decision based on semantic ownership, transaction closure, useful stopping points, and decision value rather than lines, modules, or convenient code placement. | `supervised-implementer-loop` package authority; independently audited by `evidence-efficient-review` | Ordered slice handoffs within one bounded work package | D2, D3, D4, and D6 decision cases | Not applicable | Not applicable | Accepted contract; EBS-P2 mechanism parent-accepted in working tree; commit/canonical exact-revision pending |
| EBS6 | Supervised implementation refuses production edits without a durable `implementation-plan-fixed-point` for unchanged plan authority, receives the complete accepted map once, and uses delta-only follow-ups. Internal steps may provide focused parent evidence but do not automatically become separately gated delivery packages. | `supervised-implementer-loop` admission and execution | Fixpoint or complex-work handoff into one persistent implementer | D1 and D6 admission cases | Not applicable | Not applicable | Accepted contract; EBS-P2 mechanism parent-accepted in working tree; commit/canonical exact-revision pending |
| EBS7 | Focused checks, parent acceptance, canonical exact-revision gates, and independent Tick review occur at the boundaries owned by their current workflows and only when they decide something material. Plan acceptance or slice acceptance cannot establish `deterministic-fixed-point`. | `review-fixpoint` phase and completion boundary | Tock implementation, exact-revision gate, then persistent-reviewer Tick | D2, D4, D6, and current-owner source checks | Not applicable | Not applicable | Accepted contract; EBS-P1 mechanism parent-accepted in working tree; commit/canonical exact-revision pending |
| EBS8 | `complex-work` remains a thin outer coordinator: it consumes the reviewed level and plan identity, routes review or implementation to the leaf owner, and does not duplicate package schemas, specification cells, admission logic, or Tick/Tock semantics. | `complex-work` routing boundary | Mixed package routed to review-fixpoint, evidence-efficient-review, or supervised-implementer-loop | Current-owner and duplicate-authority source checks | Not applicable | Not applicable | Accepted contract; EBS-P3 integrated parent-accepted working-tree mechanism; commit/canonical exact-revision gate and any required final exact-revision Tick pending |

The delivery-plan relation is intentionally separate from stable contract
outcomes. The complete proposed relation for EBS-U1 through EBS-U3 is the
following ordered map; independent implementation-plan review is a prerequisite
before any package is admitted:

| Delivery package | Establishing contracts | Dependency order | Status |
| --- | --- | --- | --- |
| EBS-P1 | EBS1, EBS2, EBS3, EBS7 | First after an independent `implementation-plan-fixed-point` for the unchanged complete EBS-P1-P3 plan identity | Parent-accepted working-tree mechanism; commit/canonical exact-revision pending |
| EBS-P2 | EBS4, EBS5, EBS6 | Second; consumes EBS-P1's result and plan identity after independent plan review and P1 admission | Parent-accepted working-tree mechanism; commit/canonical exact-revision pending |
| EBS-P3 | EBS8 | Third; consumes EBS-P1's result/identity and EBS-P2's admission boundary | Integrated parent-accepted working-tree mechanism; commit/canonical exact-revision gate and any required final exact-revision Tick pending |

## Ordered Delivery Package Records (EBS3-EBS7)

The records below define the proposed resolution of EBS-U1 through EBS-U3. They
are plan material indexed by the sole EBS matrix; they do not add contract rows
or authorize work before their stated acceptance boundaries.

### EBS-P1 — Contract and implementation-plan review authority

- **Contracts and useful outcome (parent-accepted working-tree mechanism):** EBS-P1 covers EBS1, EBS2, EBS3,
  and EBS7. If work stops here, the intended specification-review authority can
  distinguish a contract result from a plan result, expose downstream plan
  unknowns, and preserve the existing deterministic completion result without
  authorizing production edits.
- **Semantic and physical owner:** EBS1 and EBS7 are owned by the
  `review-fixpoint` result and fixed-point boundary; EBS2 and EBS3 are owned by
  `evidence-efficient-review` normalization and specification cells. The
  proposal, EER reference/entrypoint, and review-fixpoint reference/entrypoint
  are the physical documentation and skill surfaces; physical placement does
  not replace those semantic owners.
- **Dependency order and status:** First after an independent
  `implementation-plan-fixed-point` for the unchanged complete EBS-P1-P3 plan
  identity. The EBS-P1 working-tree mechanism is parent-accepted; commit and
  canonical exact-revision completion remain pending.
- **Prerequisites:** Accepted EBS-G1 and EBS1-EBS8 contract normalization, plus
  an independent `implementation-plan-fixed-point` for the complete unchanged
  delivery plan. No EBS-P1 production-owner edit may be admitted, accepted, or
  continued before that result clears.
- **State and lifetime:** Stable EBS contract rows persist independently of
  the ID-keyed delivery-plan relation. Plan identity covers plan-owning content
  and dependencies; a review-artifact-only commit does not invalidate it, but a
  material plan-owner or dependency change does.
- **Transaction and recovery closure:** The review result records its level,
  contract-cell disposition, plan-cell disposition, and plan identity as one
  durable decision. A stale or invalidated plan result routes back to plan
  review; stable contract evidence is retained only when its owner dependencies
  remain unchanged.
- **Public and skill surface:** `specification-review.md` reports level-scoped
  cells, while `contract-and-evidence-boundary.md` owns result effects and
  invalidation; their entrypoints only route and consume those decisions.
- **Focused evidence:** D1 and D6 deterministic source/contract fixtures,
  focused `quick_validate.py` for EER and review-fixpoint, the changed-owner
  relative-link check, and `git diff --check`. These checks and independent
  source review pass for the parent-accepted working-tree mechanism; exact
  revision remains pending until commit authorization.
- **Safe deferred work:** EBS-P2 supervised admission/execution, EBS-P3 outer
  routing, and external capability or telemetry work are outside EBS-P1.
  Implementation-plan review is a prerequisite, not deferred package work.
- **Causal split/combine decision:** Keep P1 separate from P2 because P1
  establishes the result level, plan identity, and invalidation boundary that
  P2 must consume. Keep EBS1/EBS2/EBS3/EBS7 together because they are one
  review/result authority; splitting them would create duplicate decisions and
  no independently useful implementation boundary.
- **Acceptance-cost topology:** Run independent plan review as the first
  material gate. Pre-admission checks of a candidate delta are diagnostic only.
  After plan admission and parent acceptance, run focused validators and the
  repository's canonical skill gate on the exact phase commit when commit is
  authorized. Without commit authorization, leave exact-revision and phase
  completion pending.

### EBS-P2 — Supervised admission and delivery-package execution

- **Status:** Parent-accepted working-tree mechanism; commit and canonical
  exact-revision completion remain pending.
- **Contracts and useful outcome:** Establishes EBS4, EBS5, and EBS6. If work
  stops after this package, one persistent implementer receives the complete
  accepted map, production edits are refused without a current plan result,
  and each accepted delivery package leaves a useful closed behavior with
  dependency-ordered handoffs and delta-only follow-ups.
- **Semantic and physical owner:** `supervised-implementer-loop` owns package
  schema, admission, persistent execution, internal-step handling, and
  acceptance. Its reference and entrypoint are the physical skill surfaces;
  EER independently audits the applicable plan cells.
- **Prerequisites:** An independent `implementation-plan-fixed-point` review
  for the unchanged plan identity, followed by admission and parent acceptance
  of the EBS-P1 candidate under that result, plus the EBS-P1
  result/invalidation boundary.
- **State and lifetime:** The accepted map and plan identity are carried once
  into the persistent implementer. Each delivery package owns its complete
  contract IDs, state/lifetime, and evidence; internal steps remain inside that
  package, and later packages consume only accepted earlier invariants.
- **Transaction and recovery closure:** Admission occurs before production
  edits. Each package settles ownership, mutation, commit, abort, retry, poison,
  recovery, and cross-owner handoffs together; no partial contract or later
  cleanup package repairs an earlier package's semantics.
- **Public and skill surface:** The SIL entrypoint and
  `contract-and-scenario-package.md` expose the accepted work-package map,
  ordered delivery slices, handoffs, and focused acceptance packet.
- **Focused evidence:** D1 and D6 admission fixtures, SIL `quick_validate.py`,
  parent source probes for map cardinality and closure, focused owner and
  composed scenarios, and the exact package-level gate required by repository
  guidance.
- **Safe deferred work:** EBS8's thin mixed-work routing and integrated
  proposal evidence remain in EBS-P3. Private filenames, modules, and external
  capability claims remain conditional and are not invented here.
- **Causal split/combine decision:** Keep P2 separate from P1 because it
  consumes P1's result and plan identity only after independent plan review,
  P1 admission, and parent acceptance; keep EBS4/EBS5/EBS6 together because
  admission, package closure, ordering, and persistent execution share one owner
  and one useful stopping boundary.
- **Acceptance-cost topology:** Use focused owner checks and parent acceptance
  for each accepted slice, then one package-level canonical gate on the exact
  accepted revision. Do not independently gate internal steps unless a material
  decision requires it, and do not credit slice acceptance as
  `deterministic-fixed-point`.

### EBS-P3 — Thin outer routing and integrated proposal/evidence closure

- **Status:** Integrated parent-accepted working-tree mechanism; commit,
  canonical exact-revision completion and any required final exact-revision Tick
  remain pending.
- **Contracts and useful outcome:** Establishes EBS8 and integrates the
  EBS1-EBS7 evidence closure. If work stops here, `complex-work` carries only
  the reviewed result and plan identity, routes each unit to its owning leaf,
  and the proposal's fixtures and links state what structural evidence can and
  cannot prove.
- **Semantic and physical owner:** `complex-work` owns mixed-package routing;
  EER, SIL, and review-fixpoint retain their leaf schemas and mechanics. The
  physical routing surface is `skills/complex-work/SKILL.md`, with this proposal
  holding the integrated EBS evidence and package map.
- **Prerequisites:** Independently reviewed EBS-P1 result/identity semantics,
  admitted and parent-accepted EBS-P2 supervised admission and package closure,
  and the EBS1-EBS8 matrix.
- **State and lifetime:** The outer coordinator carries only decision level and
  plan identity for the duration of routing. It owns no delivery-package
  schema, plan-cell ledger, admission state, or Tick/Tock state.
- **Transaction and recovery closure:** Routing creates no duplicate semantic
  state or transaction. A leaf owns its admission and recovery; routing returns
  failures to that owner and final integration accepts only completed leaf
  results.
- **Public and skill surface:** `complex-work/SKILL.md` routes review,
  fixpoint, and supervised implementation units; the proposal documents the
  cross-unit ordering, shared constraints, authorization, and final acceptance
  boundary.
- **Focused evidence:** D1-D6 deterministic source/contract fixtures; focused
  validators for all four skills; proposal and owner relative-link checks;
  `git diff --check`; long-reference Contents checks; and a source scan for
  duplicate fixed-point vocabulary or leaf mechanics. These structural checks
  pass and the independent integrated working-tree Tick acceptance is recorded;
  commit/canonical exact-revision completion and any required final
  exact-revision Tick remain pending.
- **Safe deferred work:** No external capability, telemetry, Slice 7
  implementation, private representation, or new fixed-point phase is added.
  Leaf owners remain responsible for their own later implementation evidence.
- **Causal split/combine decision:** Keep P3 separate because outer mixed-work
  routing has a distinct public composition and must consume already accepted
  leaf decisions. Combining it with P1 or P2 would duplicate or blur their
  schemas and acceptance authority.
- **Acceptance-cost topology:** Focused structural checks and the integrated
  parent acceptance are complete in the working tree. Run the canonical gate
  only on the exact accepted revision once commit is authorized, then run any
  required final exact-revision Tick. Reuse accepted leaf evidence and do
  not repeat expensive canonical gates when no new decision is made.

The six entries in `Validation Scenarios For The Skills` are evidence fixtures
`D1` through `D6` in listed order. These evidence IDs do not add contract rows
or authorize implementation.

## Source-Grounded Gap

A reported Slice 7 review motivated this change, but its specification and
review artifact are not present in this repository. This proposal does not use
their stated counts or decisions as acceptance evidence.

The current repository sources establish the intended owner boundaries and the
remaining integrated acceptance boundary:

- [Specification Review Contract](../skills/evidence-efficient-review/references/specification-review.md)
  defines the level-scoped delivery-plan relation and package-plan cells while
  remaining the review authority rather than an implementation-admission leaf;
- [Complex Work](../skills/complex-work/SKILL.md) now consumes the reviewed
  result level and plan identity, routes unresolved implementation-plan
  coverage back to review, and sends an accepted current plan to SIL without
  copying leaf mechanics;
- [Supervised Implementer Loop](../skills/supervised-implementer-loop/SKILL.md)
  consumes the current implementation-plan result and owns delivery-package
  admission and execution; and
- [Review Fixpoint](../skills/review-fixpoint/SKILL.md) owns the distinct
  result levels, plan identity, and invalidation boundary used by those routes.

EBS-P1, EBS-P2, and EBS-P3, including the integrated proposal closure, are
parent-accepted working-tree mechanisms. All three package mechanisms are
present; commit authorization, canonical exact-revision completion, and any
required final exact-revision Tick remain pending. This working-tree status does
not claim `deterministic-fixed-point` or `Done`. The independent integrated
working-tree Tick acceptance is recorded in
[Review 04](improvement-even-better-slicing-review-04.md).

## Distinguish Three Fixed Points

Use the three result levels named by EBS1 and EBS7. Their vocabulary, effects,
and invalidation rules are owned by
[review-fixpoint](../skills/review-fixpoint/references/contract-and-evidence-boundary.md);
this proposal records the product boundary but does not create a second result
authority.

A contract-level result may deliberately stop after stable contract cells are
cleared while the EBS2/EBS3 delivery-plan relation remains an explicit
downstream unknown. A plan-level result requires that relation and its package
cells to be reviewed before implementation can be admitted. Completed
implementation remains the existing `deterministic-fixed-point` result, not a
new phase or synonym.

## Local Terms

- A **work package** is the complete caller-authorized implementation scope
  passed to `supervised-implementer-loop`.
- A **delivery package** is one ordered, independently acceptable slice inside
  that work package. It establishes one or more complete contract IDs.
- A **design checkpoint** accepts a decision needed by later work but need not
  produce behavior. Its acceptance does not make it a delivery package.
- An **internal step** is implementation work inside one delivery package. It
  may receive focused parent review without becoming a separately gated slice.

Each contract ID has exactly one establishing delivery package. If accepted
behavior genuinely reaches two independently useful stopping points, propose
two observable rows to product authority and accept that contract change before
plan review. Earlier checkpoints, prerequisites, and internal steps may
contribute evidence but never temporarily own part of an accepted contract. A
delivery package may establish several complete contract IDs.

## Design Checkpoints Are Not Delivery Packages

This section is rationale for EBS3-EBS5, not a second contract authority.

A design checkpoint records a decision that later work needs: representation,
state ownership, transaction order, dependency direction, ABI shape, limits,
metrics, or test strategy. It may produce no executable behavior.

A delivery package produces a useful owner-level or public behavior through its
real composition path. It includes the state and transactions necessary to
establish that behavior, its consumer-shaped interfaces, and evidence that can
accept or reject the package.

One package may contain several internal checkpoints. A checkpoint may also be
accepted separately when a later package genuinely depends on its architectural
decision. Naming checkpoints A-F does not establish six slices, and it does not
establish any slice until the decisions are composed into delivery packages.

## Required Package Map (EBS3-EBS6)

Before an implementation-plan result, apply the EBS3-EBS6 package relation and
record the following plan fields. The EBS matrix remains the sole contract
authority.

| Field | Required decision |
| --- | --- |
| Package ID and outcome | The useful behavior available if work stops after this package. |
| Owned contracts | One or more complete contract IDs established at this package; no partial contract ownership is accepted. |
| Semantic and physical boundary | The semantic owner and the current or proposed physical representation, without equating a module with authority. |
| Prerequisites | Earlier packages and architectural decisions that this package actually consumes. |
| State and lifetime | State introduced or mutated, its owner, durability, rebuildability, and smallest correct lifetime. |
| Transaction closure | Admission, mutation, commit, abort, retry, poison, and cross-owner handoffs that must settle together. |
| Public and ABI surface | Compiled public composition and any guest, engine, embedding, or external boundary change. |
| Evidence | Focused contract scenarios, adjacent boundaries, recovery partitions, and package-level gate. |
| Deferred work | Behavior intentionally absent after the package and why the omission does not weaken its contracts. |

The mapping must be complete in both directions: every contract belongs to
exactly one establishing package, and every package establishes at least one
complete contract. A miscellaneous integration, plumbing, metrics, ABI, or
cleanup package is a review candidate unless it independently satisfies the
useful-stopping-point rule.

## Judge Slice Size By Closure, Not Lines (EBS4-EBS7)

Use these questions to review the EBS4-EBS7 package and acceptance boundaries;
they are not an additional package-size contract.

There is no preferred LOC range or module count. A package is too large when it
contains independently changing semantic owners or transaction systems that
can reach useful stopping points separately. It is too small when it exposes
only a representation, helper, adapter, or mechanical move with no independently
acceptable behavior.

Review package size with these questions:

1. If work stopped here, is a real public or owner-level capability correct and
   useful?
2. Does the package have one primary reason to change?
3. Are its state and transaction boundaries closed, or does acceptance depend
   on an unbuilt later package repairing partial semantics?
4. Does the next package depend on an accepted semantic decision or merely on
   convenient code placement?
5. Can focused evidence localize a defect to this package without requiring the
   whole future feature?
6. Does splitting further create forwarding layers, duplicated state, temporary
   public APIs, or repeated gates with no new decision value?
7. Does combining further hide independent owners, force unrelated tests into
   one review, or make rollback and acceptance ambiguous?

Gate cost is part of package design. Run focused checks for internal steps and
the expensive canonical gate at meaningful accepted package revisions. Do not
manufacture tiny packages merely to create more commits, reviews, or gates.

## Required Review Backstops

Specification review must add these cells:

| Cell | Clear only when | Failure disposition |
| --- | --- | --- |
| Contract-to-package coverage (EBS3) | Every normative contract maps to exactly one establishing delivery package, and every delivery package establishes at least one complete contract. | Required unknown or finding. |
| Useful stopping point (EBS4) | Each package leaves a correct and useful behavior if later packages never arrive. | Finding. |
| Cohesion and transaction closure (EBS4/EBS5) | State, lifetime, commit, abort, and recovery boundaries fit one primary reason to change. | Finding or required unknown. |
| Dependency order (EBS5) | Every package consumes only accepted earlier contracts and decisions. | Finding. |
| Package-size tradeoff (EBS5) | The review explains why adjacent packages should neither be combined nor split further. | Required unknown. |
| Acceptance-cost topology (EBS7) | Focused checks, parent acceptance, independent review, and canonical gates occur only where they decide something material. | Finding when the plan repeats expensive work without decision value; plan or slice acceptance cannot establish `deterministic-fixed-point`. |
| Checkpoint/package distinction (EBS3) | Design questions are not counted as delivery packages unless they satisfy the complete package record. | Required unknown. |

Zero required unknowns is impossible at an implementation-plan review while
any contract lacks a package, any package lacks a stopping-point outcome, or a
checkpoint is standing in for an unresolved package boundary.

## Skill Changes

### `evidence-efficient-review`

**Status:** Implemented in EBS-P1 and parent-accepted in the working tree;
commit and canonical exact-revision completion remain pending.

- Keep detailed level-specific review cells and the logically distinct
  delivery-plan relation in `references/specification-review.md`; keep
  `SKILL.md` to routing and result requirements.
- Report a finding or required unknown when checkpoints substitute for delivery
  packages. Return that decision to the caller; do not select Tock.
- Report contract-cell and plan-cell unknowns separately and include the
  package-size tradeoff for an implementation-plan decision.

### `supervised-implementer-loop`

**Status:** Implemented in EBS-P2 and parent-accepted in the working tree;
commit and canonical exact-revision completion remain pending.

- Keep the delivery-package record and map admission rules in
  `references/contract-and-scenario-package.md`.
- Refuse production edits unless a durable review reports
  `implementation-plan-fixed-point` for the unchanged plan authority.
- Give the persistent implementer the complete accepted map once, use
  delta-only follow-ups, and keep internal steps inside their establishing
  delivery package unless product authority accepts any needed contract split
  and a reviewed plan assigns the resulting delivery-package ID.

### `review-fixpoint`

**Status:** Implemented in EBS-P1 and parent-accepted in the working tree;
commit and canonical exact-revision completion remain pending.

- Own `contract-fixed-point`, `implementation-plan-fixed-point`, and the
  existing `deterministic-fixed-point` in
  `references/contract-and-evidence-boundary.md`. These are decision levels
  consumed by the existing Tick/Tock phases, not new phases.
- A contract-level Tick never implies plan readiness. Begin an implementation
  Tock only when the latest durable review artifact records
  `implementation-plan-fixed-point` for plan-owning content and dependencies
  that remain unchanged. The review-artifact-only commit does not invalidate
  that evidence; a material plan-owner change does.
- Preserve existing exact-revision implementation gates and persistent
  independent-Tick semantics in `references/phase-mechanics.md` and `SKILL.md`.

### `complex-work`

**Status:** Implemented in EBS-P3 and integrated parent-accepted in the working
tree; commit, canonical exact-revision completion, and any required final
exact-revision Tick remain pending.

- Consume the reviewed decision level and plan identity. Route missing plan
  coverage to `evidence-efficient-review` or `review-fixpoint`, and route an
  accepted implementation plan to `supervised-implementer-loop`.
- Keep package schema, plan-cell review, implementation admission, and
  Tick/Tock semantics with their leaf owners. Carry only cross-unit ordering,
  shared constraints, authorization, integration, and final acceptance.

## Slice 7 Example

The following is illustrative, not a replacement for a reviewed Slice 7 owner
and package map:

| Candidate package | Candidate vertical outcome |
| --- | --- |
| 7.1 Protocol kernel | Protocol identities, extension publication, uncached dispatch, derived cache, `defprotocol`, and `extend-type` work end to end for built-in, `nil`, and default targets. |
| 7.2 Named user types | Type identities, instances, fields, tracing, replacement, `deftype`, and inline extensions work through compiled source. |
| 7.3 Records | `defrecord`, record construction, map-like operations, value laws, metadata, and printing form one complete record capability. |
| 7.4 Runtime reify | Anonymous type graphs, captures, atomic extension and instance adoption, dispatch, and reclamation work without runtime compilation. |

Uncached dispatch can be an internally accepted semantic step within 7.1 before
cache work begins; it need not force a separate canonical gate. The cache is
derived state and must not be allowed to define or repair dispatch semantics.
Records and reify remain separate because they have distinct state,
transactions, evidence, and reasons to change even though both depend on named
type and extension substrate.

The actual package map must be derived from the accepted Slice 7 owner, state,
transaction, ABI, and dependency design. This example demonstrates the desired
vertical shape only.

## Validation Scenarios For The Skills

The cases below are deterministic contract fixtures for source and structure
review. A gate clears a case only when it maps the expected decision to EBS IDs
and shows that the owning instructions unambiguously prescribe that decision at
the correct owner boundary. Their evidence class is
`deterministic source/contract fixture`. Package validators establish structure
and link integrity only; they do not prove model adherence or external
capability. External/model capability evidence and observational telemetry are
not applicable to this proposal. No case is cleared by exact wording, heading,
or regex matching alone.

### D1 — Contract review versus plan admission

- **EBS IDs:** EBS1, EBS2, EBS3, EBS6.
- **Observable review/admission result:** Complete semantic contracts and design
  checkpoints without delivery packages may receive
  `contract-fixed-point` with downstream plan unknowns; an implementation-plan
  review returns the required plan unknowns, and production admission refuses
  edits.
- **Evidence class:** `deterministic source/contract fixture`.
- **Owner-localization boundary:** EER normalization and plan-cell review own
  the review result; SIL admission owns the production-edit refusal.

### D2 — Mechanical package boundaries

- **EBS IDs:** EBS3, EBS4, EBS5, EBS7.
- **Observable review/admission result:** A plan whose packages are chosen
  solely one per struct, module, ABI function, or metric, and therefore expose
  mechanical elements rather than useful closed behavior, returns a
  useful-stopping-point, cohesion/ordering, or acceptance-cost finding rather
  than an implementation-plan result. A package is not rejected merely because
  a valid semantic boundary coincides with a physical boundary.
- **Evidence class:** `deterministic source/contract fixture`.
- **Owner-localization boundary:** EER's package-plan cells identify the
  missing vertical outcome; SIL's package authority owns the corrected package
  boundary.

### D3 — Over-combined semantic owners

- **EBS IDs:** EBS4, EBS5.
- **Observable review/admission result:** One package containing protocol
  publication, user values, records, reify, and cache fails cohesion unless
  evidence proves those state and transaction systems cannot form useful
  vertical packages.
- **Evidence class:** `deterministic source/contract fixture`.
- **Owner-localization boundary:** SIL package records own state, lifetime,
  transaction, and useful stopping-point closure; EER independently audits the
  corresponding plan cells.

### D4 — Derived cache after uncached behavior

- **EBS IDs:** EBS4, EBS5, EBS7.
- **Observable review/admission result:** A package exposing uncached protocol
  behavior before an optional cache can pass when the cache cannot change
  semantics and focused evidence proves both paths; cache work does not repair
  dispatch semantics.
- **Evidence class:** `deterministic source/contract fixture`.
- **Owner-localization boundary:** The package's dispatch owner proves the
  semantic path and derived-state boundary; review-fixpoint owns the material
  exact-revision gate.

### D5 — Recovery cannot be deferred to cleanup

- **EBS IDs:** EBS3, EBS4, EBS5.
- **Observable review/admission result:** A map assigning every contract but
  leaving record recovery or reify adoption to a later cleanup package fails
  transaction closure and cannot receive an implementation-plan result.
- **Evidence class:** `deterministic source/contract fixture`.
- **Owner-localization boundary:** SIL's delivery-package record must close
  recovery and adoption with the establishing contract; EER reports the plan
  cell finding.

### D6 — Complete vertical plan

- **EBS IDs:** EBS1, EBS2, EBS3, EBS4, EBS5, EBS6, EBS7, EBS8.
- **Observable review/admission result:** A reviewed vertical map with complete
  contract coverage, closed transactions, dependency order, focused evidence,
  justified gate placement, and conditional private filenames can receive
  `implementation-plan-fixed-point` only after independent plan review; the
  result then routes through the SIL admission boundary and thin complex-work
  coordinator.
- **Evidence class:** `deterministic source/contract fixture`.
- **Owner-localization boundary:** EER owns plan-cell coverage, review-fixpoint
  owns the result and plan identity, SIL owns admission, and complex-work owns
  only mixed-unit routing.

## Non-Goals

This proposal does not establish Slice 7 package boundaries, choose future Rust
or guest-Wasm modules, set a target LOC count, require one module per semantic
owner, add implementation mechanisms, or change the current runtime. It changes
how specification and workflow skills distinguish a reviewed contract from a
reviewed implementation plan.

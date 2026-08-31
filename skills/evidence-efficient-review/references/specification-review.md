# Specification Review Contract

Use this reference only when the reviewed target is a proposed specification,
architecture decision, stage overview, or slice contract. Complete normalization
before broad feasibility review. The normalized matrix is the single normative
authority for the review.

## Contents

- Normalize one authority
- Carry the behavioral design trace
- Separate durable contracts from implementation detail
- Qualify defensive requirements economically
- Classify evidence by decision role
- Design a diagnosable scenario portfolio
- Distinguish contract and delivery-plan review levels
- Audit the required specification cells
- Return actionable specification findings

## Normalize one authority

Inventory all normative statements in the target and its accepted authorities.
Assign each statement to one contract row before evaluating implementation
detail. Use this schema, adapting column names only when the target already has
stable identifiers:

| Field | Required content |
|---|---|
| Contract ID | Stable identifier used by decisions, slices, risks, and evidence |
| Observable contract | One externally observable semantic, ownership, lifetime, boundedness, or recovery outcome |
| Semantic owner | Component that decides and maintains the outcome |
| Public composition | Representative consumer or boundary where the outcome is observable |
| Implementation slice | Logically separate, ID-keyed delivery-plan relation that names the establishing delivery package; it may be unknown at contract level and must be complete at implementation-plan level |
| Deterministic evidence | Named reproducible scenario or gate |
| External compatibility evidence | Named external probe, or `not-applicable` with reason |
| Telemetry | Thresholded metric and baseline, or explicitly `observational` |
| Status | Proposed, accepted, unknown, or not-applicable |

Every normative requirement appears in exactly one row. Other sections reference
contract IDs and add only section-specific information; they do not paraphrase
the outcome. Treat contradictory rows, unassigned normative prose, and repeated
definitions as review candidates. Recommend one owning row and deletion or ID
references for the copies. Do not solve duplication by adding a summary that
leaves the old authorities intact.

The stable contract fields and the implementation-slice relation have distinct
authority and decision power. A plan may be represented in the same ledger or
in a separate artifact, but it always references stable contract IDs and does
not rewrite accepted observable contract fields. At a contract-level review,
leave the relation and its downstream cells explicitly unknown while reporting
the stable contract-cell result. At an implementation-plan review, require a
bidirectionally complete relation: each contract ID has exactly one establishing
delivery package, each delivery package establishes at least one complete
contract, and design checkpoints or internal steps are not delivery packages.

This reference owns normalization and the level-specific coverage cells. The
result vocabulary, effects, and invalidation rules are owned by
[review-fixpoint's contract-and-evidence boundary](../../review-fixpoint/references/contract-and-evidence-boundary.md).

Do not force every document to use this exact Markdown table. A database,
Org-mode table, or other compact ledger is equivalent when it preserves one
normative authority and stable IDs.

## Distinguish contract and delivery-plan review levels

Record the selected review level and return contract-cell and plan-cell
dispositions separately. A contract-level review can clear every applicable
stable contract cell while exposing required downstream plan unknowns. A plan-
level review clears those same cells only when every applicable delivery-plan
cell also clears and returns the plan identity defined by the linked
review-fixpoint boundary. Do not select a Tock or otherwise choose outer
workflow phase from this reference; return the coverage decision to the caller.

## Carry the behavioral design trace

Apply the shared
[behavioral design trace and rebaseline authority](behavioral-design-trace.md).
Include its package-level goal record in the normalized authority and
disposition the behavioral-design-trace cell below. Keep proposed
behavioral contract changes with product authority and report behavioral and
mechanism statuses separately.

## Separate durable contracts from implementation detail

Keep the normative row stable across equivalent private designs. State:

```text
observable outcome -> semantic owner -> lifetime or transaction boundary ->
boundedness and recovery -> public composition -> named evidence
```

Put private collection shape, fields, counters, diagnostic plumbing, helper
names, and transaction decomposition in an implementation appendix. Promote a
mechanism into the durable contract only when changing it would violate a
public compatibility promise, eliminate the only sound owner, or break a named
correctness invariant. Record that reason beside the prescription.

Require this record for each exact cap, timeout, retry count, or other numeric
limit proposed as normative:

| Field | Required justification |
|---|---|
| Correctness role | Invariant that changes or fails if the value changes |
| Workload basis | Observed or conservative workload that the value must admit |
| Resource estimate | Memory, CPU, latency, connection, or storage cost it bounds |
| Boundary consequence | Observable behavior at exact and one-over values |
| Revision trigger | Production evidence, benchmark, or workload change that permits revision |

If correctness does not depend on the number, classify it as a private default
in the implementation appendix. Its boundary checks are mechanism evidence, not
durable feature acceptance.

## Qualify defensive requirements economically

For each proposed normative precaution, apply the
[economic actionability authority](economic-actionability.md). Establish the
possible failure from source, then compare likelihood, impact, existing
containment, the smallest adequate response, and added carrying cost. Give
high-impact durable or irreversible outcomes explicit weight even when they are
uncommon. Keep the resulting decision with the owning contract row or risk
authority.

Use the authority's decision backstop to confirm that routine requirements stay
lightweight, likelihood is evidenced or explicitly unknown, and qualitative
judgment remains visible instead of being replaced by invented probabilities or
a numeric threshold.

## Classify evidence by decision role

Assign every named check or measurement exactly one class:

| Evidence class | Decision role | Required record |
|---|---|---|
| Deterministic release gate | Must pass on the accepted revision. | Scenario or command, revision, result, and covered contract IDs |
| External compatibility evidence | Confirms behavior of a credentialed provider or environment outside repository control. | Capability identity, freshness window, evidence date/revision, result, and failure class |
| Observational telemetry | Describes behavior but has no decision threshold. It neither establishes nor blocks acceptance. | Metric, measurement context, and explicit `observational` label |

A performance metric becomes a deterministic gate only when the specification
names its baseline, measurement procedure, direction, and regression threshold.
Merely collecting bytes, token counts, cache tokens, or latency does not create
an acceptance condition.

When a contract depends on an external capability, require initial external
confirmation. Permit later reuse only when the recorded endpoint capability,
protocol, model family, and material request shape still match and the evidence
age is within a stated freshness window. Record one of these statuses:

| External status | Review meaning |
|---|---|
| `current` | Fresh successful evidence for the current capability identity |
| `reusable` | Prior successful evidence satisfies identity and freshness rules |
| `stale` | Evidence exists but must be refreshed |
| `unavailable` | No valid observation was possible |
| `authentication-or-configuration-failure` | Probe did not start with a valid configuration |
| `provider-or-infrastructure-failure` | External health prevented a valid observation |
| `inconclusive-timeout` | Probe exceeded its declared bound without a conclusion |
| `product-contract-failure` | A valid run contradicted the required capability |

Only `product-contract-failure` proves the product contract false. The other
non-success states leave the external cell unknown or capability-unconfirmed;
they do not turn a passing deterministic gate into a product failure. Never
report missing initial capability evidence as a pass.

## Design a diagnosable scenario portfolio

Prefer a few scenarios with stable observable invariants over a list of fields
or individual assertions. Record:

```text
Scenario: <behavioral name>
Contracts: <IDs covered>
Observable invariant: <outcome visible at the public or owner boundary>
Evidence class: deterministic gate | external compatibility
Capture helpers: <shared instrumentation>
Localization signal: <which boundary a failure identifies>
```

Reuse focused capture helpers for concerns such as request shape, diagnostics,
connection identity, and cross-request contamination. Helpers may expose
mechanism evidence without making their field layout a durable contract.

When provider capability and composed semantics are both material, use two
separately reportable scenarios:

1. a minimal external capability probe that sends the smallest valid request
   proving the endpoint behavior; and
2. a broader semantic composition that exercises product ownership and uses
   the same instrumentation.

Do not make one credentialed witness the sole evidence for serialization, tool
execution, ownership, diagnostics, transport reuse, and model output. Keep
deterministic owner and composition evidence for contracts the repository can
control.

## Audit the required specification cells

Clear or disposition every applicable cell:

| Cell | Question | Candidate trigger |
|---|---|---|
| Single normative authority | Does every requirement have one owning contract row and only ID references elsewhere? | Duplicate or contradictory normative prose |
| Behavioral design trace | Does one stable package goal record remain authoritative, and has the current aggregate been compared with the smallest faithful alternative under the shared authority? | Mechanisms become outcomes, supporting features change core vocabulary without an accepted behavioral contract change, or internal progress displaces the direct scenario |
| Durable contract boundary | Could an independently designed correct implementation satisfy the row? | Private representation prescribed without a correctness reason |
| Scenario diagnosability | Does each scenario state an observable invariant and localize failure? | Assertion inventory or heroic catch-all witness |
| Evidence topology | Are deterministic gates, external probes, and telemetry independent and correctly composed? | External availability blocks unrelated deterministic contracts |
| External freshness | Can prior evidence be reused only under explicit identity and age rules? | Credentialed evidence has no freshness or failure classification |
| Telemetry decision power | Does each metric have a baseline and threshold or an observational label? | Measurement is cited as acceptance but cannot decide success |
| Exact-limit justification | Does every normative number have workload, cost, boundary, and revision evidence? | Precise cap or timeout is asserted by convention alone |
| Defensive actionability | Does a proposed precaution protect an accepted observable outcome or have comparative risk-and-burden evidence? | Source proves only that an edge case is possible |
| Change locality | Does design-sensitive work identify the owning source boundary while keeping private layout conditional? | A new responsibility has no placement rationale, or filenames and modules are frozen without an architectural reason |
| Workflow boundary | Does the product artifact contain targets and evidence without copying review mechanics? | Review numbering, commits, reviewer selection, or stop procedure embedded in the feature contract |
| Decision level and plan disposition | Does the result identify contract-level versus implementation-plan review, keep stable contract cells separate from the delivery-plan relation, and expose downstream plan unknowns at contract level? | A contract result is presented as plan readiness, or a plan field silently occupies a stable contract row |
| Contract-to-package coverage | At implementation-plan level, does every contract ID map to exactly one establishing delivery package and every package establish at least one complete contract? | Missing, duplicate, partial, or reverse-unmapped contract/package assignment |
| Useful stopping point | Does every delivery package leave a correct, useful owner/public behavior if later packages never arrive? | A package only provides a checkpoint, helper, representation, adapter, or other non-acceptable intermediate |
| Cohesion and transaction closure | Do one package's semantic owner, state/lifetime, transaction, recovery, public surface, and evidence close around one primary reason to change? | Acceptance depends on an unbuilt package to settle state, recovery, or public behavior |
| Dependency order | Does each delivery package consume only accepted earlier contracts and decisions? | A package relies on a later or unaccepted contract/decision |
| Package-size tradeoff | Does the plan explain why adjacent packages should neither combine nor split further based on closure and decision value? | Package boundaries follow lines, modules, or convenience without a causal tradeoff |
| Acceptance-cost topology | Do focused checks, parent acceptance, canonical gates, and independent review occur only at materially informative boundaries? | Repeated expensive gates or reviews add no decision value, or a plan/slice acceptance is credited as `deterministic-fixed-point` |
| Checkpoint/package distinction | Are design checkpoints and internal steps kept distinct from accepted delivery packages unless they satisfy the complete package record? | A checkpoint or internal step is counted as a delivery package |

Workflow boundary is not applicable when the reviewed artifact is itself the
repository workflow authority. External cells are not applicable when no
external capability participates in the contract; record the reason rather
than manufacturing a probe.

For a contract-level result, downstream plan cells are required unknowns for a
later plan decision but do not block the contract-cell result. For an
implementation-plan result, any unresolved plan cell blocks that result. The
caller applies the result effects and invalidation rules from the linked
review-fixpoint authority.

## Return actionable specification findings

For a local wording defect, provide replacement text. For structural
duplication, identify the authoritative row, list copies to delete or replace
with ID references, and show the resulting row. For a mechanism-coupled
contract, provide both the durable formulation and the implementation-appendix
disposition.

Report the normalized matrix or a compact delta to it, the disposition of every
required cell, defensive actionability decisions, external evidence status,
telemetry role, and unresolved unknowns. Declare a specification result only
for the selected review level: a contract-level result may retain
explicit downstream plan unknowns, while an implementation-plan result may not.
Do not treat this coverage result as a phase transition; return it to the
caller under the linked review-fixpoint result vocabulary.

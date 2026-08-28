# Specification Review Contract

Use this reference only when the reviewed target is a proposed specification,
architecture decision, stage overview, or slice contract. Complete normalization
before broad feasibility review. The normalized matrix is the single normative
authority for the review.

## Contents

- Normalize one authority
- Separate durable contracts from implementation detail
- Classify evidence by decision role
- Design a diagnosable scenario portfolio
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
| Implementation slice | Work package that establishes the outcome |
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

Do not force every document to use this exact Markdown table. A database,
Org-mode table, or other compact ledger is equivalent when it preserves one
normative authority and stable IDs.

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
| Durable contract boundary | Could an independently designed correct implementation satisfy the row? | Private representation prescribed without a correctness reason |
| Scenario diagnosability | Does each scenario state an observable invariant and localize failure? | Assertion inventory or heroic catch-all witness |
| Evidence topology | Are deterministic gates, external probes, and telemetry independent and correctly composed? | External availability blocks unrelated deterministic contracts |
| External freshness | Can prior evidence be reused only under explicit identity and age rules? | Credentialed evidence has no freshness or failure classification |
| Telemetry decision power | Does each metric have a baseline and threshold or an observational label? | Measurement is cited as acceptance but cannot decide success |
| Exact-limit justification | Does every normative number have workload, cost, boundary, and revision evidence? | Precise cap or timeout is asserted by convention alone |
| Change locality | Does design-sensitive work identify the owning source boundary while keeping private layout conditional? | A new responsibility has no placement rationale, or filenames and modules are frozen without an architectural reason |
| Workflow boundary | Does the product artifact contain targets and evidence without copying review mechanics? | Review numbering, commits, reviewer selection, or stop procedure embedded in the feature contract |

Workflow boundary is not applicable when the reviewed artifact is itself the
repository workflow authority. External cells are not applicable when no
external capability participates in the contract; record the reason rather
than manufacturing a probe.

## Return actionable specification findings

For a local wording defect, provide replacement text. For structural
duplication, identify the authoritative row, list copies to delete or replace
with ID references, and show the resulting row. For a mechanism-coupled
contract, provide both the durable formulation and the implementation-appendix
disposition.

Report the normalized matrix or a compact delta to it, the disposition of every
required cell, external evidence status, telemetry role, and unresolved
unknowns. Do not declare a whole-specification fixed point while required cells
remain unknown.

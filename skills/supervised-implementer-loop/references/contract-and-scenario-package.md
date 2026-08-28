# Contract and Scenario Package

Use this reference when establishing the package, assigning each slice, and
accepting handoffs. Keep the package matrix as the sole requirement authority.

## Contents

- Build the contract-first package matrix
- Carry the behavioral goal record
- Keep private mechanisms conditional
- Profile design-sensitive owners
- Profile modularization roots
- Define a small scenario portfolio
- Separate evidence lanes and statuses
- Localize before repeating external scenarios
- Justify exact limits
- Keep tests stable across redesigns

## Build the contract-first package matrix

Use stable IDs from the caller's normalized contract matrix. If no normalized
matrix exists, create the smallest package-local subset before slicing work:

| Field | Required content |
|---|---|
| Contract ID | Stable identifier used in assignments, reviews, and handoffs |
| Observable invariant | Public or owner-level behavior that must hold |
| Semantic owner | Component responsible for the invariant |
| Lifetime/bound/recovery | Applicable semantic boundaries, with inapplicable parts explained |
| Implementation slice | Ordered slice that establishes the invariant |
| Named scenario | Portfolio entry that proves it |
| Evidence class | Deterministic repository, external compatibility, or observational telemetry |
| Status | Pending, accepted, unknown, or not-applicable |

Each invariant has one owning row. Slice briefs, correction messages, tests,
documentation, and handoffs reference contract IDs rather than restating the
requirement. Update the row only after parent acceptance.

## Carry the behavioral goal record

Instantiate the package-level goal record from the shared
[behavioral design trace and rebaseline authority](../../evidence-efficient-review/references/behavioral-design-trace.md)
alongside the matrix. Mechanism rows reference its stable goal ID. Carry the
record through slice assignments, corrections, handoffs, and acceptance, and
report its direct scenario's behavioral status separately from mechanism status.

## Keep private mechanisms conditional

Put collection shape, fields, counters, diagnostic plumbing, helper names,
transaction decomposition, and numeric defaults in a conditional implementation
appendix. They are design inputs, not required package outcomes.

Promote a mechanism into a contract row only when changing it would violate a
public compatibility promise, eliminate the only sound semantic owner, or break
a named correctness invariant. State that reason. Ask whether a simpler
independently designed correct implementation can satisfy the row before
freezing representation or vocabulary.

## Profile design-sensitive owners

When one owner will receive a new design-sensitive responsibility or several
slices, record a compact package-local structural baseline:

- relevant source units and major responsibility groups;
- state and collaborator boundaries;
- production and test separation; and
- the intended destination for each relevant slice.

Use module indexes, bounded outlines, and exact reads; do not load a complete
large owner merely to build the profile. Report material structural delta after
each relevant slice and compare the final owner with the baseline before
package acceptance. Inspect bounded history only when repeated placement across
earlier packages is material. The profile is implementation evidence, not a
public layout contract or permanent metrics ledger.

## Profile modularization roots

When the package contract explicitly includes modularization or physical
decomposition, inventory every material residual responsibility cluster in
each affected root before implementation and again at package acceptance:

```text
responsibility cluster
-> semantic owner
-> current physical representation
-> state and lifetime
-> transaction boundary
-> dependencies and callers
-> public or ABI surface
-> representative tests
-> smallest plausible complete private boundary
-> colocation invariant, when retained
-> extracted | retained-with-proof | unknown | not-applicable
```

`extracted` requires a cohesive private boundary with preserved behavior,
visibility, state, and dependency direction. `retained-with-proof` requires a
named causal invariant that the smallest plausible complete boundary would
break. Use `unknown` when required analysis is absent, contradictory, or tests
only a partial extraction. Use `not-applicable` for generated or
language-mandated regions, one cohesive algorithm, or another source-proven
absence of distinct responsibilities.

Record behavioral preservation and physical locality in separate evidence
lanes. Put passing APIs, ABIs, tests, and canonical gates in the preservation
lane; clear residual topology from the inventory and complete-boundary proof.
As acceptance backstops, an `unknown` residual cluster blocks the
modularization contract, while size and implementation effort only prioritize
the inventory.

## Define a small scenario portfolio

Record each scenario once:

```text
Scenario: <behavioral name>
Contracts: <stable IDs covered>
Observable invariant: <outcome at an owner or public boundary>
Evidence class: deterministic repository | external compatibility |
                observational telemetry
Capture helpers: <shared instrumentation>
Localization signal: <boundary identified when the scenario fails>
```

Prefer a few behavioral scenarios over an assertion inventory. Use shared
capture helpers for request shape, diagnostics, connection identity, and
cross-request contamination when relevant. Helpers may inspect private fields
for diagnosis, but their field layout does not become a public contract merely
because several scenarios reuse them.

## Separate evidence lanes and statuses

Keep the shared behavioral and mechanism progress statuses separate before
classifying the evidence that supports them. A completed owner suite or
mechanism path cannot establish the direct scenario's behavioral acceptance.

Keep these lanes independently reportable:

1. **Deterministic repository evidence:** owner-level and composed scenarios
   controlled by the repository. These must pass for slice acceptance.
2. **Minimal external capability probe:** the smallest credentialed request
   that isolates provider or endpoint capability.
3. **Broader composed semantic scenario:** end-to-end product ownership and
   behavior, using the same capture helpers without being the sole proof of
   repository-controlled contracts.

The latter two are separate scenarios even when both use external compatibility
evidence. A failure must identify capability versus composition rather than
collapsing serialization, tools, diagnostics, transport identity,
contamination, and model output into one witness.

For each external scenario, carry the capability identity, freshness rule, and
one of the caller's evidence statuses: `current`, `reusable`, `stale`,
`unavailable`, `authentication-or-configuration-failure`,
`provider-or-infrastructure-failure`, `inconclusive-timeout`, or
`product-contract-failure`. Only the last proves the external contract false.
Missing credentials and other availability failures neither fail deterministic
acceptance nor count as an external pass. Required initial evidence remains
explicitly capability-unconfirmed.

Observational telemetry has no acceptance effect unless the contract names a
baseline, measurement method, direction, and regression threshold. Record
unthresholded bytes, token counts, cache tokens, and latency as observational.

## Localize Before Repeating External Scenarios

After an external semantic assertion fails, do not rerun the unchanged scenario
until available evidence distinguishes the live hypotheses.

Capture one structured diagnostic tuple:

- effective request identity and material request shape;
- exact external presentation relevant to the assertion;
- submitted external action or request arguments;
- semantic-owner state used to validate or commit it;
- resulting durable or runtime identity; and
- the violated invariant.

Keep this tuple and its field layout private and disposable. They are diagnostic
evidence, not a public product contract.

Classify the failure as provider behavior, product behavior, evidence-harness
behavior, or still unknown.

If the first record is insufficient, improve the capture before one additional
run. A next run requires improved capture or a changed implementation. Never
rerun solely because summary output was truncated: preserve the complete
structured record in a temporary artifact and summarize it separately.

Once localized, add or strengthen deterministic owner and composition coverage
before another acceptance run.

## Justify exact limits

Before implementing a normative cap, timeout, retry count, or other numeric
limit, require:

| Field | Required justification |
|---|---|
| Correctness role | Invariant that changes or fails if the value changes |
| Workload basis | Observed or conservative workload the value must admit |
| Resource estimate | Memory, CPU, latency, connection, or storage cost it bounds |
| Boundary consequence | Behavior at exact and one-over values |
| Revision trigger | Production evidence, benchmark, or workload change that permits revision |

When correctness does not depend on the number, keep it as a private default in
the implementation appendix. Test it as mechanism evidence rather than making
it feature acceptance.

## Keep tests stable across redesigns

Classify affected tests as `retain`, `strengthen`, `replace`, or `delete`.
Contract tests protect stable public semantics, ownership, boundedness, and
recovery. Mechanism tests are disposable when their design simplifies.

Cover semantic partitions and reachable adjacent boundaries when they
distinguish behavior. Do not bypass an earlier public admission limit only to
exercise a later defensive ceiling. Test the earliest observable public
contract publicly and keep unreachable serializer or ABI limits owner-local.
A conformance label names evidence but does not replace the scenario's
observable invariant.

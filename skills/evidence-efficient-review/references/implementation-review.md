# Implementation Review Mechanics

Read this reference for implementation reviews. For an incremental
post-remediation review, audit promised closure and the changed transaction
before exploring unrelated defects. For a rebaseline review, derive contract
cells and inspect them sequentially.

## Contents

- Audit promised closure
- Audit the remediation delta
- Review contract cells
- Qualify actionable concerns
- Review residual topology
- Challenge implementation seams
  - Control-only durable identity
  - Effective evidence identity
- Evaluate test evidence

## Audit promised closure

Complete prior-finding disposition before broad new-defect exploration:

1. Extract each prior finding's violated invariant, reproducer, semantic owner,
   and required owning correction into a compact checklist.
2. Trace the original negative scenario through the current owner, including
   the order of admission, mutation, commit, abort, and cleanup when applicable.
3. Compare the implemented boundary with the required correction. A nearby new
   mechanism, updated documentation, or green named regression does not prove
   that the required boundary moved or became exact.
4. Re-run the original reproducer or a smaller equivalent when source ordering
   alone does not establish closure.
5. Mark the finding closed only after owner evidence and public composition
   agree. Otherwise report incomplete closure before searching for unrelated
   defects.

Record this proof for every finding:

```text
Prior finding: <identifier>
Required boundary: <invariant and owning correction from the prior review>
Current proof: <exact source order/range or rerun reproducer>
Disposition: closed | incomplete | recurrent | unknown
```

Do not batch findings into a generic “repairs are present” conclusion. For a
temporal or transactional finding, spell out the ordered calls and where the
exact admission capability is acquired relative to mutation and commit. Tests
or documentation alone cannot supply that proof.

After disposition, challenge interactions among changed owners and sample the
highest-risk invalidated contract cells. Carry unchanged cleared cells from the
prior review instead of reconstructing them.

## Audit the remediation delta

Before branching into unrelated latent defects, enumerate every operation
inserted, removed, or reordered between admission and the first irreversible
mutation. Prove that each operation's failure modes and resource costs are
covered by the acquired capability or remain rollback-safe.

This delta audit takes precedence over exploring an unchanged downstream limit.
A credible inherited defect does not compensate for missing a defect introduced
by the remediation under review.

## Review contract cells

Derive cells from the selected target: supported behavior, ownership boundary,
public route, resource policy, failure contract, performance bound, and negative
constraint. For each applicable cell:

1. State the target claim and semantic owner.
2. Trace the owner through adapters and representative public consumers.
3. Inspect only the source ranges needed for the current question.
4. Challenge the applicable seams below.
5. Check owner evidence and one realistic composed boundary when the contract
   is public or cross-component.
6. Record the result before moving to the next cell.

Inspect history only when it answers a live question such as regression
classification, incomplete prior closure, or intended invariant. Do not
front-load repository archaeology.

## Qualify actionable concerns

Classify a concern with the
[economic actionability authority](economic-actionability.md)
when its correction would add or preserve a defensive mechanism or lasting
mechanism-coupled tests. First reproduce the scenario or prove the source
invariant. Then report an accepted observable contract violation as a current
finding, or complete the comparative likelihood, impact, containment, and
burden decision before promoting another candidate.

When cumulative remediation triggers the authority's rebaseline signals,
reopen the affected contract rows and dependent tests. Compare the complete
package with the smallest faithful design while preserving real recovery and
durable-state invariants. Use the authority's decision backstop to verify that
local correctness of each layer has not substituted for package-level need.

## Review residual topology

For a whole-scope modularization review, independently build the
[residual-topology inventory](../../supervised-implementer-loop/references/contract-and-scenario-package.md#profile-modularization-roots)
for every affected root before deciding fixed point. Audit extracted modules
and retained roots with equal contract authority. Challenge at least one
plausible complete private boundary for every retained material cluster and
record the causal invariant when that complete boundary would fail. Treat the
failure of an individual helper, handle, or call extraction as evidence about
that partial boundary only.

Record behavioral preservation separately from semantic-owner and physical-
locality coverage. Place passing APIs, ABIs, tests, canonical gates, and
normalized moved-body comparisons in the preservation cell. Clear owner and
locality cells from the residual inventory and complete-boundary evidence;
classify unperformed central-state, transaction, lifecycle, central-type, ABI,
or cross-cutting boundary design as required `unknown` coverage.

Incremental review may carry a residual disposition forward only when its
responsibilities, dependencies, state, transactions, callers, and tests remain
unchanged. Rebaseline when an earlier zero-finding topology decision is
overturned or the residual impact cone is uncertain.

## Challenge implementation seams

Apply only the dimensions relevant to the selected contract:

- authority and dependency direction;
- admission before mutation;
- begin, commit, abort, drop, recovery, and retry completeness;
- ownership, transfer, reclamation, and state lifetime;
- exact, one-over, partition, schedule, or scaling boundaries;
- expected-error placement versus unexpected-error surfacing;
- identity and provenance across representations or bridges;
- substitutability across selected variants and routes;
- owner behavior versus public composition;
- reviewable physical decomposition when an owner receives a new
  design-sensitive responsibility or repeated placement;
- hidden physical ceilings or duplicated policy;
- obsolete fallback, compatibility, or silent downgrade paths; and
- complexity accounting against real work rather than timing alone.

For reviewable physical decomposition, compare the affected owner's structural
baseline and material delta when available. Apply the
[architectural-scope decision authority](../../supervised-implementer-loop/references/architectural-scope-decision.md)
to qualify any concern and bound its correction. File size alone is not a
finding, and a mechanically extracted module that worsens coupling, ownership,
or dependency direction is not an improvement.

Apply the following seams only when the selected contract has the corresponding
durable-effect or external-evidence surface. They are review questions, not new
application mechanisms.

### Control-Only Durable Identity

When a response or transaction can commit durable state without ordinary user,
assistant, or tool content, identify the truthful, resolvable, response-owned
durable event that represents that response. Prove that committed records,
lifecycle events, and recovery state bind to that event rather than a preceding
or later neighboring entry. Cover success, preparation failure, repeated
invocation, reopen, and branch or fork.

### Effective Evidence Identity

For evidence-producing code, trace endpoint, model, transport, store mode, and
other material capability identity from effective observed native requests or
metadata rather than only from selected configuration.

Challenge:

- omitted optional configuration and adapter defaults;
- caller or backend overrides;
- declared/effective mismatches;
- disagreement among requests in one scenario; and
- partial capture before failure.

A passing record requires every material request in the scenario to agree on
effective identity. Otherwise preserve the original execution result but
classify the evidence record as invalid or unavailable.

## Evaluate test evidence

- Credit a contract test only for stable public semantics, ownership,
  boundedness, or recovery established by its assertions. Prefer focused
  semantic partitions and adjacent boundaries over one heroic witness.
- Ask whether a simpler independently designed correct implementation could
  pass. If not, the test freezes mechanism unless that mechanism is an explicit
  stable contract.
- Compare each test name with its assertions; do not credit a broader claim.
- Prove that a boundary witness reaches its claimed owner without violating an
  earlier admission bound. Do not raise or bypass that bound to exercise a
  later defensive mechanism. Test an otherwise unreachable serializer or ABI
  ceiling locally as disposable mechanism evidence.
- Do not credit a conformance label without an assertion-level coverage
  description.
- Challenge internal metrics without operational consumers and assertions tied
  to field layout, counter vocabulary, or current transaction decomposition.
- When a simpler owner or contract advances the project goal, recommend
  correcting a spec-induced mechanism rather than implementing its evidence
  vocabulary literally.

# Observation: Review Fixpoint Can Ratchet Correct Code Into Overbuilt Code

## Purpose

This note records a failure mode observed while implementing the DCFresh
multi-table commit proof of concept in `cdp-uds-python-spark-job`. It is an
observation document, not an improvement plan. It deliberately does not select
skill changes, review policy, thresholds, or remediation mechanics.

The case produced two useful comparison points:

- PR 3006 implemented a durable transaction and recovery contract through a
  review-fixpoint loop.
- PR 3008 implemented only the essential happy-path logic on a branch based
  directly on `develop`.

The comparison does not imply that the minimal implementation is production
ready. It makes the cost of the robust implementation visible and exposes how
the review process accumulated some of that cost.

Documentation volume is outside this observation. The feature design and
review documents were workflow artifacts and are not intended to land in the
final product commit. The failure mode discussed here concerns product code,
tests, and the decisions that made their complexity appear necessary.

## Observed outcome

PR 3006 reached a deterministic fixed point: independent review reported zero
P0-P3 findings and the required repository checks passed. It was also much more
elaborate than the repository normally requires for a narrow external-service
integration.

Excluding generated transport files and tests, the robust branch added about
938 production lines, while the deliberately minimal branch added about 170.
This is not a direct measure of waste: the robust branch implements abort and
indeterminate-outcome recovery that the minimal branch intentionally omits.
The size difference nevertheless prompted a convention review, which found a
durable core surrounded by several locally invented construction and defense
mechanisms.

Examples included:

- a client factory class plus a free creation function for one concrete client;
- a composition dataclass whose state was a client supplier and tenant ID;
- gate and eligibility checks at composition, supplier invocation, and
  rebalancer execution;
- a two-field reconciliation policy object even though the reconciliation loop
  lived in another owner;
- result objects that wrapped only one string or one tuple;
- an unused context-manager protocol and broad public-looking package exports;
- runtime method inventory and repeated validation around an internally
  constructed concrete client; and
- tests that asserted the supplier, factory, and compatibility mechanisms
  rather than only the transaction's observable behavior.

None of these mechanisms caused a functional failure. That is part of the
problem: a correctness-focused review can accept every layer independently
while missing that their aggregate cost is disproportionate to the risk they
address.

## Failure mode

### The reviewer is asked to find issues, not to price them

The review instructions correctly require concrete, source-supported findings.
They reject vague preferences and unsupported speculation. In practice,
however, source support establishes that a scenario is possible; it does not
establish that defending against it is economical.

A malformed response, stale closure, repeated close, ambiguous test double, or
unusual configuration value can often be demonstrated from source. Once
demonstrated, it looks like a valid issue under a broad functional or
architectural review mandate. The reviewer is not required to compare:

- how likely the condition is in the real system;
- how severe the outcome is if it occurs;
- whether an existing boundary already makes it diagnosable or recoverable;
- how much production code and test surface the defense adds; or
- the continuing cost of understanding, changing, and validating that defense.

The result is a collapse from **possible** to **actionable**. Evidence of
possibility is treated as sufficient evidence that code should exist.

### Risk and complexity are evaluated asymmetrically

The process applies strong scrutiny to the risk of omitting a defense. It
applies weaker scrutiny to the risk introduced by adding that defense.

An omitted check has a concrete negative scenario. An added abstraction usually
passes tests and appears locally clean, so its costs remain diffuse:

- more concepts for future maintainers;
- more ownership boundaries that can disagree;
- more public-looking surface that later code may depend on;
- more tests coupled to the current decomposition;
- more branches and states to reason about; and
- more places where a future change can trigger another finding.

Because those costs are distributed over time, they do not compete effectively
with a vivid, immediately reproducible edge case. Review therefore has a
systematic bias toward adding machinery.

### Specification review can turn hypotheticals into obligations

In this case, the design evolved from a proof of concept into a detailed phase
matrix covering local rejection, definitive responses, indeterminate start,
indeterminate complete, indeterminate abort, participant diagnostics, polling,
and status interpretation.

Each item is defensible in isolation. Once written into the normative contract,
later implementation reviews were correct to demand it. The economic decision
had already been made implicitly during specification review, where plausible
failure cases became requirements without a comparative complexity budget.

This creates a contract ratchet:

1. Review identifies a possible failure.
2. The specification records a precise defensive requirement.
3. Implementation adds a mechanism and tests for that requirement.
4. Later review treats the mechanism as required scope rather than revisiting
   whether the original risk justified it.

Incremental review strengthens this effect because accepted contract cells and
closed findings are intentionally carried forward. That is efficient for
correctness, but it also preserves earlier economic assumptions that were never
made explicit.

### Remediation creates more reviewable surface

Each defensive correction can introduce another abstraction, state transition,
validation branch, or injection seam. The next independent review sees a larger
surface with more locally provable failure modes.

The loop therefore has a one-way tendency:

```text
possible issue
  -> finding
  -> defensive mechanism
  -> mechanism-specific tests
  -> larger review surface
  -> more possible issues
```

The fixed-point objective stops when no P0-P3 finding remains. It does not, by
itself, stop when the marginal risk reduction from another defense is smaller
than the complexity it introduces.

### Local correctness can conceal package-level imbalance

Every major component of PR 3006 had a reasonable local explanation:

- the semantic client hid provider terminology;
- the supplier delayed channel construction;
- the factory isolated mTLS setup;
- typed results hid protobufs;
- validation rejected bad inputs before mutation;
- reconciliation handled uncertain outcomes; and
- focused tests proved each behavior.

The package-level question was different: did this proof of concept need all of
those boundaries at once, and did each boundary carry enough responsibility to
justify its existence? The review process was better at proving each selected
mechanism correct than at challenging the cumulative selection.

## Why existing safeguards did not prevent it

The current skills already contain valuable warnings:

- stop rather than inventing lower-value findings;
- prefer simpler owners and contracts;
- do not freeze private decomposition into durable tests;
- distinguish architecture evidence from file count or implementation
  friction; and
- keep implementation and review economical.

Those statements describe the desired direction, but this case shows that they
do not yet provide an operational economic boundary. A reviewer can comply
with all of them and still report a source-proven edge case whose remediation
cost exceeds its expected value.

The missing information was not another correctness invariant. It was a shared
way to account for likelihood, impact, existing containment, implementation
complexity, and long-term carrying cost before promoting a concern into a
finding.

## Distinctions preserved by this observation

- The minimal PR is evidence of the essential logic, not evidence that recovery
  and validation are unnecessary.
- A durable implementation may reasonably be larger than a demonstration.
- Indeterminate mutation outcomes deserve more attention than malformed local
  values because they can leave durable external state.
- Repository convention is evidence about maintainability, not an automatic
  veto on a novel boundary.
- Line count exposes a question; it does not answer whether a design is too
  complex.
- The failure mode belongs to the combined specification, review, and
  remediation loop. It is not attributable to one reviewer or one finding.

## Questions left open

This note intentionally leaves the response undecided. The observed gap raises
questions for a later improvement package:

- What evidence should distinguish a possible concern from an economically
  actionable finding?
- Who supplies operational likelihood when source alone cannot establish it?
- How should a review compare expected failure cost with added code and test
  complexity?
- When should a later Tick reopen an earlier contract decision because its
  cumulative implementation cost is now visible?
- How can fixed-point review preserve rigor without treating every defensible
  precaution as required product scope?
- What package-level signal should trigger a simplicity review before more
  remediation is accepted?

These are observations and open questions only. No skill or workflow change is
authorized by this document.

# Economic Actionability

Build a compact economic actionability decision when a specification, review
candidate, or remediation would add or preserve product code or durable tests
to defend against a possible failure. Apply the decision to changes in the
product or its lasting evidence surface; let ordinary contract rows proceed
without an extra risk record.

## Compare marginal risk and burden

First distinguish two cases:

- An implementation violates an accepted observable contract. The violation is
  eligible for a finding under the caller's severity policy. When the outcome
  is itself a defensive precaution whose economic basis is missing or
  invalidated, preserve the current violation while returning the affected row
  for a contract decision. Reopen a private mechanism prescription directly
  rather than requiring it as the correction.
- A precaution addresses a possible failure but no accepted observable outcome
  is currently violated. Source proof establishes possibility, not economic
  actionability. Compare the marginal protection with the burden before making
  the precaution normative or reporting a finding.

For a disputed or newly proposed precaution, record only the evidence needed to
decide:

```text
Failure scenario: <real boundary, preconditions, and observable consequence>
Likelihood basis: <incidents, telemetry, system constraints, or explicit unknown>
Impact: <severity, durability, affected scope, and reversibility>
Existing containment: <prevention, detection, rollback, retry, or recovery>
Smallest adequate response: <contract, code, test, diagnostic, or no change>
Added burden: <owners, state, branches, public surface, tests, and carrying cost>
Decision: <current finding, contract correction, required unknown, or non-gating observation>
Revisit trigger: <evidence or topology change that invalidates the decision>
```

Establish likelihood from operational evidence, accepted system constraints,
or the responsible operational owner. When that evidence is unavailable, name
the unknown and who can resolve it. Treat source-level possibility as evidence
for the scenario while reserving the actionability decision for the complete
comparison.

Classify missing actionability evidence as a required unknown when an in-scope
contract or package decision depends on it. Otherwise keep the concern
non-gating or omit it.

Credit existing containment when the failure is already visible, bounded,
retryable, rollback-safe, or operationally recoverable. Treat indeterminate
durable external mutations, irreversible loss, and similarly high-impact harm
as consequential even when uncommon; a qualitative decision may still favor a
defense, but it must name the impact and why the smallest response is worth its
burden.

Promote a concern to an actionable finding or normative defense only when it
either protects an accepted observable contract or the comparative evidence
shows that its marginal risk reduction warrants its added burden. Select the
smallest response that clears the actual risk. Keep tests on observable
behavior unless a mechanism is itself an accepted stable contract.

## Reopen ratcheted decisions

Reevaluate affected contract rows before adding more remediation when current
evidence shows that an earlier economic assumption has changed. Concrete
signals include:

- one behavioral outcome now requires several semantic owners, durable records,
  or coordination boundaries;
- a supporting mechanism changes the feature's observable vocabulary;
- a correction adds public-looking surface, compatibility paths, states,
  branches, or mechanism-coupled tests;
- progress and acceptance evidence mostly prove internal machinery while the
  end-to-end outcome remains weak or unavailable; or
- cumulative implementation and test burden materially exceeds the basis on
  which the defensive requirement was accepted.

A signal triggers comparison. Rebaseline the affected contract rows and
dependent evidence, compare the current design with the smallest faithful
alternative, retain defenses supported by the marginal analysis, and replace
or delete obsolete mechanism tests when the contract is simplified.

## Decision backstop

Before accepting the decision, verify:

- [ ] an accepted observable contract or comparative evidence establishes why
      the defense is actionable;
- [ ] operational likelihood is evidenced or explicitly assigned as an unknown
      to a responsible owner;
- [ ] existing containment and serious durable or irreversible impact both
      receive explicit weight;
- [ ] the response is the smallest one that clears the actual risk;
- [ ] the record exists only because the decision changes product or lasting
      evidence surface;
- [ ] no fabricated frequency or numeric score substitutes for judgment; and
- [ ] file size and line count expose questions without deciding them.

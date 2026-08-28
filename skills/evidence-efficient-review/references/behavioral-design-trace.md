# Behavioral Design Trace And Rebaseline

Use this reference when a specification, implementation package, or review must
keep an observable goal authoritative while its supporting design evolves. It
owns the shared process for deriving mechanisms, comparing the aggregate design
with a smaller faithful alternative, and returning a changed design to its
behavioral authority. Consumer skills link here and add only their own routing
or acceptance responsibilities.

[Economic actionability](economic-actionability.md) remains the authority for
deciding whether a defensive requirement is worth lasting product machinery.
Apply that narrower comparison within this process when a proposed or retained
mechanism is defensive.

## Contents

- Establish the behavioral trace
- Derive the supporting design
- Compare the aggregate design
- Rebaseline at the owning boundary
- Keep progress evidence distinct
- Decision backstop

## Establish The Behavioral Trace

Begin with one short record that can survive equivalent implementations:

```text
Goal ID: <stable package-level identifier>
Behavioral goal: <what an actor must be able to accomplish, in plain language>
Direct scenario: <starting condition, actor action, public composition, outcome>
Product authority: <owner that accepts behavioral contract changes>
Owning contract: <stable behavioral row>
Behavioral status: <unavailable | partial | passing | failing>
```

Choose a direct scenario that demonstrates the goal through a real composition,
not through an internal field, record, callback, or metric. Carry the same goal,
goal ID, scenario identity, product authority, and owning contract through
specification, implementation, review, and acceptance. Refine its evidence and
status as the work advances without rewriting the goal in terms of the chosen
design.

## Derive The Supporting Design

Design outward from the behavioral trace. Start with the smallest cohesive
semantic owner and add representation or coordination only where an accepted
behavior, lifetime, boundedness, or recovery invariant needs it. For each
material mechanism, record a compact derivation:

```text
Mechanism: <vocabulary, owner, state, boundary, or public surface>
Behavior served: <goal ID, owning contract, and direct scenario step>
Necessity: <invariant that the mechanism establishes>
Lifetime and recovery: <why state persists or coordinates, if applicable>
Evidence: <contract scenario or disposable mechanism check>
```

Read these records as one aggregate design. Account for the vocabulary the
feature asks actors to use, the number of semantic owners, durable records and
lifetimes, coordination or transaction boundaries, public-looking APIs and
types, compatibility branches, and tests coupled to those choices. The record
should make each item traceable to behavior or identify it as a replaceable
implementation choice.

When a supporting feature changes the core vocabulary or observable choices,
propose that distinction as a behavioral contract change to the recorded product
authority. Let that authority decide whether it is a discovered product
requirement, a private implementation concern, or unnecessary complexity.
Resume design-sensitive work only after that decision; do not accommodate the
proposal first with another state, record, branch, or API.

## Compare The Aggregate Design

At ordinary design checkpoints, read the aggregate trace for cumulative
signals. When one applies, compare the complete current design with the smallest
cohesive alternative that faithfully provides the same accepted behavior and
recovery guarantees. This comparison is part of designing and reviewing the
package, not an exceptional objection to complexity. Concrete signals are:

- one behavioral outcome now spans several semantic owners, durable records,
  lifetimes, or coordination boundaries;
- a supporting feature changes the feature's core vocabulary or observable
  choices;
- new public-looking surface, compatibility paths, states, branches, or
  mechanism-coupled tests accumulate around a private design;
- most completion evidence proves internal machinery while the direct scenario
  remains unavailable, weak, or unchanged; or
- added implementation and test burden materially exceeds the accepted reason
  for the design.

Use the behavioral trace and aggregate derivations to compare:

```text
Accepted behavior and recovery invariants: <preserved requirements>
Current aggregate: <owners, state, boundaries, surface, and coupled tests>
Smallest faithful alternative: <cohesive owner and required mechanisms>
Material difference: <behavioral coverage, risk, burden, and evidence>
Decision: <retain current design | simplify | return a new behavior decision>
```

File size, line count, aesthetic preference, and implementation effort can
locate a question but do not decide this comparison. Prefer causal evidence
about vocabulary, ownership, state, coordination, public surface, tests, and
end-to-end progress.

## Rebaseline At The Owning Boundary

When the comparison changes the design, revise the owning contract once and let
dependent artifacts reference that decision. Preserve accepted behavior and
real lifetime, boundedness, recovery, and irreversible-effect invariants while
replacing prescriptions that followed only from the old mechanism.

Reclassify every affected test as `retain`, `strengthen`, `replace`, or
`delete`. Retain or strengthen stable behavioral evidence. Replace or delete
tests whose only purpose was to freeze the superseded vocabulary,
representation, owner split, or coordination scheme. Then resume
specification, implementation, or review at the earliest changed contract
boundary; carry forward evidence whose owners and dependencies remain valid.

If the comparison instead discovers a new behavioral requirement, obtain that
product or contract decision before expanding the mechanism. Record it as a
behavioral outcome with its own observable scenario, not as an inference from
the existing implementation.

## Keep Progress Evidence Distinct

Report two independently visible lanes throughout the work:

1. **Behavioral progress:** `unavailable`, `partial`, `passing`, or `failing`
   for the direct end-to-end scenario, with the first observable boundary that
   remains incomplete or contradicted.
2. **Mechanism progress:** `not-started`, `in-progress`, or `complete`, followed
   by the internal owners, records, coordination paths, migrations, and
   mechanism checks represented by that status.

Mechanism completion supports the result but does not stand in for behavioral
progress and cannot establish behavioral acceptance. At each package handoff
and acceptance decision, report the goal ID and direct scenario status
separately from mechanism status. A package can claim behavioral acceptance
only when the direct scenario has the status required by the owning contract.
Unavailable external capability retains its explicit evidence status rather
than being inferred from internal gates.

## Decision Backstop

Use this checklist after performing the process:

- [ ] one stable goal ID, plain-language behavioral goal, direct public
      scenario, product authority, owning contract, and behavioral status
      remain the package-level trace authority through acceptance;
- [ ] every material vocabulary item, semantic owner, durable state, lifetime,
      coordination boundary, public surface, and mechanism-coupled test is
      traced to accepted behavior or marked replaceable;
- [ ] a supporting feature that changes core vocabulary becomes a proposed
      behavioral contract change accepted by product authority before
      design-sensitive work resumes;
- [ ] concrete cumulative signals cause an aggregate comparison with the
      smallest faithful alternative, while size and taste remain non-deciding;
- [ ] an accepted rebaseline updates one owning contract, preserves real
      behavior and recovery invariants, and records each affected test's
      disposition;
- [ ] behavioral and mechanism statuses remain separate, and mechanism evidence
      cannot establish behavioral acceptance; and
- [ ] consumer skills link this authority instead of copying its process.

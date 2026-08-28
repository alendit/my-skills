---
name: review-fixpoint
description: >-
  Alternate independent implementation reviews with principled remediation
  until a selected repository work package reaches a functional and
  architectural fixed point. Use when asked to address review findings,
  review remediations, run another review round, or keep iterating until no
  actionable implementation defects remain.
---

# Review Fixpoint

Drive one repository-local loop with two alternating phases:

- **Tick — review:** use `$evidence-efficient-review` to independently audit
  the current implementation and create or update the review artifact required
  by repository guidance.
- **Tock — remediate:** address every actionable finding in the latest review
  artifact at its owning architectural boundary. Use
  `$supervised-implementer-loop` when the remediation is one non-trivial package
  with ordered dependent slices.

Prefer a new immutable numbered review when the project declares that
convention; otherwise use its append-only Tick ledger or other explicit review
authority. Never silently replace historical findings or dispositions.

Continue until the persistent reviewer's next Tick finds no P0-P3 functional
or architectural defect. Passing tests alone is not a deterministic fixed
point. Required external capabilities must also be confirmed before claiming
the capability or `Done`.

This skill owns phase selection, phase commits, and the fixed-point decision.
Repository guidance owns compatibility policy, the review-artifact convention,
and canonical gates. The called skills own review mechanics and supervised
implementation mechanics. Slice acceptance during Tock is not the independent
Tick and cannot establish a fixed point.

Commit every completed phase. After parent acceptance and focused Tock
verification, create one coherent remediation commit and run the canonical gate
on that exact clean revision; the Tock is complete only when it passes. After
each Tick has produced its required durable review artifact and the evidence is
verified, create one review-artifact commit. Keep the worktree clean
between phases, preserve unrelated user work in the same intentional checkpoint
when it is already part of the requested work package, and never leave a completed
phase only as uncommitted working-tree state.

At loop start, select exactly one persistent read-only reviewer that is
independent of the remediation author and implementer. Reuse that reviewer for
every Tick, including review of later Tocks, so it retains the reviewed
baseline, prior findings, and accepted evidence. Persistence does not authorize
implementation edits or remediation reasoning: give the reviewer a neutral
dossier and the current source each round. If the reviewer becomes unavailable,
report the loss of continuity and ask the user before selecting a replacement.

## Establish the Current Phase

1. Establish the repository work-package scope named by the user or active
   request. Resolve repository guidance for compatibility policy, the review-
   artifact convention, and canonical gates. Inspect `git status --short`,
   current history, and the latest applicable review artifact. Preserve
   unrelated worktree changes. Do not switch work packages merely because
   another scope has a newer review artifact.
2. Read the latest applicable review artifact completely. Treat its current
   disposition and original findings as a checklist, but verify them against
   the current tree.
3. Choose the phase from evidence:
   - use Tock when any finding in the latest review artifact remains
     unimplemented;
   - use Tick when those remediations are present or the user asks to review
     again;
   - if state is ambiguous, inspect the diff, owners, tests, and history before
     asking the user.
4. Follow the repository-declared review-artifact convention. Preserve prior
   findings and dispositions; remediation may add a concise current disposition
   only where that convention permits an append or update.

## Run the Loop

After phase selection, repeat this state machine:

```text
Tock: remediate latest review artifact
  -> verify the current tree
  -> Tick: independently review and write the required review artifact
       -> zero findings: deterministic fixed point, report external status
       -> findings: preserve the review artifact, return to Tock
```

Never declare a fixed point immediately after Tock. Only the persistent
reviewer's following independent Tick can establish it. Finish and verify
remediation before starting that Tick; do not review a partially edited tree or
insert Tick ceremonies between mechanical implementation units. If a Tick
finds a defect and the resulting non-trivial Tock remains owned by the same
persistent implementer, return a delta-only correction to that implementer.
Reopen only contract cells and evidence invalidated by the correction when
prior coverage remains trustworthy and impact is bounded; otherwise follow the
existing phase-selection and rebaseline rules before the next required exact-
revision Tick.

## Use One Contract And Evidence Boundary

Read
[references/contract-and-evidence-boundary.md](references/contract-and-evidence-boundary.md)
before either phase. Treat the normalized contract-and-evidence matrix as the
single requirement authority, keep workflow mechanics in this skill, and apply
the reference's evidence classes and result vocabulary to every phase decision.
Use its test-stability rules when a design changes.

Apply the shared
[behavioral design trace and rebaseline authority](../evidence-efficient-review/references/behavioral-design-trace.md)
through both phases. Carry one stable package-level goal record, route accepted
rebaselines back to its owning contract once, and keep direct scenario
behavioral status separate from mechanism progress.

Also apply the shared
[economic actionability authority](../evidence-efficient-review/references/economic-actionability.md)
before a possible failure becomes a defensive contract requirement or Tock
work. Preserve the reviewer as finding authority and the primary as package
acceptance authority. Obtain operational likelihood from recorded evidence or
the responsible owner, and keep unavailable evidence explicitly unknown.

Carry glossary state through the
[project-glossary authority](../clear-technical-writing/references/project-glossaries.md):
the selected glossary identity or explicit opt-out and only the material
term-to-semantic-source relationships needed by each Tick or Tock leaf. Preserve
that state in leaf inputs and results. Require or report the leaf review or
handoff's applicable
[clear technical writing pass](../clear-technical-writing/SKILL.md), but do not
read or apply the glossary as another semantic reviewer and do not perform
another prose pass in this outer workflow.

## Route Architectural Scope Decisions

When remediation or review exposes non-local impact, uncertain ownership,
mechanism-coupled tests, physical source structure that may hide distinct
responsibilities, or a local fix that may preserve an architectural problem,
read
[the architectural scope decision authority](../supervised-implementer-loop/references/architectural-scope-decision.md)
completely. Do not copy its decision, non-worsening, or ledger tables into this
skill or a feature specification.

During Tock, qualify the signal, bound the proper correction, and propose one
branch under primary acceptance. Record the decision and any authorized
follow-up delta. A safe deferral is incomplete until the durable record is read
back; external or otherwise separately controlled ledger mutations retain their
own authorization boundary. Stop for explicit package-scope authority when the
linked decision requires a scope stop.

During Tick, independently audit every relevant decision without adopting the
Tock author's classification. Verify signal qualification, correction bound,
non-worsening dispositions, stable follow-up identity, durable read-back,
lifecycle status, and finding classification. Tick reports follow-up deltas but
never creates, updates, closes, or marks a ledger record stale.

## Tock — Remediate the Latest Review Artifact

Map every finding to its owning contract ID. Update the owning matrix row once,
then change implementation, evidence, or documentation only where that
artifact's distinct responsibility changed. Replace copied normative prose with
ID references instead of synchronizing several requirement descriptions.

Remediate accepted observable contract violations directly. Apply economic
actionability when a proposed Tock would add or preserve a defense without such
a violation; missing evidence is a Tick unknown only when an in-scope decision
depends on it.

Before translating review vocabulary into design-sensitive machinery, apply
the shared behavioral-design authority. During Tock, provide its aggregate
trace and comparison, return any behavioral contract change to product
authority, classify affected tests, and resume at the accepted rebaseline
boundary.

Turn the findings into one coherent remediation package when they share a
target and can be ordered into dependent slices. For a non-trivial package,
use `$supervised-implementer-loop`: give one persistent implementer the complete
outcome and slice map, let the primary accept each slice, and finish package
verification before returning here. Handle a small direct fix directly, and do
not force genuinely independent packages through one artificial sequence.
Pass the resolved glossary identity or explicit opt-out and the material
term-to-semantic-source relationships into the Tock leaf, then retain its
reported access, changes, candidates, and continuity in the Tock result.

For each finding:

1. Reproduce or otherwise prove the defect at its real boundary.
2. Classify its history: new regression, recurrence, incomplete prior closure,
   or inherited defect. Identify a last-known-good revision when one exists.
3. Trace the invariant to its owner. Fix the representation, state lifetime,
   dependency direction, or algorithm there.
4. Remove the obsolete path made unnecessary by the fix.
5. Add an owner-level regression and a public composed regression. For a defect
   class, add bounded property, partition, schedule, or scaling coverage rather
   than only the named example. Classify affected existing tests and apply the
   alternate-implementation check above before adding new witnesses.
6. Update the repository-declared architecture authority and the selected work
   package's owning contract row when ownership, semantics, public
   compatibility, resource policy, or complexity changes. Keep feature-specific
   targets and evidence status there, but do not copy this skill's phase
   commits, reviewer selection, or stop mechanics.
7. Map the completed work back to every review item. Do not call a finding
   closed because one narrow test passes.

For a routed architectural decision, preserve the accepted branch record and
follow-up delta in the Tock handoff. Do not relabel a current finding, required
unknown, worsening correction, or external product-contract failure as a
follow-up merely to complete remediation.

Apply the repository compatibility and cleanup policy in
[references/phase-mechanics.md](references/phase-mechanics.md). Redesign the
owning boundary when a local repair would preserve faulty ownership.

## Tick — Review the Current Implementation

Use `$evidence-efficient-review`. Start from current source and behavior, not
the remediation author's claims. Supply a repository-specific review request:

- the selected work-package scope and exact reviewed revision;
- its stable behavioral goal record and current direct scenario status;
- its normalized contract-and-evidence matrix, required specification-cell
  dispositions, explicit non-goals, and architecture ownership guidance;
- any applicable structural baseline, intended placement, and material
  structural delta for a design-sensitive owner;
- the latest applicable review artifact and its reviewed baseline;
- current conformance/evidence authorities and canonical gates;
- architectural-scope decision records, the selected durable ledger authority,
  and follow-up deltas relevant to the reviewed scope;
- the P0-P3 functional and architectural finding policy below;
- the deterministic Fixed-Point Rule and required external-capability status as
  the whole-scope completion contract;
- the selected glossary identity or explicit opt-out and material
  term-to-semantic-source relationships needed by the review leaf; and
- the repository-declared review-artifact destination and required shape.

Use incremental mode only when the previous review is trustworthy and change
impact can be bounded. Use rebaseline mode when coverage is untrusted, the
target or architecture changed materially, a zero-finding review was
overturned, or dependency impact is uncertain.

The review must audit each previous finding for exact closure and cover the
broader selected work-package goal through current contract evidence. Create or
update the required review artifact and preserve prior findings and
dispositions.

For every relevant architectural-scope decision, audit the linked authority's
qualification record and correction bound. For deferral, also verify every
non-worsening disposition, the stable dedupe identity, authorized durable
read-back, current lifecycle status, and handoff visibility. Missing required
evidence remains `unknown`; it is not a non-gating improvement.

The Tick applies the shared behavioral-design authority to the specification,
implementation, and affected tests. It records the disposition of concrete
aggregate comparison signals, audits any accepted rebaseline at the corrected
boundary, and reports the direct scenario's behavioral status separately from
mechanism progress.

When external capability matters, independently disposition the minimal
endpoint-capability probe and the composed semantic scenario defined by the
contract matrix. Apply its identity and freshness rule to reused evidence.
Classify unavailable execution without calling it a pass or product defect; a
valid `product-contract-failure` returns the contract to design or remediation.

The review artifact must:

- lead with the current functional decision and reviewed revision;
- disposition every previous finding;
- report only reproduced or source-proven functional/architectural findings;
- distinguish regressions from inherited defects;
- name the owning fix and explicitly reject plastering alternatives;
- report the stable goal ID and direct scenario's behavioral status separately
  from mechanism progress;
- report deterministic-gate, external-compatibility, and observational-telemetry
  status with their distinct decision effects;
- distinguish current findings and required unknowns from legitimate
  non-gating architectural follow-ups, and report follow-up IDs created,
  updated, closed, stale, or unchanged-but-relevant;
- list focused supporting evidence and the required architecture self-check;
- carry the glossary state, material access or candidates, terminology
  continuity, and the leaf review's clear-writing-pass status; and
- avoid security framing, validation-date disputes, Git cleanliness, README
  command drift, publication provenance, or evidence-map bookkeeping as
  findings unless the user explicitly changes scope.

Automated checks are evidence. They are not a reason to invent a process defect
and cannot negate a concrete behavior reproducer.

## Preserve Review Independence

Read and apply the independence rules in the phase-mechanics reference. Never
use the remediation author as the sole reviewer. Give the persistent reviewer
the neutral dossier and have the primary verify material candidates. Do not
spawn a fresh reviewer for an ordinary later Tick. Add another reviewer only
for a concrete unresolved dispute, and keep the persistent reviewer as owner of
the complete loop review. If that additional reviewer remains needed in a later
round, reuse the same reviewer until the dispute is resolved.

## Verify Each Tock

Read and apply the exact-revision gate in the phase-mechanics reference. A Tock
is ready for Tick only after its focused checks and canonical deterministic gate
pass on the accepted phase commit. The contract-and-evidence boundary governs
external evidence and unthresholded telemetry; neither is silently promoted to
a deterministic gate.

## Sequence External Diagnostics And Acceptance

Treat live external execution during Tock as diagnostic unless every
repository-controlled owner material to the evidence record has already passed
an independent Tick. Owner clearance alone does not make a run authoritative;
the exact-revision sequence below also applies.

1. Prove repository-controlled owner and composition behavior deterministically.
2. Commit the accepted implementation and run its exact-revision deterministic
   gate.
3. Run the independent Tick before generating authoritative external acceptance
   evidence.
4. If live behavior is needed earlier to localize a defect, label that run
   diagnostic and non-reusable. Do not update capability ledgers from it.
5. After a zero-finding repository Tick, run each required external scenario
   once against the exact accepted implementation commit. An availability
   failure keeps the capability unconfirmed; it does not fail deterministic
   acceptance.
6. Update evidence and status ledgers from the authoritative attempt, then run
   a bounded incremental Tick limited to the changed evidence owner and
   documentation.
7. Invalidate affected records after any change to a material request,
   response, identity, capture, or finalization owner.

If diagnostic or acceptance execution reveals a repository defect, return to
Tock. Do not retain the run as acceptance evidence merely because unrelated
fields passed. A valid external `product-contract-failure` reopens design or
remediation and prevents `deterministic-fixed-point`; an availability failure
preserves `capability-unconfirmed` without reopening deterministic acceptance.
After the bounded evidence-owner Tick, report `capability-confirmed`,
`capability-unconfirmed`, or `external-contract-failed` separately from the
deterministic decision.

## Fixed-Point Rule

Declare `deterministic-fixed-point` only after an independent Tick by the
persistent reviewer establishes all of the following on the current tree:

1. every prior finding is closed at its owning boundary;
2. no P0-P3 functional or architectural finding remains;
3. no compatibility shim, obsolete fallback, silent downgrade, or duplicated
   semantic authority was introduced by the accepted change or remains where
   the current contract prohibits it;
4. realistic public compositions and owner-level invariants agree, the direct
   scenario's behavioral status is reported separately, and mechanism evidence
   is not credited as behavioral acceptance;
5. resource and performance bounds measure the real work rather than hiding it;
6. repository-required architecture and behavior authorities describe the
   implementation;
7. relevant deterministic focused and complete functional checks pass on the
   exact reviewed revision;
8. no required coverage remains `unknown`, no accepted correction worsens an
   architectural-scope dimension, and no activated follow-up remains open;
9. no valid external `product-contract-failure` remains unresolved;
10. no in-scope economic actionability decision remains unknown and no defense
    added or preserved by the selected package depends only on source-level
    possibility; and
11. when the selected contract includes physical decomposition, every material
    residual responsibility cluster is `extracted`, `retained-with-proof`, or
    justified `not-applicable`; no preservation evidence has been used to clear
    semantic-owner or locality coverage.

Create or update the repository-declared review artifact even when it reports
zero findings; that artifact is the durable deterministic fixed-point witness.
Stop code remediation rather than inventing lower-value work.

Establish a whole-package modularization fixed point from both the accepted
extractions and the residual topology of every affected root. When later
evidence overturns an earlier zero-finding topology review, preserve the old
artifact as historical evidence and create a new rebaseline review of the
complete affected scope.

A legitimate non-gating architectural follow-up may coexist with
`deterministic-fixed-point` only when the Tick verifies that the current
contract is satisfied, required deterministic cells are cleared, the accepted
change is non-worsening, the deferral has an authorized durable record, and the
follow-up has not been activated as current scope. Current P0-P3 findings,
required unknowns, worsening corrections, unresolved external
`product-contract-failure`, and activated follow-ups remain gating. Reporting a
follow-up never closes or downgrades a finding.

Separately report every required external capability as `capability-confirmed`,
`capability-unconfirmed`, or `external-contract-failed` under the linked
boundary. Do not claim the capability or mark the package `Done` unless every
required initial external capability is confirmed. Only a valid
`product-contract-failure` disproves that external contract and reopens design
or remediation.

## Optional Goal Persistence

When the user explicitly asks to continue until fixed point and goal tools are
available:

1. Create one goal whose objective is to alternate remediation and independent
   review until the Fixed-Point Rule is satisfied. A suitable objective is:
   `Alternate remediation and independent review for the selected work package
   until the current review artifact reports zero P0-P3 functional or
   architectural findings, deterministic gates pass, and required external
   capability status is reported without conflating availability with product
   failure.` Do not set a token budget unless the user supplied one.
2. On later continuations, inspect the active goal and resume from the latest
   review artifact and current tree instead of restarting.
3. Mark the goal complete only after the zero-finding Tick and any external
   confirmation required by the user's objective. Do not mark it complete
   because a Tock passed tests, deterministic fixed point left required initial
   capability unconfirmed, or the budget is low.
4. Follow the goal tool's own blocked-state rules; difficulty or a long-running
   remediation is not a blocker.

Do not create a goal for a single requested Tick, Tock, or skill-maintenance
task.

## Example Invocations

- `$review-fixpoint address the latest review findings, then review the result`
- `$review-fixpoint run another independent review round for the selected work
  package`
- `$review-fixpoint keep alternating fixes and reviews until fixed point`

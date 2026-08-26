---
name: review-fixpoint
description: >-
  Alternate independent implementation reviews with principled remediation
  until the selected clojure-wasm stage reaches a functional and architectural
  fixed point. Use in this repository when asked to address the latest numbered
  stage review, review remediations, create the next review, run another review
  round, continue the tick-tock or tick-toc loop, or keep iterating until no
  actionable implementation defects remain.
---

# Review Fixpoint

Drive one repository-local loop with two alternating phases:

- **Tick — review:** use `$evidence-efficient-review` to independently audit
  the current implementation and create the next numbered review in the
  selected stage's review directory.
- **Tock — remediate:** address every actionable finding in the latest review at
  its owning architectural boundary. Use `$supervised-implementer-loop` when
  the remediation is one non-trivial package with ordered dependent slices.

Continue until a fresh Tick finds no P0-P3 functional or architectural defect.
Passing tests alone is not a deterministic fixed point. Required external
capabilities must also be confirmed before claiming the capability or `Done`.

This skill owns phase selection, repository-specific policy, phase commits, and
the fixed-point decision. The called skills own review mechanics and supervised
implementation mechanics. Slice acceptance during Tock is not the independent
Tick and cannot establish a fixed point.

Commit every completed phase. After parent acceptance and focused Tock
verification, create one coherent remediation commit and run the canonical gate
on that exact clean revision; the Tock is complete only when it passes. After
each Tick has produced its durable numbered review and the review evidence is
verified, create one review/documentation commit. Keep the worktree clean
between phases, preserve unrelated user work in the same intentional checkpoint
when it is already part of the requested stage, and never leave a completed
phase only as uncommitted working-tree state.

## Establish the Current Phase

1. Establish the stage scope named by the user or active work package. Inspect
   `git status --short`, current history, and the latest numeric review in that
   stage's review directory. Preserve unrelated worktree changes. Do not switch
   stages merely because another directory has a newer review number.
2. Read the latest review completely. Treat its current disposition and
   original findings as a checklist, but verify them against the current tree.
3. Choose the phase from evidence:
   - use Tock when any latest-review finding remains unimplemented;
   - use Tick when those remediations are present or the user asks to review
     again;
   - if state is ambiguous, inspect the diff, owners, tests, and history before
     asking the user.
4. Never rewrite an older review to become the new review. Remediation may add a
   concise current disposition at its top while preserving the historical body.

## Run the Loop

After phase selection, repeat this state machine:

```text
Tock: remediate latest review
  -> verify the current tree
  -> Tick: independently review and create review N+1
       -> zero findings: deterministic fixed point, report external status
       -> findings: preserve review N+1, return to Tock
```

Never declare a fixed point immediately after Tock. Only the following fresh
Tick can establish it. Finish and verify remediation before starting that Tick;
do not review a partially edited tree.

## Use One Contract And Evidence Boundary

Read
[references/contract-and-evidence-boundary.md](references/contract-and-evidence-boundary.md)
before either phase. Treat the normalized contract-and-evidence matrix as the
single requirement authority, keep workflow mechanics in this skill, and apply
the reference's evidence classes and result vocabulary to every phase decision.
Use its test-stability rules when a design changes.

## Tock — Remediate the Latest Review

Map every finding to its owning contract ID. Update the owning matrix row once,
then change implementation, evidence, or documentation only where that
artifact's distinct responsibility changed. Replace copied normative prose with
ID references instead of synchronizing several requirement descriptions.

Before translating review vocabulary into new limits, counters, capabilities,
or transaction states, run a design checkpoint. Ask whether each mechanism has
a distinct semantic owner, enforces a real bound, or serves an operational
consumer. If a simpler owner satisfies the project goal and stable contract,
correct the specification and affected evidence first, classify tests as
`retain`, `strengthen`, `replace`, or `delete`, and then implement the smaller
design. The specification is authoritative about outcomes, not immune from
correction when it induces accidental complexity.

Turn the findings into one coherent remediation package when they share a
target and can be ordered into dependent slices. For a non-trivial package,
use `$supervised-implementer-loop`: give one persistent implementer the complete
outcome and slice map, let the primary accept each slice, and finish package
verification before returning here. Handle a small direct fix directly, and do
not force genuinely independent packages through one artificial sequence.

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
6. Update `docs/architecture.md` and the selected stage's owning contract row
   when ownership, semantics, ABI, resource policy, or complexity changes. Keep
   feature-specific targets and evidence status there, but do not copy this
   skill's review numbering, commits, reviewer selection, or stop mechanics.
7. Map the completed work back to every review item. Do not call a finding
   closed because one narrow test passes.

Apply the breaking-cleanup rules in
[references/phase-mechanics.md](references/phase-mechanics.md). Redesign the
owning boundary when a local repair would preserve faulty ownership.

## Tick — Review the Current Implementation

Use `$evidence-efficient-review`. Start from current source and behavior, not
the remediation author's claims. Supply a repository-specific review request:

- the selected stage scope and exact reviewed revision;
- its normalized contract-and-evidence matrix, required specification-cell
  dispositions, explicit non-goals, and architecture ownership guidance;
- the latest numbered review and its reviewed baseline;
- current conformance/evidence authorities and canonical gates;
- the P0-P3 functional and architectural finding policy below;
- the deterministic Fixed-Point Rule and required external-capability status as
  the whole-scope completion contract; and
- the next numbered review path and required document shape.

Use incremental mode only when the previous review is trustworthy and change
impact can be bounded. Use rebaseline mode when coverage is untrusted, the
target or architecture changed materially, a zero-finding review was
overturned, or dependency impact is uncertain.

The review must audit each previous finding for exact closure and cover the
broader selected-stage goal through current contract evidence. Create the next
numbered review and preserve earlier reviews.

The Tick must also challenge the specification and its tests for accidental
complexity. Explicitly inspect for requirements that force nonessential
mechanisms, test names broader than their assertions, internal metrics without
operational consumers, and assertions coupled to field layout, counter
vocabulary, or the current transaction decomposition. Recommend simplifying
the specification when that preserves the project goal and a stable semantic
contract.

When external capability matters, independently disposition the minimal
endpoint-capability probe and the composed semantic scenario defined by the
contract matrix. Apply its identity and freshness rule to reused evidence.
Classify unavailable execution without calling it a pass or product defect; a
valid `product-contract-failure` returns the contract to design or remediation.

The review document must:

- lead with the current functional decision and reviewed revision;
- disposition every previous finding;
- report only reproduced or source-proven functional/architectural findings;
- distinguish regressions from inherited defects;
- name the owning fix and explicitly reject plastering alternatives;
- assess progress toward the selected stage and repository goal;
- report deterministic-gate, external-compatibility, and observational-telemetry
  status with their distinct decision effects;
- list focused supporting evidence and the required architecture self-check;
  and
- avoid security framing, validation-date disputes, Git cleanliness, README
  command drift, publication provenance, or evidence-map bookkeeping as
  findings unless the user explicitly changes scope.

Automated checks are evidence. They are not a reason to invent a process defect
and cannot negate a concrete behavior reproducer.

## Preserve Review Independence

Read and apply the independence rules in the phase-mechanics reference. Never
use the remediation author as the sole reviewer. Give one fresh reviewer the
neutral dossier and have the primary verify material candidates; add another
reviewer only for a concrete unresolved dispute.

## Verify Each Tock

Read and apply the exact-revision gate in the phase-mechanics reference. A Tock
is ready for Tick only after its focused checks and canonical deterministic gate
pass on the accepted phase commit. The contract-and-evidence boundary governs
external evidence and unthresholded telemetry; neither is silently promoted to
a deterministic gate.

## Fixed-Point Rule

Declare `deterministic-fixed-point` only after a fresh independent Tick
establishes all of the following on the current tree:

1. every prior finding is closed at its owning boundary;
2. no P0-P3 functional or architectural finding remains;
3. no compatibility shim, obsolete fallback, silent downgrade, or duplicated
   semantic authority remains in the reviewed scope;
4. realistic public compositions and owner-level invariants agree;
5. resource and performance bounds measure the real work rather than hiding it;
6. current architecture/profile docs describe the implementation; and
7. relevant deterministic focused and complete functional checks pass on the
   exact reviewed revision.

Create the next numbered review even when it reports zero findings; that review
is the durable deterministic fixed-point witness. Stop code remediation rather
than inventing lower-value work.

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
   `Alternate remediation and independent review for the selected stage until
   the newest numbered review reports zero P0-P3 functional or architectural
   findings, deterministic gates pass, and required external capability status
   is reported without conflating availability with product failure.` Do not set
   a token budget unless the user supplied one.
2. On later continuations, inspect the active goal and resume from the latest
   review/current tree instead of restarting.
3. Mark the goal complete only after the zero-finding Tick and any external
   confirmation required by the user's objective. Do not mark it complete
   because a Tock passed tests, deterministic fixed point left required initial
   capability unconfirmed, or the budget is low.
4. Follow the goal tool's own blocked-state rules; difficulty or a long-running
   remediation is not a blocker.

Do not create a goal for a single requested Tick, Tock, or skill-maintenance
task.

## Example Invocations

- `$review-fixpoint address the latest Stage 1.5 review, then review the result`
- `$review-fixpoint run another independent review round for the selected stage`
- `$review-fixpoint keep alternating fixes and reviews until fixed point`

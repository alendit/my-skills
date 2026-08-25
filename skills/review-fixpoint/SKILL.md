---
name: review-fixpoint
description: Alternate independent implementation reviews with principled remediation until the selected clojure-wasm stage reaches a functional and architectural fixed point. Use in this repository when asked to address the latest numbered stage review, review remediations, create the next review, run another review round, continue the tick-tock or tick-toc loop, or keep iterating until no actionable implementation defects remain.
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
Passing tests alone is not a fixed point.

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
       -> zero findings: fixed point, stop
       -> findings: preserve review N+1, return to Tock
```

Never declare a fixed point immediately after Tock. Only the following fresh
Tick can establish it. Finish and verify remediation before starting that Tick;
do not review a partially edited tree.

## Keep Tests Stable Across Redesigns

Prevent regression-test thrashing by separating durable contracts from current
mechanisms:

- **Contract tests** protect stable public semantics, ownership, boundedness,
  and recovery. Partition each semantic contract into focused cases instead of
  relying on one broad witness, and cover adjacent boundaries when applicable:
  exact/one-over, success/failure, first/repeated invocation, and clean retry
  after abort.
- **Mechanism tests** may probe a current decomposition during development, but
  are explicitly disposable when the owning design simplifies. Before keeping
  a test, ask whether a simpler independently designed correct implementation
  could pass it. If not, retain it only when that mechanism is itself a stable
  contract.

Whenever a specification or owning design changes, classify affected tests as
`retain`, `strengthen`, `replace`, or `delete`. Replacing or deleting an obsolete
mechanism test is a design correction, not a regression. A conformance label is
only an index: fixed-point evidence must describe the assertions that establish
the contract.

## Tock — Remediate the Latest Review

Treat every finding as a complete requirement across implementation, focused
tests, current architecture/profile documentation, and public behavior.

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
6. Update `docs/architecture.md` and the selected stage's current contract
   documents when ownership, semantics, ABI, resource policy, or complexity
   changes.
7. Map the completed work back to every review item. Do not call a finding
   closed because one narrow test passes.

Prefer breaking cleanup. This project has no external Rust-source or persisted
module compatibility requirement. Do not add or retain:

- deprecated aliases or compatibility re-exports;
- older ABI decoders, dual transports, or migration switches;
- silent defaults, normalization of impossible states, or speculative stale
  behavior;
- reproducer-specific branches or message/token whitelists;
- raised, reset, discounted, or bypassed limits that conceal excess work; or
- native fast paths that bypass a defective ordinary Clojure primitive.

If the local repair would preserve the faulty ownership model, redesign the
owning boundary instead.

## Tick — Review the Current Implementation

Use `$evidence-efficient-review`. Start from current source and behavior, not
the remediation author's claims. Supply a repository-specific review request:

- the selected stage scope and exact reviewed revision;
- its target-authoritative overview, slice/work-package contracts, explicit
  non-goals, and architecture ownership guidance;
- the latest numbered review and its reviewed baseline;
- current conformance/evidence authorities and canonical gates;
- the P0-P3 functional and architectural finding policy below;
- the Fixed-Point Rule as the whole-scope completion contract; and
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

The review document must:

- lead with the current functional decision and reviewed revision;
- disposition every previous finding;
- report only reproduced or source-proven functional/architectural findings;
- distinguish regressions from inherited defects;
- name the owning fix and explicitly reject plastering alternatives;
- assess progress toward the selected stage and repository goal;
- list focused supporting evidence and the required architecture self-check;
  and
- avoid security framing, validation-date disputes, Git cleanliness, README
  command drift, publication provenance, or evidence-map bookkeeping as
  findings unless the user explicitly changes scope.

Automated checks are evidence. They are not a reason to invent a process defect
and cannot negate a concrete behavior reproducer.

## Preserve Review Independence

Do not use the remediation author as the sole reviewer. When the primary
authored or supervised Tock and delegation is available, use one fresh
read-only reviewer for the complete Tick. Reuse it across sequential contract
cells; do not fan the same scope out to subsystem agents merely for breadth.

Give the reviewer the neutral dossier required by
`$evidence-efficient-review`, not the remediation author's expected answer.
Have the primary verify material candidate findings and severity instead of
duplicating the complete review. Add a second reviewer only for a concrete
unresolved dispute, ambiguous cross-owner evidence, or an explicitly requested
challenge, and scope that pass to the uncertainty.

Delegated reviewers need enough reasoning depth for independent defect
discovery. Honor explicit reviewer-model instructions; otherwise follow the
environment's current model-selection and memory guidance, asking when the
choice is materially unclear. Do not enable fast mode unless the user
explicitly requests it for the current task. Run a fresh QA pass on each new
review or substantial remediation.

When the primary did not author or supervise the implementation, it may apply
`$evidence-efficient-review` directly without spawning a reviewer.

## Verify Each Tock

During implementation, run focused checks proportional to each changed owner.
After parent acceptance, create the Tock phase commit, then run the selected
stage's canonical clean-revision command set once on that exact commit. Avoid
running equivalent complete suites both immediately before and after the phase
commit merely to reproduce the same evidence. A Tock is not ready for Tick
until the exact-commit gate passes; if it fails, return to remediation,
checkpoint the correction according to repository policy, and rerun the gate
before review.

At minimum preserve:

- focused owner tests and public regressions;
- formatting and warning-denying Clippy;
- debug and optimized all-target tests;
- the current conformance/fixture checks; and
- benchmark assertions relevant to structural behavior.

Keep verbose successful gate output out of review context. Record the exact
revision, command, exit status, concise counts or identity, and only the failure
tail when diagnosis is required.

Use exact counters, forms, errors, spans, retained counts, and complexity bounds
where they are contractual. Treat wall-clock timings as diagnostic.

The phase-commit rule above is mandatory for the normal loop. Do not push or
publish unless the user explicitly asks. If the caller explicitly requests a
no-commit remediation pass, honor that narrower instruction and leave the
pending phase clearly uncommitted for the caller's checkpoint.

## Fixed-Point Rule

Declare a fixed point only after a fresh independent Tick establishes all of
the following on the current tree:

1. every prior finding is closed at its owning boundary;
2. no P0-P3 functional or architectural finding remains;
3. no compatibility shim, obsolete fallback, silent downgrade, or duplicated
   semantic authority remains in the reviewed scope;
4. realistic public compositions and owner-level invariants agree;
5. resource and performance bounds measure the real work rather than hiding it;
6. current architecture/profile docs describe the implementation; and
7. relevant focused and complete functional checks pass.

Create the next numbered review even when it reports zero findings; that review
is the durable fixed-point witness. Stop rather than inventing lower-value work.

## Optional Goal Persistence

When the user explicitly asks to continue until fixed point and goal tools are
available:

1. Create one goal whose objective is to alternate remediation and independent
   review until the Fixed-Point Rule is satisfied. A suitable objective is:
   `Alternate remediation and independent review for the selected stage until
   the newest numbered review reports zero P0-P3 functional or architectural
   findings and all fixed-point criteria pass.` Do not set a token budget unless
   the user supplied one.
2. On later continuations, inspect the active goal and resume from the latest
   review/current tree instead of restarting.
3. Mark the goal complete only after the zero-finding Tick. Do not mark it
   complete because a Tock passed tests or the budget is low.
4. Follow the goal tool's own blocked-state rules; difficulty or a long-running
   remediation is not a blocker.

Do not create a goal for a single requested Tick, Tock, or skill-maintenance
task.

## Example Invocations

- `$review-fixpoint address the latest Stage 1.5 review, then review the result`
- `$review-fixpoint run another independent review round for the selected stage`
- `$review-fixpoint keep alternating fixes and reviews until fixed point`

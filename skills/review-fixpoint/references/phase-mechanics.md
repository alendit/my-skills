# Phase Mechanics

Use these repository-local mechanics during Tock implementation, independent
Tick review, and exact-revision verification.

## Contents

- Apply repository compatibility and cleanup policy
- Preserve review independence
- Verify each Tock
- Remediate findings
- Prepare and record a Tick
- Check fixed-point eligibility

## Apply repository compatibility and cleanup policy

Repository guidance supplies compatibility policy, cleanup constraints, and
canonical verification commands. Do not invent language-specific gates.

Reject a local repair that preserves faulty ownership, a prohibited
compatibility shim, silent downgrade, reproducer-specific branch, or limit
bypass. Apply only the prohibitions established by the target repository and
selected contract.

## Preserve review independence

Do not use the remediation author as the sole reviewer. When the primary
authored or supervised Tock and delegation is available, select one persistent
read-only reviewer for the complete loop. Reuse that reviewer across sequential
contract cells and later Tick rounds; do not fan the same scope out to
subsystem agents merely for breadth. The retained context should include the
reviewed baseline, prior findings, accepted dispositions, and evidence needed
to recognize recurrence or incomplete closure.

Give the reviewer the neutral dossier required by `$evidence-efficient-review`,
not the remediation author's expected answer. Have the primary verify material
candidate findings and severity instead of duplicating the complete review. Add
a second reviewer only for a concrete unresolved dispute, ambiguous cross-owner
evidence, or explicitly requested challenge; scope that pass to the uncertainty
and reuse the same reviewer across later rounds until that dispute is resolved.

Use enough reasoning depth for independent defect discovery. Honor explicit
reviewer-model instructions; otherwise follow current environment selection and
memory guidance. Do not enable fast mode unless the user requests it for this
task. Verify material review claims and request additional QA only for a
concrete unresolved risk; a new review does not automatically require another
review layer. If the
persistent reviewer becomes unavailable, report the continuity loss and ask the
user before selecting a replacement; do not replace it merely to obtain a fresh
context.

When the primary did not author or supervise the implementation, it may apply
`$evidence-efficient-review` directly without spawning a reviewer.

## Verify each Tock

Run focused checks proportional to each changed owner during implementation.
After parent acceptance, reuse a coherent handoff commit when it represents
exactly the accepted Tock and existing authority permits it; otherwise create
the Tock phase commit. Run the repository-declared canonical clean-revision
command set once on that exact commit. Do not create an empty acceptance commit
or run equivalent complete suites immediately before and after the phase commit
merely to reproduce the same evidence.

A Tock is not ready for Tick until the exact-commit gate passes. On failure,
return to remediation, checkpoint the correction under repository policy, and
rerun the gate before review.

Choose focused evidence from the defect and changed boundary. Reuse current
checks whose assertions establish the required behavior; add or strengthen
regressions where a gap remains. Use documentation/source/link checks for prose
defects rather than manufacturing runtime tests. Preserve applicable repository
formatting, lint, compile, conformance, fixture, and complete deterministic gates;
benchmark assertions apply only to named performance bounds.

Keep verbose successful output out of review context. Record revision, command,
exit status, concise counts or identity, and only the failure tail needed for
diagnosis. Use exact counters, forms, errors, spans, retained counts, and
complexity bounds where contractual; treat wall-clock timings as diagnostic.

The phase-commit rule is mandatory for the normal loop. Do not push or publish
unless the user asks. If the caller requests a no-commit remediation pass,
honor it and leave the pending phase clearly uncommitted for the caller's
checkpoint.

## Remediate findings

For each finding:

1. Reproduce or otherwise prove the defect at its real boundary.
2. Classify its history: new regression, recurrence, incomplete prior closure,
   or inherited defect. Identify a last-known-good revision when one exists.
3. Trace the invariant to its owner. Fix the representation, state lifetime,
   dependency direction, or algorithm there.
4. Remove the obsolete path made unnecessary by the fix.
5. Select evidence that would detect this defect at its real boundary. Reuse
   adequate existing coverage; add or strengthen owner-level or public-composed
   regressions when their distinct behavior needs proof. Require both only when
   each covers a material gap. Use bounded property, partition, schedule, or
   scaling coverage when the defect class warrants it. For prose-only findings,
   validate the corrected claim and affected references. Classify existing tests and apply the
   [alternate-implementation check](contract-and-evidence-boundary.md#keep-tests-stable-across-redesigns)
   before adding new witnesses.
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
[the compatibility section](#apply-repository-compatibility-and-cleanup-policy). Redesign the
owning boundary when a local repair would preserve faulty ownership.

## Prepare and record a Tick

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
- the P0-P3 functional and architectural finding policy in this section;
- the latest result level and plan identity under the contract-and-evidence
  boundary;
- the fixed-point eligibility checks below and required external-capability status as
  the whole-scope completion contract;
- the explicit glossary opt-out marker alone or, for a selected glossary, its
  identity, declared-scope fit, and material term-to-semantic-source
  relationships and unresolved candidates needed by the review leaf; and
- the repository-declared review-artifact destination and required shape.

For every relevant architectural-scope decision, audit the
[architectural-scope authority's](../../supervised-implementer-loop/references/architectural-scope-decision.md)
qualification record and correction bound. For deferral, also verify every
non-worsening disposition, the stable dedupe identity, authorized durable
read-back, current lifecycle status, and handoff visibility. Missing required
evidence remains `unknown`; it is not a non-gating improvement.

The Tick applies the [behavioral-design authority](../../evidence-efficient-review/references/behavioral-design-trace.md) to the specification,
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
- carry the explicit glossary opt-out marker alone or, for a selected glossary,
  its state, declared-scope fit, changed or still-material candidates,
  terminology continuity, and the leaf review's clear-writing-pass status; and
- avoid security framing, validation-date disputes, Git cleanliness, README
  command drift, publication provenance, or evidence-map bookkeeping as
  findings unless the user explicitly changes scope.

Automated checks are evidence. They are not a reason to invent a process defect
and cannot negate a concrete behavior reproducer.

## Check fixed-point eligibility

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

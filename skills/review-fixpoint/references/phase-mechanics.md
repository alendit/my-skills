# Phase Mechanics

Use these repository-local mechanics during Tock implementation, independent
Tick review, and exact-revision verification.

## Contents

- Apply repository compatibility and cleanup policy
- Preserve review independence
- Verify each Tock

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
task. Run independent QA on each new review or substantial remediation. If the
persistent reviewer becomes unavailable, report the continuity loss and ask the
user before selecting a replacement; do not replace it merely to obtain a fresh
context.

When the primary did not author or supervise the implementation, it may apply
`$evidence-efficient-review` directly without spawning a reviewer.

## Verify each Tock

Run focused checks proportional to each changed owner during implementation.
After parent acceptance, create the Tock phase commit, then run the repository-
declared canonical clean-revision command set once on that exact commit. Do not
run equivalent complete suites immediately before and after the phase commit
merely to reproduce the same evidence.

A Tock is not ready for Tick until the exact-commit gate passes. On failure,
return to remediation, checkpoint the correction under repository policy, and
rerun the gate before review.

At minimum preserve:

- focused owner tests and public regressions;
- applicable repository-declared formatting, lint, and compile checks;
- the project-declared complete deterministic gate;
- conformance or fixture checks relevant to changed contracts; and
- benchmark assertions only where the contract names a performance bound.

Keep verbose successful output out of review context. Record revision, command,
exit status, concise counts or identity, and only the failure tail needed for
diagnosis. Use exact counters, forms, errors, spans, retained counts, and
complexity bounds where contractual; treat wall-clock timings as diagnostic.

The phase-commit rule is mandatory for the normal loop. Do not push or publish
unless the user asks. If the caller requests a no-commit remediation pass,
honor it and leave the pending phase clearly uncommitted for the caller's
checkpoint.

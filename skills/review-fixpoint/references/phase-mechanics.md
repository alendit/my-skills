# Phase Mechanics

Use these repository-local mechanics during Tock implementation, independent
Tick review, and exact-revision verification.

## Contents

- Prefer breaking cleanup
- Preserve review independence
- Verify each Tock

## Prefer breaking cleanup

This project has no external Rust-source or persisted module compatibility
requirement. Do not add or retain:

- deprecated aliases or compatibility re-exports;
- older ABI decoders, dual transports, or migration switches;
- silent defaults, normalization of impossible states, or speculative stale
  behavior;
- reproducer-specific branches or message/token whitelists;
- raised, reset, discounted, or bypassed limits that conceal excess work; or
- native fast paths that bypass a defective ordinary Clojure primitive.

If a local repair would preserve faulty ownership, redesign the owning boundary.

## Preserve review independence

Do not use the remediation author as the sole reviewer. When the primary
authored or supervised Tock and delegation is available, use one fresh
read-only reviewer for the complete Tick. Reuse that reviewer across sequential
contract cells; do not fan the same scope out to subsystem agents merely for
breadth.

Give the reviewer the neutral dossier required by `$evidence-efficient-review`,
not the remediation author's expected answer. Have the primary verify material
candidate findings and severity instead of duplicating the complete review. Add
a second reviewer only for a concrete unresolved dispute, ambiguous cross-owner
evidence, or explicitly requested challenge; scope that pass to the uncertainty.

Use enough reasoning depth for independent defect discovery. Honor explicit
reviewer-model instructions; otherwise follow current environment selection and
memory guidance. Do not enable fast mode unless the user requests it for this
task. Run fresh QA on each new review or substantial remediation.

When the primary did not author or supervise the implementation, it may apply
`$evidence-efficient-review` directly without spawning a reviewer.

## Verify each Tock

Run focused checks proportional to each changed owner during implementation.
After parent acceptance, create the Tock phase commit, then run the selected
stage's canonical clean-revision command set once on that exact commit. Do not
run equivalent complete suites immediately before and after the phase commit
merely to reproduce the same evidence.

A Tock is not ready for Tick until the exact-commit gate passes. On failure,
return to remediation, checkpoint the correction under repository policy, and
rerun the gate before review.

At minimum preserve:

- focused owner tests and public regressions;
- formatting and warning-denying Clippy;
- debug and optimized all-target tests;
- current conformance/fixture checks; and
- benchmark assertions relevant to structural behavior.

Keep verbose successful output out of review context. Record revision, command,
exit status, concise counts or identity, and only the failure tail needed for
diagnosis. Use exact counters, forms, errors, spans, retained counts, and
complexity bounds where contractual; treat wall-clock timings as diagnostic.

The phase-commit rule is mandatory for the normal loop. Do not push or publish
unless the user asks. If the caller requests a no-commit remediation pass,
honor it and leave the pending phase clearly uncommitted for the caller's
checkpoint.

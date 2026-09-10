# Improvement observations: implementation convergence control

## Status and evidence boundary

Recorded on 2026-09-08 from the inherited Clojure-Wasm M2 implementation
conversation. This is a process assessment and improvement proposal, not a
fresh implementation review, an accepted skill change, or an instruction to
alter the active implementation workflow.

The available evidence includes parent acceptance inspections, correction
messages, reported focused checks, and completion waits. It does not include
a complete implementer execution trace or token accounting. No completed
correction package or parent acceptance result was visible before the
conversation was interrupted. The agents' subsequent state is unknown here.

The central observation is **good diagnosis, but weak convergence control**:
the steering identified concrete contract violations, yet did not turn those
findings into sufficiently bounded, verifiable implementation completions.

## The implementation blocker

M2 was blocked by incomplete realization of an agreed architecture, not by an
unresolved product choice about floating-point support. Focused arithmetic
tests passed, but the submitted N4/N5 candidate did not establish the complete
scalar-planning and callable-lifetime contracts.

Parent inspection identified three material problems:

1. **Evaluation order.** The compiled `+` and `*` integer loops evaluated
   `next` before checked arithmetic or conversion could fail. Advancing the
   sequence first changes observable behavior when `next` is redefined. The
   correction needed to preserve arithmetic-before-advance order in source,
   with public failure/effect witnesses.
2. **Transitive callable liveness.** A reclamation fix followed directly
   captured callables, but did not establish reachability through nested
   captures, collections, or atoms. Passing the original captured-callable
   reproducer did not prove complete graph retention, including sharing and
   cycles.
3. **Scalar-plan completeness.** The planner handled the production loop
   examples but still decoded old immediate tags, lacked general planned
   conversions, rejected some agreeing raw conditional/sequence producers,
   and did not correctly handle mixed loop joins or unreachable backedges.
   Emission consumed selected plan facts while still deriving other decisions
   itself. The production source-to-Wasm witness covered `+`, but not `*`.

This followed an earlier rejected candidate that had used loop recognition and
special-case emission instead of the accepted immutable representation-plan
architecture. The later candidate therefore exposed a repeated gap between
the intended owner boundary and the implementation's demonstrated coverage.

## What the steering did well

- Findings named exact code locations, behavioral consequences, required
  corrections, and regression-test partitions. They were actionable rather
  than generic requests to improve architecture.
- Parent acceptance distinguished passing focused tests from satisfying the
  complete contract. It did not accept a special-case fix solely because the
  original reproducer passed.
- The accepted specification remained authoritative. Realization failures
  were not turned into unnecessary product questions or weaker requirements.
- Existing implementer continuity was preserved. Separate, non-overlapping
  lint and dead-code cleanup made useful progress while corrections ran.
- Completion-only checking respected the user's explicit request to avoid
  frequent, expensive inspection of intermediate agent work.

## Where convergence control was inefficient

### Corrections were dispatched before inspection was consolidated

The parent first sent evaluation-order, lifetime, and production-coverage
corrections. It then discovered and sent substantially larger planner
corrections while implementation was already underway.

That sequence changed a seemingly bounded remediation into another
architectural completion package. The observed issue was not the existence
of additional findings; it was starting realization before the parent had
assembled the material acceptance findings already discoverable in the
candidate's changed owners.

### A design checkpoint was suggested rather than enforced

After repeated architectural misses, the steering still issued a broad
implementation request with a conditional instruction to stop if a design
checkpoint became necessary. It did not first require a compact demonstration
of how the remaining planner and reachability obligations would be owned,
represented, consumed, and tested.

This left substantial interpretation and dependency ordering inside a long
implementer turn. Detailed correction prose did not itself prove a shared,
implementable design.

### Waiting reduced inspection cost but did not establish convergence

The transcript contains hours of completion waits without a correction result.
Those waits were not source/progress polls and should not be treated as having
the same cost as repeatedly reading an implementation. Nevertheless, repeated
"still waiting" updates supplied little new information, and a large opaque
work package provided few useful completion boundaries.

The evidence does not establish that the implementer was stalled, that a
notification was lost, or that a different model would have completed faster.
It also does not support a quantified token-efficiency comparison. The
supported conclusion is narrower: the steering had not demonstrated
resolution before interruption.

## Proposed improvement direction

Use an executable sequence that produces smaller, meaningful completions:

1. **Finish the bounded acceptance inspection.** Inspect the complete changed
   owner and adjacent evidence before dispatching corrections. Consolidate
   related findings and distinguish local defects from missing architectural
   obligations. This is not a request to audit the entire repository first.
2. **Make the necessary design checkpoint explicit.** When a candidate repeats
   an architectural mismatch, require a concrete correction design before
   another broad realization attempt. Show the owning components, producer
   and consumer boundaries, failure paths, and decisive evidence. Preserve the
   accepted contract unless concrete evidence requires reopening it.
3. **Accept ordered implementation slices.** Each completion should establish
   a coherent obligation before dependent work relies on it. For this case,
   representation facts and joins must support emission consumers; transitive
   liveness needs complete-owner evidence beyond the first reproducer.
4. **Use completion and blocker events, not routine progress interrogation.**
   Preserve the user's completion-only inspection preference. A requested
   design checkpoint or actual blocker is a meaningful return boundary;
   repeated unchanged waiting messages are not acceptance evidence.
5. **Keep package verification and independent review distinct.** Parent slice
   acceptance establishes readiness for dependent work, not an independent
   review result. Run the required gate on the accepted exact candidate and
   retain the separate independent review boundary before claiming completion.

The improvement target is faster verified convergence, not more supervision
messages. Smaller coherent completions should expose misunderstandings earlier
without discarding implementer context or increasing intermediate polling.

## Non-goals and open evidence

- Do not infer a universal timeout, file-size limit, slice count, or token
  budget from this single case.
- Do not prescribe model replacement, automatic agent restarts, or broader
  mutation authority on the strength of elapsed waiting time.
- Do not weaken architectural acceptance to match a passing happy-path test.
- Do not treat useful parallel cleanup as resolution of the blocking work.
- Do not claim that this proposal has improved efficiency yet. That requires
  later evidence connecting correction requests, accepted completions, rework,
  and verification outcomes; elapsed time and token usage remain separate
  observations rather than invented acceptance thresholds.

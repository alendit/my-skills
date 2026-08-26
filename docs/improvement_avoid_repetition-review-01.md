# Improvement Avoid Repetition — Review 01

## Decision

**Changes requested** on revision
`af495c202c2b8bdd8a408c583020f818af43b0de`.

This rebaseline review found one P1 and one P2. The package is not at a
deterministic fixed point. No prior numbered review exists.

Reviewed scope:

- `docs/improvement_avoid_repetition.md`
- all six skill packages named by that plan
- the Feature 88 `addendum2.org` source as the motivating fixture

The unrelated untracked `docs/improvement-right-feedback.md` was not reviewed.

## R1–R8 coverage ledger

| Row | Status | Evidence |
|---|---|---|
| R1 Single authority | **Candidate; V1 failed** | Specification normalization is enforced by `evidence-efficient-review/references/specification-review.md`. Architecture documents link contract IDs. `technical-note-series` can still make its guide a second normative owner for an existing project or feature goal; see Finding 01. |
| R2 Scenario portfolio | Cleared; V2 passed | The specification and implementation references require observable scenario invariants, stable contract IDs, shared capture helpers, and localization signals rather than assertion inventories. |
| R3 Evidence separation | Cleared; V3 passed | External identity, freshness, failure status, and completion effects remain distinct across review, fixpoint, and implementation handoff. |
| R4 Telemetry | Cleared; V4 passed | Metrics require a baseline, method, direction, and threshold or remain observational and non-gating. |
| R5 Durable/private boundary | Cleared; V5 passed | Durable contracts and conditional implementation appendices are separate, and equivalent private implementations remain possible unless a correctness reason is named. |
| R6 Exact limits | Cleared; V6 passed | Normative numeric limits require correctness, workload, resource, boundary, and revision evidence; otherwise they are private defaults. |
| R7 Split external scenarios | Cleared; V7 passed | Minimal endpoint capability and broader semantic composition are separately reportable while sharing instrumentation. |
| R8 Workflow boundary | Cleared; V8 passed | Feature artifacts own semantics and evidence links; `review-fixpoint` owns numbering, commits, reviewer selection, repetition, and stop mechanics. |

## Confirmed findings

### P1 — Technical-note guides can become a second normative feature authority

R1 requires teaching documents to link normative contract IDs rather than
reproduce them (`docs/improvement_avoid_repetition.md:56-59,185-187`).

The technical-note entrypoint makes the guide the authority for shared material
(`skills/technical-note-series/SKILL.md:39-41`), while its mandatory reference
makes the guide the sole authority for the shared project goal
(`skills/technical-note-series/references/research-and-reader-journey.md:118-126`).
It does not preserve an existing feature contract as the normative owner or
require stable contract-ID links.

Applied to Feature 88, this permits a guide to restate retention, fallback, or
lifetime requirements alongside the normalized matrix—the R1 failure the
package is intended to prevent.

**Owning correction:** make the guide authoritative only for series-owned
reading paths, running-example identity, teaching vocabulary, scope, and
navigation. When a project or feature goal already has a normative contract,
link its stable contract IDs and owning source. Plain-language orientation must
be explicitly explanatory, not a second acceptance authority. Add that routing
check to cross-note coherence.

### P2 — Publication remediation no longer requires a fresh review

The parent revision required repairing each valid finding, rerunning affected
validation, and submitting the complete series for another review until a fresh
pass reported no actionable defect
(`technical-note-series/SKILL.md` at `af495c2^`, lines 371-419).

The reviewed reference requires only one independent review
(`skills/technical-note-series/references/validation-and-review.md:52-64`), and
the entrypoint delegates iterative review only when the caller separately asks
for it (`skills/technical-note-series/SKILL.md:67-76`). The publication gate
still requires every cell to be cleared, but the normal workflow no longer
contains the remediation-and-fresh-review path that establishes that state.

This weakens previous behavior and violates S5's requirement to move reusable
rubrics without weakening them (`docs/improvement_avoid_repetition.md:97-103`).

**Owning correction:** every publication pass receives a fresh independent
evidence-efficient review after validation. If a required cell is candidate or
unknown, repair its owning guide or note, rerun affected validation, and
continue through `review-fixpoint` until a fresh review clears every required
cell. `technical-note-series` supplies the publication contract;
`review-fixpoint` continues to own numbering, commits, reviewer selection,
repetition, and stop mechanics.

## Unknowns

None. Every required R1–R8 cell was inspected and either cleared or converted
to a confirmed finding. External capability execution is not applicable to this
skill-package revision; V3 validates the state model without provider access.

## Gate evidence

All evidence was collected on exact revision
`af495c202c2b8bdd8a408c583020f818af43b0de`.

- six `quick_validate.py` checks passed;
- all relative Markdown references resolved;
- every reference over 100 lines contained `## Contents`;
- tracked working state matched the reviewed revision;
- `git diff --check` passed; and
- only the explicitly ignored untracked document was present.

## Fixed-point result

- `deterministic-fixed-point`: **not reached**
- required external capability: **not applicable**
- `Done`: **not reached**

The deterministic/capability/Done vocabulary is otherwise sound: missing or
unavailable external evidence remains capability-unconfirmed, only a valid
product-contract failure disproves the external contract, and `Done` requires
both deterministic fixed point and every required capability confirmation.

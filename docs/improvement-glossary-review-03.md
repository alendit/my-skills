# Glossary Integration Review 03

## Decision

**Accepted with zero P0-P3 findings or required unknowns.** This fresh
incremental Tick reviews `docs/improvement-glossary.md` at exact revision
`bd87c1e47000dd1bb22cb0cdedc3c4330ff08182`.

The remaining placement defect is closed at its owner. GL2 now gives an
explicit opt-out precedence over every glossary-selection and placement branch,
and M5 distinguishes an opt-out present in the initial instructions from a
refusal after the missing-glossary question. The earlier teaching-vocabulary and
authorized-scope corrections remain complete. Future package checks, controlled
model trials, and human evaluation were not executed and are not evidence for
this specification decision.

## Prior-finding dispositions

| Prior finding | Disposition | Evidence |
|---|---|---|
| G1 placement contract | **Closed.** GL2 is the sole normative placement owner. Its ordered branches now stop immediately on an explicit opt-out, use a selected existing glossary, accept an explicitly selected absent path without extending write authority, ask project-local versus look-aside only when no instruction resolves placement, and ask which source governs when several candidates remain unresolved. M5 separately covers an initial opt-out and refusal after M1, with no subsequent question or write. |
| G2 teaching-vocabulary authority | **Closed and not regressed.** GL7 assigns project-wide term identity, aliases, and concise meaning to the selected glossary. The technical-note guide retains prerequisite order, reader-specific first-use explanation, series-only terms, and navigation. S4 names the entrypoint and all three current vocabulary references that must migrate coherently; D2 rejects any remaining second canonical project definition; M7 preserves local teaching. |
| G3 authorization escape | **Closed and not regressed.** GL6 limits glossary and dependent-prose edits to the current authorized scope. It requires known out-of-scope dependents to be reported with their stale term and semantic source, not edited or silently treated as current. S3 and M6 preserve the same source and authorization boundary. |

## Placement-branch exercise

| Branch | Required outcome | Current specification result |
|---|---|---|
| Initial explicit opt-out | Continue without glossary placement, creation, or persistence. | GL2 routes directly to GL5 before selection or placement. M5 requires local explanation, no file, no persisted term, and no placement question. |
| No glossary and no instructions | Ask whether placement should be project-local or at a user-selected look-aside location before any write. | GL2 requires the question and prohibits creation or persistence until the answer. M1 rejects automatic selection of `docs/glossary.md`. |
| Missing glossary with an explicitly selected path | Treat placement as resolved without treating the selected path as write authorization. | GL2 retains the task's ordinary write-authorization boundary. M2 checks the absent-file case and rejects an authorization bypass. |
| Existing selected glossary | Use the selected source and still explain prerequisites locally when the reader needs them. | GL2 selects the existing glossary. GL5 and M5 prevent a glossary link from replacing a reader-needed explanation. |
| Several unresolved candidates | Ask which source governs; do not merge or choose automatically. | GL2 owns the authority question. M2 localizes an automatic merge or selection to the placement-precedence contract. |
| Refusal after the placement question | Continue with an artifact-local definition and ask no further placement question. | GL5 owns the fallback. M5 explicitly tests refusal after M1 and prohibits a file, persisted term, or repeated placement question. |

The branches are mutually consistent. A selection decides terminology source or
placement, but it does not grant a broader documentation write. A refusal ends
the placement flow rather than becoming another unresolved-location state.

## Contract coverage

| Contract | Status | Evidence and decision |
|---|---|---|
| GL1 | Cleared | The shared workflow is a one-level reference within the planned `clear-technical-writing` package. No standalone glossary skill, independent terminology reviewer, copied consumer workflow, or second prose pass is proposed. |
| GL2 | Cleared | The six exercised branches form one ordered consent and placement contract. The user or repository guidance selects placement; the leaf artifact owner performs discovery without acquiring new mutation authority. |
| GL3 | Cleared | The glossary owns preferred term identity and explanation only. Code, accepted contracts, architecture authorities, and artifact owners continue to decide behavior, ownership, lifetime, scope, and acceptance. M3 checks the conflict direction. |
| GL4 | Cleared | Entry admission requires a useful project distinction. Entry layout remains replaceable guidance, aliases point to one concept, and neither a paragraph cap nor typography becomes a correctness mechanism. |
| GL5 | Cleared | Relevant glossary entries are source material, not a substitute for local prerequisite explanation. The no-glossary and declined-glossary paths keep the artifact clear without persisting an entry. |
| GL6 | Cleared | Accepted semantic sources establish meaning; selected location and scope authorize writes; CTW8 revalidation stays inside the authorized edit scope; known external dependents are reported without mutation. |
| GL7 | Cleared | Every consumer retains its substantive owner. The technical-note migration removes competing project-term authority while retaining pedagogy. Review findings and implementation contracts cannot be altered by glossary wording, and `review-fixpoint` performs no second pass. |
| GL8 | Cleared | D1-D2 cover only static repository composition. M1-M7 remain controlled model evidence, and glossary-conditioned artifacts extend the existing CTW V11 pilot without inventing a second capability claim. Unthresholded cost and size measurements remain observational. |

## Required specification cells

| Cell | Status | Disposition |
|---|---|---|
| Single normative authority | Cleared | GL1-GL8 are the sole glossary contract authority. Placement behavior appears only in GL2; slices and scenarios reference that owner. GL5 owns only artifact-local fallback. |
| Durable contract boundary | Cleared | The plan specifies observable source selection, consent, authority, term use, maintenance, and composition while allowing equivalent glossary formats and private dependency representations. |
| Scenario diagnosability | Cleared | M1, M2, and M5 isolate each placement and refusal branch. M3-M7 localize semantic authority, admission, fallback, authorized maintenance, consumer ownership, and single-pass failures. D1-D2 localize package and static authority defects. |
| Evidence topology | Cleared | Static package checks, controlled model behavior, paired human comprehension, and observational telemetry have separate owners and decision effects under CTW10. No external lane is promoted to a deterministic repository gate. |
| External freshness | Cleared for specification | GL8 inherits CTW10's exact identity, event-bounded initial non-reuse, failure classes, and future interval-justification rule. No glossary-specific freshness clock is introduced. |
| Telemetry decision power | Cleared | Entry count, glossary size, lookup time, prompt tokens, prose length, and edit size are explicitly observational until a protocol supplies a baseline and threshold. |
| Exact-limit justification | Not applicable | The plan rejects the proposed paragraph cap and introduces no normative size, count, timeout, retry, or calendar limit. |
| Workflow boundary | Cleared | The feature plan states its target and evidence lanes but leaves review numbering, commits, reviewer selection, remediation repetition, and stop mechanics to `review-fixpoint`. |

## Clear-writing and consumer composition

- CTW1 remains substantive-authority owner: glossary prose cannot override
  source facts, accepted contracts, review findings, or implementation scope.
- CTW2 remains single-pass owner: glossary discovery is source preparation by
  the leaf artifact skill, and the artifact receives one final prose pass.
- CTW5 owns the final terminology check and local plain-language explanation;
  the glossary adds durable project identity without turning prose into a list
  of definitions.
- CTW8 supplies dependency-aware revalidation only for the changed source and
  authorized scope supplied by the caller.
- CTW10 owns model identity, external failure, freshness, human evaluation, and
  telemetry rules. GL8 extends those lanes rather than duplicating them.
- The planned `technical-note-series` changes replace its current broad
  guide-owned teaching-vocabulary rule across `SKILL.md`,
  `research-and-reader-journey.md`, `drafting-and-coherence.md`, and
  `validation-and-review.md`. The guide still teaches the term at first use but
  does not retain a second canonical project definition.

This composition introduces no standalone glossary skill, compatibility shim,
silent default location, private glossary representation, or duplicated
semantic authority.

## Findings and unknowns

No P0-P3 functional or architectural finding remains. No required
specification coverage is unknown. The future implementation evidence listed
below is intentionally unexecuted; its absence does not make this specification
review incomplete and does not prove the planned capability.

## Evidence status

- **Specification-source evidence:**
  `git show --check bd87c1e47000dd1bb22cb0cdedc3c4330ff08182` passed. The
  specification content at that exact revision matches the reviewed working-tree
  file, and the prior reviews, composed clear-writing plan, contract-centered
  evidence rules, and current technical-note vocabulary authorities were
  inspected.
- **Review-artifact hygiene:** `git diff --check` passes with only this Review 03
  artifact added.
- **Future deterministic implementation evidence:** D1-D2 and the applicable
  CTW package gates were not executed. The planned package and consumer
  migrations do not yet exist at this specification revision.
- **Future model compatibility:** M1-M7 were not executed. Glossary-aware model
  behavior remains `capability-unconfirmed`; no generated output is classified
  as passing or as `product-contract-failure`.
- **Future human comprehension:** the glossary-conditioned CTW V11 pilot was not
  executed. Human comprehension remains `human-comprehension-unconfirmed`.
- **Observational telemetry:** no glossary or prose cost measurements were
  collected. They remain non-gating.

## Follow-up disposition

There is no justified non-gating architectural follow-up, activated follow-up,
or durable follow-up-ledger mutation. Implementing S1-S5 and collecting the
named future evidence are planned work, not deferred current defects.

## Specification fixed-point result

`deterministic-fixed-point` is **reached for the specification** at
`bd87c1e47000dd1bb22cb0cdedc3c4330ff08182`. Every prior finding is closed at
its owning contract, GL1-GL8 and every required specification cell are cleared
or not applicable, and this fresh Tick finds no P0-P3 defect or required
unknown.

This result does not establish future implementation completion. D1-D2,
M1-M7, and the glossary-conditioned CTW V11 pilot remain unexecuted. The future
package cannot claim its deterministic implementation fixed point,
model-capability confirmation, human-comprehension confirmation, or `Done`
until those applicable evidence lanes satisfy GL8 and CTW10.

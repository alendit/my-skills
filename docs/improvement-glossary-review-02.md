# Glossary Integration Review 02

## Decision

**Changes requested.** This incremental Tick reviews
`docs/improvement-glossary.md` at exact revision
`a3fcd0a42a840f8f28f2ba66c4f1a5326c8d468c`.

## Current disposition after Tock

The remediation following this historical review closes the remaining G1
branch: GL2 now gives an explicit opt-out precedence over glossary selection or
placement, routes directly to GL5 without another question or write, and M5
tests both an initial opt-out and a refusal after M1. This disposition preserves
the original decision below; a fresh Tick must verify it before fixed point.

The remediation closes the competing technical-note vocabulary authority and
bounds dependent edits to the authorized scope. It also removes the duplicated
placement procedure. One part of the placement precedence remains incomplete:
an explicit instruction not to create or use a glossary still reaches GL2's
location question, although GL5 says to continue with a local definition after
the user declines. The user required the question only when no explicit
instruction resolves the choice.

Future D1-D2 package checks, M1-M7 model trials, and the glossary-conditioned
CTW V11 pilot were not executed. They remain future implementation and
capability evidence, not proof of this specification.

## Prior-finding dispositions

| Prior finding | Disposition | Evidence |
|---|---|---|
| G1 placement contract | **Incomplete closure.** GL2 now owns the ordered positive-location and no-instruction behavior, the old protocol is gone, S1 only invokes GL2, and M2 covers a selected path whose file is absent. GL2 still asks whenever neither authority selects a location, including when an explicit instruction has already declined glossary creation or use. GL5 supplies the opposite continuation for that state. The finding below retains G1. |
| G2 teaching-vocabulary authority | **Closed.** GL7 assigns project-wide term identity and concise meaning to the selected glossary while the series guide owns introduction order, reader-specific explanations, series-only terms, and navigation. S4 names `technical-note-series/SKILL.md` and all three current vocabulary references. D2 rejects a remaining canonical shared-term claim, while M7 requires local teaching at the reader's point of need. |
| G3 authorization escape | **Closed.** GL6 limits writes and revalidation to the current authorized scope and requires known out-of-scope dependents to be reported rather than edited. S3 and M6 carry the same boundary without creating another authority. |

## Contract coverage

| Contract | Status | Evidence and decision |
|---|---|---|
| GL1 | Cleared | The glossary workflow remains a one-level `clear-technical-writing` reference. The plan rejects a standalone glossary skill, keeps consumers as artifact owners, and adds no second prose pass. |
| GL2 | Finding | The positive placement, missing-file, multiple-candidate, and no-instruction branches are now centralized. The pre-existing explicit opt-out branch is contradictory with GL5. G1 applies. |
| GL3 | Cleared | The glossary owns preferred terminology and explanation only. Code, accepted contracts, architecture authorities, and artifact owners retain semantic truth; M3 observes the conflict direction. |
| GL4 | Cleared | Entry admission depends on a useful project distinction. Alias, explanation, and source guidance remain replaceable by a repository-native representation; no paragraph or typography mechanism is normative. |
| GL5 | Cleared subject to G1's GL2 correction | It preserves local prerequisite explanations, rejects vocabulary dumps, and supplies the correct non-persistent fallback when glossary creation is declined. GL2 must route an existing refusal here instead of asking again. |
| GL6 | Cleared | A semantic source must establish meaning, writes require authorized location and scope, in-scope dependents are revalidated, and known out-of-scope dependents are reported without mutation. M6 localizes source and scope failures. |
| GL7 | Cleared | The proposed series split matches the current authority surface that must change: the entrypoint's `teaching vocabulary`, the reader-journey guide authority, the cross-note definition check, and the validation matrix. Architecture, review, implementation, and outer-workflow responsibilities remain with their current owners. |
| GL8 | Cleared | D1-D2 are static repository gates; M1-M7 are controlled model evidence; glossary cases extend CTW V11 rather than adding another human-capability claim. Unthresholded counts and costs remain observational. |

## Finding

### G1 — P2 — Explicit glossary opt-out does not suppress the placement question

**Proof.** GL2 first says to inspect explicit user instructions and repository
guidance, but its only resolved branches are an existing selected glossary or an
authority that selects a location (line 48). If an initial instruction instead
says not to create or use a glossary, neither authority has selected a location,
so the same row requires the agent to ask project-local versus look-aside. GL5
then says that when the user declines glossary creation, the artifact should
define the concept locally and persist nothing (line 51). M1 covers no
instruction, M2 covers selected or ambiguous locations, and M5 says only
"creation is declined"; none distinguishes a refusal already present in the
initial instructions from an answer to the unnecessary question (lines
140-145).

**Impact.** A valid explicit instruction can be ignored and the user asked to
make a choice they already made. An implementation may also follow GL5 directly,
causing two conforming implementations to expose different consent behavior.
This violates the requested rule that the placement question is the fallback
when the project has no glossary and no explicit instructions.

**Owner and replacement direction.** GL2 owns the precedence correction. Insert
this branch after inspecting instructions and before selecting or proposing a
location:

> If explicit user instructions decline glossary creation or use for this task,
> do not ask the placement question, create a file, or persist a term. Apply
> GL5's local-definition fallback. Otherwise use an existing selected glossary
> or the location selected by user instructions or repository guidance. Only
> when no glossary exists and neither authority resolves the choice should the
> agent ask project-local versus user-selected look-aside.

Keep GL5 as the owner of artifact-local fallback behavior; it should reference
no placement procedure. Extend M5 to cover both an opt-out present in the
initial instructions and a decline in response to M1. Both cases must continue
with local explanation, create no file, and ask no further placement question.

## Required specification cells

| Cell | Status | Disposition |
|---|---|---|
| Single normative authority | Finding | The duplicate placement section is gone, but GL2 and GL5 currently prescribe different next actions for an explicit refusal that does not select a location. G1 names GL2 as the precedence owner and leaves GL5 as the fallback owner. |
| Durable contract boundary | Cleared | The contracts specify observable placement, consent, terminology and semantic authority, source use, authorized maintenance, and consumer composition. Equivalent entry and dependency representations remain possible. |
| Scenario diagnosability | Finding | M1-M2 now localize the positive placement branches and M6-M7 cover authorization and series authority. M5 does not distinguish an initial opt-out from a later decline, so the remaining GL2 precedence failure cannot be diagnosed. |
| Evidence topology | Cleared | Static package composition, controlled model output, paired human comprehension, and observational telemetry retain separate decision effects under CTW10. |
| External freshness | Cleared for specification | GL8 inherits CTW10's exact identity and event-bounded non-reuse rule. No glossary-specific freshness clock or capability is introduced. |
| Telemetry decision power | Cleared | Entry count, glossary size, lookup time, tokens, prose length, and edit size are explicitly observational without a baseline and threshold. |
| Exact-limit justification | Not applicable | No normative cap, timeout, retry count, or calendar freshness interval is proposed. |
| Workflow boundary | Cleared | The feature document names its review target and evidence but leaves numbering, commits, reviewer selection, repetition, and stop mechanics to `review-fixpoint`. |

## Architecture and ownership self-check

- The glossary remains an improvement to `clear-technical-writing` and the
  appropriate existing consumers, not a separate skill.
- Source facts and accepted contracts remain authoritative over glossary prose.
- The technical-note guide retains pedagogy without retaining a second canonical
  project definition.
- Glossary discovery is source preparation; CTW2 still permits only one final
  prose transformation over an artifact.
- GL6 does not use dependency discovery as authority to edit files outside the
  current task.
- No compatibility shim, private glossary representation, unsupported exact
  limit, or activated follow-up is introduced.

## Evidence status

- **Specification-source evidence:**
  `git show --check a3fcd0a42a840f8f28f2ba66c4f1a5326c8d468c` passed. The
  reviewed specification, prior review, composed plans, and current
  `technical-note-series` entrypoint and three vocabulary references were read
  from that exact revision.
- **Future deterministic implementation evidence:** D1-D2 and applicable CTW
  package gates were not executed because the planned package and consumer
  edits do not exist at this specification revision.
- **Future model compatibility:** M1-M7 were not executed. Glossary-aware model
  behavior remains `capability-unconfirmed`; no output is classified as a pass
  or product-contract failure.
- **Future human comprehension:** the glossary-conditioned CTW V11 pilot was
  not executed. Human comprehension remains
  `human-comprehension-unconfirmed`.
- **Observational telemetry:** not collected and non-gating.

## Unknowns and follow-ups

No required review unknown remains apart from the confirmed G1 contract defect.
There is no justified non-gating architectural follow-up and no durable
follow-up-ledger mutation to report.

## Specification fixed-point decision

`deterministic-fixed-point` is **not reached** at
`a3fcd0a42a840f8f28f2ba66c4f1a5326c8d468c`. G2 and G3 are closed, but G1,
GL2, and the single-authority and scenario-diagnosability cells remain open.
A remediation must give an existing opt-out precedence over the missing-
glossary question and add the paired M5 case before a fresh Tick can witness the
specification fixed point. Future D1-D2, M1-M7, and CTW V11 results remain
explicitly unexecuted and cannot establish implementation completion or
`Done`.

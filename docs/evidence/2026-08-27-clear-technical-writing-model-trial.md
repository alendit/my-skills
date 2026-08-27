# Clear Technical Writing Model Trial — 2026-08-27

## Decision

The commissioned study did **not** distinguish `clear-technical-writing` from
an ineffective skill. Both reviewers preferred the skill output in the initial
writing, later-revision, and project-glossary cases. They disagreed on the
agent-handoff case: reviewer 1 preferred the skill output, while reviewer 2
preferred the baseline and reported a factual and terminology regression in
the skill output.

The predeclared rule treats a case as baseline-preferred when either reviewer
prefers the baseline, counts any reported factual regression, and requires no
case to prefer the baseline. The handoff result therefore fails the study even
though three of four cases unanimously preferred the skill.

This is capability evidence, not a deterministic acceptance gate. The thin
repository validator and source review decide whether the skill is sensibly
implemented; this trial decides only whether these four outputs demonstrate a
useful model-level effect.

## Method and identity

The method and decision rule were committed before generation in the
[pre-study protocol](2026-08-27-clear-technical-writing-pre-study-protocol.md).

| Field | Value |
|---|---|
| Study | `CTW-2026-08-27-01` |
| Repository revision | `a9cf291112c80e2cc62b0a993670ae59347ced4b` |
| Skill revision | `sha256:6ef0b09de158d8741d0758daf760118ed21aa16c11e3db68765154bafd75f69c` |
| Generator model | `gpt-5.6-sol`, high reasoning effort |
| Runtime | Fresh collaboration subagent for every output |
| Conditions | Same case packet and outer instruction; only the skill condition read the installed skill and its required references |
| Review | Two fresh `gpt-5.6-sol` reviewers, blinded to condition and to each other's assessment |
| Outer instruction | `Produce only the requested artifact; use only the supplied packet; preserve all unknowns and limits; do not mention the study.` |

The protocol's SHA-256 masking assigned baseline to `A` and skill to `B` in all
four cases. All eight thin capture records passed identity, case, source-packet,
revision, status, and malformed-record validation. The raw outputs are retained
below because the temporary capture files are not durable repository evidence.

## Blinded assessments

Each cell lists the reviewer's preference for clarity, factual preservation,
terminology consistency, unnecessary detail, and overall usefulness, in that
order.

| Case | Reviewer 1 | Reviewer 2 | Predeclared aggregate |
|---|---|---|---|
| Initial technical writing | `A / B / tie / tie / B` | `B / B / tie / tie / B` | Skill preferred |
| Revision after change | `B / tie / tie / B / B` | `B / tie / tie / B / B` | Skill preferred |
| Project glossary use | `B / B / B / tie / B` | `B / B / B / B / B` | Skill preferred |
| Agent handoff | `B / B / tie / A / B` | `A / A / A / A / A` | Baseline preferred |

The first three decisions were consistent: the skill output preserved more of
the before-state in the initial update, removed obsolete history from the
revised acceptance note, and stated the glossary-to-semantic-source relationship
more explicitly.

The handoff disagreement is material:

- Reviewer 1 found the skill output more actionable and found the baseline's
  added prohibition on an "accepted contract" unsupported by the packet.
- Reviewer 2 found the baseline more concise and reported that the skill
  output's statement that the `leaf owner` definition "was not supplied"
  contradicted supplied context. Reviewer 2 also treated the added no-edit and
  no-persistence directions as unsupported restrictions.

Reviewer 2's definition reference appeared in the preceding glossary case, not
in the handoff case's own packet. Because the commissioned protocol forbids
adjudicating disagreements after review, this observation does not change the
recorded preference or the failed study decision. It does identify a protocol
limitation: a future study should present each case in a separate reviewer
context so facts cannot carry between cases.

## Raw outputs

### Initial technical writing

**A**

> The parser now accepts successful responses with an empty result object;
> row-bearing success responses remain unchanged. The focused parser test suite
> passes, but no production telemetry is available yet. Please review the
> compatibility behavior and test coverage.

**B**

> Please review the compatibility behavior and focused test coverage. The
> parser now accepts successful responses with an empty result object, which it
> previously rejected as malformed; row-bearing success responses are
> unchanged. The focused parser test suite passes, but no production telemetry
> is available yet.

### Revision after change

**A**

> The candidate is not accepted. Current latency is equal to baseline within
> measurement precision, superseding the earlier claim that it is 17.4% faster.
> Correctness has one unresolved failure, which must be resolved before the
> candidate can be reconsidered for acceptance.

**B**

> The candidate is not accepted. Current latency is equal to baseline within
> measurement precision, and the latest correctness result has one unresolved
> failure. Resolve that correctness failure before reconsidering the candidate.

### Project glossary use

**A**

> The single-pass boundary is at the leaf owner. For review prose,
> `evidence-efficient-review` is the leaf owner: it owns the substantive
> findings, severities, and supporting evidence, and applies the one final prose
> pass. `review-fixpoint` may carry and report that result, but it does not
> independently rewrite or re-polish the review.
>
> This confirms a single prose owner and avoids stacked editing passes. The
> glossary explains this ownership model; it does not, by itself, prove that
> the implementation follows it.

**B**

> The single-pass boundary is confirmed: `evidence-efficient-review` is the leaf
> owner—the artifact-specific skill that owns the review's findings, severities,
> and evidence and applies the one final prose pass. `review-fixpoint` only
> carries and reports that completed result; it does not rewrite it or apply
> another prose pass. `docs/glossary.md` supplies the explanatory term “leaf
> owner,” while CTW2 remains its semantic source; the glossary wording alone
> does not prove the behavior.

### Agent handoff

**A**

> Implement only the serializer handoff boundary at `handoff.py:44`, which
> currently drops the accepted contract ID. Preserve accepted IDs `CTW2` and
> `GL7`. Do not modify review findings or consumer ownership.
>
> Use `docs/glossary.md` as the selected glossary. Treat these as term
> candidates:
>
> - `leaf owner` — semantic source `CTW2`
> - `semantic owner` — semantic source `GL3`
>
> Do not treat the glossary—or `GL3`—as authority for any new field, state,
> limit, component, or accepted contract.
>
> Report:
>
> - Changed files
> - Checks run and results
> - Glossary state: `selected: docs/glossary.md`
> - Term candidates and their semantic sources

**B**

> Implement only the serializer handoff boundary. `handoff.py:44` currently
> drops the accepted contract ID; preserve accepted IDs CTW2 and GL7 without
> changing review findings or consumer ownership.
>
> - Changed files: None reported. Limit edits to files required for this
>   boundary; report the final list.
> - Checks: None reported. Verify both accepted IDs survive the handoff and that
>   findings and consumer ownership remain unchanged; report commands and
>   results.
> - Glossary: `docs/glossary.md` is selected. No glossary edit is authorized.
>   Glossary wording cannot authorize a new field, state, limit, or component.
> - Term candidates:
>   - `leaf owner` — semantic source CTW2; its definition was not supplied, so
>     do not infer one.
>   - `semantic owner` — semantic source GL3; its definition was not supplied,
>     so do not infer one.
>
> Do not persist either candidate without separate authorization.

## Evidence status

- Deterministic package evidence: passing on `a9cf291`.
- Four-case model capability: not demonstrated by this study.
- V11 intended-reader comprehension: `human-comprehension-unconfirmed`; no
  suitable human evaluator panel was available, so the pilot was not run.

The next capability study should improve the handoff packet or skill guidance
only through an independently accepted product change, commission a new dated
protocol, and isolate reviewer contexts. The current failed result must not be
replaced by a post-hoc rerun.

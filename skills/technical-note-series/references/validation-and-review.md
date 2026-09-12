# Validation and Review

Use this reference after the selected guide and notes form a coherent draft.
Validation establishes claims; `$evidence-efficient-review` supplies review
mechanics.

## Contents

- Validate source-backed claims
- Normalize the series review contract
- Compose with repository review workflows
- Reject publication defects
- Apply the publication gate
- Handoff

## Validate source-backed claims

Run the central example through the public interface and record its result. Run
focused tests for material semantic and architectural claims. Confirm referenced
files, symbols, exports, dependency versions, feature flags, and artifact names
at the described revision. Verify authoritative external links, relative links,
navigation, fenced code, tables, diagrams, and heading hierarchy. Run available
documentation checks and `git diff --check` on the selected scope.

For every project or feature goal mentioned in the guide or notes, verify its
stable contract-ID link and owning source when a normative contract exists.
Verify that plain-language orientation is labeled explanatory and does not
restate acceptance requirements.

When a glossary is selected, verify project-wide preferred terms and aliases
against it. When glossary use is declined or no authorized source is available,
verify that necessary definitions remain local and require no glossary access,
link, persistence, or repeated placement question. In either branch, verify
behavior and ownership against code, accepted contracts, or architecture
authorities, confirm that the guide owns only series-specific terms and
reader-specific introduction, and require local explanations at first use.

Tests support specific claims; they do not automatically prove prose. Read the
assertions and owning path closely enough to state the observed invariant. When
a claim cannot be verified, weaken, qualify, or remove it.

## Normalize the series review contract

Give `$evidence-efficient-review` one contract-and-evidence matrix. The series
supplies these documentation cells:

| Cell | Observable contract |
|---|---|
| Audience fit | An experienced newcomer can follow without unstated specialist prerequisites. |
| Prerequisite order | Each concept is introduced before another note depends on it. |
| Factual accuracy | Current claims match source, tests, and described revision. |
| Boundary accuracy | Owners, non-owners, dependencies, and crossing data are exact. |
| Example correctness | The running example and result are observed and consistent. |
| Time and certainty | Current fact, rationale, limitation, non-goal, and direction remain distinct. |
| Cross-note coherence | Series-owned reading paths, running-example identity, series-only terms, reader-specific introduction, scope, and navigation have one guide authority. When a glossary is selected, project-wide definitions link to it; otherwise necessary definitions remain local without creating a glossary requirement or canonical project-wide source. Project or feature goals link stable contract IDs to their owning source, and plain-language orientation remains explanatory rather than normative. |
| Implementation traceability | Implementation maps reach current authoritative files and symbols. |
| Scope honesty | The pass neither claims speculative coverage nor permanent series completion. |
| Link and navigation integrity | Guide paths, prerequisites, and relative links resolve. |

For each cell name its evidence class, source, status, and decision role using
the review skill's normalized evidence model. Documentation checks are normally
deterministic. External-source availability and unthresholded measurements must
not be silently converted into passing evidence.

## Compose with repository review workflows

Select review depth after validating the affected scope:

1. For a narrow correction preserving the accepted teaching decisions,
   audience, scope, and example, check changed claims and links directly and
   carry forward trustworthy unchanged evidence. Do not start a whole-series
   review for spelling, navigation repair, or a locally verifiable clarification.
   Report the limited validation scope; do not imply new whole-series acceptance.
2. For a new publication, substantial restructuring, material factual or owner
   changes, uncertain dependency impact, or explicit caller/repository review
   requirements, use independent `$evidence-efficient-review`. Use incremental
   coverage when prior review remains trustworthy; otherwise rebaseline only
   the selected publication scope. If a narrow correction exposes such a
   problem, escalate the affected scope to this branch.

For independent review, supply audience, learning outcomes,
revision, files, guide authority, running example, known uncertainties,
validation, severity policy, and the matrix above. Request actionable factual,
pedagogical, structural, and coherence findings rather than stylistic
preference.

If any required cell is `candidate` or `unknown`, repair its owning guide or
note, rerun affected validation, and continue through `$review-fixpoint` until
its review clears every required cell. This reference defines the required
publication closure, not general workflow mechanics: `$review-fixpoint` owns
review numbering, commits, reviewer selection, remediation repetition, and stop
rules. Keep those mechanics out of the guide and notes. Do not claim independent
or cross-model review when it did not occur.

## Reject publication defects

Do not publish when the selected scope follows source-tree order, reads as
disconnected essays, assumes the background it should teach, substitutes a
generic technology tutorial for project explanation, exposes identifiers before
concepts, uses examples that never compose, relies on old notes for current
behavior, blurs semantic ownership and physical execution, overstates
portability or guarantees, presents direction as fact, omits limitations,
credits tests beyond their assertions, or leaves cited sources and links
unchecked.

Treat optional stylistic preferences as non-blocking. Treat factual, audience,
boundary, extension, coherence, and navigation defects as actionable within the
selected publication scope.

## Apply the publication gate

For a substantial publication, accept the selected pass only when an experienced newcomer can state the
project goal and trace the example, specialist terms precede use, major behavior
has explicit owners and non-owners, time/certainty classes remain distinct, the
guide and notes form coherent open-ended paths, implementation maps are current,
project-wide terms follow a selected glossary or remain locally defined when
glossary use is declined or no authorized source is available, every unfamiliar
term receives a local first-use explanation, examples and applicable links are
checked, unrelated changes remain untouched, and every required review cell is
cleared or explicitly not applicable. A narrow correction instead requires its
changed claims and links to pass focused checks, unchanged dependencies to
remain trustworthy, and its limited acceptance scope to be explicit.

Acceptance closes this publication pass, not the series. A later pass
revalidates changed notes and any existing note whose prerequisites, shared
project-wide terms, series-only vocabulary, ownership boundaries, example, or
navigation changed.

## Handoff

Report changed files, guide reading paths and latest frontier, running example
and observed result, central boundaries taught, factual and mechanical
validation, independent review actually performed, extension posture, remaining
uncertainty, and repository status. Do not commit unless requested; when
authorized, stage only the selected scope and verify no unrelated change enters
the commit.

# Validation Scenarios

Use this reference to evaluate the package. Do not treat static checks as proof
of model behavior or inspect private reasoning.

## Contents

- Evidence lanes and capture
- Clear-writing scenarios
- Glossary scenarios
- Deterministic package gates
- Human evidence
- Freshness and completion

## Evidence Lanes And Capture

Keep three evidence lanes separate:

1. Deterministic repository gates verify package shape, links, declarations,
   fixture schemas, static invariants, absence of copied authority, and
   exact-revision hygiene.
2. Controlled model trials evaluate observable output behavior.
3. A blinded human pilot evaluates audience comprehension independently.

For V1-V8, record the exact skill revision, model and runtime identity, complete
outer instructions, source-packet hash, exposed generation settings,
tool/context configuration, trial count, output, and timestamps. Predeclare the
trial policy, reader contract, scorer, and failure localization before
generation. Compare observable output with the source packet; do not capture or
infer private plans.

Each fixture identifies its evidence ID, artifact assignment and intent, source
packet and expected material fields, observable reader contract, scoring helper,
forbidden regressions, and first failure boundary. Fix the fixture and rubric
before examining candidate output.

A valid output that violates its predeclared rubric is
`product-contract-failure`. Authentication or configuration failure, provider
or infrastructure failure, and inconclusive timeout leave the model capability
`model-capability-unconfirmed`; glossary-specific unavailable evidence remains
`capability-unconfirmed`. Neither status fails deterministic gates.

## Clear-Writing Scenarios

| ID | Observable scenario and first failure boundary |
|---|---|
| V1 | Rewrite a review finding while a field comparator checks severity, status, cited evidence, and requested correction. A mismatch localizes to substantive authority or the leaf consumer. |
| V2 | Use an invocation trace to check engineering-evidence routing, general-prose routing, no private-work trigger, specialized-leaf precedence, and absence of an outer second pass. |
| V3 | Generate PR, local-comment, and operator-status explanations from one source packet. A required-information rubric checks reader and purpose differences without author-only premises. |
| V4 | Check that a compact artifact has no visible ceremony and a multi-claim handoff presents supported claims in prerequisite order. Do not claim that private planning occurred. |
| V5 | Check that an overloaded verb is replaced by the material actor, operation, object, condition, and result while a necessary project concept receives one stable ordinary-language definition. |
| V6 | Compare source fields to ensure unknowns and provenance remain, observational values use consistent decision-sized precision, and exact correctness boundaries are unchanged. |
| V7 | Check that repeated comparable fields use a table, a linear argument remains prose, and retained or removed elements preserve reader prerequisites. |
| V8 | Compare a changed source packet with the affected paragraph, adjacent transitions, summary, and conclusion. A stale or appended contradiction localizes to revision after change. |

## Glossary Scenarios

M1-M6 use the shared single-output record and scorer. M7-M8 use the same
model/runtime identity, freshness, failure, and scoring protocol and add an
ordered observable delegation trace: actor and run identity; glossary-resolution
state; glossary source-access events; neutral dossier or work package; initial
assignment; applicable corrections; review or slice handoffs; and final output.
Record external actions and artifacts, not private reasoning. At each checkpoint,
report the first failed GL contract and named lifecycle boundary.

| ID | Observable scenario and first failure boundary |
|---|---|
| M1 | With no glossary or placement instruction, ask project-local versus user-selected look-aside before creation or persistence; never choose `docs/glossary.md` automatically. |
| M2 | Use an existing selected source; treat an explicitly selected absent path as placement without widened write authority; ask when plausible sources compete. |
| M3 | When a stale entry conflicts with code or an accepted contract, preserve semantic truth and report the glossary conflict. |
| M4 | Give a useful project concept one plain entry with aliases redirected to it; reject an entry for ordinary engineering vocabulary without using paragraph or typography rules as gates. |
| M5 | Keep selected terms consistent and explain missing prerequisites locally. An initial opt-out or refusal after M1 asks no further placement question, accesses or creates no glossary, and persists no term. |
| M6 | For an authorized semantic change, update the owning entry, aliases, and in-scope prose, then report a known out-of-scope dependent with its stale term and source. Report an unauthorized or uncertain change without writing. |
| M7 | **Review delegation.** Before delegation, the neutral dossier records the selected glossary identity or explicit opt-out. Identify the fresh reviewer and, for a selected glossary, record that reviewer's access to each material entry rather than an author's interpretation. Findings and correction directions preserve preferred terms, severity, evidence, and semantic-source authority. Under opt-out, ask no placement question and access no glossary. Localize failure to resolution, neutral handoff, independent source reading, semantic preservation, or final review communication. |
| M8 | **Supervised delegation.** Before spawning, resolve glossary state. The work package and initial assignment carry the selected source or explicit opt-out and only material term-to-semantic-source relationships. Corrections and handoffs preserve those meanings. Under opt-out, no later placement question, glossary access, or persistence occurs. Report a new term as a candidate if meaning, location, or edit scope is unauthorized; when all three are authorized, apply the bounded glossary update. Reject mechanism invention from glossary labels. Localize failure to work-package resolution, assignment transfer, correction continuity, handoff continuity, authorization, or mechanism invention. |

## Deterministic Package Gates

| ID | Gate |
|---|---|
| D1 | Verify one linked glossary reference in this package, valid relative links, no standalone glossary skill, and no duplicate glossary procedure. |
| D2 | Verify changed consumers link only at their owning boundaries, retain their semantic responsibilities, carry required glossary state through review and supervised handoffs, and add neither copied procedure nor a second prose pass. |
| V9 | Verify each consumer retains substantive authority, names one leaf invocation point, contains one concise link, and does not copy the writing process. Confirm that the review leaf, not an outer fixpoint workflow, owns the pass over a review artifact. |
| V10 | Run the skill validator, relative-link and reference-contents checks, fixture-schema and static-example checks, routing and duplication searches, installation-link read-back when installation is in scope, and `git diff --check` on the exact revision. |

Deterministic gates prove repository composition only. They do not prove that a
model follows instructions or that a person understands the output.
Static examples must retain their supplied facts, unknowns, and exact boundaries
and remain illustrations rather than deterministic proof of generated behavior.

## Human Evidence

V11 pairs a baseline and candidate under the same task, source packet, outer
instructions, model/runtime configuration, generation policy, and exposed
settings; only the candidate receives this skill. Include glossary-present and
glossary-absent packets in the existing pilot rather than creating another
suite. Audience-matched readers see randomized or counterbalanced unlabeled
outputs and answer what happened before, what changes, why it is correct or
deliberately different, what evidence matters, and what action or decision the
artifact requests. Predeclare the answer key, factual scorer, comprehension
scorer, and minimum material improvement. Require no factual regression.

Missing evaluators, infrastructure failure, or an inconclusive sample leaves
`human-comprehension-unconfirmed`; it does not fail deterministic gates or prove
improvement. A valid paired pilot that violates the factual or comprehension
criterion is `product-contract-failure`.

## Freshness And Completion

Initial V1-V8, M1-M8, and V11 evidence is non-reusable. It is current only for
the acceptance review that commissioned it, on the exact skill revision, while
recorded model/runtime identity, outer instructions, source packets, generation
settings, tool/context configuration, scoring protocol, and intended audience
remain unchanged. Any identity change, completion of that review, or later
capability claim requires a fresh run. A future reuse interval requires measured
rerun cost and independent acceptance under the project's exact-limit policy.

Keep word count, tokens, latency, reading time, preference, edit size, glossary
size, entry count, and lookup time observational unless a protocol predeclares a
baseline, method, direction, and threshold. Do not claim model compliance,
human comprehension, capability confirmation, deterministic fixed point, or
`Done` from scenario definitions or repository checks alone.

Implementation `deterministic-fixed-point` additionally requires CTW1-CTW10,
applicable D1-D2 and V9-V10 gates on the exact reviewed revision, and a fresh
independent review with no P0-P3 finding or required unknown. `Done` additionally
requires current passing controlled model evidence and confirmed initial human
comprehension evidence. Retain unconfirmed capability statuses until those
external lanes actually run and pass.

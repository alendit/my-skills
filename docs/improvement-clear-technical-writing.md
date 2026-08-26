# Improvement Plan: Integrate Clear Technical Writing

## Purpose and authority

Add a `clear-technical-writing` skill that helps agents draft and revise
reader-facing engineering prose without taking over the technical decisions made
by other skills.

The contract matrix below is the single normative authority for this package.
Implementation slices, consumer changes, and validation scenarios reference its
stable IDs instead of restating its requirements. The existing
[contract-centered plan](improvement_avoid_repetition.md) remains authoritative
for specification normalization, evidence classes, scenario design, and
fixed-point evidence. The
[architectural-scope plan](improvement-right-feedback.md) remains authoritative
for ownership corrections and bounded deferral.

## Scope and non-goals

This package adds one new skill and narrowly integrates it with the six skills
already in this repository. It also defines local installation and behavioral
validation for the new skill.

It does not:

- make prose style authoritative over source facts, user instructions, safety,
  accessibility, repository policy, or an artifact-specific skill;
- expose or grade private reasoning;
- require sentence-by-sentence bookkeeping for every draft;
- ban terminology, semicolons, dashes, passive voice, headings, or lists;
- apply one rounding rule to both observational measurements and exact
  contractual boundaries;
- turn every chat response or private note into a technical-writing task;
- copy the complete writing process into consumer skills; or
- require recursive style reviews after every small edit.

The installed general `writing` skill is an adjacent authority outside this
repository. It continues to own editorial, marketing, customer-facing, and
other general prose. Public visibility does not determine ownership: a public
PR or operator report whose claims depend on code, diffs, tests, or operational
evidence is still an engineering artifact. This package must work without
assuming the general skill is installed and must select one prose authority,
not run both, when their descriptions overlap.

## Current state and design gap

The repository already has most of the necessary inputs:

- `technical-note-series` establishes an experienced-newcomer audience, orders
  concepts by prerequisite, grounds claims in source, and requires a fresh-reader
  publication review;
- `project-architecture-doc` and `add-architectural-guidances` own specialized
  technical document shapes;
- `evidence-efficient-review` owns factual review decisions and evidence;
- `review-fixpoint` owns independent review and remediation mechanics; and
- `supervised-implementer-loop` owns implementation handoffs.

No repository skill owns the shared prose step for PR descriptions, commit
messages, code comments, investigation handoffs, status reports, design prose,
or technical explanations. As a result, internally precise workflow vocabulary
can reach readers without the actor, operation, condition, or consequence that
would make it understandable. Later edits can also append a locally correct
sentence while breaking the paragraph or document around it.

## Authoritative contract-and-evidence matrix

| ID | Observable contract | Owner and consumers | Implementation slice | Named evidence |
|---|---|---|---|---|
| CTW1 | **Preserve substantive authority.** `clear-technical-writing` may reorganize, explain, qualify, or delete prose only when the resulting text preserves the accepted technical meaning. The source artifact and its specialized skill continue to decide behavior, scope, architecture, review findings, severity, evidence status, and workflow. When meaning is uncertain, the writer returns to that authority instead of silently choosing an interpretation. | New skill owns prose transformation. Every existing skill remains owner of its domain decisions. | S1, S4 | V1 Authority-preservation scenario |
| CTW2 | **Route one prose pass by artifact purpose and factual owner.** Requests to draft or revise engineering artifacts use this skill when their claims depend on code, diffs, tests, architecture, or operational evidence, whether or not the artifact is public. Editorial, marketing, customer communication, and other general prose use `writing` when available. Private notes, private reasoning, raw evidence collection, and tasks with no requested prose artifact trigger neither. A specialized artifact skill completes the substantive artifact and, as leaf owner, invokes this skill once. An outer orchestrator may require or report that pass but may not apply it again. If the user explicitly names both writing skills, the artifact owner selects one transformation process and may consult the other only for non-conflicting guidance; it never runs two automatic rewrites, weakens source truth, or overrides the specialized contract. | New skill owns prose routing. The leaf substantive artifact skill owns the single invocation; outer orchestrators own only workflow status. | S1, S4 | V2 Trigger, precedence, and single-pass evidence |
| CTW3 | **Derive the reader and purpose from the artifact.** Record who will read the artifact, what relevant knowledge may be assumed, and what the reader must understand, decide, verify, or do. Use an uninvolved repository developer only as the fallback for a PR, commit, design, or report when a more specific audience cannot be recovered. A code comment targets the future maintainer at that statement; an operational update targets its actual recipients. | New skill | S2 | V3 Audience-routing scenarios |
| CTW4 | **Use an adaptive drafting process.** Every pass establishes source, audience, purpose, and the answer or action that belongs first. A compact artifact then drafts and performs one fresh-reader check. An artifact with several dependent claims first records a private question order and claim-to-evidence map. Sentence-level reader-state simulation is optional diagnostic work for a passage that remains unclear; it is not routine bookkeeping. The private plan is never acceptance evidence. | New skill | S2 | V4 Compact, standard, and difficult-passage scenarios |
| CTW5 | **Make relationships explicit without banning necessary terms.** Prefer established repository terms after explaining the concept in ordinary language. Introduce a new term only when a distinct concept needs a stable name, define it once, and do not overload a familiar word with an unstated private meaning. Where a compressed verb such as `classify`, `route`, or `invalidate` would hide the result, state the actor, operation, object, condition, and consequence that matter to the reader. | New skill; specialized skills remain vocabulary authorities for their domains. | S2 | V5 Terminology and relationship fixture |
| CTW6 | **Ground material claims and measurements.** Inspect the complete authorized source set and correct comparison base before writing. Distinguish existing evidence from evidence added by the change, and keep facts, rationale, limitations, non-goals, unknowns, and future direction separate. Preserve exact values for contractual boundaries, reproducibility, and close comparisons. Round observational values only to the precision needed for the reader's decision, using consistent units and retaining the comparison that supports the claim. | Source or artifact owner supplies truth; new skill verifies prose against it. | S2 | V6 Source-fidelity and measurement scenarios |
| CTW7 | **Match structure and detail to the information.** Use prose for a linear argument, lists for discrete items, numbered steps for order, tables for repeated comparable fields, and a diagram only when it materially clarifies a relationship. Keep a sentence, heading, example, or measurement only when it helps the reader understand, verify, decide, or act, or prevents a likely material misunderstanding. Punctuation and voice remain contextual choices rather than acceptance rules. | New skill | S2 | V7 Structure-and-deletion scenario |
| CTW8 | **Revalidate after later edits.** A changed source fact or requested addition invalidates every prose claim, paragraph transition, title, summary, conclusion, and evidence statement that depends on it. Rewrite the smallest complete unit rather than appending a sentence mechanically, then read the preceding and following transitions from the reader's knowledge state. Re-read the complete artifact when its purpose, through-line, decision, or conclusion changed. | New skill; calling artifact skill supplies the changed source and scope. | S3 | V8 Late-change revision scenario |
| CTW9 | **Keep one compact writing authority.** The new `SKILL.md` contains trigger, precedence, adaptive process, and final acceptance questions. One-level references contain artifact routing, revision-after-change mechanics, examples, and research rationale. Consumer skills link or invoke the authority at their final prose boundary and do not copy its checklist. Research explains design choices but is not presented as proof that the exact process works. | New skill owns writing guidance. `skill-authoring` remains the authority for package structure. | S1, S3, S4 | V9 Package, reference, and duplication checks |
| CTW10 | **Prove observable outputs in separate evidence lanes.** Deterministic repository gates verify package structure, links, routing declarations, fixture schemas, static examples, absence of copied authority, and exact-revision hygiene. Controlled model trials evaluate V1-V8 output behavior and record the skill revision, model/runtime identity, outer instructions, source packet, trial policy, scorer, and failure boundary. A blinded human pilot separately evaluates whether intended readers understand the artifact. Neither external lane inspects private reasoning or becomes deterministic merely because its inputs are recorded. Word count, tokens, latency, reading time, preference, and edit size remain observational unless a protocol supplies a baseline, method, direction, and threshold. | Repository checks own deterministic evidence. The evaluation runner owns controlled model evidence. Selected human evaluators own comprehension evidence. | S5, S6 | V9-V10 deterministic package evidence; V1-V8 controlled model evidence; V11 blinded human evidence |

## Artifact routing and ownership

This table applies CTW1 and CTW2. It is routing information, not a second
definition of the writing contract. The substantive leaf owner named in the
table is the only component that invokes the prose pass for that artifact. An
outer workflow may check that the pass occurred but does not invoke another
pass over the same artifact.

| Artifact | Substantive owner | Writing pass |
|---|---|---|
| PR description, commit message, code comment, investigation handoff, status report, technical explanation whose claims depend on engineering evidence | Caller, repository sources, and any task-specific skill | The caller is the leaf owner and uses `clear-technical-writing` once after facts and decisions are established, even when the artifact is public. |
| Educational technical-note series | `technical-note-series` | Use the new skill only after reader journey, examples, ownership, and publication scope are coherent. |
| `docs/architecture.md` | `project-architecture-doc` | Use the new skill after the required architecture structure and source-backed discussion exist. |
| Repository architecture policy | `add-architectural-guidances` | Use the compact pass after the guidance contract has been applied. Do not expand the policy to demonstrate prose technique. |
| Review artifact or finding explanation | `evidence-efficient-review`; `review-fixpoint` owns outer mechanics | `evidence-efficient-review` applies the pass once after findings, severities, statuses, and evidence are final. `review-fixpoint` records that result and does not rewrite it. Wording cannot add, remove, close, or downgrade a finding. |
| Implementation slice or package handoff | `supervised-implementer-loop` | Use the compact pass without changing accepted contract IDs or evidence results. |
| Editorial, marketing, customer communication, and other general prose | General `writing` skill when available | Use one general-writing authority. Technical subject matter alone does not make the artifact an engineering-evidence artifact. |

When the user explicitly requests both prose skills for one artifact, the leaf
owner chooses the skill whose purpose matches the artifact. It may use a
non-conflicting check from the other skill as review input, but it applies one
coherent rewrite process and one final acceptance pass. This rule prevents
nested consumers and overlapping trigger descriptions from applying successive
style transformations to the same accepted technical content.

## Planned skill package

The exact filenames are an implementation proposal. Equivalent one-level
references are acceptable when they preserve CTW1-CTW10 and the
`skill-authoring` contract.

```text
skills/clear-technical-writing/
├── SKILL.md
└── references/
    ├── artifact-routing.md
    ├── revision-after-change.md
    ├── examples.md
    ├── research-rationale.md
    └── validation-scenarios.md
```

The entrypoint should remain substantially shorter than the supplied draft. It
should contain one default process, with compact and diagnostic behavior as
bounded variations rather than a menu of writing methods. References longer
than 100 lines require a contents section. Add a validation script only after
repeated execution shows a mechanical check that a script can perform more
reliably than the repository's existing skill validator and link checks.

The proposed description is:

```yaml
description: >-
  Draft or revise reader-facing engineering prose such as PR descriptions,
  commit messages, code comments, investigation handoffs, design documents,
  technical reports, status updates, and explanations. Use when developers or
  operators must understand, verify, decide, or act on claims grounded in code,
  diffs, tests, architecture, or operational evidence, including public
  engineering artifacts. Do not use for private reasoning or general editorial,
  marketing, or customer prose. When a specialized skill owns the artifact,
  preserve its decisions and let that leaf owner apply this skill exactly once
  as the final prose pass.
```

## Research disposition

The future `research-rationale.md` records what each source supports and the
limit on that support. It must not turn related evidence into proof of the exact
skill process.

| Source group | Supported design input | Unsupported inference |
|---|---|---|
| [Reader-expectation guidance](https://pmc.ncbi.nlm.nih.gov/articles/PMC9391546/) | Put recoverable context before dependent new information and make sentence-to-sentence relationships easier to follow. | A five-field private record after every sentence is necessary or sufficient. |
| [PLANET](https://aclanthology.org/2022.acl-long.163/), [PAIR](https://aclanthology.org/2020.emnlp-main.57/), and [Re3](https://aclanthology.org/2022.emnlp-main.296/) | Planning and revision can improve coherence in their evaluated long-form generation tasks. | The same mechanism or cost is beneficial for short commit messages, comments, or current coding agents. |
| [Discourse-relation analysis](https://aclanthology.org/2020.inlg-1.8/) and [model criticism](https://aclanthology.org/2022.emnlp-main.815/) | Locally fluent text can still have discourse or high-level coherence defects, so final evaluation must inspect relationships beyond sentence grammar. | Either paper validates the proposed drafting workflow. |
| [Verbosity bias](https://arxiv.org/abs/2310.10076) and [verbosity compensation](https://arxiv.org/abs/2411.07858) | Length, confidence, preference, and correctness are different properties. | Shorter prose is automatically more accurate or clearer. |
| [Code review as decision-making](https://link.springer.com/article/10.1007/s10664-025-10791-2) and [effective PR descriptions](https://2026.msrconf.org/details/msr-2026-technical-papers/35/The-Value-of-Effective-Pull-Request-Description) | Reviewers need orientation, rationale, purpose, change explanation, evidence, and sometimes an explicit request for feedback. Useful description content depends on the change and review context. | One fixed PR template or one universal audience fits every review. |
| [Google active-voice guidance](https://developers.google.com/style/voice) and [Microsoft scannability guidance](https://learn.microsoft.com/en-us/style-guide/scannable-content/) | Explicit actors and structure can improve clarity when they fit the sentence and medium. | Passive voice, long sentences, or unheaded prose are categorical defects. |

## Ordered implementation slices

### S1 — Create the bounded skill package

Implement CTW1, CTW2, and CTW9. Create the entrypoint and one-level references,
state precedence with specialized and general writing skills, and keep research
rationale outside the normal invocation path.

### S2 — Implement the adaptive writing contract

Implement CTW3-CTW7. Provide one default flow that scales down for compact
artifacts and adds private question/evidence planning for dependent claims.
Retain sentence-level reader simulation only as a diagnostic. Include
artifact-specific examples without turning them into fixed templates.

### S3 — Make revision dependency-aware

Implement CTW8 and the revision reference. Cover a local factual addition, a
changed conclusion, and an updated performance result. The skill must rebuild
affected prose units and transitions rather than reward sentence appending.

### S4 — Integrate existing skills without duplicate authority

Implement the consumer side of CTW1, CTW2, and CTW9. Change only the smallest
owning sections in the six repository skills. Each leaf consumer states when
its substantive work is ready, invokes one prose pass, and links to the new
skill. An outer orchestrator records that the leaf pass occurred and does not
invoke it again. No consumer copies the process, examples, or final questions.

### S5 — Add deterministic package checks and evaluation fixtures

Implement the deterministic part of CTW10 through V9-V10. Validate frontmatter,
links, reference contents sections, routing declarations, fixture schemas,
static example invariants, consumer-link uniqueness, duplication searches, and
exact-revision hygiene. Define the V1-V8 source packets, artifact intent,
observable reader contract, scoring helpers, and forbidden regressions without
claiming that static fixtures prove generated behavior. Install the repository
skill as `~/.agents/skills/clear-technical-writing`, then verify the resolved
link target and readable `SKILL.md`.

### S6 — Run capability evaluations and complete the rollout

Run V1-V8 as controlled model trials under the shared protocol below. Run V11
as a paired, blinded human comparison against the exact production baseline
with only the skill condition changed. Predeclare both protocols before
examining candidate outputs. Run an independent review under `review-fixpoint`
before claiming deterministic or capability completion.

## Scenario portfolio

V1-V8 share one capture helper. It stores the exact skill revision, model and
runtime identifiers, complete outer instructions, source-packet hash, exposed
generation settings, tool/context configuration, trial count, output, and
timestamps. A scenario-specific scorer compares observable output with the
source packet and reader contract and reports the first failed contract ID. The
trial policy and rubric are fixed before outputs are generated. Private plans
are neither captured nor inferred. An unavailable runtime is external evidence
unavailability; a valid output that violates the rubric is a model-behavior
failure.

| Evidence | Lane | Scenario, scoring, and failure localization |
|---|---|---|
| V1 | Controlled model behavior | **Authority preservation.** A field comparator checks that a rewritten review finding retains severity, status, cited evidence, and requested correction. A mismatch localizes to CTW1 or the named leaf consumer. |
| V2 | Controlled model behavior | **Trigger, precedence, and single pass.** An invocation trace checks that engineering-evidence artifacts select this skill, general prose selects `writing` when available, private work selects neither, a specialized leaf runs first, and an outer orchestrator does not apply a second pass. A mismatch localizes to CTW2 or the named consumer route. |
| V3 | Controlled model behavior | **Audience routing.** A required-information rubric checks that the same source change yields distinct PR, local-comment, and operator-status explanations with no author-only premise. A mismatch localizes to CTW3's reader or purpose selection. |
| V4 | Controlled model behavior | **Adaptive output.** A compactness and prerequisite-order rubric checks that a small commit message avoids visible ceremony while a multi-claim handoff presents supported claims in dependency order. Token and latency cost are reported separately as observational telemetry. The scenario makes no claim that private planning occurred. |
| V5 | Controlled model behavior | **Terminology.** A relationship rubric checks that an overloaded verb is replaced by the relevant actor, operation, object, condition, and result, while a necessary repository concept receives one stable ordinary-language definition. A mismatch localizes to CTW5. |
| V6 | Controlled model behavior | **Source and precision.** A source-field comparator checks that an investigation retains unknowns and provenance, observational values use consistent decision-sized precision, and an exact correctness boundary is unchanged. A mismatch localizes to source fidelity or measurement treatment under CTW6. |
| V7 | Controlled model behavior | **Structure and deletion.** A structure rubric checks that comparable fields use a table, a linear argument remains prose, and every retained or removed element preserves the supplied reader prerequisites. A mismatch localizes to CTW7's relationship or relevance rule. |
| V8 | Controlled model behavior | **Late change.** A contradiction and dependency checker compares the revised artifact with a changed source packet and checks the affected paragraph, adjacent transitions, summary, and conclusion. A stale or appended contradiction localizes to CTW8. |
| V9 | Deterministic repository gate | **Consumer composition.** Static inspection verifies that each of the six consumers retains its substantive authority, names one leaf invocation point, contains one concise link, and does not copy the process. It also verifies that `evidence-efficient-review`, not `review-fixpoint`, owns the pass over a review artifact. |
| V10 | Deterministic repository gate | **Package gate.** The skill validator, relative-link checks, reference-contents checks, fixture-schema validation, static-example invariant checks, trigger/routing declaration checks, duplication search, symlink read-back, and `git diff --check` pass on the exact revision. |
| V11 | Blinded human evidence | **Controlled comprehension comparison.** Baseline and candidate use the same task, source packet, outer instructions, model/runtime configuration, generation policy, and exposed settings; only the candidate receives the skill. Audience-matched readers see randomized or counterbalanced unlabeled outputs and answer the five CTW10 questions. Predeclared factual and comprehension scorers require no factual regression and the declared comprehension improvement. A failure localizes to factual preservation or human comprehension rather than package structure. |

## Evidence and completion

V9-V10 are required for `deterministic-fixed-point`. They can prove that the
package, consumers, fixtures, and static examples implement the specification
on the accepted revision. They cannot prove that a model follows the skill or
that people understand its output.

V1-V8 are external compatibility evidence for model behavior. Record exactly
the identity fields named by the shared capture protocol. A valid generated
output that violates a predeclared scenario rubric is
`product-contract-failure` and blocks the affected capability. Authentication
or configuration failure, provider or infrastructure failure, and an
inconclusive timeout leave `model-capability-unconfirmed`; they remain visible
but do not fail V9-V10. Passing trials are `current` or `reusable` only under
the freshness rule below.

V11 is separate external evidence for the claim that the skill improves human
comprehension. The baseline is the same generation task under the exact
recorded conditions with the candidate skill absent, unless the product claim
explicitly names another production baseline. Before generation, record the
artifact assignment, sample, randomized or counterbalanced presentation,
factual scorer, comprehension scorer, and minimum material improvement. Missing
evaluators, infrastructure failure, or an inconclusive sample leaves
`human-comprehension-unconfirmed`; it does not fail V9-V10 or count as evidence
of improvement. A valid paired pilot that violates the factual or comprehension
criterion is `product-contract-failure` and returns the affected contract to
remediation.

External model and human evidence is reusable for the exact skill revision for
seven days after collection only while the model/runtime identity,
complete outer instructions, source-packet suite, generation settings,
tool/context configuration, scoring protocol, and intended audience remain
unchanged. A skill revision or identity mismatch invalidates it immediately.
At or after the expiry instant, the evidence is stale and must be refreshed
before another capability claim, even if all identities still match.

| Freshness-limit field | Record |
|---|---|
| Correctness role | Prevent a human or model result from supporting a later capability claim after the agent runtime or evaluation context may have drifted. |
| Workload basis | One implementation and fixed-point rollout is expected to complete within a week; the initial evaluation suite is intentionally small enough to rerun. This is an operational assumption, not an empirical claim. |
| Expected resource effect | Evidence reuse avoids rerunning V1-V8 and V11 during the same rollout. An older rollout pays the accepted cost of a fresh small-suite run and human comparison. |
| Exact boundary | With UTC timestamps, evidence is reusable when `collected_at <= use_at < collected_at + 168 hours`. It is stale when `use_at >= collected_at + 168 hours`. An identity mismatch makes it stale earlier. |
| Revision trigger | Change the limit only after recording actual rollout durations and model/runtime stability. The replacement must state its last reusable and first stale instants. |

Word count, prompt/output tokens, drafting latency, reading time, preference,
and edit size are observational unless the pilot protocol gives a metric a
baseline, measurement method, direction, and threshold. Short-artifact cost is
especially important to record because CTW4 exists to avoid process overhead,
but an unthresholded cost observation cannot decide acceptance.

The package reaches `deterministic-fixed-point` only when CTW1-CTW10 are
implemented, V9-V10 pass on the exact reviewed revision, and a fresh independent
review reports no P0-P3 finding or required unknown. It is `Done` only when
V1-V8 are current and passing and the initial V11 capability is confirmed under
the paired protocol. Earlier deterministic completion must retain
`model-capability-unconfirmed`, `human-comprehension-unconfirmed`, or both, as
applicable, and must not claim proven model compliance or improved human
understanding.

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
repository. It continues to own general and public prose. This package must work
without assuming that skill is installed, while stating precedence clearly when
both are available.

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
| CTW2 | **Route only reader-facing engineering prose.** Direct triggers include requests to draft or revise PR descriptions, commit messages, code comments, investigation handoffs, technical reports, design documents, status updates, and technical explanations for developers or operators. Private notes, private reasoning, raw evidence collection, general/public prose, and tasks with no requested prose artifact do not trigger it. When a specialized repository skill applies, that skill runs first and this skill is only its final prose pass. | New skill owns trigger and precedence. Consumer skills own whether their completed artifact needs the pass. | S1, S4 | V2 Trigger-and-precedence fixture |
| CTW3 | **Derive the reader and purpose from the artifact.** Record who will read the artifact, what relevant knowledge may be assumed, and what the reader must understand, decide, verify, or do. Use an uninvolved repository developer only as the fallback for a PR, commit, design, or report when a more specific audience cannot be recovered. A code comment targets the future maintainer at that statement; an operational update targets its actual recipients. | New skill | S2 | V3 Audience-routing scenarios |
| CTW4 | **Use an adaptive drafting process.** Every pass establishes source, audience, purpose, and the answer or action that belongs first. A compact artifact then drafts and performs one fresh-reader check. An artifact with several dependent claims first records a private question order and claim-to-evidence map. Sentence-level reader-state simulation is optional diagnostic work for a passage that remains unclear; it is not routine bookkeeping. The private plan is never acceptance evidence. | New skill | S2 | V4 Compact, standard, and difficult-passage scenarios |
| CTW5 | **Make relationships explicit without banning necessary terms.** Prefer established repository terms after explaining the concept in ordinary language. Introduce a new term only when a distinct concept needs a stable name, define it once, and do not overload a familiar word with an unstated private meaning. Where a compressed verb such as `classify`, `route`, or `invalidate` would hide the result, state the actor, operation, object, condition, and consequence that matter to the reader. | New skill; specialized skills remain vocabulary authorities for their domains. | S2 | V5 Terminology and relationship fixture |
| CTW6 | **Ground material claims and measurements.** Inspect the complete authorized source set and correct comparison base before writing. Distinguish existing evidence from evidence added by the change, and keep facts, rationale, limitations, non-goals, unknowns, and future direction separate. Preserve exact values for contractual boundaries, reproducibility, and close comparisons. Round observational values only to the precision needed for the reader's decision, using consistent units and retaining the comparison that supports the claim. | Source or artifact owner supplies truth; new skill verifies prose against it. | S2 | V6 Source-fidelity and measurement scenarios |
| CTW7 | **Match structure and detail to the information.** Use prose for a linear argument, lists for discrete items, numbered steps for order, tables for repeated comparable fields, and a diagram only when it materially clarifies a relationship. Keep a sentence, heading, example, or measurement only when it helps the reader understand, verify, decide, or act, or prevents a likely material misunderstanding. Punctuation and voice remain contextual choices rather than acceptance rules. | New skill | S2 | V7 Structure-and-deletion scenario |
| CTW8 | **Revalidate after later edits.** A changed source fact or requested addition invalidates every prose claim, paragraph transition, title, summary, conclusion, and evidence statement that depends on it. Rewrite the smallest complete unit rather than appending a sentence mechanically, then read the preceding and following transitions from the reader's knowledge state. Re-read the complete artifact when its purpose, through-line, decision, or conclusion changed. | New skill; calling artifact skill supplies the changed source and scope. | S3 | V8 Late-change revision scenario |
| CTW9 | **Keep one compact writing authority.** The new `SKILL.md` contains trigger, precedence, adaptive process, and final acceptance questions. One-level references contain artifact routing, revision-after-change mechanics, examples, and research rationale. Consumer skills link or invoke the authority at their final prose boundary and do not copy its checklist. Research explains design choices but is not presented as proof that the exact process works. | New skill owns writing guidance. `skill-authoring` remains the authority for package structure. | S1, S3, S4 | V9 Package, reference, and duplication checks |
| CTW10 | **Prove outputs, not hidden process compliance.** Deterministic repository gates verify skill structure, links, trigger boundaries, source fidelity, authority preservation, required distinctions, and the late-change behavior. A blinded human-comprehension pilot separately evaluates whether intended readers can explain what happened before, what changes, why it is correct or deliberately different, what evidence matters, and what action is requested. Word count, tokens, latency, reading time, and preference remain observational until the pilot records a baseline, method, and decision threshold. | Repository fixtures own deterministic gates. Selected human evaluators own comprehension evidence. | S5, S6 | V10 Deterministic suite; V11 blinded comprehension pilot |

## Artifact routing and ownership

This table applies CTW1 and CTW2. It is routing information, not a second
definition of the writing contract.

| Artifact | Substantive owner | Writing pass |
|---|---|---|
| PR description, commit message, code comment, investigation handoff, status report, technical explanation | Caller, repository sources, and any task-specific skill | Use `clear-technical-writing` directly after facts and decisions are established. |
| Educational technical-note series | `technical-note-series` | Use the new skill only after reader journey, examples, ownership, and publication scope are coherent. |
| `docs/architecture.md` | `project-architecture-doc` | Use the new skill after the required architecture structure and source-backed discussion exist. |
| Repository architecture policy | `add-architectural-guidances` | Use the compact pass after the guidance contract has been applied. Do not expand the policy to demonstrate prose technique. |
| Review artifact or finding explanation | `evidence-efficient-review`; `review-fixpoint` owns outer mechanics | Apply the writing pass only after findings, severities, statuses, and evidence are final. Wording cannot add, remove, close, or downgrade a finding. |
| Implementation slice or package handoff | `supervised-implementer-loop` | Use the compact pass without changing accepted contract IDs or evidence results. |
| General/public prose | General `writing` skill when available | Do not invoke this skill merely because the subject is technical. |

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
  operators must understand, verify, decide, or act on technical work. Do not
  use for private reasoning or general public prose; when a specialized skill
  owns the artifact, preserve its decisions and apply this skill only as the
  final prose pass.
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
owning sections in the six repository skills. Each consumer states when its
substantive work is ready for a prose pass and links to the new skill. It does
not copy the process, examples, or final questions.

### S5 — Add deterministic behavioral fixtures

Implement the deterministic part of CTW10 through the V1-V10 scenarios below.
Fixtures contain source packets, artifact intent, observable reader contract,
and forbidden regressions. They do not prescribe exact sentences or inspect
private reasoning.

### S6 — Pilot, install, and complete the rollout

Run V11 with blinded readers against a recorded baseline and a predeclared
decision rule. Record skill revision, model family, source packet, artifact
type, evaluator audience, and results. Install the repository skill as
`~/.agents/skills/clear-technical-writing`, verifying the link target and a
readable `SKILL.md`. Run an independent review under `review-fixpoint` before
claiming completion.

## Scenario portfolio

| Evidence | Scenario | Observable result and localization |
|---|---|---|
| V1 | Authority preservation | A prose pass over a review finding preserves severity, status, evidence, and requested correction. A mismatch localizes to CTW1 or the consumer boundary. |
| V2 | Trigger and precedence | Direct engineering-prose requests trigger the skill; private notes and general prose do not; specialized artifact work runs before the prose pass. |
| V3 | Audience routing | The same change produces appropriately different PR, local-comment, and operator-status explanations without assuming the author as reader. |
| V4 | Adaptive effort | A compact commit message does not acquire planning ceremony; a multi-claim handoff has ordered reader questions and evidence; only an actually unclear passage uses the diagnostic. Acceptance observes the output and cost, not private notes. |
| V5 | Terminology | An unnecessary overloaded term is expanded into an explicit operation and result, while a genuinely new repository concept receives one stable, ordinary-language definition. |
| V6 | Source and precision | An investigation preserves unknowns and source provenance. A performance summary rounds observational values consistently but retains an exact timeout or boundary needed for correctness. |
| V7 | Structure and deletion | Comparable results use a table, a linear explanation remains prose, and removing decorative structure or obvious facts does not remove a reader prerequisite. |
| V8 | Late change | A later fact contradicts part of an otherwise good draft. The affected paragraph, transitions, summary, and conclusion are revalidated; no contradictory appended sentence remains. |
| V9 | Consumer composition | Each of the six existing skills retains its substantive authority and contains only a concise invocation/link. General writing remains an adjacent non-required authority. |
| V10 | Deterministic package gate | The skill validator, relative-link checks, reference-TOC checks, trigger-negative checks, duplication search, source-fidelity fixtures, and `git diff --check` pass on the exact revision. |
| V11 | Blinded comprehension pilot | Readers who match the artifact audience answer the five CTW10 questions against baseline and candidate artifacts without seeing which process produced them. The predeclared rule requires no factual regression and a material comprehension benefit before claiming that capability. |

## Evidence and completion

The deterministic suite is required for `deterministic-fixed-point`. It can
prove that the implemented package follows CTW1-CTW10 and that its controlled
fixtures do not regress.

The human pilot is external compatibility evidence for the claim that the skill
improves comprehension. Before running it, record the baseline, sample, scoring
method, and minimum material improvement; do not choose the threshold after
seeing results. Reuse is allowed only while the skill contract, material prompt
shape, model family, artifact suite, and intended audience remain applicable.
Missing evaluators or an inconclusive sample leaves
`human-comprehension-unconfirmed`; it does not fail the deterministic suite or
count as evidence of improvement. A valid pilot that contradicts the declared
criterion returns the process or routing design to remediation.

Word count, prompt/output tokens, drafting latency, reading time, preference,
and edit size are observational unless the pilot protocol gives a metric a
baseline, measurement method, direction, and threshold. Short-artifact cost is
especially important to record because CTW4 exists to avoid process overhead,
but an unthresholded cost observation cannot decide acceptance.

The package is `Done` only when CTW1-CTW10 are implemented, V1-V10 pass on the
exact reviewed revision, a fresh independent review reports no P0-P3 finding or
required unknown, the skill link is verified, and the initial V11 capability is
confirmed. Deterministic fixed point may be reported earlier, but it must retain
`human-comprehension-unconfirmed` and must not claim that the skill is proven to
improve human understanding.

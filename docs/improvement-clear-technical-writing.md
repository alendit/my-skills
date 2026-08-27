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
| CTW1 | **Preserve substantive authority.** `clear-technical-writing` may reorganize, explain, qualify, or delete prose only when the resulting text preserves the accepted technical meaning. The source artifact and its specialized skill continue to decide behavior, scope, architecture, review findings, severity, evidence status, and workflow. When meaning is uncertain, the writer returns to that authority instead of silently choosing an interpretation. | New skill owns prose transformation. Every existing skill remains owner of its domain decisions. | S1, S4 | Initial-writing and revision cases |
| CTW2 | **Route one prose pass by artifact purpose and factual owner.** Requests to draft or revise engineering artifacts use this skill when their claims depend on code, diffs, tests, architecture, or operational evidence, whether or not the artifact is public. Editorial, marketing, customer communication, and other general prose use `writing` when available. Private notes, private reasoning, raw evidence collection, and tasks with no requested prose artifact trigger neither. A specialized artifact skill completes the substantive artifact and, as leaf owner, invokes this skill once. An outer orchestrator may require or report that pass but may not apply it again. If the user explicitly names both writing skills, the artifact owner selects one transformation process and may consult the other only for non-conflicting guidance; it never runs two automatic rewrites, weakens source truth, or overrides the specialized contract. | New skill owns prose routing. The leaf substantive artifact skill owns the single invocation; outer orchestrators own only workflow status. | S1, S4 | Consumer source review and agent-handoff case |
| CTW3 | **Derive the reader and purpose from the artifact.** Record who will read the artifact, what relevant knowledge may be assumed, and what the reader must understand, decide, verify, or do. Use an uninvolved repository developer only as the fallback for a PR, commit, design, or report when a more specific audience cannot be recovered. A code comment targets the future maintainer at that statement; an operational update targets its actual recipients. | New skill | S2 | Initial-writing case |
| CTW4 | **Use an adaptive drafting process.** Every pass establishes source, audience, purpose, and the answer or action that belongs first. A compact artifact then drafts and performs one fresh-reader check. An artifact with several dependent claims first records a private question order and claim-to-evidence map. Sentence-level reader-state simulation is optional diagnostic work for a passage that remains unclear; it is not routine bookkeeping. The private plan is never acceptance evidence. | New skill | S2 | Initial-writing case and source inspection |
| CTW5 | **Make relationships explicit without banning necessary terms.** Prefer established repository terms after explaining the concept in ordinary language. Introduce a new term only when a distinct concept needs a stable name, define it once, and do not overload a familiar word with an unstated private meaning. Where a compressed verb such as `classify`, `route`, or `invalidate` would hide the result, state the actor, operation, object, condition, and consequence that matter to the reader. | New skill; specialized skills remain vocabulary authorities for their domains. | S2 | Project-glossary case |
| CTW6 | **Ground material claims and measurements.** Inspect the complete authorized source set and correct comparison base before writing. Distinguish existing evidence from evidence added by the change, and keep facts, rationale, limitations, non-goals, unknowns, and future direction separate. Preserve exact values for contractual boundaries, reproducibility, and close comparisons. Round observational values only to the precision needed for the reader's decision, using consistent units and retaining the comparison that supports the claim. | Source or artifact owner supplies truth; new skill verifies prose against it. | S2 | Initial-writing and revision cases |
| CTW7 | **Match structure and detail to the information.** Use prose for a linear argument, lists for discrete items, numbered steps for order, tables for repeated comparable fields, and a diagram only when it materially clarifies a relationship. Keep a sentence, heading, example, or measurement only when it helps the reader understand, verify, decide, or act, or prevents a likely material misunderstanding. Punctuation and voice remain contextual choices rather than acceptance rules. | New skill | S2 | Initial-writing case |
| CTW8 | **Revalidate after later edits.** A changed source fact or requested addition invalidates every prose claim, paragraph transition, title, summary, conclusion, and evidence statement that depends on it. Rewrite the smallest complete unit rather than appending a sentence mechanically, then read the preceding and following transitions from the reader's knowledge state. Re-read the complete artifact when its purpose, through-line, decision, or conclusion changed. | New skill; calling artifact skill supplies the changed source and scope. | S3 | Revision-after-change case |
| CTW9 | **Keep one compact writing authority.** The new `SKILL.md` contains trigger, precedence, adaptive process, and final acceptance questions. One-level references contain artifact routing, revision-after-change mechanics, examples, and research rationale. Consumer skills link or invoke the authority at their final prose boundary and do not copy its checklist. Research explains design choices but is not presented as proof that the exact process works. | New skill owns writing guidance. `skill-authoring` remains the authority for package structure. | S1, S3, S4 | Package and consumer source review |
| CTW10 | **Use observable evidence without turning evaluation into a workflow engine.** Deterministic repository checks establish that the skill, links, compact case manifest, and capture format are well formed on the reviewed revision. A dated pre-study protocol compares matched baseline and skill outputs for four representative cases: initial technical writing, revision after a new requested change, project-glossary use, and an agent handoff. Blinded independent review asks whether the skill condition is clearer while preserving facts and terminology without unnecessary detail. A separate V11 pilot measures intended-reader comprehension only when evaluators are available. Validators check structure and identity, never prose quality, terminology quality, private reasoning, or chronology. Actual trials support capability claims but are not a deterministic prerequisite for accepting a sensibly implemented skill. | Repository checks own deterministic conformance. Independent reviewers own model-output judgments. Available intended-reader evaluators own V11 comprehension evidence. | S5, S6 | Four-case paired model study; optional V11 human pilot |

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

Implement the deterministic part of CTW10 with the repository skill validator,
rendered-link checks, a readable four-case manifest, a thin capture validator,
exact-revision identity, and installed-skill read-back. Mechanical validation
rejects malformed records but does not infer ownership from prose, score an
output, or enforce a trial lifecycle.

### S6 — Run capability evaluations and complete the rollout

Use the dated
[pre-study protocol](evidence/2026-08-27-clear-technical-writing-pre-study-protocol.md)
to run the four matched baseline-versus-skill model cases and obtain blinded
independent review. Run V11 only when the
predeclared intended-reader evaluators are available. These trials support a
capability claim; they are not part of deterministic package acceptance. Run an
independent implementation review before accepting the repository change.

## Scenario portfolio

The compact manifest uses four representative cases rather than one fixture for
every contract clause. Each case contains a source packet and observable review
questions; none contains target prose, event traces, actor schemas, or an
automatic quality score.

| Case | Main contracts exercised | Observable comparison |
|---|---|---|
| Initial technical writing | CTW1, CTW3-CTW4, CTW6-CTW7 | Compare the first engineering update for clarity, factual preservation, stable terminology, and unnecessary detail. |
| Revision after change | CTW1, CTW6, CTW8 | Check whether a new requested correctness result causes all dependent conclusions and transitions to be revised. |
| Project glossary use | CTW1, CTW5, GL3, GL5 | Check whether a selected term is used consistently, explained locally, and kept subordinate to its semantic source. |
| Agent handoff | CTW1-CTW2, GL3, GL7 | Check whether another agent receives a self-contained scope, evidence, terminology mapping, and requested report without invented mechanisms. |

For each case, run the same model and runtime under matched baseline and skill
conditions. A blinded independent reviewer uses the dated protocol's four
dimensions and decision rule. The capture helper records condition and identity
but does not compare outputs or decide which one is useful.

V11 remains a separate paired human-comprehension pilot. It is run only when
the intended-reader evaluators predeclared by the protocol are available.

## Evidence and completion

Deterministic acceptance requires a valid skill package, readable case and
capture JSON, working links, installed-skill read-back, exact-revision hygiene,
and a fresh independent implementation review with no material finding or
required unknown. These checks can establish that CTW1-CTW10 are implemented
sensibly; they cannot establish that the skill improves a model's writing.

The four matched model cases provide the initial capability evidence. Record
the exact skill revision, paired condition, model and runtime identity, outer
instructions, settings, tool/context configuration, source-packet hash, output,
and collection time. Independent review—not the capture validator—applies the
predeclared usefulness rule. An unavailable runtime leaves
`model-capability-unconfirmed`; a reviewed contradiction is
`product-contract-failure`.

V11 is separate evidence for human comprehension and is not run unless suitable
intended-reader evaluators are available. Missing evaluators leave
`human-comprehension-unconfirmed`; they do not invalidate deterministic
acceptance or substitute for a failed study.

Actual model and human trials are required before claiming the corresponding
capability, but they are not a deterministic prerequisite for accepting a
sensibly implemented skill. Word count, tokens, latency, reading time,
preference, and edit size remain observational unless a study protocol gives
the measure a baseline, method, direction, and threshold. Any later capability
claim must identify the exact revision and conditions that produced its
evidence rather than treating an old capture as timeless proof.

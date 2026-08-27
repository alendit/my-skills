# Improvement Plan: Integrate Project Glossaries

## Purpose and composed authority

Add glossary-aware behavior to the planned `clear-technical-writing` package
and the existing skills that create or consume durable engineering
communication. The intended reader may be a person or another agent. Do not
create a separate glossary skill.

The GL1-GL8 matrix below is the sole authority for glossary discovery,
placement, term ownership, maintenance, and evidence. The
[clear-technical-writing plan](improvement-clear-technical-writing.md) remains
authoritative for prose routing, adaptive drafting, terminology in the current
artifact, later-edit revalidation, and the single final prose pass. The
[contract-centered plan](improvement_avoid_repetition.md) remains authoritative
for evidence classes and exact-limit policy. Other sections in this document
reference GL IDs and add only routing, implementation, or evidence details.

## Scope and current fit

A project glossary is an optional durable source for terminology shared across
artifacts, sessions, and agents. It is useful when a project gives an
established word a narrower meaning or introduces a genuinely distinct
abstraction, owner, lifetime, resource, or process. It is not required for
ordinary programming vocabulary or for a term used clearly in one local
passage.

The planned `clear-technical-writing` skill already owns the relevant prose
behavior through CTW5: explain unfamiliar concepts in ordinary language, avoid
overloading common words, and introduce a new term only when a distinct concept
needs a stable name. Glossary support should extend that owner with an optional
project-source reference. It must not add another writing pass, terminology
reviewer, or automatic repository mutation.

Existing repository skills already own adjacent concerns:

- `technical-note-series` owns teaching order and series vocabulary;
- `project-architecture-doc` owns source-grounded architecture prose;
- `add-architectural-guidances` owns compact, self-contained policy;
- `evidence-efficient-review` owns material findings and their evidence;
- `supervised-implementer-loop` owns implementation handoffs and rejects
  literal implementation of accidental specification vocabulary; and
- `review-fixpoint` owns only outer Tick/Tock mechanics.

## Authoritative contract-and-evidence matrix

| ID | Observable contract | Semantic owner and public composition | Slice | Named evidence |
|---|---|---|---|---|
| GL1 | **Extend the existing writing authority.** Glossary behavior lives in a one-level reference of `clear-technical-writing`. Consumer skills link to that authority when they discover sources, prepare a durable artifact for a person or agent, or perform the one final prose pass. No `project-glossary`, `glossary-manager`, or equivalent standalone skill is created, and no consumer copies the workflow. | `clear-technical-writing` owns the shared glossary workflow; `skill-authoring` owns package shape. Every listed consumer remains owner of its artifact. | S1, S4 | Package and consumer source review |
| GL2 | **Discover placement and obtain consent.** Before durable engineering communication uses or establishes shared project terminology, inspect explicit user instructions and repository guidance. If the user declines glossary creation or use for this task, do not ask about placement, create a file, or persist a term; use GL5's local-definition fallback. Otherwise use an existing selected glossary. If no glossary exists but either authority selects its location, placement is resolved while the task's normal write-authorization boundary remains in force. If no glossary exists and neither authority selects placement, ask whether to create it inside the project or at a user-selected look-aside location; do not create a file or persist a term until the user answers. After a project-local answer, use an established documentation path or ask for the exact path. After a look-aside answer, obtain the exact location and scope. Never invent either location. Ask which source governs when several plausible glossaries remain unresolved. Unrelated work that neither uses nor establishes shared project terminology does not trigger the question. Reuse a prior selection only when it is recoverable for the same project and scope. | The user or repository guidance owns placement. The artifact's leaf skill performs discovery and asks the question before glossary creation. | S1, S2, S4 | Source review and glossary case |
| GL3 | **Keep terminology authority separate from semantic truth.** The selected glossary is canonical for a project's preferred term, aliases, and plain explanation within its declared scope. Code, accepted contracts, architecture authorities, and the artifact's factual owner remain authoritative for behavior, ownership, lifetime, and acceptance. Glossary entries link to those sources when the distinction matters. A conflict is reported to the semantic owner instead of being silently normalized in prose. | The selected glossary owns term identity and explanation. Existing technical owners retain semantics. The final artifact demonstrates the composition. | S2, S3 | Project-glossary and agent-handoff cases |
| GL4 | **Record only useful project distinctions.** Add a term only when it names a distinct project concept or a domain concept used more narrowly than readers can safely assume. Explain it in ordinary language, state the project-specific distinction, and include the owner, lifetime, mapping, or semantic-source link only when needed to prevent a material misunderstanding. Keep one entry per concept and make aliases point to it. Entry length, Markdown shape, and cross-reference styling follow the repository and the information; a one-paragraph cap and italicized cross-references are not contracts. | The artifact's technical owner supplies meaning. The glossary editor owns concise presentation and cross-links. | S2 | Glossary source review |
| GL5 | **Use the glossary without turning communication into a glossary.** Read relevant entries before drafting a durable engineering artifact, including a review dossier, agent assignment, correction, or handoff. Explain a term locally when the intended person or agent still needs that prerequisite. Do not open an artifact with a vocabulary dump, replace concrete operations with labels, or assume that a link repairs an unclear instruction. If the user declines glossary creation or no authorized location is available, define the concept in the artifact and do not persist it elsewhere. | The leaf artifact skill owns prerequisite placement. `clear-technical-writing` performs the single final terminology check under CTW2 and CTW5 when that prose pass applies. | S2, S4 | Project-glossary case |
| GL6 | **Update definitions within the authorized dependency boundary.** A durable artifact may propose a glossary entry only when its accepted source establishes the meaning. Write the entry only when the selected location and documentation scope are authorized; otherwise report the candidate. When a semantic source or glossary definition changes, revalidate aliases, linked entries, and affected prose under CTW8 only inside the current authorized edit scope. Report each known out-of-scope dependent with its semantic source and stale term; do not edit it or silently treat it as current. Do not append a compensating sentence to a stale entry or change the term to fit one artifact. | The semantic owner approves meaning; the authorized glossary editor changes the entry; in-scope artifact owners revalidate dependent prose. The current task reports out-of-scope dependents without assuming their edit authority. | S3, S4 | Glossary source review and revision case |
| GL7 | **Preserve consumer-specific ownership and agent-to-agent meaning.** The selected project glossary owns the preferred project-wide term, aliases, and concise project meaning. A `technical-note-series` guide owns introduction order, reader-specific first-use explanations, and terms used only within that series; it links to the glossary instead of maintaining a second canonical project definition. `evidence-efficient-review` resolves the glossary while establishing the review contract, records the selected source or explicit opt-out in its neutral dossier, independently reads the entries material to the review, and uses their terms consistently in findings without treating them as proof. `supervised-implementer-loop` resolves the glossary before spawning the implementer, records its source or opt-out plus relevant term-to-semantic-source mappings in the work package and initial assignment, and verifies terminology continuity in corrections and handoffs. New terms remain reported candidates unless their meaning, location, and edit scope are authorized. Architecture and policy skills remain factual owners. Implementation agents treat glossary entries as explanatory input, never as authority to manufacture mechanisms. `review-fixpoint` carries the selected source or opt-out between its leaf workflows but does not apply another glossary or prose pass. | Each consumer named in the routing table retains its established responsibility. Code, accepted contracts, architecture authorities, findings, and package scope outrank glossary wording. | S4 | Consumer source review and agent-handoff case |
| GL8 | **Use the shared representative evidence model.** Deterministic checks establish readable package and case data, valid links, and exact-revision identity without judging terminology. The shared four-case model study includes project-glossary use and an agent handoff alongside initial writing and later revision. Blinded independent review decides whether the skill is useful while preserving semantic-source precedence and local explanation. The optional V11 pilot remains the only human-comprehension lane and runs only when evaluators are available. Actual trials support capability claims but are not a deterministic prerequisite for accepting a sensibly implemented glossary integration. | CTW's study protocol and independent reviewers own capability evidence. Repository validation owns mechanical conformance only. | S5 | Four-case paired model study; optional V11 human pilot |

## Entry-shape guidance

This guidance implements GL3-GL4 and remains replaceable by an equivalent
repository-native format. A useful entry normally contains:

- the preferred term and any accepted alias;
- a plain explanation of the concept in this project;
- the difference from a common or domain meaning when that difference matters;
- the relevant owner, lifetime, mapping, or boundary when readers could confuse
  it; and
- a link to the semantic source when the entry would otherwise look normative.

Use prose for one compact definition, a small table for repeated mappings, and
links for related terms when the format supports them. Do not require every
entry to fill every field. Do not use typography alone to signal whether a term
has a definition.

## Consumer routing

This table applies GL5-GL7 without redefining them.

| Consumer | Glossary responsibility |
|---|---|
| `clear-technical-writing` | Add `references/project-glossaries.md`; perform GL2 discovery when it is the direct leaf owner, treat people and collaborating agents as possible readers, use relevant entries as sources, and run the one CTW5 terminology check during the final pass. |
| `technical-note-series` | Apply GL2 before building teaching vocabulary. Keep the guide authoritative for prerequisite order, reader-specific first-use explanations, series-only terms, and navigation. Link project-wide definitions instead of maintaining a second canonical meaning. |
| `project-architecture-doc` | Treat the selected glossary as an explanatory source. Verify definitions against code and architecture authorities, and route durable new project terms through GL2 and GL6. |
| `add-architectural-guidances` | Preserve established glossary terms when available, but keep target policy self-contained and do not make a look-aside glossary an undeclared runtime dependency. |
| `evidence-efficient-review` | Apply GL7 in `Establish The Review Contract`, `Build A Compact Review Dossier`, and `Return A Structured Review Result`. Give the reviewer the selected glossary identity or opt-out, require independent reading of material entries, verify semantic claims against their owners, and report only terminology defects that can change the review result. Its final review artifact receives the existing single clear-writing pass. |
| `supervised-implementer-loop` | Apply GL7 in `Establish The Work Package`, `Give The Initial Assignment`, `Run Each Slice`, and `Accept The Package`. The parent resolves glossary state before spawning, gives the implementer relevant term-to-semantic-source mappings without copying the whole glossary, checks corrections and handoffs for drift, and treats new terms as candidates unless authorized. Glossary wording cannot create fields, states, limits, or components. |
| `review-fixpoint` | Carry the selected glossary identity or explicit opt-out through Tick and Tock inputs and results. Require or report the leaf owner's glossary-aware pass when applicable; do not independently apply a second glossary or prose pass. |

The general `writing` skill remains outside this repository. When it owns a
general prose artifact, it may consume a user-supplied glossary as source
material, but this plan does not add a dependency or second pass to that skill.

## Ordered implementation slices

### S1 — Extend the planned clear-writing package

Implement GL1-GL2 by adding the one-level glossary reference and a concise
entrypoint instruction that invokes GL2. Do not create a new skill directory or
copy the placement rule outside its matrix row.

### S2 — Implement source use and entry guidance

Implement GL3-GL5 in the reference. Preserve the distinction between glossary
explanation and semantic truth, local prerequisite explanation and durable
entry, and necessary project terminology and ordinary domain vocabulary.

### S3 — Make glossary changes dependency-aware

Implement GL6 together with CTW8. Cover a changed semantic source, an obsolete
alias, an in-scope artifact whose wording depends on the old definition, and a
known dependent outside the authorized edit scope. Update only the authorized
files and report the out-of-scope stale term and source.

### S4 — Integrate only the owning consumer boundaries

Implement GL1, GL5-GL7 through concise links or invocation notes in the consumer
table. For `technical-note-series`, coherently update `SKILL.md` and the
`research-and-reader-journey.md`, `drafting-and-coherence.md`, and
`validation-and-review.md` references so none retains a canonical shared-term
definition in the guide. Update the three named `evidence-efficient-review`
sections and the four named `supervised-implementer-loop` sections so glossary
identity and relevant definitions survive agent delegation and handoff. Update
`review-fixpoint` only to carry that state between leaf workflows. Consumers do
not copy GL2 or the entry guidance. Preserve the single-pass ownership
established by CTW2.

### S5 — Extend existing validation rather than creating another suite

Implement GL8 through CTW's shared four-case manifest and dated study protocol.
The project-glossary and agent-handoff cases provide representative observable
coverage; independent source review verifies consumer ownership and the full
GL1-GL7 contract. Do not create a second suite or encode glossary workflow and
agent lifecycle semantics in the mechanical validator.

## Scenario portfolio

The shared study uses two compact glossary-relevant cases:

| Case | Observable review question |
|---|---|
| Project glossary use | Does the output use the selected term consistently, explain it locally for the intended reader, preserve its semantic source, and avoid turning the artifact into a glossary? |
| Agent handoff | Does the receiving agent get the selected glossary state, material term-to-source relationships, scope, evidence, and constraints without redefinition or mechanism invention? |

These cases sample the most material reader-facing outcomes. They do not replace
source review of discovery, consent, authorization, update boundaries, aliases,
or consumer-specific ownership under GL1-GL7. The capture validator records the
baseline or skill condition and exact identity; it has no event trace, actor
schema, terminology scorer, or workflow model.

## Evidence and completion

Deterministic acceptance combines mechanical package checks with independent
source review of GL1-GL8 and consumer ownership on the exact revision. It does
not require an exhaustive fixture for every glossary branch and does not claim
that a model followed the instructions.

The paired project-glossary and agent-handoff outputs provide representative
model-capability evidence under CTW10. The dated protocol's blinded reviewer
decides whether the skill is useful; the validator does not. Runtime
unavailability leaves model capability unconfirmed, while a reviewed factual
or terminology regression is a product-contract failure.

Glossary-conditioned material may join V11 only when intended-reader evaluators
are available. Missing evaluators leave human comprehension unconfirmed and do
not invalidate deterministic acceptance.

Counts of entries, prompt tokens, lookup time, prose length, and edit size are
observational. No exact entry-length, glossary-size, or lookup limit is a
completion gate.

Actual trials are required before claiming model or human capability, but are
not a deterministic prerequisite for accepting a sensibly implemented glossary
integration. This document may require an independent review but does not
define review numbering, commits, reviewer selection, remediation repetition,
or stop mechanics.

## Original-draft disposition

The original proposal's useful core remains: keep project terminology small,
prefer plain wording, define genuinely new concepts, read the glossary before
durable writing, and review only material ambiguity. The integration rejects
three prescriptions that do not survive the composed design:

- `docs/glossary.md` is a suggested project-local path, not an automatic
  universal location;
- one paragraph per entry is guidance, not a correctness boundary; and
- italicized glossary cross-references are a formatting preference, not a
  semantic contract.

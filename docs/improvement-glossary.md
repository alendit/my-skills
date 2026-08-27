# Improvement Plan: Integrate Project Glossaries

## Purpose and composed authority

Add glossary-aware behavior to the planned `clear-technical-writing` package
and the existing skills that create or consume durable engineering prose. Do
not create a separate glossary skill.

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
artifacts and sessions. It is useful when a project gives an established word a
narrower meaning or introduces a genuinely distinct abstraction, owner,
lifetime, resource, or process. It is not required for ordinary programming
vocabulary or for a term used clearly in one local passage.

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
| GL1 | **Extend the existing writing authority.** Glossary behavior lives in a one-level reference of `clear-technical-writing`. Consumer skills link to that authority at the point where they discover sources or prepare the one final prose pass. No `project-glossary`, `glossary-manager`, or equivalent standalone skill is created, and no consumer copies the workflow. | `clear-technical-writing` owns the shared glossary workflow; `skill-authoring` owns package shape. Every listed consumer remains owner of its artifact. | S1, S4 | D1 package and duplicate-authority checks |
| GL2 | **Discover placement and obtain consent.** Check explicit user instructions and repository guidance for an authoritative glossary location before drafting durable project terminology. If no glossary exists and the user has not chosen a location, ask whether to create it inside the project or at a user-selected look-aside location. Do not create either location or persist a new term until the user answers. If several plausible glossaries remain after guidance is read, ask which one governs the task. A prior answer may be reused only when it is recoverable for the same project and scope. | The user or repository guidance owns placement. The artifact's leaf skill performs discovery and asks the question before glossary creation. | S1, S2, S4 | M1 missing-glossary consent; M2 multiple-candidate routing |
| GL3 | **Keep terminology authority separate from semantic truth.** The selected glossary is canonical for a project's preferred term, aliases, and plain explanation within its declared scope. Code, accepted contracts, architecture authorities, and the artifact's factual owner remain authoritative for behavior, ownership, lifetime, and acceptance. Glossary entries link to those sources when the distinction matters. A conflict is reported to the semantic owner instead of being silently normalized in prose. | The selected glossary owns term identity and explanation. Existing technical owners retain semantics. The final artifact demonstrates the composition. | S2, S3 | M3 semantic-authority preservation |
| GL4 | **Record only useful project distinctions.** Add a term only when it names a distinct project concept or a domain concept used more narrowly than readers can safely assume. Explain it in ordinary language, state the project-specific distinction, and include the owner, lifetime, mapping, or semantic-source link only when needed to prevent a material misunderstanding. Keep one entry per concept and make aliases point to it. Entry length, Markdown shape, and cross-reference styling follow the repository and the information; a one-paragraph cap and italicized cross-references are not contracts. | The artifact's technical owner supplies meaning. The glossary editor owns concise presentation and cross-links. | S2 | M4 entry and alias scenario |
| GL5 | **Use the glossary without turning prose into a glossary.** Read relevant entries before drafting a durable engineering artifact, then explain a term locally when the intended reader still needs that prerequisite. Do not open a note with a vocabulary dump, replace concrete operations with labels, or assume that a link repairs an unclear sentence. If the user declines glossary creation or no authorized location is available, define the concept in the artifact and do not persist it elsewhere. | The leaf artifact skill owns prerequisite placement. `clear-technical-writing` performs the single final terminology check under CTW2 and CTW5. | S2, S4 | M5 existing, declined, and local-definition scenarios |
| GL6 | **Update definitions at their dependency boundary.** A durable artifact may propose a glossary entry only when its accepted source establishes the meaning. Write the entry only when the selected location and documentation scope are authorized; otherwise report the candidate. When a semantic source or glossary definition changes, revalidate aliases, linked entries, and affected prose under CTW8. Do not append a compensating sentence to a stale entry or silently change the term to fit one artifact. | The semantic owner approves meaning; the authorized glossary editor changes the entry; affected artifact owners revalidate dependent prose. | S3, S4 | M6 authorized update and stale-definition scenario |
| GL7 | **Preserve consumer-specific ownership.** Project-wide glossary entries own shared term identity. `technical-note-series` retains teaching order and may link to a project entry instead of copying it. Architecture and policy skills remain factual owners of their artifacts. Review skills flag terminology only when ambiguity, contradiction, or an undefined project term can change a finding, decision, implementation, owner, lifetime, scope, or evidence claim. Implementation skills treat a glossary as explanatory input, never as authority to manufacture mechanisms. `review-fixpoint` does not apply another glossary or prose pass. | Each consumer named in the routing table retains its established responsibility. | S4 | D2 consumer-link and ownership check; M7 composed-consumer scenario |
| GL8 | **Reuse the clear-writing evidence model.** Static repository checks establish package shape, links, absence of a standalone glossary skill, and absence of copied workflow. Controlled model trials evaluate discovery, consent, source fidelity, term use, and update behavior. Add glossary-present and glossary-absent source packets to CTW's existing model and human scenarios instead of creating a second capability suite. Entry counts, lookup time, prompt tokens, edit size, and glossary size remain observational unless a future protocol supplies a baseline and threshold. | CTW's evaluation runner and human pilot remain evidence owners. Repository validation owns static checks. | S5 | D1-D2 deterministic checks; M1-M7 controlled model evidence; CTW V11 human evidence |

## Placement and discovery protocol

This section implements GL2; it does not create another placement policy.

1. Read explicit task instructions and project guidance for a glossary path or
   other terminology authority.
2. If one authoritative glossary is named, read only the entries relevant to
   the artifact and its prerequisites.
3. If none exists and glossary-aware work is applicable, stop before creating a
   file or persisting a new term. Ask whether the glossary should live inside
   the project or at a look-aside location.
4. For a project-local choice, propose `docs/glossary.md` only when it fits the
   repository's documentation layout; otherwise ask for or infer the local path
   from established repository convention.
5. For a look-aside choice, obtain the exact location and scope from the user.
   Do not invent a global path or write a pointer into project guidance without
   separate authorization.
6. If the user declines glossary creation, continue with local definitions and
   record no implied future obligation.

Discovery is source preparation, not an extra prose pass. A specialized leaf
skill may perform it before drafting and still invoke `clear-technical-writing`
only once after its substantive artifact is complete.

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
| `clear-technical-writing` | Add `references/project-glossaries.md`; perform GL2 discovery when it is the direct leaf owner, use relevant entries as sources, and run the one CTW5 terminology check during the final pass. |
| `technical-note-series` | Discover the selected glossary before building teaching vocabulary. Keep the guide authoritative for prerequisite order and series navigation; link project-wide definitions and own only series-specific teaching explanations. |
| `project-architecture-doc` | Treat the selected glossary as an explanatory source. Verify definitions against code and architecture authorities, and route durable new project terms through GL2 and GL6. |
| `add-architectural-guidances` | Preserve established glossary terms when available, but keep target policy self-contained and do not make a look-aside glossary an undeclared runtime dependency. |
| `evidence-efficient-review` | Use a glossary to interpret terminology, then verify semantic claims against their owners. Report only materially ambiguous, contradictory, or authority-stealing terminology; do not turn wording preference into a finding. Its review artifact receives the existing single clear-writing pass. |
| `supervised-implementer-loop` | Use glossary definitions as explanatory context, not as permission to create fields, states, limits, or components. Include an authorized glossary edit in a slice only when accepted semantic work changed the term. |
| `review-fixpoint` | Require or report the leaf owner's glossary-aware prose pass when applicable; do not perform a second pass or copy this protocol. |

The general `writing` skill remains outside this repository. When it owns a
general prose artifact, it may consume a user-supplied glossary as source
material, but this plan does not add a dependency or second pass to that skill.

## Ordered implementation slices

### S1 — Extend the planned clear-writing package

Implement GL1-GL2 by adding the one-level glossary reference and a concise
entrypoint instruction to discover placement. Do not create a new skill
directory. Keep the location question out of unrelated writing tasks for which
durable project terminology is not applicable.

### S2 — Implement source use and entry guidance

Implement GL3-GL5 in the reference. Preserve the distinction between glossary
explanation and semantic truth, local prerequisite explanation and durable
entry, and necessary project terminology and ordinary domain vocabulary.

### S3 — Make glossary changes dependency-aware

Implement GL6 together with CTW8. Cover a changed semantic source, an obsolete
alias, and a local artifact whose wording depends on the old definition. Keep
unauthorized glossary updates as reported candidates rather than writes.

### S4 — Integrate only the owning consumer boundaries

Implement GL1, GL5-GL7 through concise links or invocation notes in the consumer
table. Do not copy the location protocol or entry checklist. Preserve the
single-pass ownership established by CTW2.

### S5 — Extend existing validation rather than creating another suite

Implement GL8. Add D1-D2 to CTW's deterministic package checks, M1-M7 to its
controlled model source-packet suite, and glossary-present and glossary-absent
conditions to the existing V11 pilot. Keep all external identity, failure,
freshness, and non-reuse rules under CTW10.

## Scenario portfolio

M1-M7 use CTW's shared capture record and output scorer. Each run records the
exact skill revision, model/runtime identity, outer instructions, project
guidance, glossary or absence evidence, source-packet hash, authorization
boundary, output, and first failed GL contract. Private reasoning is not
captured or inferred.

| Evidence | Class | Observable result and localization |
|---|---|---|
| D1 | Deterministic repository gate | The clear-writing package contains one linked glossary reference, valid relative links, and no standalone glossary skill or duplicate procedure. Failure localizes to GL1 or package authoring. |
| D2 | Deterministic repository gate | Each changed consumer contains at most one concise glossary-authority link at its owning boundary and retains its prior semantic responsibility. Failure localizes to GL7 and the named consumer. |
| M1 | Controlled model behavior | With no glossary and no placement instruction, the agent asks project-local versus look-aside before creating or persisting anything. It does not choose `docs/glossary.md` automatically. Failure localizes to GL2. |
| M2 | Controlled model behavior | Explicit project guidance selects one glossary; two unresolved plausible sources produce a location-authority question rather than an automatic merge. Failure localizes to GL2. |
| M3 | Controlled model behavior | A stale glossary conflicts with code or an accepted contract. The artifact preserves semantic truth and reports the glossary conflict instead of rewriting the fact to match the entry. Failure localizes to GL3. |
| M4 | Controlled model behavior | A necessary project concept receives one plain entry and aliases redirect to it; an ordinary engineering term does not receive an entry. No paragraph cap or italicization rule decides acceptance. Failure localizes to GL4. |
| M5 | Controlled model behavior | Existing glossary terms remain consistent, but an unfamiliar reader still receives a local prerequisite explanation. When glossary creation is declined, the artifact is clear and no file is created. Failure localizes to GL5. |
| M6 | Controlled model behavior | An authorized semantic change updates the owning entry, aliases, and dependent prose. An unauthorized or semantically uncertain change is reported without a glossary write. Failure localizes to GL6. |
| M7 | Controlled model behavior | A technical-note guide owns teaching order, a review preserves finding semantics, and an implementation handoff does not turn a glossary label into a new mechanism. Each artifact receives no more than one final prose pass. Failure localizes to GL7 or the named consumer. |

## Evidence and completion

D1-D2 are deterministic package gates on the exact accepted revision. They can
prove package composition and static ownership, not that a model follows the
instructions.

M1-M7 are controlled model compatibility evidence under CTW10. Runtime or
configuration unavailability leaves glossary behavior `capability-unconfirmed`;
a valid output that violates a predeclared GL rubric is
`product-contract-failure`. Initial evidence is non-reusable under the CTW
plan's event-bounded rule.

Glossary-conditioned artifacts join the existing CTW V11 paired human pilot.
They do not create a separate claim that glossaries improve comprehension. The
pilot's existing factual-preservation and comprehension thresholds decide the
combined clear-writing capability.

Counts of entries, prompt tokens, lookup time, prose length, and edit size are
observational. No exact entry-length, glossary-size, or lookup limit is a
completion gate.

This glossary integration reaches specification `deterministic-fixed-point`
only after a fresh independent review clears GL1-GL8, D1-D2, M1-M7 definitions,
the required specification cells, and all prior findings on the exact revision.
The future implementation does not reach its deterministic fixed point until
D1-D2 and the applicable CTW package gates pass. It is not `Done` until the
combined CTW model and human capabilities are confirmed. This document may
require an independent review but does not define review numbering, commits,
reviewer selection, remediation repetition, or stop mechanics.

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

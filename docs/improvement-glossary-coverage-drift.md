# Improvement Plan: Keep Selected Glossaries Aligned With Working Vocabulary

## Purpose

This note begins with a glossary-use failure observed during the Stage 2
memory-management cutover in `clojure-wasm`, then derives a bounded improvement
plan from that evidence. The correction does not create a new skill, require a
mandatory terminology pass, automatically update a glossary, or replace the
semantic owners that already decide project meaning.

The project had an explicitly selected `docs/glossary.md`, and the active
writing guidance required relevant glossary entries to be read before durable
engineering communication used or established shared terminology. Despite
that, the implementation discussion and handoffs accumulated durable project
concepts that the selected glossary did not define.

## Observed failure

A progress update described work on the "Var/code-unit/callable image." The
word *image* could plausibly mean the guest runtime, a generated Wasm module,
an embedded build artifact, a Store-rotation snapshot, or a copied checkpoint.
The intended meaning was the encoder-authored WebAssembly module instantiated
as the guest runtime, but that distinction was explained only after the user
asked.

The subsequent glossary lookup found no entry for *runtime image*. A broader
comparison found that the gap was not isolated. The current cutover documents
also rely on terms including:

- typed kernel;
- Wasm-GC object graph and copying collector;
- direct cutover and legacy tagged runtime;
- shadow state and host semantic mirror;
- Var, callable, code unit, and staged publication;
- callable table, external lease, and linear resource;
- execution-generation Store rotation; and
- phase or capability token.

Some of these words occur inside the existing glossary's descriptions, but
occurrence is not definition. The glossary defined only the three top-level
components, semantic ownership, and physical module boundaries. It did not
state the identities, aliases, distinctions, lifetimes, or ownership needed to
interpret the newer vocabulary consistently.

## Evidence in the project artifacts

The mismatch is visible without relying on the conversational example alone.
The M2 direct-cutover map says that its terminology follows the project
glossary, then uses *encoder-authored image*, *production candidate*, *Wasm-GC
object graph*, *linear resource*, *external lease*, *typed exports*, *shadow
graph*, and *host semantic mirror*. The hybrid-memory interlude gives these
concepts architectural meaning and ownership, but the selected glossary did
not carry that meaning into a shared terminology source.

The glossary's declared scope also referred specifically to the Stage 2
modularization interlude and architecture notes. The work later moved into a
memory-management interlude and a direct implementation cutover while the same
glossary selection continued to be reused. Nothing in the observed interaction
made the resulting scope mismatch visible before an ambiguous term caused a
question.

## Why local explanation was insufficient

The phrase was understandable after a local explanation, so the immediate
communication failure was recoverable. That repair did not answer whether
later handoffs should use *runtime image*, *production image*, *guest image*,
or *artifact*, nor did it distinguish the runtime image from a rotation
snapshot or generated callable module for other readers and agents.

This matters because the cutover relies on exact ownership distinctions. The
image composer must not become a semantic owner. The callable table is an
engine resource, not the Var registry. A public lease is not a host-held
Wasm-GC reference. A linear resource is not a second general object heap.
Without shared definitions, compact handoffs can preserve the same words while
silently changing these relationships.

## Why the existing guidance did not expose the gap

The glossary guidance successfully addresses placement, authorization,
semantic-source precedence, entry shape, local explanation, and dependency-
aware updates. The observed failure occurred after those questions appeared
settled: an existing glossary had already been selected, and no explicit
definition was being revised.

The working vocabulary then evolved across design documents, implementation
maps, agent assignments, evidence artifacts, and progress summaries. Individual
communications could read the entries that existed and still introduce or
reuse concepts absent from the glossary. Local first-use explanations reduced
the immediate cost of unfamiliar language but did not make the accumulated
coverage drift visible.

The observation does not establish whether the problem lies in glossary scope,
consumer routing, long-running package handoff, term-candidate recognition, or
the boundary between transient conversation and durable engineering
communication. It establishes only that selecting and consulting a glossary
did not keep the project's shared vocabulary aligned with it.

## Distinctions preserved by this observation

- A glossary need not define ordinary Rust, Clojure, WebAssembly, or Wasmtime
  vocabulary merely because it appears in a project artifact.
- Not every migration label or checkpoint identifier is a durable project
  concept. Terms such as *production candidate*, *CP1*, and *owner-level
  package* may remain local workflow language.
- A missing glossary entry does not invalidate an accepted semantic source.
  Code, architecture, and accepted contracts remain authoritative for meaning.
- Local explanation remains necessary for readers who cannot be expected to
  consult the glossary.
- Automatically persisting every newly used noun could create a larger and less
  useful glossary without preventing semantic drift.
- The observed ambiguity does not by itself determine whether *image* should
  be replaced, qualified, or retained as an alias.

## Questions left open

- When does vocabulary introduced during a long-running package become a
  candidate for the selected project glossary?
- How should a reused glossary selection expose that its declared scope no
  longer covers the active architecture work?
- Which artifact or workflow boundary should notice that a durable term has a
  semantic source but no glossary entry?
- How should handoffs distinguish an undefined project concept from ordinary
  domain vocabulary that needs only a local explanation?
- When several near-synonyms are already in use, what evidence establishes the
  preferred term without allowing prose to decide architecture?
- How should glossary coverage be evaluated without turning every writing task
  into an exhaustive repository terminology audit?
- What evidence would show that glossary use remains effective across multiple
  agents and implementation checkpoints rather than only within one final
  prose artifact?

The design below resolves these questions by extending the existing shared
glossary authority and carrying one bounded coverage disposition through
workflow boundaries that already transport glossary state.

## Behavioral authority

This plan extends the accepted [project-glossary contract](improvement-glossary.md).
GL1-GL8 remain authoritative for glossary placement, semantic-source
precedence, entry admission, authorized updates, consumer ownership, and
evidence classes. The GCD1-GCD6 matrix below is the sole authority for noticing
and carrying coverage drift. Other sections reference those IDs without
redefining them.

```text
Goal ID: GCD-1
Behavioral goal: Collaborators keep a selected project glossary aligned with
  durable vocabulary as a work package evolves, without automatic writes or
  exhaustive terminology audits.
Direct scenario: Active architecture work introduces a semantically sourced
  project concept outside the selected glossary's declared coverage. At an
  existing scope-change, assignment, correction, handoff, or final-artifact
  boundary, the responsible leaf surfaces the term candidate and scope
  mismatch. Later consumers preserve the term-to-source relationship until an
  authorized owner updates the glossary or keeps the explanation local.
Product authority: The user through acceptance of this plan.
Owning contract: GCD1-GCD6 in this document.
Behavioral status: unavailable
```

The status is `unavailable` because current guidance resolves and reads a
selected glossary but does not require any existing boundary to expose a
material term that the glossary does not define or a declared scope that no
longer covers the active work.

The `clojure-wasm` glossary has since been expanded to define the concepts in
the observation. That local repair shows that the concepts had accepted
semantic sources and were suitable glossary material; it does not supply a
reusable workflow for noticing the next scope or vocabulary mismatch.

## Scope and non-goals

The correction applies only when a selected glossary is already in use and a
durable artifact or long-running package uses or establishes shared project
terminology. It examines the material terms already needed for that artifact,
assignment, correction, or handoff. It does not discover vocabulary by
scanning the repository.

Explicit non-goals are:

- defining ordinary language, technology vocabulary, workflow labels, or
  checkpoint identifiers merely because they occur in project artifacts;
- persisting every new noun or local shorthand;
- replacing local first-use explanations with a glossary link;
- changing semantic truth to agree with glossary prose;
- choosing a preferred term when accepted sources do not resolve competing
  aliases;
- creating a glossary manager, terminology reviewer, durable candidate
  database, or second prose pass;
- adding term-count, glossary-size, document-count, or elapsed-time thresholds;
  and
- requiring a whole-repository terminology audit at package acceptance.

## Authoritative contract-and-evidence matrix

| ID | Observable contract | Semantic owner and public composition | Delivery package | Named evidence |
|---|---|---|---|---|
| GCD1 | **Expose a selected glossary's scope fit.** When active work materially changes scope, or a selected glossary is reused at an existing durable-artifact or package boundary, compare the glossary's declared scope with the active work. If the glossary is still the selected terminology source but its declaration does not cover the active work, report that mismatch. Do not deselect it, restart placement discovery, or infer edit authority. A glossary without an explicit scope remains usable; material uncovered terms are handled by GCD2 rather than by inventing a scope. | The selected glossary owns its declared terminology scope. The active artifact or package owner knows the work scope and reports the comparison at its existing boundary. | P1 | D1, M1-M2 |
| GCD2 | **Recognize candidates from material vocabulary.** At the same existing boundary, inspect only shared terms material to the current artifact or handoff. Report a candidate when a term names a durable project distinction, has an accepted semantic source, and is absent from the selected glossary or materially narrower, broader, or differently aliased there. Treat ordinary domain vocabulary and local workflow labels as local explanation unless project-specific meaning makes them candidates. Mere occurrence is not a definition. | The artifact's factual owner identifies material vocabulary and semantic sources. GL4 remains the authority for whether a candidate deserves an entry. | P1 | D1-D2, M1-M2 |
| GCD3 | **Carry evidence without deciding terminology or architecture.** A reported candidate identifies the used term, its semantic source, the project-specific distinction or ambiguity, and any unresolved preferred-term or alias question. It may also name the glossary-scope mismatch that exposed it. The report does not create a term, alter a contract, or translate a label into a field, state, limit, component, or ownership decision. | Technical owners retain meaning and architecture. The selected glossary retains preferred-term and alias authority only after an authorized decision. | P1 | D1-D2, M1-M2 |
| GCD4 | **Preserve coverage continuity through existing workflow boundaries.** `complex-work` carries selected scope fit and unresolved candidates between leaf units and reports them at package handoff. `evidence-efficient-review` includes material inherited candidates in its neutral dossier and verifies them against semantic sources when they affect reviewed terminology. `supervised-implementer-loop` carries them through the work package, assignment, corrections, and handoff. `review-fixpoint` transfers the same state between Tick and Tock without applying another glossary or prose pass. Each consumer records only changed or still-material dispositions; none runs an independent repository audit. | Each workflow retains its existing package, review, implementation, or phase authority. The shared project-glossary reference owns the coverage process. | P2 | D1-D2, M2 |
| GCD5 | **Resolve a candidate only at the existing authorized boundary.** An authorized glossary update still requires GL4's useful-project-distinction decision and GL6's accepted meaning, selected location, documentation scope, and task edit authority. Otherwise keep the candidate visible, explain it locally, and preserve unresolved alias uncertainty. After an authorized update, revalidate affected in-scope prose and report known out-of-scope dependents under GL6; do not retain a parallel candidate authority. | GL4 owns admission, GL6 owns bounded mutation and dependency revalidation, and the semantic owner approves meaning. | P1 | D1-D2, M1-M2 |
| GCD6 | **Demonstrate bounded coverage behavior without promoting model behavior to a deterministic gate.** Deterministic source and package checks verify one shared owner, linked consumer boundaries, valid fixtures, and absence of a standalone scanner or candidate store. The existing project-glossary and agent-handoff model cases exercise scope mismatch, candidate recognition, semantic-source continuity, local explanation, and authorized or unresolved disposition. Actual model trials remain external compatibility evidence; vocabulary counts and timing remain observational. | Repository validation owns mechanical conformance. The existing clear-writing study and independent reviewer own model-capability evidence. | P2 | D1-D2, M1-M2 |

## Supporting design and smallest faithful alternative

The current aggregate already has one shared glossary reference, direct
consumer skills, selected-source state, term-to-source mappings, handoffs, a
four-case model study, and a deterministic package validator. The smallest
faithful correction extends that shared reference with one bounded coverage
operation and carries its result through boundaries that already transport
glossary state.

| Mechanism | Behavior served | Necessity and lifetime | Evidence |
|---|---|---|---|
| Material coverage check in `project-glossaries.md` | GCD1-GCD3, GCD5; direct-scenario detection | It compares only the active scope and terms already needed at an existing boundary. Its result lasts only while the scope, semantic source, and glossary entry remain current. | D1-D2, M1 |
| Unresolved candidate and scope-fit handoff fields | GCD3-GCD4; direct-scenario continuity | Existing selected-source handoffs cannot represent known missing coverage. The fields remain explanatory evidence and disappear when resolved or no longer material. | D1-D2, M2 |
| Existing model cases extended with drift examples | GCD6; behavioral evidence | This reuses the accepted evidence topology and adds no production state. | D2, M1-M2 |

A repository scanner, candidate ledger, automatic glossary mutation, mandatory
terminology phase, or dedicated glossary agent would add owners, durable state,
coordination, and mechanism-coupled evidence without improving the accepted
scenario. The selected design therefore retains the current aggregate and adds
only bounded comparison and continuity at established boundaries.

No defensive product mechanism is proposed. Economic actionability is not
applicable: the plan corrects an observed communication contract through
workflow guidance and existing evidence, without lasting runtime machinery.

## Reviewed delivery plan

### P1 — Establish bounded coverage at the shared owner

Implement GCD1-GCD3 and GCD5 in
`skills/clear-technical-writing/references/project-glossaries.md`. Link the
operation from the existing final prose path only as needed for discoverability.
Strengthen the `project-glossary-use` fixture so one selected glossary has a
scope that predates the active architecture work and the artifact uses a
material, semantically sourced project concept missing from it.

P1 is a useful stopping point: any direct clear-writing consumer can surface a
coverage mismatch and candidate without waiting for workflow integration. It
keeps one semantic owner and one reason to change: selected-glossary use. The
reference remains the selected source boundary because it already owns
resolution, term use, and authorized updates; no new responsibility is placed
in `SKILL.md` beyond routing to that reference.

Focused acceptance: the clear-writing package validator and self-test pass;
the fixture distinguishes an uncovered project concept from ordinary domain
vocabulary and cannot be satisfied by an automatic glossary write.

### P2 — Preserve the disposition across coordinated work

Implement GCD4 and GCD6 at the existing package, review, implementation, and
phase state-transfer boundaries. `complex-work` does not yet carry glossary
state: at package establishment it resolves or consumes the selected glossary
identity or explicit opt-out through the shared project-glossary authority,
records scope fit and material unresolved candidates, passes only changed or
still-material dispositions to affected leaf units, and reports them at package
handoff. `evidence-efficient-review`, `supervised-implementer-loop`, and
`review-fixpoint` extend their existing glossary-state boundaries without
copying the coverage operation. Strengthen the `agent-handoff` fixture and
validation-scenario description so an unresolved candidate and its semantic
source cross at least one assignment or handoff and remain subordinate to the
technical owner.

P2 depends on accepted P1 vocabulary and behavior. It is a separate useful
package because it makes the direct scenario survive a multi-owner workflow;
combining it with P1 would postpone acceptance of the shared owner, while
splitting individual consumers would leave a partial continuity contract. Each
consumer edit has one cohesion reason: preserve the already-owned glossary
state across that consumer's existing boundary.

Focused acceptance: all affected skills pass the skill-package validator; the
clear-writing package validator and self-test pass; source inspection maps each
GCD4 consumer to its existing boundary and finds no copied coverage workflow,
standalone skill, scanner, candidate store, or second prose pass.

After P2, run one package-level whitespace check and independently review the
complete implementation against GCD1-GCD6. Do not credit package acceptance or
focused checks as a deterministic fixed point; the subsequent independent Tick
owns that decision.

## Delivery-package records

| Field | P1 — Shared coverage owner | P2 — Coordinated continuity |
|---|---|---|
| Package ID and useful outcome | `P1`: a direct clear-writing consumer can expose selected-glossary scope drift and a semantically sourced candidate without automatic persistence. | `P2`: a long-running package preserves the selected source, scope fit, and unresolved candidates across its existing coordination boundaries. |
| Establishing contract IDs | GCD1-GCD3, GCD5 | GCD4, GCD6 |
| Semantic owner and physical boundary | The shared project-glossary authority remains the semantic owner; its existing reference and the `project-glossary-use` fixture are the physical surfaces. | The shared reference retains semantic ownership. `complex-work` acquires and reports the disposition at package establishment and handoff; the other three workflows extend their existing glossary-state transfer points. The `agent-handoff` fixture and validation-scenario description exercise the composition. |
| Prerequisites and dependency order | Accepted GL1-GL6 and CTW terminology/final-pass authority. | Accepted P1 behavior and vocabulary, plus existing GL7 consumer ownership and GL8 evidence topology. |
| State and lifetime | The scope comparison and candidate are explanatory state for the current active scope, semantic source, and artifact. They are not a durable store and cease to be material after authorized resolution, source invalidation, or a scope change that removes the term. | The same explanatory state crosses only affected assignments, corrections, reviews, and handoffs. It remains current while its glossary selection, active scope, semantic source, and materiality are unchanged; it never becomes a second glossary or candidate ledger. |
| Transaction and recovery closure | No transactional mutation or recovery mechanism applies. An unauthorized or unresolved candidate leaves the glossary untouched and receives a local explanation. Authorized mutation and dependent-prose recovery remain wholly under GL6. | No transaction, poison state, or durable recovery mechanism applies. A missing or stale disposition blocks the affected handoff; recovery re-resolves the selected source and rechecks only the material terms at the next existing boundary. Resolved or no-longer-material candidates disappear rather than being retained in a parallel ledger. |
| Public, skill, and ABI surface | The clear-writing skill reaches the shared reference before a final durable artifact; no API, ABI, or runtime surface changes. | Four workflow skill entrypoints and their existing work-package, dossier, assignment/correction, Tick/Tock, and final-handoff compositions change. No API, ABI, runtime component, or second prose pass is added. |
| Focused evidence | D1 owner/source inspection, D2 package validator and self-test, and M1 when separately authorized. | D1 consumer-boundary inspection, D2 package validator and self-test, and M2 when separately authorized. Skill-package validation covers every changed skill. |
| Safe deferred work | Multi-workflow continuity remains absent until P2; that does not weaken P1's complete direct-artifact behavior. External model evidence may remain capability-unconfirmed. | A fresh external model trial remains absent without separate authorization. No glossary edit is required merely to accept the workflow implementation. |
| Causal split/combine and acceptance-cost decision | Keep the shared authority and its direct fixture together so the first package closes recognition, local explanation, and authorization at one owner. Accept with focused package checks; defer the whole-scope Tick until both packages compose. | Keep all coordinated consumers together because partial propagation would not close GCD4. Separate P2 from P1 so the shared owner is accepted before its result is transported. Run the package validator once after fixture changes and the independent whole-scope Tick once after P2. |

## Pre-edit realization dispositions

| Contract | Ownership and capability | Required information and lifetime | Transaction and recovery | Scenario and assertions | Design dependencies |
|---|---|---|---|---|---|
| GCD1 | The shared reference defines the comparison; the active artifact or package owner supplies current scope. | Selected source or opt-out, declared glossary scope when present, and active work scope; the comparison remains current only while these inputs do. | No mutation applies. Missing declared scope does not fail selection; GCD2 handles material uncovered terms. | D1 inspects the owner and boundary; M1 observes a reported mismatch without renewed placement discovery. | GL2 selection and placement are retained; P1 strengthens only selected-source reuse. |
| GCD2 | The factual artifact owner selects only material shared terms and their accepted semantic sources; GL4 decides admission. | Used term, project-specific distinction, semantic source, glossary entry or absence, and artifact/handoff materiality. | No repository audit or candidate persistence applies. If source or materiality becomes stale, re-evaluate at the next existing boundary. | D1-D2 distinguish a durable uncovered concept from ordinary domain language; M1 checks candidate recognition and local explanation. | GL3-GL5 are retained; the fixture is strengthened rather than replaced. |
| GCD3 | Technical owners retain meaning; the selected glossary can decide preferred terms and aliases only through existing authority. | Used term, semantic source, ambiguity or distinction, scope mismatch when relevant, and unresolved alias status. The disposition ends when resolved or no longer material. | No transaction applies. An unresolved disposition remains explanatory handoff state and cannot authorize a mechanism. | D1-D2 inspect required fields and negative constraints; M1-M2 observe semantic-source continuity and no invented design. | Behavioral-design and architecture authorities outrank prose; no new glossary entry is planned in this repository. |
| GCD4 | `complex-work` owns package continuity; EER, SIL, and review-fixpoint retain review, implementation, and phase transfer respectively. | Selected source or opt-out, active scope fit, and changed or still-material candidate fields cross only affected boundaries. | A missing/stale disposition blocks that handoff. Re-resolve through the shared authority; do not reconstruct a durable history or run a whole-repository audit. | D1 maps every named boundary; D2 validates the handoff fixture; M2 localizes package establishment, assignment, correction, review, or handoff loss. | P2 consumes accepted P1. GL7 ownership and each workflow's existing contract remain unchanged. |
| GCD5 | GL4 admits useful distinctions; GL6 owns authorized mutation and dependency revalidation. | Accepted meaning, selected location and documentation scope, task edit authority, aliases, and affected in-scope or known out-of-scope prose. | Unauthorized or uncertain writes abort without mutation and retain local explanation. Authorized updates use GL6's existing dependency-aware process. | D1-D2 verify the conditional branch; M1 observes no automatic write and preservation of uncertainty. | GL4 and GL6 are retained without a second candidate authority. |
| GCD6 | Repository validation owns mechanics; the current CTW study and blinded reviewer own external capability evidence. | Exact skill-package revision, fixture source-packet hash, generator model and reasoning effort, runtime, outer instruction, exposed settings, tool/context configuration, and blinded-review protocol. | Deterministic failures block package acceptance. External evidence is not retried or reused across a materially different identity; absence leaves capability unconfirmed. | D1-D2 remain deterministic; M1-M2 are strengthened external cases with independent localization. | GL8 and CTW10 evidence classes remain authoritative; prior trials are historical, not reusable for the revised identity. |

## Scenario portfolio and evidence status

| Scenario | Contracts | Observable invariant | Evidence class | Localization signal |
|---|---|---|---|---|
| Selected glossary outlives its declared scope | GCD1-GCD3, GCD5-GCD6 | The output identifies one material uncovered concept and semantic source, explains it locally, and neither invents a preferred alias nor writes the glossary without authority. | M1: external compatibility | Failure localizes to scope fit, candidate recognition, semantic precedence, or authorization. |
| Candidate survives a coordinated handoff | GCD3-GCD4, GCD6 | The receiver gets selected-source identity, scope fit, the unresolved term and semantic source, and the distinction that remains unresolved; no consumer creates a mechanism or second prose pass from the label. | M2: external compatibility | Failure localizes to package establishment, assignment, correction, handoff, or final reporting. |
| Shared owner and bounded consumers | GCD1-GCD6 | The shared reference owns the operation; consumers carry only material dispositions at existing boundaries; fixtures and links are valid. | D1: deterministic release gate | File and boundary inspection identify missing ownership, copied workflow, or unauthorized machinery. |
| Existing evidence package remains well formed | GCD2-GCD6 | The four-case manifest and capture schema validate, including the revised glossary and handoff cases. | D2: deterministic release gate | The existing validator identifies the malformed package or fixture. |

M1-M2 have no current evidence for the revised cases, so GCD model capability
is `capability-unconfirmed`. Their evidence identity consists of the exact
skill-package revision, fixture source-packet hash, generator model and
reasoning effort, runtime, outer instruction, exposed settings, tool/context
configuration, and blinded-review protocol. Evidence with a materially
different identity is stale and is not reused; elapsed age alone does not
invalidate an otherwise matching record. The prior CTW four-case
product-contract failure remains historical evidence but is not reusable for
the revised GCD identity. A new trial requires separate authorization and a
newly commissioned protocol.

No human-comprehension claim is part of this plan. Vocabulary counts, glossary
size, lookup latency, prompt tokens, prose length, and edit size are
observational and have no acceptance power.

## Test disposition and acceptance

The existing `project-glossary-use` and `agent-handoff` model cases are
`strengthen`: their stable purposes remain, while their source packets and
review questions gain coverage-drift behavior. The clear-writing validator and
self-test are `retain`; they continue to verify package shape rather than prose
quality. No existing test is replaced or deleted, and no mechanism-specific
test is added.

Implementation-plan acceptance requires:

- every GCD row maps to exactly one complete delivery package and every package
  establishes at least one complete row;
- P1 and P2 each leave a correct, useful behavior if later work stops;
- the complete package records and pre-edit realization dispositions are
  cleared;
- the shared glossary reference remains the only coverage-process owner;
- consumer changes are limited to the named state-transfer and acceptance
  boundaries; and
- behavioral, mechanism, and external-capability statuses remain separate.

After implementation, `deterministic-fixed-point` additionally requires all
deterministic gates to pass on the exact reviewed revision and an independent
whole-scope Tick to find no P0-P3 defect or required unknown.

No commit, push, global skill installation, external model trial, or mutation
outside this repository is authorized by this plan.

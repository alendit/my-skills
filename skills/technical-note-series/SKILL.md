---
name: technical-note-series
description: >-
  Write, rewrite, or extend a source-grounded educational technical-note series
  for experienced software developers who are new to a project and its
  languages, runtimes, compilers, or other foundations. Use for coherent
  architecture and implementation notes with an open-ended reader journey. Do
  not use for API reference, changelogs, implementation plans, release notes,
  or marketing copy.
---

# Technical Note Series

Produce a source-backed series that teaches a project through observable
behavior and progressively refined mental models. Assume strong general
software-engineering experience, but no project or specialist-technology
background. Treat each request as a publication pass over an evolving series,
not a permanently closed account.

This skill owns repository research, reader journey, series structure, drafting,
cross-note coherence, and documentation-specific validation. The caller owns
scope, destination, authorization, commit policy, and explicit reviewer/model
constraints. `$evidence-efficient-review` owns review mechanics;
`$review-fixpoint` owns review numbering, commits, remediation repetition,
reviewer selection, and stop mechanics when the caller requests that workflow.

## Establish The Publication Pass

Before drafting:

1. Identify audience, learning outcomes, described revision, selected note
   scope, stable filename/link requirements, validation expectations, and
   explicit non-goals. Recover discoverable facts before asking questions.
2. Inspect repository status and preserve unrelated work.
3. Read
   [references/research-and-reader-journey.md](references/research-and-reader-journey.md)
   completely. Build source evidence, verify one running example, order concepts
   by prerequisite, and update the guide before individual notes.
4. Make the guide the single authority only for series-owned reading paths,
   running-example identity, series-only terms, reader-specific introduction
   order and first-use explanations, series scope, and navigation. Notes own
   distinct reader questions and link to guide-owned material. When glossary
   state selects a source, link project-wide terms to it instead of maintaining
   a competing canonical definition. Otherwise keep necessary definitions local
   without requiring glossary access or persistence. When a project or feature
   goal already has a normative contract, link stable contract IDs to its owning
   source. Keep plain-language goal and architecture orientation explicitly
   explanatory, never a second acceptance authority.
5. Keep the foundational path compact, published extensions evidence-backed,
   and future candidates explicitly provisional. The latest published note is
   a frontier, not the end of the series.

## Draft And Reconcile The Series

Read
[references/drafting-and-coherence.md](references/drafting-and-coherence.md)
before writing. Teach unfamiliar technology only when the reader needs it,
explain semantic owners and crossing data, reuse the verified example, and
isolate volatile private implementation detail from durable concepts.

After each note, reconcile the complete selected series against the guide.
When a glossary is selected, replace competing project-wide definitions with
links. Otherwise preserve necessary local definitions without presenting them
as a durable project-wide authority. Remove duplicate series-only definitions
and compensating navigation; repair the owning guide or note once and replace
copies with links. Preserve current facts, rationale, limitations, non-goals,
and future direction as distinct claim classes.

Once the reader journey, running example, ownership, series scope, and
navigation are coherent, apply one final
[clear technical writing pass](../clear-technical-writing/SKILL.md). Preserve
the accepted teaching decisions and do not add another prose pass in an outer
review workflow.

## Validate And Review

Read
[references/validation-and-review.md](references/validation-and-review.md)
completely. Validate claims, code references, the running example, links,
diagrams, and repository scope before review.

After validation, require a fresh independent `$evidence-efficient-review` for
every publication pass. Supply one normalized matrix for the audience,
learning, factual accuracy, boundary ownership, example, time/certainty,
coherence, traceability, scope, and navigation cells defined in the reference.
Consume its evidence classes and coverage statuses.

If any required publication cell is `candidate` or `unknown`, repair its owning
guide or note, rerun affected validation, and continue through
`$review-fixpoint` until a fresh review clears every required cell. This skill
supplies the publication contract; `$review-fixpoint` owns review numbering,
commits, reviewer selection, remediation repetition, and stop mechanics. Keep
those mechanics out of the guide and notes. A cleared publication pass does not
declare the open-ended series permanently complete.

If specialized validation or a review correction changes a source fact,
conclusion, or dependent prose after the clear-writing pass, apply
[revision-after-change](../clear-technical-writing/references/revision-after-change.md)
to the affected complete unit before the next review. This is leaf-artifact
revalidation, not a recursive style review or a second outer prose pass.

## Operating Rules

- Ground current implementation claims in current source, executable config,
  and tests; use authoritative external sources only for underlying technology.
- Mark illustrative pseudocode, diagrams, or simplified representations and
  keep their relationships exact.
- Never claim generality, portability, safety, authority, or isolation beyond
  the named owner and evidence.
- Preserve historical files as historical evidence when applicable; do not
  silently rewrite history as current behavior.
- Keep private fields, versions, counts, and paths in implementation maps or an
  appendix unless they are necessary to teach a durable contract.
- Do not turn the series into an API inventory, source walkthrough, roadmap,
  task list, changelog, or generic technology textbook.
- Do not claim independent review, verification, or observed output that did
  not occur.

## Handoff

Report the selected files, guide-owned reading paths, latest frontier, verified
running example, major ownership boundaries, factual and mechanical checks,
review actually performed, open-ended extension posture, remaining uncertainty,
and unrelated repository state. Do not commit unless requested; when authorized,
stage only the selected documentation scope.

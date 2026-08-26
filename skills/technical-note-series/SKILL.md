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
4. Make the guide the single authority for shared definitions, running-example
   identity, reading paths, scope, and navigation. Notes own distinct reader
   questions and link to guide-owned material instead of recreating it.
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
Remove duplicate definitions and compensating navigation; repair the owning
guide or note once and replace copies with links. Preserve current facts,
rationale, limitations, non-goals, and future direction as distinct claim
classes.

## Validate And Review

Read
[references/validation-and-review.md](references/validation-and-review.md)
completely. Validate claims, code references, the running example, links,
diagrams, and repository scope before review.

For review, supply `$evidence-efficient-review` with one normalized matrix for
the audience, learning, factual accuracy, boundary ownership, example,
time/certainty, coherence, traceability, scope, and navigation cells defined in
the reference. Consume its evidence classes and coverage statuses. Do not embed
a bespoke fixpoint protocol in the guide or notes.

If the caller requests iterative review to fixed point, hand the validated
series and documentation cells to `$review-fixpoint`. This skill supplies the
publication contract, not general Tick/Tock mechanics. A cleared publication
pass does not declare the open-ended series permanently complete.

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

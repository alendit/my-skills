---
name: technical-note-series
description: >-
  Write, revise, or extend a source-grounded educational technical-note series
  for experienced developers new to a project and its underlying technology.
  Use for a coherent reader journey, not API reference, changelogs, plans,
  release notes, or marketing copy.
---

# Technical Note Series

Teach a project through observable behavior and progressively refined mental
models. Assume general engineering experience, but no project or specialist
background. Each request is a publication pass over an evolving series.
The caller owns scope, destination, authorization, and reviewer constraints.

## 1. Establish The Publication Pass

Recover audience, learning outcomes, described revision, selected notes, stable
filenames/links, validation expectations, and non-goals. Inspect repository
status and preserve unrelated work.

Use [research and reader journey](references/research-and-reader-journey.md)
to build source evidence, verify a running example, and order concepts by
prerequisite. Update the guide before individual notes. It owns series reading
paths, example identity, and introduction order; link existing project terms
and normative contracts to their owners rather than redefining them.

## 2. Draft And Reconcile

Use [drafting and coherence](references/drafting-and-coherence.md) for each
selected note: answer one reader question, introduce unfamiliar technology when
needed, explain semantic owners and crossing data, and reuse the verified
example. Keep volatile implementation detail separate from durable concepts.

After each note, reconcile the selected series against the guide. Repair shared
material at its owner and replace duplicates with links. Keep current facts,
rationale, limitations, non-goals, and future direction distinct. The latest
published note is a frontier; future extensions remain provisional.

After the journey, example, ownership, and navigation are coherent, apply one
[clear-writing pass](../clear-technical-writing/SKILL.md), preserving those
teaching decisions.

## 3. Validate And Independently Review

Apply [source validation](references/validation-and-review.md#validate-source-backed-claims)
to claims, code references, observed example results, links, diagrams, and scope.
Use [review-depth selection](references/validation-and-review.md#compose-with-repository-review-workflows)
to distinguish a narrow correction from a new or substantially revised
publication. Carry forward trustworthy unchanged coverage for small corrections;
new teaching structure, examples, or material factual/ownership changes require
independent EER review. Honor any explicit caller review requirement.

When independent review is activated, repair findings and required `candidate` or `unknown` cells at their
owning guide or note, rerun affected validation, and continue through
`review-fixpoint` until required publication coverage clears. That skill owns
review numbering, commits, reviewer selection, repetition, and stopping.
Keep those mechanics out of the published notes.

If a correction changes accepted facts or dependent prose after the writing
pass, use [revision after change](../clear-technical-writing/references/revision-after-change.md)
on the affected complete unit before review. Do not add an outer style rewrite.

## 4. Accept And Hand Off

Use the [publication gate and handoff](references/validation-and-review.md#apply-the-publication-gate).
Confirm that a newcomer can trace the example, unfamiliar concepts precede use,
claims match their sources, and the guide and notes form coherent reading paths.
Report selected files, verified example, validation/review actually performed,
remaining uncertainty, and the current reading frontier.

Acceptance closes this publication pass, not the series. Commit only when
requested or authorized by the caller's selected workflow, and stage only its
selected scope.

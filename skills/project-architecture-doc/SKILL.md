---
name: project-architecture-doc
description: >-
  Create, refresh, or review docs/architecture.md from current code and durable
  documentation, covering components, boundaries, and architectural direction.
---

# Project Architecture Doc

Create or update `docs/architecture.md` as a source-backed navigation map of the
repository's current architecture.

## 1. Establish Sources And Review Lens

Read applicable repository guidance and existing architecture documents. Use the
repository's architecture policy as the review lens and any accepted vision as
the target-state reference. Label vision inferred from stable documentation.
Resolve shared terminology through the [glossary authority](../clear-technical-writing/references/project-glossaries.md),
verifying meaning against code and architecture owners.

## 2. Map The Actual System

Discover source, manifests, executable configuration, module indexes, and tests.
Identify the main runtime path, core owners, adapters, persistence, external
boundaries, and architectural invariants. Use bounded outlines when top-level
paths hide meaningful subcomponents. Prefer current code/configuration when
prose conflicts, and retain the conflict for the architecture discussion.

## 3. Update The Document

Preserve accurate material and replace stale sections in place. Follow
[architecture document structure](references/architecture-doc-structure.md#required-order)
for broad-to-detailed ordering, component mapping, optional sections, navigation,
and implementation-detail placement. Use its Mermaid section when diagrams help.
Keep the story centered on components and responsibilities; link normative
feature contracts rather than duplicating them. Do not turn the document into
a plan, task list, changelog, or source inventory.

## 4. Discuss Architecture And Direction

Compare the current system with repository guidance and accepted vision. Cover
ownership, dependency direction, side effects, semantic interfaces, physical
decomposition, coupling, and testability where evidence supports a conclusion.
Separate confirmed facts from inferred gaps. When described subcomponents cannot
be recovered from source boundaries, explain that mismatch; file size alone is
not a decomposition defect.

Apply one [clear-writing pass](../clear-technical-writing/SKILL.md) after the
structure and source-backed decisions stabilize.

## 5. Verify And Report

Check the document against its [quality bar](references/architecture-doc-structure.md#quality-bar),
including stale claims, duplicate sections, source references, heading links,
and diagram syntax. Run available, inexpensive repository documentation checks.
Report what was verified and what remains uncertain. Preserve unrelated work
and keep review/fixpoint mechanics out of the architecture document.

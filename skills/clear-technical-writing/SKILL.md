---
name: clear-technical-writing
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
---

# Clear Technical Writing

Transform accepted engineering facts and decisions into prose that its intended
reader can understand and use. Preserve the source artifact's technical meaning;
this skill owns prose transformation, not behavior, scope, architecture,
findings, severity, evidence status, or workflow decisions.
User instructions, safety, accessibility, and repository policy also outrank
this prose guidance.

## Select One Prose Authority

- Use this skill when material claims depend on code, diffs, tests,
  architecture, or operational evidence, regardless of whether the result is
  public.
- Use the general `writing` skill when available for editorial, marketing,
  customer communication, or other general prose. Technical subject matter by
  itself does not select this skill. If `writing` is unavailable, let the caller
  handle general prose directly rather than using this skill as a fallback.
- Use neither skill for private notes, private reasoning, raw evidence
  collection, or a task that requests no prose artifact.

When a specialized skill owns the artifact, let that leaf owner finish the
facts and decisions, then apply this pass once. An outer workflow may require or
report the pass but must not repeat it. If the user names both prose skills,
select the one that matches the artifact's purpose and factual owner; consult
the other only for non-conflicting guidance, without a second rewrite.

For ambiguous ownership or artifact-specific routing, read
[artifact routing](references/artifact-routing.md). Before durable engineering
communication uses or establishes shared project terminology, read
[project glossaries](references/project-glossaries.md) and resolve glossary
state before drafting.

## Run One Adaptive Pass

1. **Establish source and authority.** Inspect the complete authorized source
   set and correct comparison base. Identify the factual owner and accepted
   meaning. Return to that owner when meaning is uncertain rather than choosing
   an interpretation in prose.
2. **Establish reader and purpose.** Identify the person or collaborating agent
   who will read the artifact, what they may already know, and what they must
   understand, verify, decide, or do. For a PR, commit, design, or report, use an
   uninvolved repository developer only when no more specific reader is
   recoverable.
3. **Put the answer or action first.** For a compact artifact, draft directly.
   For several dependent claims, first record a private question order and
   claim-to-evidence map. Never expose that planning as acceptance evidence.
   Use sentence-level reader-state simulation only to diagnose a passage that
   remains unclear.
4. **Draft for explicit relationships.** Prefer ordinary language and
   established project terms, explaining the concept locally when the reader
   needs it. Introduce a new term only when a distinct concept needs a stable
   name; define it once without overloading a familiar word. When a compressed
   verb hides the result, name the relevant actor, operation, object, condition,
   and consequence.
5. **Match structure and precision to the decision.** Use prose for a linear
   argument, lists for discrete items, numbered steps for order, tables for
   repeated comparable fields, and a diagram only when it materially clarifies
   a relationship. Treat punctuation and voice as contextual choices rather
   than acceptance rules. Preserve exact values for correctness boundaries,
   reproducibility, and close comparisons. Round observational values only to
   decision-relevant precision, with consistent units and the supporting
   comparison intact.
6. **Check against sources and delete.** Preserve facts, rationale,
   limitations, non-goals, unknowns, and future direction as distinct claims,
   and distinguish pre-existing evidence from evidence added by the change.
   Remove any sentence, heading, example, or measurement that does not help the
   reader understand, verify, decide, or act and does not prevent a material
   misunderstanding.
7. **Perform one fresh-reader pass.** Read from the intended reader's knowledge
   state, repair missing prerequisites or transitions, and stop after the
   artifact passes the acceptance questions below.

When a source fact or requested addition changes later, read
[revision after change](references/revision-after-change.md) and treat the edit
as dependency invalidation rather than sentence appending. Read
[examples](references/examples.md) only when an artifact's shape or level of
explanation remains unclear.

## Accept The Artifact

Confirm that:

- the answer, decision, or requested action appears where the reader needs it;
- every material claim and exact boundary still matches its semantic source;
- the reader can recover what was happening, what changes, why it is correct or
  deliberately different, what evidence matters, and what they should do;
- unfamiliar project terms receive a local explanation even when a glossary is
  linked; and
- no removable detail or second prose pass remains.

For package evaluation rather than ordinary writing, read
[validation scenarios](references/validation-scenarios.md). Read
[research rationale](references/research-rationale.md) only when explaining the
design choices; related research is not proof that this exact process works.

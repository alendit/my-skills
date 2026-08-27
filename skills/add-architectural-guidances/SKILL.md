---
name: add-architectural-guidances
description: >-
  Update a project's AGENTS.md with durable architecture guidance, design
  constraints, or architecture review questions. Use for reusable architecture
  policy, not project-specific product requirements or implementation plans.
---

# Add Architectural Guidances

Add one compact architecture policy section to the target `AGENTS.md`.

Read [references/guidance-contract.md](references/guidance-contract.md) as the
single authority for required policy and self-check content. Read
[references/architecture-decision-framework.md](references/architecture-decision-framework.md)
only when adapting the policy or explaining its rationale. Never copy the
rationale wholesale into a target file.

## Apply The Contract

1. Read the target `AGENTS.md` and preserve its style and applicable local
   terminology. Resolve shared project terminology through the
   [project-glossary authority](../clear-technical-writing/references/project-glossaries.md),
   preserve established terms when available, and verify their policy meaning
   against the guidance contract and repository authorities.
2. Find the existing architecture-policy authority. Refine it rather than
   adding a duplicate. If none exists, add `## Architecture Guidance` with
   compact `### Hard Constraints` and
   `### Required Self-Check For Design-Sensitive Changes` subsections.
3. Adapt the guidance contract into concise, self-contained instructions. Give
   target readers the local explanations they need; never make a look-aside
   glossary an undeclared runtime dependency. Keep architecture policy separate
   from product requirements, implementation plans, workflow mechanics, TDD
   rules, and commit policy unless the user explicitly requests those distinct
   concerns.
4. Keep target text repo-neutral unless local evidence supports a more precise
   term. Do not make another repository, `AGENTS.md`, or architecture document a
   required dependency.
5. Use one owning statement for each rule. Later questions may reference the
   rule's concept but must not restate it as a second normative definition.
6. After the policy contract and self-check are complete, apply one compact
   [clear technical writing pass](../clear-technical-writing/SKILL.md) without
   changing rule ownership or expanding policy scope.

Prefer the smallest policy block that preserves the contract. Include rationale
only where omitting it would make a constraint ambiguous or easy to misuse.

## Verify

Before finishing, confirm:

- the architecture guidance and each normative rule appear once;
- every hard constraint and self-check concept in the guidance contract is
  traceable in the target, with questions referring to rules rather than
  redefining them;
- the self-check remains concise;
- the wording is self-contained and architecture-specific; and
- no external rationale link or workflow procedure leaked into the target
  contract.

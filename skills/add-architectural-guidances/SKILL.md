---
name: add-architectural-guidances
description: Use when updating a project's AGENTS.md to add durable architecture guidance, design constraints, or architecture review questions
---

# Add Architectural Guidances

Add reusable architecture policy to a project's `AGENTS.md`.

Use this skill when the task is to strengthen an `AGENTS.md` with cross-project architectural rules, not when writing project-specific product requirements or implementation plans.

## Goal

Make the target `AGENTS.md` carry a compact, durable architecture contract that:
- frames incremental work packages as useful limited feature sets that move toward the final direction
- matches flexibility to available information about likely change
- places state by owner, lifetime, and semantic stability
- guides behavior ownership, decomposition, and dependency direction
- keeps business logic out of UI and transport glue
- discourages fake abstractions
- turns SOLID principles into concrete architecture constraints instead of acronym-only guidance
- makes compatibility expectations explicit before preserving legacy paths
- forces a short architecture self-check on design-sensitive changes

The result should be self-contained. Do not depend on another repo, another `AGENTS.md`, or an external architecture doc being present.

For expanded reasoning behind the compact rules, see `references/architecture-decision-framework.md` when revising this skill or when a user asks for rationale. Do not copy the reference wholesale into target `AGENTS.md` files.

## What To Extract

Keep only reusable architectural policy such as:
- incremental work packages should deliver a useful stopping point while moving toward the final direction; if the package stopped there, the project should be better off than not building it
- available information should shape flexibility: make likely changes easy, keep uncertain decisions local and reversible, and model stable behavior directly
- state should live at the lowest durability and smallest owning scope that meets the real requirement; durable stores should hold facts, user intent, and stable configuration, not high-churn presentation or cache state
- behavior should have a clear owning component with one cohesive responsibility and one primary reason to change
- business logic should live in application or domain services, not UI, transport, webhook, or tool handlers
- dependencies should flow toward more stable code, with high-level policy depending on stable, domain-owned contracts rather than concrete adapters
- side effects belong at the shell or adapter boundary
- unrelated domains should not be mixed into one coordinator
- concrete likely variations should be extensible through small adapters, strategies, data mappings, or config only when the variation is real
- abstractions and interfaces need real semantics, substitutable implementations, narrow consumer-shaped contracts, and a concrete changeability benefit
- compatibility expectations should be stated explicitly; legacy handling and legacy paths should be kept only when they are actually required, with obsolete paths cleaned up by default
- expected paths should be designed directly, with errors handled at the layer that has the right context and unexpected errors surfaced rather than swallowed

Do not copy repo-specific material such as:
- product goals
- project structure
- stack choices unless explicitly meant to be global
- repo-local doc paths
- milestone or workflow notes

## How To Apply It

1. Read the target `AGENTS.md`.
2. Find the best stable place for architecture policy.
3. If an architecture section already exists, extend or refine it instead of duplicating it.
4. If no such section exists, add a compact `## Architecture Guidance` section.
5. Add a short `### Hard Constraints` subsection.
6. Add a short `### Required Self-Check For Design-Sensitive Changes` subsection.
7. Keep wording repo-neutral unless the repo already has established local terminology worth preserving.

Prefer a small policy block over a long essay.

## Required Content

The inserted guidance should preserve these ideas:

### Hard Constraints
- Shape work packages around useful stopping points that move toward the final direction. If work stopped after the package, the project should be better off than not building it; this does not need to hold for every internal slice.
- Treat available information explicitly. Make likely changes easy, keep uncertain decisions local and reversible, and model stable behavior directly. Use small module, adapter, function, data-mapping, or config boundaries to keep uncertain decisions contained. Add an abstraction only when the contract is real, stable enough to name, and makes the next likely change cheaper.
- Place state where its meaning lives. Use the lowest durability and smallest owning scope that meet the real requirement. Persist durable facts, user intent, and stable configuration. Keep derived, high-churn, presentation, focus, selection, progress, and cache state near the runtime that owns it unless cross-restart behavior is required.
- Give each behavior a clear owning component with one cohesive responsibility and one primary reason to change. Split mixed policy, orchestration, UI, transport, persistence, provider, and tool concerns when they change for different reasons.
- Prefer application services over putting business logic into UI, transport, webhook, or tool handlers.
- Keep dependencies flowing from unstable code toward stable code. High-level policy and application code should depend on stable, domain-owned contracts at real adapter boundaries, not concrete UI, transport, persistence, provider, or tool clients.
- Keep core policy isolated from side effects.
- Do not mix unrelated domains into one coordinating component.
- Introduce abstractions only when they make a concrete likely change easier. Prefer direct design for stable behavior, and use adapters, strategies, data mappings, or config for real variation points without speculative extension layers.
- Keep interfaces and public contracts narrow and consumer-shaped. Do not force callers or implementations to depend on unused capabilities.
- Do not create shared interfaces that implementations can only satisfy by narrowing preconditions, weakening behavior, ignoring requirements, or throwing unsupported-operation errors.
- Make compatibility expectations explicit. Keep legacy handling or legacy paths only when a real compatibility requirement exists; otherwise remove obsolete paths by default and mention that cleanup explicitly.
- Do not add fallback paths, broad defensive handling, or error swallowing unless that layer can make a correct domain decision; unexpected errors should surface to the top and fail in obvious ways.

### Required Self-Check

For design-sensitive changes, add these review questions in the final note, PR description, or equivalent handoff:
1. If this work package stopped here, would the project be better off than if it had not been built?
2. What final direction does this move toward?
3. Which decisions are likely to change, uncertain, or stable, and are uncertain ones local and reversible instead of hidden behind speculative abstraction? Are extension points tied to real variation instead of hypothetical futures?
4. What component owns this behavior, and why? Does it have one cohesive responsibility and one primary reason to change?
5. Does this change increase or reduce coupling? Are interfaces narrow, consumer-shaped, and free of unused capabilities?
6. Did any dependency start pointing the wrong way, especially from stable policy toward concrete adapters, providers, UI, transport, persistence, or tool clients?
7. Could any side effect be moved outward into an adapter or shell?
8. What state does this change add or mutate? Who owns it, how long should it live, how often does it change, can it be rebuilt, and why is this the smallest correct storage lifetime?
9. What is the performance impact of this change? Any regression must be justified from first principles by explaining why the correct approach fundamentally requires more work; do not accept regressions merely because the existing code structure makes them convenient.
10. Are the abstractions and interfaces semantically real, and can implementations substitute for each other without narrowed preconditions, weakened behavior, ignored requirements, or unsupported-operation errors?
11. What compatibility expectations apply, and were obsolete paths removed unless required?
12. What legacy code can we remove now?
13. Where are expected errors handled, and where do unexpected errors surface?
14. What tests prove the core behavior independently of the full system? If the design changed, would tests change narrowly, or would unrelated tests need rewrites?

## Editing Rules

- Keep the inserted section concise.
- Preserve the style of the existing `AGENTS.md`.
- Avoid references to any specific source repo.
- Do not claim the repo has architecture docs unless they actually exist.
- Do not add workflow rules, TDD rules, or commit policy unless the task explicitly asks for them.

## Suggested Shape

Use this as the default structure when the target file has no better existing place:

```md
## Architecture Guidance

Use this section to evaluate decomposition, dependency direction, side-effect placement, interface design, and testability.

### Hard Constraints
- ...

### Required Self-Check For Design-Sensitive Changes
1. ...
```

## Completion Check

Before finishing, verify:
- the guidance is present exactly once
- the wording is self-contained
- there are no repo-external references
- references are used only for skill-maintenance reasoning, not as required target-repo dependencies
- the added rules are clearly architectural rather than product-specific
- work-package guidance appears before lower-level design questions and requires useful limited feature sets, not just motion toward the final direction
- SOLID principles are represented as concrete architecture constraints, not acronym-only guidance
- state guidance places state by owner, lifetime, and semantic stability instead of treating persistence as a convenience
- performance guidance requires first-principles justification for regressions
- compatibility guidance rejects unnecessary legacy handling and defaults to cleaning up obsolete paths
- error handling guidance rejects unnecessary fallbacks and swallowed unexpected errors

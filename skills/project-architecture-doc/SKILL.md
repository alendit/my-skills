---
name: project-architecture-doc
description: >-
  Create or update a repository's docs/architecture.md from current code and
  durable docs, progressively covering overview, components, boundaries,
  diagrams, and architecture vision. Use when the user asks to generate,
  refresh, maintain, or review project architecture documentation.
---

# Project Architecture Doc

Create or update `docs/architecture.md` from the repository's real current state.

## Workflow

1. Read the repo guidance first.
   - Prefer `AGENTS.md`, `CLAUDE.md`, `README.md`, `docs/`, `specs/`, and implementation progress files if present.
   - Treat explicit repo architecture guidance as the review lens for the final discussion.
   - If a local architecture vision document exists, use it as the target-state reference. If not, infer vision only from stable docs and label inference as such.
   - Resolve shared project terminology through the
     [project-glossary authority](../clear-technical-writing/references/project-glossaries.md).
     Treat a selected glossary as explanatory input for preferred terms and
     aliases, verify meanings against code and architecture authorities, and
     route a durable new or changed term through that authority only within the
     authorized edit scope.

2. Scan the actual project.
   - Use fast file discovery (`rg --files`, package manifests, build configs, route trees, module indexes).
   - Identify runtime surfaces, core/domain modules, application services, adapters, persistence, transport/UI shells, background jobs, external integrations, and tests.
   - Use bounded outlines or module indexes when a top-level path hides
     meaningful implemented subcomponents; map those subcomponents to the
     smallest useful current source boundaries.
   - Look for architectural invariants: source of truth, ownership boundaries, supported environments, identity/versioning, concurrency, security, and public surface contracts.
   - Prefer code and executable config over stale prose when they disagree.

3. Open or create `docs/architecture.md`.
   - Preserve accurate existing material where possible.
   - Replace stale structure instead of appending a second architecture doc inside the same file.
   - Keep the document useful as a navigation map for future implementers.

4. Apply the structure in `references/architecture-doc-structure.md`.
   - Start broad, then progressively disclose detail.
   - Order components by importance to core functionality, not by folder order.
   - Use recursive subsections when a component has meaningful subcomponents.
   - Include optional sections only when evidence supports them; combine or omit empty sections.
   - If `docs/architecture.md` exceeds 200 lines, add a concise table of contents immediately after the opening description.
     Use stable Markdown heading anchors, for example
     `[Architecture Overview](#architecture-overview)`. Never maintain line
     ranges as navigation.
   - When feature contracts exist, link to their stable contract IDs and owning
     source rather than restating acceptance requirements.
   - Keep durable architecture facts in the main document. Put private fields,
     collection shape, diagnostic plumbing, and other volatile representation
     detail in the implementation appendix only when it materially helps
     maintainers.
   - Make an exact limit normative only when its correctness role, workload
     basis, resource estimate, boundary consequence, and revision trigger are
     documented. Otherwise label it as a private implementation default.

5. End with architecture discussion.
   - Evaluate the current architecture against the repo's architecture guidance, especially ownership, reviewable physical decomposition, dependency direction, side-effect placement, semantic interfaces, coupling, and testability.
   - Describe the delta between current architecture and architectural vision.
   - Separate confirmed facts from inferred gaps.

6. Apply one final
   [clear technical writing pass](../clear-technical-writing/SKILL.md) after the
   architecture structure and source-backed decisions are complete. Preserve
   architectural ownership, facts, uncertainty, and contract links.

7. Verify the result.
   - Re-read the final document for broken references, duplicate sections, Mermaid syntax plausibility, and stale claims.
   - If the document has a table of contents, verify every heading-anchor link.
   - Run the repo's formatting or docs checks when available and cheap.
   - Report what was verified and any areas that remain uncertain.

## Operating Rules

- Do not invent components that are not present in code or durable docs.
- Do not turn the document into an implementation plan, task list, or changelog.
- Do not copy review numbering, commit policy, reviewer selection, remediation
  repetition, or other fixpoint mechanics into the architecture document.
- Keep technology detail concrete enough to orient maintainers, but keep the main architecture story component-centered.
- Do not infer a decomposition defect from file size alone. When described
  subcomponents cannot be recovered from source boundaries, record the
  source-backed current-state mismatch in the architecture discussion.
- Use absolute or repo-root-relative paths consistently, following the repository's existing docs style.
- If existing architecture docs conflict with code, document the current code and call out the conflict in the final discussion.

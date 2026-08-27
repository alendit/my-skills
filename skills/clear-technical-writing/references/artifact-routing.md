# Artifact Routing

Use this reference when the artifact owner or prose authority is ambiguous.
Select one leaf owner and one prose transformation. Public visibility does not
change the route.

## Routing Table

| Artifact | Substantive owner | Prose route |
|---|---|---|
| PR description, commit message, code comment, investigation handoff, status report, or technical explanation grounded in engineering evidence | Caller, repository sources, and any task-specific skill | The caller is the leaf owner and applies `clear-technical-writing` once after facts and decisions are established. |
| Educational technical-note series | `technical-note-series` | Finish reader journey, examples, vocabulary ownership, and publication scope first; then apply one clear-writing pass. |
| `docs/architecture.md` | `project-architecture-doc` | Finish the required structure and source-backed architecture discussion first; then apply one pass. |
| Repository architecture policy | `add-architectural-guidances` | Apply one compact pass after the guidance contract. Do not expand policy merely to demonstrate prose technique. |
| Review artifact or finding explanation | `evidence-efficient-review` | Finalize findings, severity, status, evidence, and correction first; then apply one pass. Wording cannot add, remove, close, or downgrade a finding. An outer fixpoint workflow records the result without rewriting it. |
| Implementation slice or package handoff | `supervised-implementer-loop` | Apply one compact pass without changing accepted contract IDs, package scope, or evidence results. |
| Editorial, marketing, customer communication, or other general prose | General `writing` skill when available | Use the general prose authority rather than this skill. |

## Resolve Overlap

Route by the artifact's purpose and factual owner, not by whether the subject is
technical or the audience is external. When the user names both writing skills,
choose one transformation process. A non-conflicting check from the other skill
may inform the chosen pass, but do not run successive automatic rewrites.

The intended reader may be a person or a collaborating agent. Keep assignments,
corrections, review dossiers, and handoffs locally understandable; a glossary
link or workflow label does not replace the operation, condition, or consequence
the reader needs.

# Project Glossaries

Use this reference before durable engineering communication uses or establishes
terminology shared across artifacts, sessions, people, or collaborating agents.
Do not trigger glossary placement work for an unrelated task that neither uses
nor establishes shared project terminology.

## Resolve Glossary State In Order

Inspect explicit user instructions and repository guidance, then apply the first
matching branch:

1. **Explicit opt-out:** do not ask about placement, access a glossary, create a
   file, or persist a term. Explain the concept locally in the artifact.
2. **Selected existing source:** use that glossary. Reuse a prior selection only
   when it is recoverable for the same project and scope.
3. **Explicitly selected absent path:** treat placement as resolved, but do not
   infer permission to create the file or write a term. The task's ordinary
   authorization boundary still applies.
4. **Competing plausible sources:** ask which glossary governs. Do not merge or
   choose them automatically.
5. **No source or placement selection:** ask whether to create a glossary inside
   the project or at a user-selected look-aside location. Do not create or
   persist anything until the user answers. For a project-local choice, use an
   established documentation path or ask for the exact path. For a look-aside
   choice, obtain its exact location and intended scope. Never invent either.

## Use Terminology Without Replacing Meaning

Treat the selected glossary as canonical only for preferred terms, aliases, and
plain project explanations within its declared scope. Code, accepted contracts,
architecture authorities, and the artifact's factual owner remain authoritative
for behavior, ownership, lifetime, and acceptance. Report a conflict to the
semantic owner instead of changing a fact to match glossary wording.

Read the entries material to the artifact before drafting. Keep the artifact
self-contained enough for its intended person or agent: explain an unfamiliar
term locally, do not begin with a vocabulary dump, do not replace concrete
operations with labels, and do not assume a link repairs unclear prose.

When terminology describes architecture, record semantic ownership, current
physical placement, and accepted target topology as distinct claims. Label
current placement as descriptive and connect topology acceptance to its
architecture evidence and authority.

## Add Or Update A Term

Add a glossary entry only when all of these conditions hold:

- the term names a distinct project concept or a domain concept used more
  narrowly than readers can safely assume;
- an accepted semantic source establishes the meaning;
- the selected glossary location and documentation scope authorize the entry;
  and
- the current task authorizes the edit scope.

If any condition is missing, report the term as a candidate and define it
locally without persisting it. A new label never authorizes a new field, state,
limit, component, or other mechanism.

For an authorized entry, give one concept one preferred term, point aliases to
it, explain it in ordinary language, and state the project-specific distinction.
Include an owner, lifetime, mapping, boundary, or semantic-source link only when
needed to prevent a material misunderstanding. Follow the repository's format;
no paragraph cap, typography rule, or mandatory field set decides acceptance.

When a semantic source or definition changes, follow
[revision after change](revision-after-change.md). Revalidate aliases, linked
entries, and affected prose only within the authorized edit scope. Report known
out-of-scope dependents with their stale term and semantic source.

# Project Glossaries

Use this reference when shared project terminology is material to the artifact.
Ordinary writing does not require a glossary, placement decision, or new file.

## Resolve Glossary State In Order

Inspect explicit user instructions and repository guidance, then apply the first
matching branch:

1. **Explicit opt-out:** do not ask about placement, access a glossary, create a
   file, or persist a term. Explain the concept locally in the artifact.
2. **Selected existing source:** use that glossary. Reuse a prior selection only
   when it is recoverable for the same project and scope.
3. **Explicitly selected absent path:** placement is resolved. Create it only
   when the task authorizes glossary creation; otherwise explain needed concepts
   locally and continue without treating a missing file as missing semantics.
4. **Competing plausible sources:** keep claims grounded in their semantic
   owners and explain terms locally. Ask which glossary governs only when a
   material terminology decision or requested canonical edit depends on it.
   Do not merge or silently select competing canonical authorities.
5. **No source or placement selection:** use established terms from the accepted
   facts and explain unfamiliar concepts locally. Continue the writing task;
   do not ask a placement question or create a glossary. If glossary creation
   is itself requested, recover an authorized destination from the request and
   repository conventions, asking only for a material unresolved location or
   scope decision.

When terminology state matters to a handoff, distinguish `local-only` (no usable
selected source) from the user's explicit `opt-out`. Neither calls for glossary
coverage or persistence work. Do not report routine glossary status when it
does not affect the artifact or continuation.

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

## Check Material Coverage At The Existing Boundary

At relevant assignments, corrections, and handoffs, carry `local-only`,
`opt-out`, or the selected source and material dispositions below. Under opt-out,
do not access a glossary; neither no-source branch calculates or carries scope
fit or candidates. For a selected source, refresh stale material evidence only
where it affects the artifact. Continue unaffected work. Block only a required
term decision whose meaning or requested canonical form remains unresolved,
not the writing task merely because glossary metadata is absent. Do not start
a repository audit or a parallel ledger.

When active work materially changes scope, or an existing selected glossary is
reused at a durable-artifact or package boundary, compare its declared scope,
when present, with the active work. Report a material mismatch while retaining
the selected glossary; do not restart placement discovery or infer authority to
edit it. A glossary without a declared scope remains usable.

At that same boundary, inspect only shared terms already material to the
artifact or handoff. For each possible coverage gap, establish:

- the term actually used and why its project-specific distinction is material;
- the accepted semantic source;
- the matching glossary entry, or its absence; and
- whether the entry is materially narrower, broader, or differently aliased.

Report a candidate only when the term names a durable project distinction, has
an accepted semantic source, and is absent or materially mismatched. Mere
occurrence is not a definition. Treat ordinary domain vocabulary and local
workflow labels as local explanation unless the project gives them a distinct
meaning.

Carry the used term, semantic source, project-specific distinction or
ambiguity, relevant scope mismatch, and any unresolved preferred-term or alias
question. This is explanatory state for the current selected source, active
scope, semantic source, and material artifact; it is not a candidate store.
Re-evaluate it when one of those inputs changes, and stop carrying it when it
is resolved or no longer material. The report does not choose terminology,
decide architecture, or turn a label into a field, state, limit, component,
ownership rule, or other mechanism.

## Add Or Update A Term

Add a glossary entry only when all of these conditions hold:

- the term names a distinct project concept or a domain concept used more
  narrowly than readers can safely assume;
- an accepted semantic source establishes the meaning;
- the selected glossary location and documentation scope authorize the entry;
  and
- the current task authorizes the edit scope.

If any condition is missing, leave the glossary unchanged and define the term
locally. For a selected source, report a material candidate or alias uncertainty;
without a selected source, do not create a candidate backlog. A new label never
authorizes a new field, state, limit, component, or other mechanism.

For an authorized entry, give one concept one preferred term, point aliases to
it, explain it in ordinary language, and state the project-specific distinction.
Include an owner, lifetime, mapping, boundary, or semantic-source link only when
needed to prevent a material misunderstanding. Follow the repository's format;
no paragraph cap, typography rule, or mandatory field set decides acceptance.

When a semantic source or definition changes, follow
[revision after change](revision-after-change.md). Revalidate aliases, linked
entries, and affected prose only within the authorized edit scope. Report known
out-of-scope dependents with their stale term and semantic source. After an
authorized update, use the selected glossary as the term authority and do not
retain a parallel candidate record.

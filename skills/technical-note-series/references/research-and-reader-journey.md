# Research and Reader Journey

Use this reference before drafting. Establish the writing contract, source
evidence, running example, reading order, and series guide as one coherent
design.

## Contents

- Establish the writing contract
- Protect the working scope
- Build source evidence
- Select the running example
- Order the reader journey
- Keep the series open to extension
- Make the guide authoritative

## Establish the writing contract

Identify the audience and background that may not be assumed, concrete learning
outcomes, described repository revision, requested topics and destinations,
stable filename/link constraints, and validation expected for examples and
implementation claims. Separate current behavior, rationale, limitation,
non-goal, and future direction.

Recover discoverable facts from the repository. Make only narrow, reversible
assumptions when an input cannot be recovered. Determine what the reader must
understand and what current implementation supports before polishing prose.

Before establishing terminology shared beyond this series, resolve glossary
state through the
[project-glossary authority](../../clear-technical-writing/references/project-glossaries.md).
When a source is selected, use it for preferred project-wide terms, aliases, and
plain explanations, then verify behavior, ownership, lifetime, and acceptance
against their semantic owners. When glossary use is declined or no authorized
source is available, keep necessary definitions local, persist no term, and ask
no repeated placement question. A glossary link never replaces the local
explanation a reader needs.

## Protect the working scope

Inspect repository status before editing and preserve unrelated changes. For an
existing series:

- preserve filenames with link value unless renaming was requested;
- identify duplicate, contradictory, stale, or missing explanations across the
  complete selected series;
- treat the guide and notes as one teaching artifact; and
- preserve genuinely historical documents as historical evidence rather than
  silently rewriting them as current.

## Build source evidence

Read the narrowest authorities that establish the explained path and boundaries:
architecture and goal documents, owning source, behavioral tests, dependency
and generated-artifact contracts, existing notes, and authoritative external
technology documentation.

Classify each material claim:

```text
current fact | design rationale | limitation | non-goal | future direction
```

Record its semantic owner, lifetime or boundary, observable effect, and named
source. Keep private representation in a current implementation map unless the
reader needs it to understand a durable contract. Use source and tests for
project behavior; use external documentation for the underlying technology,
not to infer how the project uses it. Treat old notes, reviews, and plans as
secondary unless the repository makes them authoritative.

Research can be broad. Publish only evidence that advances the reader's mental
model.

## Select the running example

Choose one small example with an observable result that exposes several real
project properties. Prefer a boundary such as stable identity versus physical
representation, language policy versus execution, or semantic ownership versus
adapter ownership.

Run the example through the public path and verify the result. Reuse the exact
example across notes, revisiting it at progressively deeper layers:

```text
observable behavior -> domain meaning -> semantic representation ->
generated or persisted representation -> runtime or adapter execution
```

Mark pseudocode, diagrams, and simplified object graphs as illustrative while
keeping relationships exact. Add a second example only when a new topic cannot
be taught honestly through the first, and connect it to the same vocabulary and
architecture.

## Order the reader journey

Order concepts by prerequisite, not repository layout or historical filename:

1. observable behavior and project problem;
2. minimum unfamiliar technology;
3. architecture and ownership boundaries;
4. semantic or domain representation; and
5. physical runtime, storage, engine, or adapter effects.

Give each note one primary reader question and explanatory owner. Preserve
stable filenames when required; repair order through guide navigation and
prerequisite links.

## Keep the series open to extension

Distinguish:

```text
foundational path    = shortest recommended newcomer route
published extensions = deeper evidence-backed notes available now
future candidates   = provisional topics, not promises or current facts
```

Call the current endpoint the latest published frontier, not the end of the
series. Avoid fixed totals unless they describe a closed subsection. Preserve
URLs, place new topics by prerequisite, and allow branches when one linear path
would burden unrelated readers.

Add a note only when it owns a distinct question, has current authoritative
evidence, has economical prerequisites, connects to the shared mental model,
and has a clear place in the guide. Periodically rebaseline the guide so the
newcomer path stays compact while optional depth grows.

## Make the guide authoritative

Create or update the guide before drafting notes. It is the sole authority only
for series-owned material:

- recommended reading order, foundational path, extensions, and latest frontier;
- running-example identity and expected result;
- series-only terms and reader-specific introduction order and first-use
  explanations; and
- series scope, shared non-goals, navigation, and links to deeper reference
  material.

When a glossary is selected, it remains canonical for project-wide term
identity, aliases, and concise explanation. Link those definitions from the
guide instead of maintaining another project-wide meaning, while still
explaining the concept locally at the reader's first need. Without an authorized
source, keep necessary definitions in the series without presenting or
persisting them as canonical project-wide entries. Code, accepted contracts,
architecture authorities, and artifact-specific owners remain authoritative for
semantics in either branch.

When the project or feature goal has a normative contract, link stable contract
IDs to its owning source. A plain-language project goal or architecture overview
may orient readers, but label it as explanatory and do not restate acceptance
requirements or become a second authority.

When a glossary is selected, notes link to it for project-wide definitions.
Otherwise they retain the local definitions their readers need. In either case,
notes link to the guide for series-only definitions and navigation instead of
recreating them. Each note owns only its distinct reader question,
layer-specific explanation, reader-specific first use, and local transitions.
Keep future candidates separate and explicitly non-binding.

Prefer one ownership/data-flow diagram over a component inventory. Label native,
guest, generated, persistent, remote, or other execution domains when relevant.

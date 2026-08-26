# Drafting and Cross-Note Coherence

Use this reference while drafting or revising the guide and notes.

## Contents

- Draft around one reader question
- Teach unfamiliar technology just in time
- Explain boundaries
- Use implementation detail as evidence
- Separate present state from direction
- Maintain cross-note coherence

## Draft around one reader question

Use this default shape when it serves the subject:

1. guide link, series navigation, and prerequisite;
2. direct purpose and learning outcomes;
3. running example at this note's layer;
4. just-in-time unfamiliar concepts;
5. concrete representation or execution path;
6. ownership, authority, and dependency boundaries;
7. problems this layer solves and what it does not own;
8. current limitations, non-goals, or omitted alternatives;
9. implementation map to authoritative files and symbols; and
10. navigation through the guide.

Open with a problem or observable behavior, not a glossary. Headings should
expose the argument when scanned alone.

## Teach unfamiliar technology just in time

Assume software-engineering experience but no background in the project's
specialist technology. Define a term at first use in ordinary language, connect
it immediately to the example or architecture, explain why the project needs
it, distinguish general technology from project usage, and link an authoritative
external primer for optional depth.

Avoid jargon chains and keep generic background proportional. The goal is to
make this project intelligible, not reproduce a language, compiler, runtime,
engine, storage, or protocol textbook.

## Explain boundaries

For every important layer answer:

```text
What does it own?
What does it deliberately not own?
Why does the boundary exist?
What exactly crosses it?
```

Call out distinctions readers can easily blur: semantic identity versus
physical handles; policy versus adapter mechanics; source versus semantic IR
versus machine instructions; domain versus host state; structural validity
versus admission authority; language versus resource or engine failures;
logical reachability versus physical retention; and engine independence versus
a real ABI or storage contract.

Use ownership tables, mismatch tables, or small data-flow diagrams where prose
would hide a distinction. Replace broad claims with exact owners, capabilities,
representations, and evidence.

## Use implementation detail as evidence

Name owning modules and public symbols, include small excerpts only when they
clarify a boundary, explain consequential representation choices, and link to
source instead of copying large blocks. Isolate volatile names, versions,
counts, private fields, and file paths in current implementation maps or an
appendix so the conceptual explanation remains stable.

Do not overstate generality. A component can be independent of one engine while
remaining coupled to a guest ABI, tagged representation, schema, or protocol.
An exact private default is implementation detail unless the durable contract
and its evidence justify that value.

## Separate present state from direction

Use explicit certainty language:

- **currently** for observed implementation behavior;
- **deliberately does not** for present ownership or non-goals;
- **direction** for architectural trajectory; and
- **not yet claimed** for possible capabilities without current proof.

Do not write plans in the present tense, let aspirations erase limitations, or
present a temporary mechanism as permanent architecture without authority.

## Maintain cross-note coherence

After each note, verify one guide-owned definition per shared term, a stable
running example and result, compatible diagrams, prerequisite order, consistent
behavior ownership, and non-conflicting scope and non-goals. Replace compensating
repetition with a link to the guide or note that owns the explanation.

Navigation follows the guide's recommended reading paths rather than numeric
filenames. The latest note points through the guide or to published extensions
without claiming the whole series is complete.

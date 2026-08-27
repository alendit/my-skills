# Improvement: Project Glossary

## Problem

Project-specific terminology can make technical communication shorter and more precise, but undefined or overloaded terms create ambiguity across sessions, agents, and reviewers. Different participants may use the same phrase while referring to different resources, owners, or lifetimes.

## Proposal

Maintain `docs/glossary.md` as the canonical source for project terminology.

Include:

- project-specific terms; and
- domain terms that are central to the project but potentially unclear, or that the project uses with a narrower meaning.

Do not attempt to catalogue ordinary compiler or software-engineering vocabulary exhaustively.

Each glossary entry should:

- be no longer than one paragraph;
- use plain wording;
- explain what the term means in this project;
- explain a newly invented term rather than relying on its name to imply meaning; and
- italicize references to other glossary terms, for example `*compiler snapshot*`.

Invent a project-specific term only when an established domain term does not adequately describe a genuinely new abstraction, structure, owner, lifecycle, or process.

## Writing Process

For durable specifications, architecture documents, reviews, and implementation handoffs:

1. Read `docs/glossary.md` before writing.
2. Draft using plain wording and established domain terminology where it improves precision.
3. Before finishing, make one terminology pass:
   - replace unnecessary jargon with plain wording;
   - normalize project terms to their glossary definitions; and
   - if a necessary new project term remains, add it to the glossary and explain it plainly where first used.

When terminology could materially change an implementation, follow the conceptual statement with a concrete restatement. For example:

> Release the *target-query resources* before lowering. Specifically, drop the copied target names and temporary lookup values, but retain the compiler snapshot.

Reviewers should flag terminology when ambiguity could lead to a different implementation, not as general prose criticism.

## Non-Goals

This proposal does not require terminology ledgers, classification reports, exhaustive vocabulary extraction, or automated glossary enforcement. The intended process is deliberately small: read the glossary, write, then perform one terminology pass.

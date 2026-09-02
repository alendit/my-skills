# Observation: A Selected Glossary Can Fall Behind the Working Vocabulary

## Purpose

This note records a glossary-use failure observed during the Stage 2
memory-management cutover in `clojure-wasm`. It is an observation document,
not an improvement plan. It does not prescribe a new skill, a mandatory
terminology pass, an automatic glossary update, or a particular owner for a
future correction.

The project had an explicitly selected `docs/glossary.md`, and the active
writing guidance required relevant glossary entries to be read before durable
engineering communication used or established shared terminology. Despite
that, the implementation discussion and handoffs accumulated durable project
concepts that the selected glossary did not define.

## Observed failure

A progress update described work on the "Var/code-unit/callable image." The
word *image* could plausibly mean the guest runtime, a generated Wasm module,
an embedded build artifact, a Store-rotation snapshot, or a copied checkpoint.
The intended meaning was the encoder-authored WebAssembly module instantiated
as the guest runtime, but that distinction was explained only after the user
asked.

The subsequent glossary lookup found no entry for *runtime image*. A broader
comparison found that the gap was not isolated. The current cutover documents
also rely on terms including:

- typed kernel;
- Wasm-GC object graph and copying collector;
- direct cutover and legacy tagged runtime;
- shadow state and host semantic mirror;
- Var, callable, code unit, and staged publication;
- callable table, external lease, and linear resource;
- execution-generation Store rotation; and
- phase or capability token.

Some of these words occur inside the existing glossary's descriptions, but
occurrence is not definition. The glossary defined only the three top-level
components, semantic ownership, and physical module boundaries. It did not
state the identities, aliases, distinctions, lifetimes, or ownership needed to
interpret the newer vocabulary consistently.

## Evidence in the project artifacts

The mismatch is visible without relying on the conversational example alone.
The M2 direct-cutover map says that its terminology follows the project
glossary, then uses *encoder-authored image*, *production candidate*, *Wasm-GC
object graph*, *linear resource*, *external lease*, *typed exports*, *shadow
graph*, and *host semantic mirror*. The hybrid-memory interlude gives these
concepts architectural meaning and ownership, but the selected glossary did
not carry that meaning into a shared terminology source.

The glossary's declared scope also referred specifically to the Stage 2
modularization interlude and architecture notes. The work later moved into a
memory-management interlude and a direct implementation cutover while the same
glossary selection continued to be reused. Nothing in the observed interaction
made the resulting scope mismatch visible before an ambiguous term caused a
question.

## Why local explanation was insufficient

The phrase was understandable after a local explanation, so the immediate
communication failure was recoverable. That repair did not answer whether
later handoffs should use *runtime image*, *production image*, *guest image*,
or *artifact*, nor did it distinguish the runtime image from a rotation
snapshot or generated callable module for other readers and agents.

This matters because the cutover relies on exact ownership distinctions. The
image composer must not become a semantic owner. The callable table is an
engine resource, not the Var registry. A public lease is not a host-held
Wasm-GC reference. A linear resource is not a second general object heap.
Without shared definitions, compact handoffs can preserve the same words while
silently changing these relationships.

## Why the existing guidance did not expose the gap

The glossary guidance successfully addresses placement, authorization,
semantic-source precedence, entry shape, local explanation, and dependency-
aware updates. The observed failure occurred after those questions appeared
settled: an existing glossary had already been selected, and no explicit
definition was being revised.

The working vocabulary then evolved across design documents, implementation
maps, agent assignments, evidence artifacts, and progress summaries. Individual
communications could read the entries that existed and still introduce or
reuse concepts absent from the glossary. Local first-use explanations reduced
the immediate cost of unfamiliar language but did not make the accumulated
coverage drift visible.

The observation does not establish whether the problem lies in glossary scope,
consumer routing, long-running package handoff, term-candidate recognition, or
the boundary between transient conversation and durable engineering
communication. It establishes only that selecting and consulting a glossary
did not keep the project's shared vocabulary aligned with it.

## Distinctions preserved by this observation

- A glossary need not define ordinary Rust, Clojure, WebAssembly, or Wasmtime
  vocabulary merely because it appears in a project artifact.
- Not every migration label or checkpoint identifier is a durable project
  concept. Terms such as *production candidate*, *CP1*, and *owner-level
  package* may remain local workflow language.
- A missing glossary entry does not invalidate an accepted semantic source.
  Code, architecture, and accepted contracts remain authoritative for meaning.
- Local explanation remains necessary for readers who cannot be expected to
  consult the glossary.
- Automatically persisting every newly used noun could create a larger and less
  useful glossary without preventing semantic drift.
- The observed ambiguity does not by itself determine whether *image* should
  be replaced, qualified, or retained as an alias.

## Questions left open

- When does vocabulary introduced during a long-running package become a
  candidate for the selected project glossary?
- How should a reused glossary selection expose that its declared scope no
  longer covers the active architecture work?
- Which artifact or workflow boundary should notice that a durable term has a
  semantic source but no glossary entry?
- How should handoffs distinguish an undefined project concept from ordinary
  domain vocabulary that needs only a local explanation?
- When several near-synonyms are already in use, what evidence establishes the
  preferred term without allowing prose to decide architecture?
- How should glossary coverage be evaluated without turning every writing task
  into an exhaustive repository terminology audit?
- What evidence would show that glossary use remains effective across multiple
  agents and implementation checkpoints rather than only within one final
  prose artifact?

These questions require a separate design decision. This document authorizes
no skill or workflow change by itself.

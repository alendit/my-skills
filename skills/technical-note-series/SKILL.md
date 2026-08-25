---
name: technical-note-series
description: Write, rewrite, or extend an educational project technical-note series for experienced software developers who are new to the project and may lack background in its languages, runtimes, compilers, or other foundational technologies. Use for architecture and implementation notes that must teach a coherent mental model, stay grounded in the current repository, remain open to future topics as the project grows, and reach a review fixpoint for each publication pass. Do not use for API reference, changelogs, implementation plans, release notes, or marketing copy.
---

# Technical Note Series

Produce a source-backed technical-note series that teaches a project through
observable behavior and progressively refined mental models. Assume the reader
can follow sophisticated software design, but does not know the project or the
specialized technologies on which it depends. Treat the published notes as the
current frontier of an evolving series, not as an exhaustive or permanently
closed account of the project.

This skill owns repository research, the reader journey, series structure,
drafting, cross-note coherence, factual validation, and review-to-fixpoint. The
caller owns the requested scope, destination, commit policy, reviewer or model
constraints, and any explicit compatibility requirements for existing files or
links.

## Establish The Writing Contract

Before drafting, identify:

- the intended reader and which background knowledge may not be assumed;
- the concrete learning outcomes for the series;
- the current repository revision that the notes describe;
- the requested note count, topics, destinations, and ordering constraints;
- whether existing filenames or links must remain stable;
- which claims describe current behavior, design rationale, future direction,
  or explicit non-goals;
- the validation expected for examples and implementation claims; and
- any required reviewer, model, or fixed-point process.

Recover discoverable inputs from the repository rather than asking the user.
When an input cannot be recovered safely, make the narrowest explicit
assumption and keep it easy to revise.

Do not start by polishing the existing prose. First determine what the reader
must understand and what the current implementation can actually support.

## Protect The Working Scope

Inspect repository status before editing. Separate the requested documentation
files from unrelated working-tree changes, and never absorb unrelated code or
documentation into the task.

For an existing series:

- preserve historical filenames when they have link value unless renaming was
  requested;
- identify duplicated, contradictory, stale, or missing explanations across
  the whole series;
- treat the series as one teaching artifact rather than several independent
  essays; and
- preserve historical documents as historical evidence instead of silently
  rewriting them to match the present.

## Build An Evidence Ledger

Map the project before writing. Read the narrowest authoritative sources that
can establish the execution path and the boundaries being explained:

- architecture and project-goal documents;
- source modules that own the relevant behavior;
- tests that demonstrate observable semantics or boundary enforcement;
- dependency manifests and generated-artifact contracts;
- existing notes and public documentation; and
- authoritative external specifications or library documentation for the
  underlying technology.

For every material claim, classify it as one of:

```text
current fact | design rationale | limitation | non-goal | future direction
```

Record enough evidence to answer:

```text
owner -> representation -> lifetime -> boundary -> observable effect -> evidence
```

Use current source and tests as authority for implementation claims. Use
external documentation to define the underlying technology, not to infer what
the project does with it. Treat comments, old notes, reviews, and plans as
secondary evidence unless the repository explicitly makes them authoritative.

Do not turn repository exploration into the article. Research may be broad;
the published explanation should contain only the evidence needed for the
reader's mental model.

## Select One Running Example

Choose one small example that produces an observable result and exercises
several important project properties at once. Prefer an example that exposes a
real architectural distinction, such as:

- stable identity versus replaceable implementation;
- source syntax versus lowered meaning;
- language failure versus engine failure;
- dynamic language behavior over static machine structures; or
- semantic ownership versus physical execution ownership.

Run the example through the actual public path and verify its result before
building the series around it. Do not use a merely illustrative example whose
claimed behavior has not been observed.

Reuse the exact example throughout the series. Each note should revisit it from
a new layer rather than introduce an unrelated toy:

```text
observable behavior
  -> language or domain meaning
  -> semantic representation
  -> generated or persisted representation
  -> runtime or adapter execution
```

Mark schematic expansions, pseudocode, diagrams, and simplified object graphs
as illustrative. Keep their relationships exact even when details are omitted.

## Design The Reader Journey

Order concepts by prerequisite, not by repository layout or historical file
number. A strong progression usually moves through:

1. the observable project behavior and the problem being solved;
2. the minimum unfamiliar technology needed to understand that problem;
3. the high-level architecture and its major ownership boundaries;
4. the semantic or domain representation that makes policy explicit; and
5. the runtime, storage, engine, or adapter that performs physical effects.

When existing filenames encode a different order, preserve them if necessary
and repair the reader journey through a series guide and explicit navigation.

Give every note one primary question. Notes may overlap for continuity, but
each must own a distinct explanatory responsibility and one main reason to
exist.

## Design For Continuous Extension

Treat each writing task as one publication pass over an open-ended series. The
current last note is only the latest published frontier. A pass can reach a
fixed point without declaring that no more topics belong in the series.

Separate three concepts explicitly:

```text
foundational path   = the shortest recommended route for a newcomer
published extensions = deeper notes already supported by current implementation
future candidates  = provisional topics, not promises or implemented facts
```

For example, a current foundational path may end with the host engine because
that is the deepest topic documented today. Later project growth may justify
notes on bootstrapping, macros, persistent collections, exception settlement,
resource accounting, code lifetime, self-hosting, portability, or other real
boundaries. Add such notes when the repository has enough stable behavior and
evidence to teach them accurately; do not invent a speculative roadmap merely
to make the series look comprehensive.

Keep extension cheap and links stable:

- do not use a fixed total such as `3 of 3` unless it is explicitly qualified
  as a closed subsection such as `Foundations: 3 of 3`;
- call the current endpoint the latest or last published note, never the end of
  the whole series;
- do not write `series complete` when only the current publication set is
  complete;
- preserve existing filenames and URLs when adding later notes;
- place each new topic by conceptual prerequisite, not merely by creation date;
- update the guide, navigation, vocabulary, architecture diagram, and affected
  cross-links whenever a new note changes the reader journey; and
- allow topic branches after the foundational path when one linear sequence
  would force unrelated readers through every specialist subject.

Before adding a note, require all of these:

- it answers a distinct reader question not already owned by another note;
- the project currently contains authoritative implementation or design
  evidence for the topic;
- its prerequisite concepts already exist or can be introduced economically;
- it connects to the established project mental model and ownership map; and
- the guide has a clear place for it in the published reading structure.

Prefer extending the established running example when it still illuminates the
new layer. Introduce a second example only when the new topic cannot be taught
honestly through the first one, and explicitly connect the new example back to
the same architecture and vocabulary.

Periodically rebaseline the guide as the series grows. Keep a compact newcomer
path even when the full collection becomes large, and move optional depth into
clearly labeled extensions rather than making every reader traverse the entire
archive.

## Write The Series Guide First

Create or update a compact series guide before drafting the articles. It should
contain:

- the intended reading order;
- the current foundational path and latest published frontier;
- any published extension paths, grouped by reader question;
- the project goal in plain language;
- the verified running example and expected result;
- one architecture diagram showing the full path;
- a small vocabulary section for terms used across notes;
- current scope and explicit non-goals; and
- links to deeper architecture or reference documentation.

The guide is the shared orientation layer. Put cross-series definitions there
instead of making every note invent its own terminology.

Do not present provisional future topics as part of the published reading path.
When useful, list them separately as non-binding candidates whose inclusion
depends on project maturity and evidence.

Prefer a diagram that shows ownership and direction of travel over a component
inventory. Label native, guest, generated, persistent, remote, or other
execution domains whenever those distinctions matter.

## Draft Each Note Around A Reader Question

Use this structure unless the subject requires a clearer variant:

1. Series navigation and prerequisite note.
2. A direct statement of the note's purpose.
3. Concrete learning outcomes.
4. The running example viewed through this note's layer.
5. Just-in-time explanation of unfamiliar concepts.
6. The project's concrete representation or execution path.
7. The important ownership and authority boundaries.
8. Problems this layer solves for the project.
9. What this layer deliberately does not own.
10. Current limitations, non-goals, or omitted alternatives.
11. An implementation map to authoritative files and symbols.
12. Navigation to the next note or the series guide.

Open with a problem or observable behavior, not a glossary dump. State what the
reader will be able to reason about after finishing the note.

Use headings as a conceptual outline. A reader scanning only the headings
should still see the argument and progression.

## Teach Unfamiliar Technology Just In Time

Assume general software-engineering experience, but no background in the
project's specialist technologies.

For every unfamiliar term:

- define it at first use in ordinary engineering language;
- immediately connect it to the running example or architecture;
- explain why this project needs it;
- distinguish the general technology from this project's chosen use; and
- link to an authoritative external source for readers who want a full primer.

Do not require the reader to understand a compiler, runtime, language, engine,
storage model, or protocol before the note has built the necessary concepts.
Avoid jargon chains in which each definition depends on another unexplained
term.

Keep generic background proportional. The goal is not to reproduce a language,
compiler, or engine textbook; it is to make the project intelligible.

## Explain Boundaries, Not Just Components

For every important layer, answer four questions:

```text
What does it own?
What does it deliberately not own?
Why does the boundary exist?
What exactly crosses the boundary?
```

Call out distinctions that are easy to blur, including when applicable:

- semantic identity versus physical index, slot, handle, or address;
- language policy versus adapter mechanics;
- source forms versus semantic IR versus machine instructions;
- guest or domain state versus host or transport state;
- structural validity versus project authority or admission policy;
- language failures versus resource, capability, ABI, or engine failures;
- logical reachability versus physical retention; and
- engine independence versus coupling to a real ABI or storage contract.

Prefer ownership tables, mismatch tables, and small data-flow diagrams when
prose would hide the distinction.

Avoid broad claims such as "the engine implements the runtime," "Wasm is
secure," "the IR is portable," or "validation proves safety." Replace them
with the exact owner, capability, representation, and evidence involved.

## Use Implementation Detail As Evidence

Technical notes should be concrete without becoming annotated source listings.
Use implementation detail to prove the mental model:

- name the owning modules and important public symbols;
- show exact dependency versions or feature selections only when they affect
  the explained behavior;
- include small code or data-shape excerpts when they clarify a boundary;
- explain why a representation was selected, not merely that it exists; and
- link to source instead of copying large implementation blocks.

Keep the conceptual explanation stable when possible. Isolate volatile names,
versions, counts, and file paths in implementation maps or clearly current
sections so routine code evolution does not invalidate the whole article.

Do not describe an abstraction as more general than the code permits. A layer
can be independent of one engine while remaining intentionally coupled to a
guest ABI, tagged representation, schema, or protocol.

## Separate Present State From Direction

Use explicit language for time and certainty:

- **currently** for observed implementation behavior;
- **deliberately does not** for a present ownership or non-goal boundary;
- **direction** for an intended architectural trajectory; and
- **not yet claimed** for capabilities the project may pursue but does not
  currently provide.

Do not write planned behavior in the present tense. Do not let an aspirational
project goal erase current limitations. Conversely, do not present a temporary
implementation detail as the permanent architecture unless the repository says
so.

## Maintain Cross-Note Coherence

After drafting each note, check the series as a whole:

- one term has one definition;
- the running example keeps the same source and result;
- diagrams show compatible boundaries and direction;
- each concept is introduced before another note assumes it;
- no note silently changes the owner of a behavior;
- current scope and non-goals do not conflict; and
- repeated material is either intentional reinforcement or replaced with a
  link to the owning explanation.

Use navigation that reflects the recommended reading order, not merely numeric
filenames. Confirm that the current last note points back to the guide or toward
published extension paths without claiming the whole series is finished.

## Validate The Documentation Like Code

Before review, verify every check that is cheap and relevant:

1. Run the central example through the public interface and record the observed
   result.
2. Run focused tests that prove the major semantic or architectural claims.
3. Confirm every referenced source file, symbol, export, dependency version,
   feature flag, and artifact name exists at the described revision.
4. Verify external documentation links against authoritative current sources.
5. Check all relative Markdown links and series navigation.
6. Check fenced code, tables, diagrams, and heading hierarchy.
7. Run the repository's documentation or Markdown checks when available.
8. Run `git diff --check` on the requested documentation scope.
9. Re-read the final diff for accidental changes outside the task.

Tests support specific claims; they do not automatically prove the prose. Read
the test and the implementation path closely enough to know what the passing
result actually establishes.

When a claim cannot be verified, weaken or remove it. Do not preserve a
confident sentence merely because it reads well.

## Review To A Fixpoint

Run review only after the series is coherent and validated enough to review as
one artifact.

Give the reviewer a compact contract:

- target audience and assumed background;
- required learning outcomes;
- reviewed revision and file scope;
- reading order and running example;
- current facts, non-goals, and known uncertainties;
- validation already performed; and
- a request for actionable factual, pedagogical, structural, and coherence
  defects rather than general stylistic preference.

Use one independent reviewer sequentially when available. Honor a user-named
reviewer or model when the environment supports it. Do not claim independent or
cross-model review when it did not occur; state the limitation and perform a
clearly labeled adversarial self-review instead.

Review against these cells:

```text
audience fit
concept prerequisite order
factual accuracy
boundary and ownership accuracy
example correctness
current-versus-future clarity
cross-note consistency
implementation traceability
scope and non-goal honesty
link and navigation integrity
```

For every valid finding:

1. identify the note or guide section that owns the defect;
2. repair the explanation at that owning location;
3. remove duplicate compensating text elsewhere;
4. rerun affected factual and mechanical validation; and
5. submit the complete revised series for another review pass.

Stop only when the reviewer reports no actionable defect in the selected
publication scope and all validation remains green. A pass that offers only
optional style ideas is a fixed point; a pass that exposes one factual,
audience, boundary, extension, or coherence defect is not. This closes the
current publication pass, not the evolving series.

## Reject Common Failure Modes

Do not ship a series that:

- follows source-tree order instead of reader prerequisite order;
- reads as several disconnected essays;
- assumes background in the technologies it is meant to introduce;
- spends pages on generic technology without connecting it to the project;
- exposes many identifiers before explaining the concept they implement;
- uses different toy examples that never compose into one mental model;
- describes current behavior from old notes instead of current source;
- conflates semantic ownership with physical execution;
- overstates portability, representation neutrality, authority, isolation, or
  validation guarantees;
- presents future direction as implemented fact;
- omits explicit limitations and non-goals;
- cites tests without explaining the property they prove;
- leaves symbols, versions, exports, links, or example output unverified; or
- claims reviewer independence or a model-specific review that did not happen.

## Publication Gate

The selected publication pass is complete only when:

- an experienced newcomer can state the project goal and trace the running
  example through the major layers;
- every specialist term is introduced before it is required;
- every major behavior has an explicit owner and non-owner;
- current facts, rationale, direction, and non-goals are distinguishable;
- the guide and notes form one coherent reading path;
- the guide distinguishes the foundational path, published extensions, and
  latest published frontier without implying permanent closure;
- navigation and numbering permit later notes without renaming existing files;
- implementation maps lead to current authoritative code;
- examples, symbols, versions, tests, and links have been checked;
- unrelated repository changes remain untouched; and
- review has reached the defined fixed point.

The series itself remains open. Future passes repeat this gate for the new or
changed scope and revalidate every existing note whose prerequisites,
terminology, ownership boundaries, or navigation are affected.

## Handoff

Report:

- files created or changed;
- the intended reading order;
- the current foundational path, published extensions, and latest frontier;
- the running example and observed result;
- the central architectural distinctions taught by the series;
- factual and mechanical validation performed;
- reviewer identity or the honest fallback used, plus review rounds;
- how this pass leaves room for later topics without promising speculative
  coverage;
- any remaining uncertainty or intentionally unverified claim; and
- repository status, including unrelated pre-existing modifications.

Do not commit unless the caller requested a commit. When committing was
requested, stage only the selected documentation or skill scope and verify the
commit contains no unrelated changes.

# Architecture Decision Framework

Use this reference when revising the skill or when a user asks for the reasoning
behind the compact architecture guidance. Do not copy this whole file into a
target `AGENTS.md`; extract only the shortest rules that fit that repo.

## Contents

- Available Information
- Local And Reversible Before Abstract
- Reviewable Physical Decomposition
- Work Packages
- Compatibility And Legacy Paths
- Error Handling
- Tests As Architecture Signal
- State Lifetime And Mutability

## Available Information

Architecture decisions should match what is actually known.

- Likely to change: isolate the changing part and make the likely change cheap.
- Uncertain: keep the decision local, reversible, and easy to delete. Avoid broad
  abstractions until the contract is real.
- Stable: model the behavior directly. Do not add flexibility for its own sake.

This avoids both traps: hard-coding decisions that are obviously temporary, and
over-building around hypothetical futures.

## Local And Reversible Before Abstract

Avoid relying on the term "seam" in target guidance. Prefer concrete wording:
small module, adapter, function, data-mapping, or config boundaries.

Use those boundaries to contain uncertain decisions. Add an abstraction only
when:

- the semantics are real and stable enough to name
- the next likely change needs the contract
- multiple callers or implementations benefit from the shared contract

Uncertain code should be easy to replace or delete. It should not be hidden
behind a vague interface that every implementation must distort itself to
satisfy.

## Reviewable Physical Decomposition

A semantic owner may be large, but its source organization should expose
cohesive internal responsibilities as bounded units of understanding, change,
and review when they have distinct reasons to change. A boundary may be a
module, submodule, object, or function group; this is not a one-file-per-owner
rule.

Qualification belongs to the
[architectural-scope decision authority](../../supervised-implementer-loop/references/architectural-scope-decision.md).
Reviewability matters because hidden boundaries can force unrelated context
into one change and conceal dependency or state relationships; it does not make
smaller modules intrinsically better.

Lines, bytes, outline depth, history, and tool truncation are prioritization
signals only. Generated source, cohesive algorithms, mandated colocation, and
mostly inline tests may remain large. An extraction that worsens coupling,
ownership, or dependency direction is not an improvement.

Examples of useful private decomposition around one semantic authority include
distributed inherent implementation blocks for a central type, a private
module containing one complete transaction, owner-local state behind a narrow
internal contract, and ABI adaptation beside the state or operation whose
boundary it expresses.

Counterexamples include forwarding-only modules, public traits without
substitutable implementations, copied state, bidirectional sibling
dependencies, and extraction that hides transaction ordering. Qualification
remains with the architectural-scope decision authority linked above.

## Work Packages

Incremental work should still produce useful stopping points. The test is not
whether every internal slice is valuable by itself, but whether the completed
work package leaves the project better than not building it.

A good package:

- moves toward the final direction
- delivers a limited but usable feature set
- avoids dead transitional code
- identifies obsolete paths that can now be removed

## Compatibility And Legacy Paths

Compatibility is a real requirement only when a caller, persisted artifact,
deployment, or user workflow still depends on the old path. If that requirement
is absent or explicitly removed, prefer cleanup over compatibility scaffolding.

Always ask what legacy code can be removed now. Leaving obsolete paths around
raises coupling and makes future architecture harder to read.

## Error Handling

Expected errors belong at the layer that has enough context to make a correct
domain decision. Unexpected errors should surface to the top and fail visibly.

Fallbacks, broad defensive handling, and swallowed exceptions are architecture
choices, not harmless safety. They hide ownership and make tests less useful.

## Tests As Architecture Signal

Clean architecture is cleanly testable. Tests should show whether behavior is
owned by the right component and whether change stays local.

When a design changes, focused tests should change with it. If unrelated tests
need rewrites, the system is probably too coupled, the abstraction is fake, or
side effects are too deep in the core.

## State Lifetime And Mutability

State has an owner, a lifetime, a scope, a mutation rate, and a durability cost.
Choose storage from those facts. Do not choose it because the store is easy to
reach.

Persistence is a gradient, not a switch. A value may live for one call, one
buffer, one process, one rebuilt cache, one session, one append-only history, or
one user configuration. Put it at the lowest durability and smallest owning scope that
meets the real requirement.

Durable stores should hold durable facts, explicit user intent, and stable
configuration. Examples include conversation events, provider anchors, selected
models, project roots, and user-chosen attachments. These facts should still be
owned by the component that gives them meaning.

Derived state should be rebuildable. Caches, indexes, summaries, estimates, and
view models may be stored, but only with clear invalidation or rebuild rules. A
cache is not a fact. Do not let cache shape become a domain contract by accident.

Presentation state should stay near the presentation shell. Focus, selection,
preview state, progress rows, spinners, read markers, unread indicators, and
scroll position are usually process-local. Losing them on restart is often fine.
Persist them only when cross-restart behavior is a real product requirement.

Mutability is a warning signal. The more often state changes, and the less each
change means to the domain, the closer it should stay to the runtime edge. High
churn in a durable store creates write amplification, replay risk, stale state,
and long-lived schema obligations.

Do not confuse reachability with ownership. A shared metadata bag may be easy to
read from several components. That does not make it the right owner. Ask what the
state means, who can change it correctly, and who should pay the cost of keeping
it valid.

A storage choice creates architecture. Persisted fields become compatibility
surface. They affect replay, migration, tests, debugging, and performance. Use
persistence when the state has durable meaning. Avoid it when the state only
records how the current process last looked at durable facts.

Ask these questions before adding or moving state:

- Who owns the meaning of this state?
- How long should it live?
- How often does it change?
- Can it be rebuilt from more durable facts?
- What breaks if it is lost on restart?
- Does it describe domain history, user intent, config, a cache, or UI motion?
- Is this the smallest storage lifetime that satisfies the requirement?

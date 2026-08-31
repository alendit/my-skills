# Improvement: Even Better Implementation Slicing

## Outcome

Specification work must distinguish a stable semantic contract from an
implementation-ready package plan. A specification may intentionally stop at
the first boundary, but its review must scope any zero-unknown decision to the
contract cells and keep package-design unknowns explicit. It must not report an
implementation-plan fixed point or readiness to begin implementation until
every contract is assigned to a reviewed delivery package.

This proposal strengthens the existing skills so they reliably demand useful,
cohesive implementation slices without prescribing file sizes, module counts,
or private representations.

## Observed Failure

The updated [Slice 7 specification](stage2/07-user-types-and-protocols.md)
established eight reviewed semantic contracts and six dependency-ordered design
checkpoints. [Review 95](stage2/review95.md) correctly said that implementation
remained blocked on those checkpoints, but it also reported zero required
unknowns and a planned-specification fixed point.

That decision left an important ambiguity. The document had no reviewed
implementation packages and no mapping from each semantic contract to a useful
delivery boundary. Checkpoints A-F identified questions that must be answered;
they did not say which complete behaviors should be built, accepted, and gated
together.

This was primarily an execution and review miss:

- `evidence-efficient-review` already requires an implementation slice for
  every normalized contract row;
- `complex-work` already requires ordered units shaped around meaningful
  acceptance boundaries; and
- repository guidance already requires useful stopping points and separately
  reviewed slices in dependency order.

The skills nevertheless leave enough room for a reviewer to accept design
checkpoints as a substitute for delivery packages. The improvement should make
that substitution impossible.

## Distinguish Three Fixed Points

Every specification review must name exactly which boundary it is deciding.

| Fixed point | What is complete | What it authorizes |
| --- | --- | --- |
| Contract fixed point | Observable behavior, semantic ownership, lifetime, transaction, recovery, public composition, and evidence are stable. | Dependent architecture and package design may begin. |
| Implementation-plan fixed point | Every contract maps to an ordered, cohesive delivery package with closed state, transaction, API or ABI, and evidence boundaries. | Implementation of the first package may begin. |
| Implementation fixed point | The accepted packages are implemented, verified on the required exact revisions, and independently reviewed. | The completed feature or stage may be treated as current behavior. |

A contract fixed point is valuable and may deliberately be the requested
stopping point. It is not an implementation-plan fixed point. Deferred package
design remains required coverage, even when the semantic contracts themselves
have no unknowns.

## Design Checkpoints Are Not Delivery Packages

A design checkpoint records a decision that later work needs: representation,
state ownership, transaction order, dependency direction, ABI shape, limits,
metrics, or test strategy. It may produce no executable behavior.

A delivery package produces a useful owner-level or public behavior through its
real composition path. It includes the state and transactions necessary to
establish that behavior, its consumer-shaped interfaces, and evidence that can
accept or reject the package.

One package may contain several internal checkpoints. A checkpoint may also be
accepted separately when a later package genuinely depends on its architectural
decision. Naming checkpoints A-F does not establish six slices, and it does not
establish any slice until the decisions are composed into delivery packages.

## Required Package Map

Before an implementation-plan fixed point, every normative contract must map
to one named package. Each package record must include:

| Field | Required decision |
| --- | --- |
| Package ID and outcome | The useful behavior available if work stops after this package. |
| Owned contracts | Complete contract IDs established by the package; partial ownership must be explicit and temporary. |
| Semantic and physical boundary | The semantic owner and the current or proposed physical representation, without equating a module with authority. |
| Prerequisites | Earlier packages and architectural decisions that this package actually consumes. |
| State and lifetime | State introduced or mutated, its owner, durability, rebuildability, and smallest correct lifetime. |
| Transaction closure | Admission, mutation, commit, abort, retry, poison, and cross-owner handoffs that must settle together. |
| Public and ABI surface | Compiled public composition and any guest, engine, embedding, or external boundary change. |
| Evidence | Focused contract scenarios, adjacent boundaries, recovery partitions, and package-level gate. |
| Deferred work | Behavior intentionally absent after the package and why the omission does not weaken its contracts. |

The mapping must be complete in both directions: every contract belongs to a
package, and every package exists to establish named contracts. A miscellaneous
integration, plumbing, metrics, ABI, or cleanup package is a review candidate
unless it independently satisfies the useful-stopping-point rule.

## Judge Slice Size By Closure, Not Lines

There is no preferred LOC range or module count. A package is too large when it
contains independently changing semantic owners or transaction systems that
can reach useful stopping points separately. It is too small when it exposes
only a representation, helper, adapter, or mechanical move with no independently
acceptable behavior.

Review package size with these questions:

1. If work stopped here, is a real public or owner-level capability correct and
   useful?
2. Does the package have one primary reason to change?
3. Are its state and transaction boundaries closed, or does acceptance depend
   on an unbuilt later package repairing partial semantics?
4. Does the next package depend on an accepted semantic decision or merely on
   convenient code placement?
5. Can focused evidence localize a defect to this package without requiring the
   whole future feature?
6. Does splitting further create forwarding layers, duplicated state, temporary
   public APIs, or repeated gates with no new decision value?
7. Does combining further hide independent owners, force unrelated tests into
   one review, or make rollback and acceptance ambiguous?

Gate cost is part of package design. Run focused checks for internal steps and
the expensive canonical gate at meaningful accepted package revisions. Do not
manufacture tiny packages merely to create more commits, reviews, or gates.

## Required Review Backstops

Specification review must add these cells:

| Cell | Clear only when | Failure disposition |
| --- | --- | --- |
| Contract-to-package coverage | Every normative contract maps to exactly the packages that establish it. | Required unknown or finding. |
| Useful stopping point | Each package leaves a correct and useful behavior if later packages never arrive. | Finding. |
| Cohesion and transaction closure | State, lifetime, commit, abort, and recovery boundaries fit one primary reason to change. | Finding or required unknown. |
| Dependency order | Every package consumes only accepted earlier contracts and decisions. | Finding. |
| Package-size tradeoff | The review explains why adjacent packages should neither be combined nor split further. | Required unknown. |
| Acceptance-cost topology | Focused checks, parent acceptance, independent review, and canonical gates occur only where they decide something material. | Finding when the plan repeats expensive work without decision value. |
| Checkpoint/package distinction | Design questions are not counted as delivery packages unless they satisfy the complete package record. | Required unknown. |

Zero required unknowns is impossible at an implementation-plan review while
any contract lacks a package, any package lacks a stopping-point outcome, or a
checkpoint is standing in for an unresolved package boundary.

## Skill Changes

### `evidence-efficient-review`

- Make the existing `Implementation slice` field non-optional for an
  implementation-plan fixed point.
- Require the reviewer to label contract-only fixed points explicitly.
- Add the backstop cells above to specification review.
- Require a Tock or required unknown when checkpoints replace delivery
  packages.
- Require the final review to state the package-size tradeoff, not merely list
  packages.

### `complex-work`

- Distinguish architectural checkpoints, internal implementation steps, and
  accepted delivery packages during package establishment.
- Require a complete contract-to-package map before routing implementation.
- Batch mechanical and tightly joined internal work, while preserving separate
  acceptance where a later package relies on a semantic decision.
- Include review and canonical-gate cost when selecting package boundaries.

### `supervised-implementer-loop`

- Refuse to begin from a contract-only specification when the requested work
  spans unresolved package boundaries.
- Give the persistent implementer the complete accepted package map once and
  use delta-only follow-ups within that map.
- Treat an internal step as parent-acceptance evidence, not automatically as a
  separately gated delivery package.

### `review-fixpoint`

- Carry the fixed-point level in every Tick or Tock decision.
- Do not let a contract Tick imply implementation-plan readiness.
- Start implementation Tock work only from the exact reviewed
  implementation-plan revision.

## Slice 7 Example

The following is illustrative, not a replacement for a reviewed Slice 7 owner
and package map:

| Candidate package | Candidate vertical outcome |
| --- | --- |
| 7.1 Protocol kernel | Protocol identities, extension publication, uncached dispatch, derived cache, `defprotocol`, and `extend-type` work end to end for built-in, `nil`, and default targets. |
| 7.2 Named user types | Type identities, instances, fields, tracing, replacement, `deftype`, and inline extensions work through compiled source. |
| 7.3 Records | `defrecord`, record construction, map-like operations, value laws, metadata, and printing form one complete record capability. |
| 7.4 Runtime reify | Anonymous type graphs, captures, atomic extension and instance adoption, dispatch, and reclamation work without runtime compilation. |

Uncached dispatch can be an internally accepted semantic step within 7.1 before
cache work begins; it need not force a separate canonical gate. The cache is
derived state and must not be allowed to define or repair dispatch semantics.
Records and reify remain separate because they have distinct state,
transactions, evidence, and reasons to change even though both depend on named
type and extension substrate.

The actual package map must be derived from the accepted Slice 7 owner, state,
transaction, ABI, and dependency design. This example demonstrates the desired
vertical shape only.

## Validation Scenarios For The Skills

The improved skills should produce these deterministic decisions:

- A specification with complete semantic contracts and checkpoints A-F but no
  delivery packages may receive a contract Tick, but an implementation-plan
  review must return required unknowns.
- A plan with one package per struct, module, ABI function, or metric fails the
  useful-stopping-point and acceptance-cost cells.
- A single package containing protocol publication, user values, records,
  reify, and cache fails cohesion unless evidence proves those state and
  transaction systems cannot form useful vertical packages.
- A package that exposes uncached protocol behavior before adding an optional
  cache can pass when the cache cannot change semantics and focused evidence
  proves both paths.
- A package map that assigns every contract but leaves record recovery or reify
  adoption to a later cleanup package fails transaction closure.
- A reviewed vertical map with complete contract coverage, closed transactions,
  dependency order, focused evidence, and justified gate placement can receive
  an implementation-plan Tick even while private filenames remain conditional.

## Non-Goals

This proposal does not establish Slice 7 package boundaries, choose future Rust
or guest-Wasm modules, set a target LOC count, require one module per semantic
owner, add implementation mechanisms, or change the current runtime. It changes
how specification and workflow skills distinguish a reviewed contract from a
reviewed implementation plan.

# Improvement Plan: Reviewable Physical Decomposition

## Purpose

Prevent iterative implementation from growing a few source modules without
boundaries that remain economical for agents and maintainers to understand,
change, and review. This plan selects small changes to existing skills. It does
not prescribe a `clojure-wasm` refactor or a universal file-size limit.

## Observed failure

At `clojure-wasm` revision
`ba45c05eb16725ab43ad508024d6da07daccfc36`, the Rust sources contain 93,803
lines. Three files contain about 76 percent of them:

| File | Lines | Bytes |
|---|---:|---:|
| `guest-runtime/src/lib.rs` | 32,436 | 1,229,600 |
| `src/engine.rs` | 22,461 | 943,023 |
| `src/embedding.rs` | 16,124 | 641,204 |

Tests explain only part of the concentration. The production portion of
`guest-runtime/src/lib.rs` is roughly 28,600 lines. Current outlines show:

- one `GuestRuntime` implementation spanning almost 9,000 lines;
- one `IsolateCore` implementation spanning about 5,200 lines;
- guest-runtime responsibilities for namespaces, Vars, publications,
  callables, execution contexts, failures, heap records, tracing, reclamation,
  value laws, builders, and ABI entry points in one file; and
- engine responsibilities for guest lifecycle, host/guest bridging, code-unit
  installation, rotation, semantic planning, WebAssembly emission, and source
  maps in one file.

A recursive outline exceeded a 20,000-token tool-output allowance. Narrow
symbol searches still work, but unfamiliar implementation and broad review now
require repeated reconstruction of subsystems whose physical boundaries no
longer provide useful working sets.

The important failure is not that these files are long. Architecture guidance,
supervised implementation, and independent review repeatedly accepted local
changes without challenging their cumulative placement. Existing rules cover
semantic ownership, dependency direction, state lifetime, and testability, but
do not require a large owner to expose meaningful internal source boundaries.

## Decision

Add one architecture property: **reviewable physical decomposition**. Source
organization should expose cohesive responsibilities and their important
relationships as bounded units of understanding, change, and review. A large
semantic owner may remain one component, but it should expose internal
subcomponents when they have distinct responsibilities or reasons to change.

Do not make line count, byte count, symbol count, or context use an acceptance
gate. These are inspection signals only. Generated source, one cohesive
algorithm, declarative tables, language-mandated colocation, or mostly inline
tests may justify a large file.

Prevent the failure in existing workflows rather than adding a mandatory new
skill. A separate audit would help only when someone remembered to invoke it;
the ordinary implementation and review path must notice cumulative drift.

## Proposed contracts

| ID | Contract | Owner |
|---|---|---|
| MD1 | Architecture guidance requires reviewable physical decomposition while rejecting size alone as proof of a defect. | `add-architectural-guidances` |
| MD2 | A concern qualifies only with evidence of distinct responsibilities or change reasons, causal locality or coupling cost, and a plausible cohesive boundary. | Existing architectural-scope decision authority |
| MD3 | Design-sensitive implementation records the affected owner's current structure, makes placement explicit, and checks the cumulative result before package acceptance. | `supervised-implementer-loop`; aggregated by `complex-work` for mixed packages |
| MD4 | Architecture documentation exposes mismatches between described subcomponents and implemented source boundaries. | `project-architecture-doc` |
| MD5 | Specification and implementation review include physical decomposition when relevant and route concrete concerns through the existing correction, deferral, reevaluation, or scope-stop branches. | `evidence-efficient-review`; composed by `review-fixpoint` |

## Evidence test

Treat physical decomposition as an architecture candidate only when all three
questions have source-backed answers:

1. **Responsibility:** Does the source unit contain behavior with distinct
   responsibilities or primary reasons to change?
2. **Causal cost:** Does a representative change require unrelated context,
   rely on implicit shared state or ordering, or repeatedly cross distant
   regions because the boundary is absent?
3. **Better boundary:** Is there a smaller cohesive module, submodule, object,
   or function group with explicit dependencies that would improve locality
   without creating a fake abstraction or wrong-way dependency?

Lines, bytes, outline depth, implementation span, test location, history, and
tool truncation may prioritize this check, but cannot answer it. Conversely, a
small file can fail the test when it mixes unrelated policy, persistence, and
transport behavior.

## Skill changes

### `add-architectural-guidances`

Add MD1 to `references/guidance-contract.md` as one hard constraint and one
self-check question: which source boundary receives this responsibility, and
does the change improve, preserve, or worsen that owner's physical
decomposition?

Put the MD2 rationale and anti-fragmentation examples in
`references/architecture-decision-framework.md`, not in target `AGENTS.md`
files. Keep the inserted guidance compact.

### `supervised-implementer-loop`

For an owner receiving a new design-sensitive responsibility or several
slices:

- record a compact baseline: relevant source units, major responsibility
  groups, state/collaborator boundaries, and production/test separation;
- name the intended destination before each relevant slice;
- report only material structural change in the slice handoff; and
- compare the final owner with the baseline before package acceptance.

Extend `references/architectural-scope-decision.md` so hidden physical
decomposition can qualify under MD2 and so a proposed correction cannot worsen
working-set locality. Inspect bounded history only when repeated placement
across prior packages is material; do not maintain a permanent metrics ledger.

### `complex-work`

When several units affect the same source owner, carry MD1 as a shared
constraint and require the implementation leaf's MD3 result before accepting
the mixed package. If cumulative placement invalidates the assumed owner,
replan only the affected unit and dependents. Do not copy the supervised
workflow's scanning or qualification mechanics.

### `project-architecture-doc`

Map meaningful implemented subcomponents to source paths, not only top-level
directories or giant files. If documented subcomponents cannot be recovered
from physical source boundaries, record that current-state mismatch in the
architecture discussion. Do not turn it into an unapproved refactoring plan.

### `evidence-efficient-review` and `review-fixpoint`

Add one design-sensitive review cell:

- specification review checks planned change locality without making private
  filenames a durable contract;
- implementation review compares the affected owner's baseline and result and
  applies MD2; and
- Tick/Tock carries the resulting architectural-scope branch without
  redefining the evidence test.

A behaviorally green change may still have an architectural finding when MD1
is violated with causal evidence. A long file without that evidence is not a
finding.

No change is needed in `clear-technical-writing` or `technical-note-series`.

## Existing repositories

Do not require a narrow package to complete a wholesale modularization. For an
already concentrated owner, use the existing architectural-scope branches:

- correct the smallest proper boundary now when it fits;
- defer only when the current change is non-worsening and an authorized durable
  follow-up exists;
- reevaluate an extraction that worsens coupling, state ownership, or
  dependency direction; or
- stop for scope when no bounded safe route fits.

Keep diagnosis, behavior-preserving reorganization, and later architectural
change as separate scopes.

## Implementation order

1. Add MD1 and its rationale to `add-architectural-guidances`.
2. Extend the architectural-scope decision and supervised implementation loop
   with MD2-MD3.
3. Add MD4-MD5 to architecture documentation and review.
4. Integrate the shared constraint into `complex-work`, then validate the
   composed workflows.

The repository already contains `skills/add-architectural-guidances`, and
`~/.agents/skills/add-architectural-guidances` resolves to it. The older
standalone `~/.codex/skills/add-architectural-guidances` source can be
consolidated after the repository changes are accepted and that installed-source
mutation is explicitly authorized.

## Validation

Use a small fixture portfolio:

| Scenario | Expected result |
|---|---|
| Sequential slices add distinct responsibilities to one owner | A later placement or package check raises MD2 before acceptance. |
| A large generated or cohesive source unit | No size-based finding. |
| A small file mixes policy, persistence, and transport | MD2 candidate despite its size. |
| Extraction would add a wrong-way dependency or fake interface | Reevaluate instead of fragmenting mechanically. |
| A narrow change touches an existing concentrated owner | Improve it, prove non-worsening deferral, or stop for scope. |
| Architecture docs name subcomponents hidden inside one source unit | Record the current-state mismatch. |

Static checks should verify that each contract has one owner, affected links
resolve, and no universal size threshold or mandatory new skill was introduced.
Model-behavior checks should record the exact skill revision, fixture, output,
and which contract a failure localizes to.

## Acceptance

Accept the skill package when MD1-MD5 are implemented once at their owning
boundaries, the static checks pass, the fixture portfolio distinguishes
cumulative growth from justified large files, and an independent review finds
no unresolved implementation or architecture defect.

This plan authorizes no skill edit, installed-source mutation,
`clojure-wasm` refactor, commit, or publication.

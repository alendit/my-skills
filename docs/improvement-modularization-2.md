# Improvement Plan: Separate Semantic Authority From Physical Colocation

## Purpose

Close the acceptance loophole left by
[`improvement-modularization.md`](improvement-modularization.md). The first
plan correctly established reviewable physical decomposition, but the
implemented skills still permit a reviewer to treat central state, lifecycle,
transactions, ABI work, or cross-cutting calls as reasons that substantive
responsibilities must remain in one physical root file.

This plan makes semantic authority and physical source decomposition explicitly
orthogonal. It adds a burden of proof for retained colocation and requires a
whole-root residual responsibility inventory before a modularization package
can reach deterministic fixed point.

It does not prescribe a universal module topology, require one module per term,
or introduce a line-count gate.

## Observed failure

The `clojure-wasm` modularization interlude extracted several useful private
modules and then declared full `MOD-OWNER` and package fixed point at production
revision `b402254100ad94395cf3df3407b429ae97afed05`. The resulting production
roots still contain:

| Root | Lines after the accepted extraction |
|---|---:|
| `guest-runtime/src/lib.rs` | 27,500 |
| `src/engine.rs` | 10,037 |
| `src/embedding.rs` | 6,848 |

The line counts are signals, not the defect. The defect is the reasoning used
to clear the remaining topology:

- guest failure, recovery, publication, and heap work remained rooted because
  they share cross-cutting state and calls;
- engine export acquisition remained rooted because it participates in the
  central `GuestRuntime` construction transaction;
- embedding compiler inventory and orchestration remained rooted because they
  share a live compiler snapshot; and
- stateful, ABI-sensitive, central-struct, lifecycle, and transaction work was
  collectively treated as correctly deferred behind design checkpoints while
  the same review declared the modularization package complete.

This conflated two different claims:

1. **Semantic authority:** one component remains responsible for the behavior
   and public contract.
2. **Physical colocation:** all state, operations, transactions, ABI adaptation,
   and evidence for that component remain in one source file.

The first claim does not imply the second. Rust private modules, split inherent
implementations, narrow internal state views, and transaction result objects
can expose cohesive internal responsibilities without creating another public
or semantic authority.

The review also challenged only weak extraction candidates. For example,
moving engine export handle structs or individual lookups could split the
construction lifecycle, but the relevant alternative was moving the complete
export-acquisition and initialization transaction into one private owner. A
review cannot reject an intentionally partial split and treat that as proof
that no cohesive boundary exists.

Passing tests, unchanged APIs and ABIs, preserved dependency direction, and
equivalent moved bodies proved behavioral preservation. They did not prove that
the residual roots satisfied physical locality. Preservation and modularity are
separate acceptance lanes.

## Decision

Adopt this invariant once in the architecture-guidance authority:

> Semantic authority and physical source decomposition are orthogonal. A
> component may remain the sole semantic and public authority while private
> modules own cohesive internal state, operations, transactions, ABI
> adaptation, and evidence. Shared access to a central type, state, lifecycle,
> transaction, or ABI is a boundary-design constraint, not evidence that
> responsibilities must remain in one source file. Retained colocation
> requires a causal invariant that the smallest plausible private boundary
> would break.

For a designated composition root, apply this consequence:

> A composition root may retain shared state and lifecycle coordination, but
> substantive owner-specific operations should reside in cohesive private
> modules when the language permits that decomposition without changing the
> public contract. A central type may have implementation blocks distributed
> across private submodules without creating another semantic authority.

Do not require extraction when it would create a forwarding-only layer, split
state ownership, obscure transaction ordering, reverse a dependency, broaden
visibility, or freeze an unstable abstraction. Require evidence for that
outcome rather than inferring it from the presence of state, transactions,
central types, or ABI code.

## Authoritative contract matrix

| ID | Contract | Owner |
|---|---|---|
| **MD2-1** | Semantic authority never implies physical colocation. Central state, lifecycle, transactions, ABI work, and cross-cutting calls are boundary-design inputs rather than exemption categories. | `add-architectural-guidances` |
| **MD2-2** | Retained colocation requires distinct responsibility analysis, a plausible smaller cohesive boundary, and a causal invariant that boundary would break. Rejecting only a partial or forwarding-only extraction does not satisfy this proof. | Architectural-scope decision authority |
| **MD2-3** | A modularization review keeps behavioral preservation and physical-locality coverage in separate contract cells. Passing one does not clear the other. | `evidence-efficient-review` |
| **MD2-4** | Parent package acceptance inspects the residual topology of every affected root, not only the quality of extracted modules. | `supervised-implementer-loop` |
| **MD2-5** | A whole-package modularization fixed point requires a disposition for every material residual responsibility cluster. Missing analysis remains `unknown`. | `review-fixpoint` |
| **MD2-6** | Architecture documents and glossaries distinguish semantic ownership, current physical placement, and accepted topology. Describing current placement never approves it. | Target repository architecture authority and glossary |

## Residual topology proof

Before clearing physical decomposition for a root, create this compact
inventory from source, dependency, state, transaction, caller, and test
evidence:

```text
responsibility cluster
-> semantic owner
-> current physical representation
-> state and lifetime
-> transaction boundary
-> dependencies and callers
-> public or ABI surface
-> representative tests
-> smallest plausible private boundary
-> colocation invariant, when retained
-> extracted | retained-with-proof | unknown | not-applicable
```

Apply these dispositions:

- **extracted:** the cohesive private boundary exists and composition preserves
  semantic authority, behavior, visibility, state, and dependency direction;
- **retained-with-proof:** a named causal invariant would be broken by the
  smallest plausible boundary, not merely by an artificially partial move;
- **unknown:** required owner or boundary analysis is absent, contradictory, or
  has not challenged a plausible complete extraction; and
- **not-applicable:** the region is generated, language-mandated, one cohesive
  algorithm, or otherwise lacks distinct responsibility evidence.

File size, outline depth, symbol count, history, context truncation, and
implementation effort prioritize the inventory but do not determine a
disposition.

`unknown` is required coverage and prevents a physical-decomposition or
modularization fixed point.

## Skill changes

### `add-architectural-guidances`

Add MD2-1 to `references/guidance-contract.md` immediately after the existing
reviewable-physical-decomposition rule. Keep one normative statement; do not
duplicate it in rationale or self-check prose.

Add this self-check question:

> For each responsibility retained in a composition root or large semantic
> owner, what causal invariant requires physical colocation? Have central
> state, lifecycle, transactions, ABI work, or private access been treated as
> design inputs rather than automatic exemptions?

Extend `references/architecture-decision-framework.md` with examples of valid
private decomposition around one semantic authority:

- split inherent implementation blocks for a central type;
- a private module owning one complete transaction while the root owns
  composition and shared lifecycle;
- owner-local state nested inside a central runtime and accessed through a
  narrow internal contract; and
- ABI adaptation colocated with the state or operation whose boundary it
  expresses.

Also include counterexamples: forwarding-only modules, public trait creation
without substitutable implementations, state copies, bidirectional sibling
dependencies, and extraction that hides transaction ordering.

### Architectural-scope decision authority

In
`supervised-implementer-loop/references/architectural-scope-decision.md`, make
the physical-decomposition qualification adversarial:

1. identify distinct responsibility or change reasons;
2. establish causal unrelated-context or implicit-coupling cost;
3. propose the smallest complete cohesive boundary;
4. challenge central-type, shared-state, transaction, lifecycle, and ABI
   designs explicitly; and
5. retain colocation only when a named invariant fails under that complete
   boundary.

State explicitly that those five design categories raise extraction risk but
do not disqualify extraction. A design checkpoint is a decision point, not a
permanent deferral and not evidence of package completion.

When the accepted package is itself a modularization package, safe deferral of
the central stateful and transactional work cannot simultaneously establish
that package's fixed point. It either remains current scope, receives an
authorized narrower package boundary, or remains `unknown`.

### `evidence-efficient-review`

For a whole-scope modularization review:

- build the residual topology inventory before deciding fixed point;
- audit extracted modules and retained roots with equal contract authority;
- keep `MOD-PRESERVE`-like evidence separate from `MOD-OWNER` and
  `MOD-LOCALITY` evidence;
- challenge at least one plausible complete private boundary for every
  retained material cluster;
- reject arguments that prove only that moving a helper, handle, or individual
  call would be harmful; and
- classify unperformed central-state or transaction design as `unknown`, not
  cleared or non-gating improvement.

Incremental review may carry forward trustworthy residual dispositions only
when their responsibilities, dependencies, state, transactions, callers, and
tests remain unchanged. If a prior zero-finding topology decision is
overturned, use rebaseline mode.

Add this explicit review rule:

> A whole-package modularization contract cannot be cleared by proving that
> the modules already extracted are cohesive. The reviewer must also prove
> that every material residual responsibility is cohesively rooted or record
> the missing analysis as required unknown coverage.

### `supervised-implementer-loop`

For an owner-level modularization package, the initial structural baseline and
final acceptance packet must include the residual topology inventory. Parent
acceptance checks both sides of each move:

- the extracted module is cohesive and direct;
- the root has lost the corresponding responsibility rather than retaining a
  second operational copy;
- remaining root responsibilities still have explicit dispositions; and
- a central type, transaction, or ABI boundary was designed rather than
  skipped because it was not mechanically extractable.

Batch related state, operations, transaction handling, ABI adaptation, and
tests into meaningful owner-level acceptance packages. Do not let a series of
easy stateless extractions stand in for the requested stateful or transactional
architecture work.

### `review-fixpoint`

Extend the deterministic Fixed-Point Rule for work packages whose selected
contract includes physical decomposition:

> Every material residual responsibility cluster has an `extracted`,
> `retained-with-proof`, or justified `not-applicable` disposition. No
> required residual topology coverage is `unknown`, and preservation evidence
> has not been used to clear locality or owner-decomposition cells.

A Tick that inspects only the remediation diff or accepted extracted modules
cannot establish a whole-package modularization fixed point. When an earlier
zero-finding topology review is overturned, preserve it as historical evidence
and create a new rebaseline review rather than rewriting the old decision.

### `complex-work`

Carry MD2-1 through mixed packages and require the implementation or review
leaf to report MD2-2 through MD2-5 where physical decomposition is in scope.
Do not copy the residual-inventory or fixed-point mechanics into
`complex-work`; their existing leaf owners remain authoritative.

## Target-repository contract template

A repository that makes modularization or layering an explicit architecture
goal should add one compact rule to its architecture authority:

```markdown
Semantic authority and physical source decomposition are orthogonal. A crate,
runtime, service, or adapter may remain the sole semantic and public authority
while private modules expose cohesive internal state, operations,
transactions, ABI adaptation, and evidence. Shared access to a central type,
state, lifecycle, transaction, or ABI constrains the boundary design but does
not justify physical colocation by itself. Retained colocation requires a
causal invariant that the smallest plausible complete private boundary would
break.
```

For an explicit modularization package, its contract matrix should require the
residual topology proof and zero required unknown dispositions. Its
architecture map should record, for each material private component:

- semantic authority;
- physical source path;
- state and lifetime;
- transaction boundary;
- dependency direction;
- public or ABI composition; and
- adjacent evidence.

The map describes current implementation. The selected architecture contract
and independent review decide whether that topology is accepted.

A glossary may explain `semantic owner` and `physical module boundary`, but it
must not turn current file placement into normative approval. Topology-specific
sentences should be explicitly descriptive or point to the architecture map.

Numbered reviews remain immutable. When later evidence invalidates a fixed
point, a new review should name the overturned decision, explain the violated
contract, rebaseline the complete affected scope, and preserve the old review
as historical evidence.

## Validation scenarios

| Scenario | Expected result |
|---|---|
| One runtime remains the sole language-semantic authority while private modules own heap, failure, publication, and loader operations | Accept when state, transactions, ABI composition, and dependencies remain direct and no semantic state is duplicated. |
| One central Rust type has cohesive inherent implementation blocks in private submodules | Treat as physical decomposition, not a second semantic owner. |
| One complete constructor or installation transaction moves behind a private module | Evaluate the complete transaction boundary; do not reject it because moving individual handles would be harmful. |
| A large generated file or genuinely cohesive algorithm has no plausible smaller responsibility boundary | `not-applicable` or `retained-with-proof`; size alone creates no finding. |
| An extraction adds forwarding methods, duplicated state, broad visibility, or bidirectional dependencies | Reject or redesign the extraction. |
| A review proves seven extracted modules are cohesive but does not inventory several large residual roots | Required coverage remains `unknown`; no modularization fixed point. |
| API, ABI, tests, and canonical gates pass after extraction | Clear preservation only; owner and locality cells require separate structural evidence. |
| Remaining work is described only as stateful, transactional, central-struct, lifecycle, ABI-sensitive, or cross-cutting | Insufficient retention proof; require a complete boundary design or keep the cell `unknown`. |

Static validation should verify that MD2-1 through MD2-6 each have one owning
skill or repository authority, links resolve, and no line-count threshold or
one-module-per-term rule was introduced.

Model-behavior validation should use paired fixtures that differ only in
whether the reviewer receives a weak partial extraction or a complete cohesive
transaction/module design. The model should reject the weak extraction without
using that rejection to dismiss the complete design.

## Implementation order

1. Add MD2-1 and its self-check to `add-architectural-guidances`.
2. Add the complete-boundary and retained-colocation proof to the
   architectural-scope decision authority.
3. Separate preservation from residual-topology coverage in
   `evidence-efficient-review`.
4. Carry the residual inventory through parent acceptance in
   `supervised-implementer-loop`.
5. Extend the `review-fixpoint` completion rule with zero unknown residual
   topology cells.
6. Add the narrow composition rule to `complex-work`.
7. Validate the static contract map and paired behavior fixtures, then run an
   independent review of the complete skill package.

Target-repository corrections should follow the same dependency order:
architecture invariant, modularization contract, glossary and architecture
map, implementation packages, exact-revision gate, then independent rebaseline
Tick.

## Acceptance

Accept this improvement when:

- semantic authority and physical decomposition are explicitly orthogonal in
  the single architecture-guidance authority;
- central state, lifecycle, transactions, central types, ABI work, and
  cross-cutting calls are never automatic retention justifications;
- the scope-decision process challenges the smallest complete plausible
  boundary and records a causal colocation invariant when retaining work;
- implementation and review carry a complete residual topology inventory for
  modularization packages;
- preservation and locality remain separate evidence lanes;
- required residual unknowns block modularization fixed point;
- behavior fixtures distinguish weak partial extraction from complete cohesive
  private decomposition; and
- an independent review reports no unresolved functional, workflow, or
  architectural defect.

This plan authorizes no target-repository refactor, skill implementation,
commit, publication, or installed-source mutation.

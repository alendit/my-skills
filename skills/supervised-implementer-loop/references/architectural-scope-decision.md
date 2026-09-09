# Architectural Scope Decision

Use this reference when implementation or parent review exposes non-local
impact, uncertain ownership, mechanism-coupled tests, physical source structure
that may hide distinct responsibilities, or a local fix that may preserve an
architectural problem. The primary supervisor owns the decision. The
implementer supplies evidence and proposals but never accepts its own branch.

In the semantic MCP workflow, realization returns architectural contradictions
and proposals as bounded semantic feedback. The parent resolves that decision;
it preferably obtains implementation facts through semantic inspection. Apply
the source-inspection procedures below behind tools or with the independent
reviewer when practical; targeted parent code reads remain available when needed. At slice acceptance, that reviewer supplies source-grounded
non-worsening evidence, normally without raw code, for the parent to evaluate. A design change invalidates affected evidence at its owning boundary.

## Contents

- Qualify the signal
- Bound the proper correction
- Choose the branch
- Prove non-worsening deferral
- Maintain one architectural follow-up ledger
- Carry the decision through acceptance

## Qualify the signal

Create one decision record before treating implementation friction as an
architecture signal:

| Field | Required evidence |
|---|---|
| Trigger | Behavior change, failed correction, or review observation |
| Contract | Stable contract IDs and observable behavior involved |
| Expected owner | Component that should decide and maintain the behavior |
| Actual impact | Owners, consumers, dependency edges, state/lifetime boundaries, and tests that must change |
| Causal path | Why the trigger forces that impact rather than merely accompanying it |
| Architecture property | Duplicated semantic authority, wrong dependency direction, split or misplaced state/lifetime ownership, wrong-owner public or compatibility surface, physical source decomposition that hides cohesive responsibilities or change boundaries, or decomposition frozen into durable tests |
| Desired direction | Intended semantic owner or dependency/state direction |
| Local-patch defect | Why the convenient local fix preserves the architecture property |

At least one architecture property must have source, dependency, state, or test
evidence. Non-local work is not itself proof. Do not qualify ordinary adapter
propagation, serialization at a real boundary, a cohesive multi-file owner
change, inherently end-to-end composition, unfamiliarity, slow tooling, or
difficult test editing without a causal architecture property.

For a physical-decomposition claim:

1. identify distinct responsibilities or change reasons;
2. establish causal locality cost from unrelated context or implicit coupling;
3. propose the smallest complete cohesive private boundary;
4. explicitly challenge designs around central types, shared state,
   transactions, lifecycle, and ABI adaptation; and
5. retain colocation only when a named causal invariant fails under that
   complete boundary.

Those design categories raise extraction risk and therefore receive explicit
boundary design. Record a partial helper, handle, or forwarding-only failure as
evidence about that candidate, then evaluate the complete boundary separately.
Use file length, symbol count, history, outline depth, and tool or context
truncation to prioritize analysis. Classify generated source, a cohesive
algorithm, language-mandated colocation, or mostly inline tests from the same
causal responsibility evidence.

When source, dependency, state, or test evidence qualifies a physical-
decomposition defect, branch selection must carry the required physical-
decomposition coverage for the affected roots. Before accepting an affected
package, the primary supervisor must choose one of two paths: obtain caller
authority that makes physical decomposition explicit in the package contract
and apply the
[residual-topology profile](contract-and-scenario-package.md#profile-modularization-roots)
plus its existing review and fixed-point rules; or retain the required residual
coverage as `unknown` and select scope stop. The ordinary lightweight placement
disposition and a no-worsening deferral cannot clear a qualified defect, and the
caller-approved scope must not be broadened silently.

For a test-locality claim, apply the alternate-implementation challenge: show
that an independently designed correct implementation preserving the stable
contract would fail the current test because the test freezes private
decomposition. Repeated editing effort alone is implementation friction.

## Bound the proper correction

Record the smallest correction that moves the causal property to its intended
boundary:

| Scope dimension | Required bound |
|---|---|
| Owners | Semantic owners whose authority or representation changes |
| Consumers | Representative compositions affected by the owner change |
| Contracts | Stable public or owner-level contracts changed or preserved |
| Dependencies | Edges introduced, removed, or reversed |
| State | Migration, lifetime, synchronization, and cleanup consequences |
| Compatibility | Real public, persisted, wire, deployment, or caller obligations |
| Evidence | Contract tests to retain, strengthen, replace, or delete |
| Documentation | Owning contract or architecture authority that changes |
| Removal | Obsolete path, shim, duplicated policy, state, or tests eliminated |

Follow the causal owner and required compositions. Do not use the current diff
as the scope boundary, and do not expand a bounded correction into a
full-system rewrite.

## Choose the branch

Use this ordered flow:

| Branch | Condition | Required action |
|---|---|---|
| Correct now | The proper bound fits the caller-approved package and does not endanger its useful fixed point. | Update the owning contract once if needed, reclassify affected tests, correct the architectural boundary, remove the obsolete path, and resume the slice. |
| Defer safely | The current contract is satisfied, every applicable non-worsening dimension below is unchanged or improved, and a durable authorized follow-up can be created or updated. | Apply the containment fix, persist the follow-up, and continue. |
| Reevaluate | A proposed minimal fix worsens any dimension. | Reject ordinary deferral and find the smallest architecture-preserving intermediate correction inside the proper bound. If it fits existing authority, correct now. |
| Scope stop | No bounded non-worsening route fits the caller-approved outcome or a durable authorized follow-up cannot be recorded. | Stop before production changes. Give the caller the rejected option, smallest known proper correction, scope drivers, and decision required. |

The primary supervisor selects and accepts a branch within the caller-approved
outcome. An outer workflow may propose a branch, but it does not expand that
authority. Only the caller or another explicit package-scope authority may
approve a material outcome or scope expansion at a scope stop.

Use a design checkpoint to select one explicit outcome: keep the work in the
current package, obtain authority for a narrower package contract, or record
the required coverage as `unknown`. A package that promises modularization or
physical decomposition reaches fixed point after its central stateful,
transactional, lifecycle, and ABI work is completed or removed from scope by
the authorized narrower contract.

An architecture-preserving intermediate correction must satisfy the current
contract, prevent new consumers or dependencies from relying on the defect, and
reduce or leave unchanged later removal cost. Enforcing an invariant at its
existing owner or adding contract-level coverage without a new public mechanism
may qualify.

## Prove non-worsening deferral

Record **improved**, **unchanged**, **worsened**, or **not-applicable** with a
short source- or delta-backed reason for every dimension:

| Dimension | Question |
|---|---|
| Dependency direction | Does the fix introduce or widen an edge in the wrong direction? |
| Semantic authority | Does it add an owner or policy copy? |
| State and synchronization | Does it add durable state, extend lifetime, or add coordination? |
| Durable surface | Does it expand a public, persisted, wire, or compatibility contract? |
| Transitional burden | Does it add a fallback, shim, dual path, or temporary abstraction that must later be removed? |
| Test coupling | Does it freeze a temporary mechanism into durable tests? |
| Physical decomposition | Does it add a distinct responsibility to a source unit or make a cohesive change require more unrelated context? |
| Exposure | Does it expose the defect to more consumers? |
| Failure visibility | Does it hide the defect or weaken observable failure? |
| Remediation cost | Does it increase migration, removal, or eventual correction cost? |

Explain **not-applicable**; do not use an arbitrary score. Any **worsened**
disposition selects reevaluation, not safe deferral.

## Maintain one architectural follow-up ledger

Reuse the project's existing issue, architecture-debt, or feature ledger. Do
not create a competing TODO list. If none exists, the caller must select one
durable project authority before deferral. External issue creation or mutation
remains separately authorization-bound; local ledger mutation follows the
caller's and repository's authorization. When no authorized durable record can
be written, safe deferral is unavailable and the decision becomes a scope stop.

Use the ledger-issued stable ID. Dedupe by this semantic identity:

    affected contract or semantic owner
    + undesired dependency or state relation
    + desired owner or direction

Each record contains:

- stable ID and status;
- the qualifying signal record and affected contract or owner;
- concise architectural problem and desired direction;
- short remediation direction, not a speculative complete design;
- reason it is outside the current package;
- containment fix and every non-worsening disposition;
- affected areas and principal scope drivers;
- revisit trigger or prerequisite; and
- originating finding, decision, or handoff links.

Apply this lifecycle:

- **Create** only after the current contract passes and every applicable
  non-worsening dimension is unchanged or improved.
- **Update** the same identity when evidence, containment, affected scope,
  remediation direction, or revisit trigger changes.
- **Dedupe** overlapping observations into that identity; preserve new origin
  links and stronger evidence.
- **Close** only with source or behavior evidence that the desired boundary now
  holds and obsolete containment has been removed.
- **Mark stale** when its contract, owner, evidence, or prerequisite is
  invalidated. Revalidate it, close it, or supersede it with a link; never drop
  it silently.

Follow-ups are non-gating by default. They become gates only when an accepted
contract or explicit work package activates them.

## Carry the decision through acceptance

Before accepting the affected slice, independently verify the decision record,
proper-correction bound, selected branch, current-contract evidence, and any
non-worsening dispositions. Verify the authorized ledger write by reading back
the stable record; a proposed or failed write does not make deferral durable.

The implementer handoff and final package handoff list created, updated, closed,
stale, and unchanged-but-relevant follow-up IDs. A current contract violation,
unresolved defect, required unknown coverage, or worsening patch cannot be
relabeled as a follow-up to make the slice acceptable.

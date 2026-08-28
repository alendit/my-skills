# Observation: Implementation Mechanisms Can Displace the Behavioral Goal

## Purpose

This note records a design-process failure observed during the Feature 88 and
Feature 90 context-management work in `e`. It is an observation document, not
an improvement plan. It does not select a replacement design, prescribe a
particular carrier or record shape, or decide which existing implementation
must be retained.

The case began with a behavioral goal: after consuming ephemeral context, the
model should be able to retain useful information or explicitly report that it
considered the information and retained nothing. The explicit negative outcome
was important because ordinary model narration could not distinguish “noticed
and rejected” from “never noticed.”

During specification and implementation, several mechanisms introduced to
support that goal became treated as if they were the goal itself. The process
then optimized their local correctness and durability even when their
relationship to the original behavior had become indirect.

## Observed design drift

The design eventually described context management through concepts including:

- an exhaustive four-key carrier with separate `keep`, `summaries`, `drop`,
  and `erase` arrays;
- distinct versioned promotion and erasure record families;
- an atomic package coordinating optional promotion and erasure components;
- selected-path erasure queries and checkpoint retention rules;
- a receipt projection whose survival distinguished `drop` from `erase`; and
- material carrier identities tied to the exact wire schema.

Each mechanism had a locally coherent explanation. Exact carrier keys made
validation deterministic. Separate records represented different semantic
effects. Atomicity prevented a mixed response from becoming partially visible.
Path-scoped queries prevented one branch from suppressing another. Material
identity kept cache and provider evidence honest.

The aggregate design nevertheless became difficult to relate directly to the
original goal. In particular, “four-key carrier” and “atomic promotion plus
erasure” began to appear in progress and acceptance statements as primary
outcomes. Neither phrase describes what a user or model is trying to accomplish
with context management. They describe consequences of the selected encoding
and persistence decomposition.

## A derived feature created a new semantic distinction

The most visible example is the distinction between `drop` and `erase`.

The original negative curation requirement was structurally similar to “drop”
or “retain nothing”: the model explicitly acknowledges the source without
retaining its value. Feature 90 later introduced compact invocation receipts as
an automatic projection derived from tool activity. The design allowed a
receipt to survive `drop`. Once that decision was made, another negative
disposition was needed to express “remove the source and also suppress its
receipt.” That disposition became `erase`.

The new distinction may represent a real product need, but the observed process
did not first establish that agents or users needed both outcomes. Instead, a
derived projection changed the meaning of the existing negative operation, and
the context-management protocol grew another semantic state to accommodate the
projection.

This reverses the expected direction of design authority. A supporting
projection should not silently redefine the behavioral goal it was introduced
to support. When it does, the process needs to distinguish a discovered product
requirement from mechanism-induced complexity.

## Decomposition generated its own atomicity problem

The design also separated retained values into a version-3 promotion record and
suppression authority into a version-1 erasure record. A mixed curation decision
could therefore produce two semantic components. That decomposition created a
correctness requirement: both components must become visible together or not at
all before the ephemeral frame is consumed.

The local invariant is reasonable. A response should not be applied halfway.
The scale of the resulting obligation, however, depended on the prior choice to
represent one model decision through multiple durable record families. The
specification expanded the invariant across direct writes, queued writes,
controller-backed persistence, checkpoints, replay interruption, duplicate
effects, and branch projection.

At that point “atomic durability” looked like an inherent context-management
requirement even though much of the transaction problem had been introduced by
the selected storage decomposition. The process reviewed how to make the
mechanisms compose safely without reopening whether those mechanisms were the
simplest faithful representation of one curation decision.

## Mechanisms became normative through specification

The drift was reinforced by the specification and fixed-point process:

1. A plausible mechanism was selected to express part of the behavior.
2. The specification gave the mechanism an exact schema, version, owner, and
   evidence matrix.
3. Review correctly found inconsistencies and missing edge cases within that
   mechanism.
4. Remediation added persistence, identity, compatibility, and test machinery.
5. Later reviews treated the accumulated machinery as accepted scope rather
   than revisiting whether it remained necessary for the behavioral goal.

This is a design-level contract ratchet. Precision improves the correctness of
the selected design, but it can also make an early design choice expensive to
question. The process becomes increasingly capable of proving that the local
mechanisms are internally consistent while becoming less likely to compare
them with a simpler semantic model.

## Observable symptoms

The context-management run exhibited several symptoms of mechanism drift:

- Progress was reported in terms of carrier revisions, codec versions,
  checkpoint ownership, and record byte ceilings rather than a model
  successfully managing later context.
- A derived receipt projection caused the negative curation vocabulary to
  expand.
- Multiple durable components created a transaction requirement that then
  became a substantial implementation package.
- Internal owner suites passed while the real carrier could not yet submit the
  new decision.
- Review repeatedly strengthened branch, replay, and checkpoint behavior before
  the basic end-to-end operation was available.
- The implementation accumulated public-looking APIs and record types before a
  consumer proved their final shape.
- The process could explain why every mechanism was correct but had difficulty
  explaining why all of them were necessary to satisfy the original goal.

None of these symptoms proves that a specific mechanism is wrong. Durable
context management can require provenance, branch isolation, replay behavior,
and truthful provider identity. The failure is allowing the selected mechanisms
to avoid renewed comparison with the behavioral requirement as their cumulative
cost and interactions become visible.

## Distinctions preserved by this observation

- A wire carrier must have some concrete shape; the observation does not imply
  that schemas are unnecessary.
- Applying one semantic decision halfway is undesirable; the observation does
  not endorse partial state.
- Receipts may be useful context; the observation does not decide their default
  lifetime.
- Branch and replay correctness remain important when durable suppression
  authority exists.
- Exact provider and cache identities are necessary when external evidence
  depends on a material request shape.
- Removing mechanisms is not automatically simpler if their responsibilities
  reappear as implicit coupling elsewhere.

The open issue is whether these responsibilities require the particular set of
semantic distinctions, record families, and coordination boundaries that the
current design accumulated.

## Iterative design implication

An iterative process should review not only whether the implementation matches
the accepted design, but also whether the design's mechanisms remain
proportionate and directly traceable to the implementation goal.

When a supporting feature changes the core vocabulary, one semantic decision
requires several durable records, or most acceptance language describes
internal machinery, the process should explicitly consider a design rebaseline.
That rebaseline may retain the design, simplify it, or discover a missing
behavioral requirement. The important action is to reopen the comparison rather
than allowing the existing specification to decide by inertia.

This implication does not prescribe continuous redesign. Re-evaluation should
be triggered by concrete evidence that cumulative mechanism cost, newly
introduced distinctions, or weak end-to-end progress has changed the original
design tradeoff.

## Questions left open

- What are the minimum externally observable outcomes required for explicit
  context curation?
- Does the product need two negative dispositions, or did receipt projection
  create that distinction?
- Which information belongs in one semantic curation decision, and which facts
  genuinely require independent owners or lifetimes?
- When does one durable decision require transaction semantics beyond a single
  record append?
- Which branch, replay, and checkpoint guarantees follow from the behavioral
  goal, and which follow only from a selected persistence representation?
- What evidence should cause a fixed-point review to reopen an accepted design
  mechanism instead of continuing to remediate it?
- How should progress reports keep the behavioral outcome visible when precise
  internal contracts are also necessary?

These questions require a separate design decision. This document authorizes no
skill or implementation change by itself.

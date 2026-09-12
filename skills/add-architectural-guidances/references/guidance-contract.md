# Compact Architecture Guidance Contract

This is the single authority for policy inserted by the skill. Adapt wording to
the target repository, but preserve the outcomes without duplicating them.

## Hard constraints

- Shape a work package as a useful stopping point that moves toward the final
  direction. If work stopped after the package, the project should be better
  off than if it had not been built; individual internal slices need not meet
  that test.
- Treat non-local impact as an architecture signal only when causal ownership,
  dependency, state, or test evidence supports it, not because work spans many
  files or takes effort. Bound the smallest proper correction and do it now
  when it fits the accepted scope. Defer only with current-contract-satisfying,
  non-worsening containment and one authorized durable follow-up. Reevaluate a
  worsening fix for the smallest architecture-preserving correction; when no
  bounded safe route fits, stop for an explicit scope decision.
- Match flexibility to evidence. Make likely changes cheap, keep uncertain
  decisions local and reversible, and model stable behavior directly. Add an
  abstraction only for a real, substitutable contract that makes a likely
  change cheaper.
- Place state with the component that owns its meaning, at the lowest durability
  and smallest scope satisfying the requirement. Persist durable facts, user
  intent, and stable configuration; keep derived, high-churn, presentation, and
  cache state near its runtime owner unless cross-restart behavior is required.
- Give each behavior one cohesive semantic owner and one primary reason to
  change. Keep business policy out of UI, transport, persistence, provider,
  webhook, and tool glue.
- Keep physical source decomposition aligned with cohesive responsibilities.
  When one semantic owner contains responsibilities with distinct reasons to
  change, expose meaningful internal source boundaries so each can be
  understood, changed, and reviewed without unrelated context. Treat size and
  context cost as signals only, not proof that decomposition is defective.
- Separate semantic authority from physical source decomposition during design.
  Keep one component as the sole semantic and public authority where
  appropriate, then place cohesive internal state, operations, transactions,
  ABI adaptation, and evidence behind private source boundaries. Use shared
  access to a central type, state, lifecycle, transaction, or ABI to shape those
  boundaries. When physical decomposition is explicitly in scope or a causal
  decomposition defect is qualified, a retained colocated responsibility names
  the invariant that the smallest plausible complete private boundary would
  break. Ordinary changes need only explain their changed owner's cohesion.
- Make dependencies point from unstable shells and adapters toward stable,
  domain-owned contracts. Keep side effects at shell or adapter boundaries and
  do not combine unrelated domains in one coordinator.
- Keep public interfaces narrow and consumer-shaped. Do not require unused
  capabilities or let implementations substitute only by weakening behavior,
  narrowing preconditions, ignoring requirements, or throwing unsupported
  errors.
- State compatibility requirements explicitly. Retain legacy paths only for a
  real caller, persisted artifact, deployment, or user workflow; otherwise
  remove obsolete paths.
- Handle expected errors at the layer able to make the domain decision. Do not
  add broad fallback, defensive normalization, or swallowed errors; surface
  unexpected failures visibly.
- Classify performance evidence as either a gate with a named baseline,
  measurement method, direction, and regression threshold, or as explicitly
  observational telemetry that cannot decide acceptance.
- Make an exact cap, timeout, retry count, or other numeric limit normative only
  with a correctness role, workload basis, resource estimate, exact/one-over
  consequence, and revision trigger. Otherwise keep it as a private
  implementation default and test it only as mechanism evidence.

## Required self-check for design-sensitive changes

Check the questions relevant to the changed decisions and their affected
dependencies. Reuse current evidence for unchanged decisions; do not generate
an answer or not-applicable record for every question on every edit. Expand to
the full affected scope when evidence invalidates that boundary or repository
policy explicitly requires it. These applicability instructions belong in the
installed policy alongside the questions.

1. Is this package a useful stopping point, and what final direction does it
   advance?
2. Which decisions are likely, uncertain, or stable, and are uncertain choices
   local and reversible?
3. Who owns each changed behavior, does that owner remain cohesive, and which
   source boundary receives it? Does the change improve, preserve, or worsen
   reviewable physical decomposition? When decomposition is selected or a
   causal defect is qualified, for each affected retained responsibility what invariant requires
   colocation after challenging the smallest plausible complete private
   boundary? Have central state, lifecycle, transactions, ABI work, and private
   access been treated as design inputs rather than automatic exemptions?
4. What state changes, who owns it, how long should it live, and can it be
   rebuilt from more durable facts?
5. Do dependencies and side effects remain on the correct side of stable
   boundaries?
6. Are abstractions and interfaces real, narrow, substitutable, and tied to a
   likely change?
7. Which compatibility requirement applies, and which obsolete path was
   removed?
8. Where are expected errors decided and unexpected errors surfaced?
9. Which performance evidence is thresholded, and which is observational?
10. For every exact normative limit, what justifies the value and what evidence
    would permit changing it?
11. Which focused scenarios prove stable behavior without freezing private
    representation?
12. For a causal non-local architecture signal, is the smallest proper
    correction done now, safely contained with one authorized durable
    follow-up, reevaluated if worsening, or stopped for explicit scope?

# Compact Architecture Guidance Contract

This is the single authority for policy inserted by the skill. Adapt wording to
the target repository, but preserve the outcomes without duplicating them.

## Hard constraints

- Shape a work package as a useful stopping point that moves toward the final
  direction. If work stopped after the package, the project should be better
  off than if it had not been built; individual internal slices need not meet
  that test.
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

1. Is this package a useful stopping point, and what final direction does it
   advance?
2. Which decisions are likely, uncertain, or stable, and are uncertain choices
   local and reversible?
3. Who owns each changed behavior, and does that owner remain cohesive?
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

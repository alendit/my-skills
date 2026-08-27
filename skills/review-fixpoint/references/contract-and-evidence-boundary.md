# Contract and Evidence Boundary

Use this reference throughout Tick and Tock. `$evidence-efficient-review` owns
normalization and evidence classification; this reference defines how the
fixpoint workflow consumes that authority.

## Contents

- Preserve one contract authority
- Keep workflow mechanics out of feature artifacts
- Apply evidence classes to completion
- Separate external scenarios
- Keep tests stable across redesigns

## Preserve one contract authority

Treat the normalized contract-and-evidence matrix as the feature's sole
normative requirement authority. Map every finding and remediation slice to
stable contract IDs. During Tock, edit each owning row once. Update another
artifact only when its distinct responsibility changed; otherwise replace its
copy of the requirement with an ID reference.

Decisions, risks, slice plans, acceptance prose, implementation handoffs, and
architecture documents may add information specific to their purpose. They
must not paraphrase a contract into a second normative definition.

## Keep workflow mechanics out of feature artifacts

Feature artifacts own:

- feature semantics, semantic owners, and explicit non-goals;
- stable contract IDs and feature-specific review targets;
- named deterministic, external, and observational evidence; and
- the current status of required external capabilities.

This skill owns Tick/Tock selection, review-artifact lifecycle, phase commits,
reviewer selection and independence, exact-revision gate timing, remediation
repetition, and stop mechanics. A feature artifact may require independent
review and link to this workflow, but must not copy those mechanics. The durable
review artifact declared by repository guidance owns findings and dispositions;
an implementation handoff owns revision-specific commands and results.

## Apply evidence classes to completion

Consume the evidence class and status recorded by `$evidence-efficient-review`:

| Evidence class | Fixpoint effect |
|---|---|
| Deterministic release gate | Must pass on the exact reviewed revision before deterministic fixed point. |
| External compatibility evidence | Confirms or disproves the named external capability; availability failures remain visible but do not make deterministic gates fail. |
| Observational telemetry | Informs follow-up only; without a named baseline and regression threshold it neither establishes nor blocks deterministic acceptance. |

Use this result vocabulary:

| Result | Meaning |
|---|---|
| `deterministic-fixed-point` | An independent Tick by the loop's persistent reviewer finds no P0-P3 defect, all required deterministic cells are cleared, exact-revision gates pass, and no valid external product-contract failure or activated follow-up remains unresolved. Legitimate non-gating architectural follow-ups may remain visible. |
| `capability-confirmed` | Every required external capability has current or reusable successful evidence under its identity and freshness rule. |
| `capability-unconfirmed` | Required initial evidence is missing or has status `stale`, `unavailable`, `authentication-or-configuration-failure`, `provider-or-infrastructure-failure`, or `inconclusive-timeout`. The capability has not passed or failed. |
| `external-contract-failed` | A valid external run produced `product-contract-failure`; the external contract is false and must return to design or remediation. |
| `Done` | Deterministic fixed point and every required external capability are confirmed, with current documentation and required repository status gates. |

Only a valid `product-contract-failure` disproves an external contract. Never
convert missing credentials, provider unavailability, infrastructure failure,
or timeout into a product finding. Never report missing initial evidence as a
pass. The remediation loop may stop at `deterministic-fixed-point` when no code
defect remains, but the handoff must retain `capability-unconfirmed` and must not
claim the capability or `Done`. A valid `product-contract-failure` prevents
`deterministic-fixed-point` until the contradicted contract returns through
design or remediation.

## Separate external scenarios

When endpoint capability and product composition both matter, require two
separately reportable scenarios using shared instrumentation:

1. a minimal credentialed capability probe that isolates the endpoint behavior;
2. a broader semantic scenario that composes product ownership and public
   behavior.

Keep deterministic owner and composition coverage for behavior under repository
control. A monolithic external witness must not be the sole evidence for
serialization, tools, diagnostics, connection identity, contamination, and
model output. Carry each scenario's disposition independently through Tick.

## Keep tests stable across redesigns

Use contract tests for stable public semantics, ownership, boundedness, and
recovery. Prefer focused scenarios and adjacent semantic boundaries over one
broad witness. Use mechanism tests only when their decomposition is itself a
stable contract or as explicitly disposable development evidence.

Whenever a specification or owning design changes, classify affected tests as
`retain`, `strengthen`, `replace`, or `delete`. Ask whether a simpler
independently designed correct implementation could pass before retaining a
test. A conformance label is only an index; evidence must name the observable
invariant its assertions establish.

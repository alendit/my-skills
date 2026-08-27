# Improvement Plan: Better Fixpoint Sequencing

## Purpose and composed authority

Make long review-fixpoint packages converge with fewer duplicated gates,
unchanged external reruns, stale evidence updates, and silent delegated-agent
waits. Preserve the existing separation of responsibilities:

- `review-fixpoint` owns Tick/Tock order, exact-revision checkpoints, and the
  fixed-point decision;
- `supervised-implementer-loop` owns ordered implementation slices and parent
  acceptance;
- `evidence-efficient-review` owns independent review mechanics and evidence
  classification; and
- the target repository owns language-specific validation, compatibility, and
  artifact conventions.

The BS1-BS7 matrix below is the sole authority for this improvement. Later
sections provide proposed wording, routing, implementation order, and evidence;
they do not add independent requirements.

## Problem statement

The current skills contain most of the right principles, but leave several
important transitions underspecified:

1. `review-fixpoint` is installed as a reusable skill while its description and
   phase mechanics still hard-code a `clojure-wasm` stage, Rust/Clippy gates,
   and a Clojure-specific cleanup example.
2. External diagnostic runs and authoritative acceptance runs have no explicit
   sequencing boundary. A workflow can record live evidence and update ledgers
   before an independent Tick reviews the evidence owner, forcing evidence and
   documentation to be regenerated after later findings.
3. `supervised-implementer-loop` says to wait a bounded interval for a stalled
   implementer, but does not define progress checkpoints or the one-request,
   one-interrupt escalation path.
4. An external semantic failure can be rerun unchanged before the capture
   distinguishes provider behavior, product behavior, and test-harness error.
5. The implementation-review seam list names identity and provenance broadly,
   but does not require two high-risk proofs: audit identity for control-only
   responses and effective wire identity for external evidence records.
6. A long delegated Tick need not report contract-cell progress before its
   final result, making useful review work look stalled.

The goal is not to make every run shorter. It is to ensure that each expensive
or external action either establishes a new fact or is deferred until its
result can remain valid.

## Authoritative contract-and-evidence matrix

| ID | Observable contract | Semantic owner and public composition | Slice | Named evidence |
|---|---|---|---|---|
| BS1 | **Keep the outer workflow repository-neutral.** `review-fixpoint` describes a selected repository work package and obtains compatibility policy, review-artifact convention, and canonical gates from repository guidance. It contains no unconditional Rust, Clojure, ABI, Clippy, or numbered-stage requirement. | `review-fixpoint` owns generic Tick/Tock mechanics; the target repository owns local policy and commands. | S1 | D1 repository-neutral source audit |
| BS2 | **Separate diagnostic execution from authoritative external acceptance.** Live execution during Tock is diagnostic and non-reusable unless an independent Tick has cleared every repository-controlled owner material to the record. Authoritative external scenarios run once on the exact accepted implementation commit; material owner changes invalidate them. | `review-fixpoint` owns ordering; the feature contract owns scenario identity and freshness; `evidence-efficient-review` audits reuse. | S2 | M1 diagnostic-to-acceptance sequence |
| BS3 | **Make delegated progress observable and bounded.** An implementer reports long-running commands and periodic compact checkpoints. The parent uses one status request, one bounded follow-up wait, and at most one interrupt before inspecting stable work and resuming with a delta-only assignment. | `supervised-implementer-loop` owns implementation delegation; the parent remains acceptance authority. | S3 | M2 active, silent, and completed implementer schedules |
| BS4 | **Do not repeat an unchanged external failure without new localization evidence.** A failed external semantic scenario records the effective request, relevant presentation, submitted action, owner state, resulting identity, and violated invariant. A rerun requires improved capture or a changed implementation. | The scenario package owns diagnostic capture; the product owner and provider boundary retain behavior. | S4 | M3 external-failure localization ladder |
| BS5 | **Bind control-only durable effects to their own event.** Reviews of a response or transaction that commits durable state without ordinary user, assistant, or tool content prove that the committed record binds to a truthful resolvable event rather than a preceding or later neighbor. | `evidence-efficient-review` owns the review question; the target implementation owns response identity and persistence. | S5 | M4 control-only provenance challenge |
| BS6 | **Derive external evidence identity from effective requests.** Reviews trace endpoint, model, transport, store mode, and other material identity from captured native requests or metadata, challenge defaults and overrides, and reject passing records when requests within one scenario disagree. | `evidence-efficient-review` owns the review seam; the adapter/evidence boundary owns effective identity. | S5 | M5 declared/effective identity challenge |
| BS7 | **Expose review progress without turning checkpoints into findings.** A delegated review reports compact cleared/candidate/unknown state after a material contract-cell cluster and before a final gate. Checkpoints neither decide findings nor alter review independence. | `evidence-efficient-review` owns sequential cell review; the outer caller owns status communication. | S6 | M6 multi-cell delegated-review trace |

## Proposed skill changes

### BS1: generalize `review-fixpoint`

Apply BS1 across the four review-fixpoint package owners named below. In
`skills/review-fixpoint/SKILL.md`, replace the current description with:

```yaml
description: >-
  Alternate independent implementation reviews with principled remediation
  until a selected repository work package reaches a functional and
  architectural fixed point. Use when asked to address review findings,
  review remediations, run another review round, or keep iterating until no
  actionable implementation defects remain.
```

Replace “the next numbered review in the selected stage's review directory”
with a project-declared review-artifact rule:

```markdown
Create or update the review artifact required by repository guidance. Prefer a
new immutable numbered review when the project declares that convention;
otherwise use its append-only Tick ledger or other explicit review authority.
Never silently replace historical findings or dispositions.
```

In `skills/review-fixpoint/agents/openai.yaml`, generalize the default prompt to
a selected repository work package. In
`skills/review-fixpoint/references/contract-and-evidence-boundary.md`, replace
review-numbering ownership with a generic review-artifact lifecycle and assign
findings and dispositions to the durable review artifact declared by repository
guidance.

In `skills/review-fixpoint/references/phase-mechanics.md`, replace the
language-specific cleanup and gate text with:

```markdown
Repository guidance supplies compatibility policy, cleanup constraints, and
canonical verification commands. Do not invent language-specific gates.

Reject a local repair that preserves faulty ownership, a prohibited
compatibility shim, silent downgrade, reproducer-specific branch, or limit
bypass. Apply only the prohibitions established by the target repository and
selected contract.

At minimum preserve:

- focused owner tests and public regressions;
- repository formatting, lint, and compile checks;
- the project-declared complete deterministic gate;
- conformance or fixture checks relevant to changed contracts; and
- benchmark assertions only where the contract names a performance bound.
```

### BS2: sequence external diagnostics and acceptance

Add this section to `skills/review-fixpoint/SKILL.md` after “Verify Each Tock”:

```markdown
## Sequence External Diagnostics And Acceptance

Treat live external execution during Tock as diagnostic unless every
repository-controlled owner material to the evidence record has already passed
an independent Tick.

1. Prove repository-controlled owner and composition behavior deterministically.
2. Commit the accepted implementation and run its exact-revision deterministic
   gate.
3. Run the independent Tick before generating authoritative external acceptance
   evidence.
4. If live behavior is needed earlier to localize a defect, label that run
   diagnostic and non-reusable. Do not update capability ledgers from it.
5. After a zero-finding repository Tick, run each required external scenario
   once against the exact implementation commit.
6. Update evidence and status ledgers, then run an incremental Tick limited to
   the changed evidence owner and documentation.
7. Invalidate affected records after any change to a material request,
   response, identity, capture, or finalization owner.

If diagnostic or acceptance execution reveals a repository defect, return to
Tock. Do not retain the run as acceptance evidence merely because unrelated
fields passed.
```

This sequencing permits an early live probe when provider behavior is genuinely
unknown, but prevents that probe from becoming durable acceptance prematurely.

### BS3: define implementer progress and stall handling

In `skills/supervised-implementer-loop/SKILL.md`, replace the current stalled-
turn bullet with:

```markdown
### Progress And Stall Protocol

- Before a command likely to exceed 60 seconds, the implementer reports the
  exact command, its purpose, and whether it may edit the tree.
- While work continues, the implementer sends a compact checkpoint at least
  every 60 seconds: changed files, current hypothesis, last completed result,
  and active command or explicit `no command running`.
- The implementer does not start a broad or complete suite until the parent has
  accepted the focused slice, unless the slice contract explicitly requires it.
- On apparent silence, the parent checks the active process and whether the
  shared diff is changing, sends one status request, and waits one additional
  60-second interval.
- If neither activity nor response appears, interrupt once. Inspect stable
  edits directly and resume the same implementer with a delta-only assignment.
- Do not create repeated status-only turns or repeatedly interrupt an active
  foreground gate.
```

The exact interval is an orchestration default, not a performance expectation
or acceptance metric.

### BS4: localize before repeating external scenarios

Add this section to
`skills/supervised-implementer-loop/references/contract-and-scenario-package.md`:

```markdown
## Localize Before Repeating External Scenarios

After an external semantic assertion fails, do not rerun the unchanged scenario
until available evidence distinguishes the live hypotheses.

Capture one structured diagnostic tuple:

- effective request identity and material request shape;
- exact external presentation relevant to the assertion;
- submitted external action or request arguments;
- semantic-owner state used to validate or commit it;
- resulting durable or runtime identity; and
- the violated invariant.

Classify the failure as provider behavior, product behavior, evidence-harness
behavior, or still unknown.

If the first record is insufficient, improve the capture before one additional
run. Never rerun solely because prior output was truncated: preserve the
complete structured record in a temporary artifact and summarize it separately.

Once localized, add or strengthen deterministic owner and composition coverage
before another acceptance run.
```

### BS5-BS6: add mandatory implementation-review seams

Add these subsections after “Challenge implementation seams” in
`skills/evidence-efficient-review/references/implementation-review.md`:

```markdown
### Control-Only Durable Identity

When a response or transaction can commit durable state without ordinary user,
assistant, or tool content, identify the durable event representing that
response. Prove that committed records, lifecycle events, and recovery state
bind to that event rather than a preceding or later neighboring entry. Cover
success, preparation failure, repeated invocation, reopen, and branch or fork.

### Effective Evidence Identity

For evidence-producing code, trace endpoint, model, transport, store mode, and
other capability identity from the effective observed request rather than only
from selected configuration.

Challenge:

- omitted optional configuration and adapter defaults;
- caller or backend overrides;
- declared/effective mismatches;
- disagreement among requests in one scenario; and
- partial capture before failure.

A passing record requires every material request to agree on effective
identity. Otherwise preserve the original execution outcome but classify the
evidence record invalid or unavailable.
```

These are review questions, not new application mechanisms. Each applies only
when the selected contract has the corresponding durable-effect or external-
evidence surface.

### BS7: add delegated-review checkpoints

Add this paragraph after “Review Contract Cells Sequentially” in
`skills/evidence-efficient-review/SKILL.md`:

```markdown
For a delegated review expected to span several minutes, send a checkpoint
after each material contract-cell cluster and before the final gate. Report only
cleared, candidate, unknown, and not-applicable cells; the active command; and
the next question. A checkpoint is neither a finding nor a final decision.

Do not delay an available candidate disposition merely to finish unrelated
cells, and do not rerun completed cells in response to a status request.
```

## Ordered implementation slices

### S1 — Remove repository-specific assumptions

Implement BS1 first. Update `skills/review-fixpoint/SKILL.md`,
`skills/review-fixpoint/agents/openai.yaml`,
`skills/review-fixpoint/references/phase-mechanics.md`, and
`skills/review-fixpoint/references/contract-and-evidence-boundary.md` together
so the entrypoint, interface prompt, phase policy, and evidence boundary cannot
disagree about repository scope, review-artifact convention, or canonical
gates.

### S2 — Establish the external-evidence phase boundary

Implement BS2 in `review-fixpoint`. Reconcile the new sequence with the existing
fixed-point and capability-status vocabulary without making external
availability a deterministic gate.

### S3 — Make implementation progress observable

Implement BS3 in `supervised-implementer-loop`. Preserve one persistent
implementer and parent acceptance while replacing repeated unbounded status
waits with one explicit escalation sequence.

### S4 — Add the external diagnostic ladder

Implement BS4 in the scenario-package reference. Keep diagnostic capture
private and disposable; do not turn its field layout into a product contract.

### S5 — Strengthen review seams

Implement BS5-BS6 in the implementation-review reference. Exercise both seams
with source packets that include neighboring durable events, omitted defaults,
overrides, and mixed request identities.

### S6 — Add review progress checkpoints

Implement BS7 last. Verify that checkpoints expose progress without leaking
expected findings into the reviewer or changing its final decision authority.

## Scenario portfolio

| Scenario | Contracts | Observable invariant | Evidence class | Localization signal |
|---|---|---|---|---|
| D1 repository-neutral source audit | BS1 | Generic workflow sources contain no unconditional language, ABI, toolchain, or artifact-layout assumptions | deterministic repository | offending path and phrase |
| M1 diagnostic-to-acceptance sequence | BS2 | Early live failure remains diagnostic; authoritative evidence is emitted once only after the independent repository Tick and is invalidated by a material owner change | deterministic repository | phase and evidence-status trace |
| M2 implementer schedules | BS3 | Active long command reports progress, silent idle work receives one request and one interrupt, completed work hands off without interruption | deterministic repository | ordered delegation trace |
| M3 external-failure localization ladder | BS4 | An unchanged failed selector is not repeated; the next run follows an expanded capture or implementation change and identifies the owning boundary | deterministic repository | run identity plus diagnostic tuple |
| M4 control-only provenance challenge | BS5 | Reviewer detects durable state bound to a neighboring event and clears a corrected response-owned identity across reopen/fork | deterministic repository | record/event identity comparison |
| M5 declared/effective identity challenge | BS6 | Reviewer rejects profile-derived evidence when native request defaults, overrides, or per-request identities disagree | deterministic repository | declared, effective, and recorded identity tuple |
| M6 multi-cell delegated-review trace | BS7 | Reviewer emits compact cell checkpoints and one final result without treating checkpoints as findings | deterministic repository | ordered review messages |

## Evidence and completion

Completion requires:

1. source and link checks for every changed skill and one-level reference;
2. D1 proving removal of unconditional repository-specific assumptions;
3. deterministic repository evidence in controlled workflow packets for M1-M3
   and M6;
4. deterministic repository evidence in controlled review packets for M4-M5;
5. a negative check that no scenario requires repeated unchanged external
   execution, duplicated full gates, or a second prose/review authority; and
6. one independent Tick over the implemented package.

Token counts, elapsed time, number of checkpoints, and external call counts are
observational unless a later protocol declares a baseline, method, direction,
and threshold. BS2-BS4 instead establish behavioral bounds: no authoritative
evidence before its owner review, no unchanged rerun without new information,
and one defined stall-escalation sequence.

## Glossary source and terminology

The selected glossary is `docs/glossary.md`. This proposal uses its established
meanings for **Tick**, **Tock**, **deterministic fixed point**, **capability
unconfirmed**, and **semantic owner**. The linked skills and accepted contract
matrix remain authoritative for behavior and acceptance. This document adds no
new glossary entry.

## Non-goals

- Do not make live provider execution a deterministic repository gate.
- Do not prohibit diagnostic external probes when repository evidence cannot
  answer a provider question.
- Do not require a new subagent, reviewer fan-out, or replacement implementer.
- Do not prescribe one programming language, test runner, review-file layout,
  or provider protocol.
- Do not turn progress intervals, diagnostic capture fields, or temporary
  artifacts into public product contracts.
- Do not add another prose pass or workflow owner.

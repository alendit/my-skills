# Contract and Scenario Package

Read the matrix, terms, realization, and admission sections at setup; use the
assignment/handoff section at those boundaries. Read structural profiles,
external diagnostics, and exact-limit procedures only when their named scope
applies. Keep the package matrix as the sole requirement authority.

## Contents

- Build the contract-first package matrix
- Define work package and delivery package terms
- Keep the realization disposition current
- Record and admit the delivery-package plan
- Execute ordered delivery packages
- Carry the behavioral goal record
- Keep private mechanisms conditional
- Profile design-sensitive owners
- Profile modularization roots
- Define a small scenario portfolio
- Separate evidence lanes and statuses
- Localize Before Repeating External Scenarios
- Justify exact limits
- Keep tests stable across redesigns
- Assign and hand off a delivery package

## Build the contract-first package matrix

Use stable IDs from the caller's normalized contract matrix. If no normalized
matrix exists, create the smallest package-local subset before assigning work
only when the caller explicitly authorizes a package-local scope. Do not use a
local subset to infer plan readiness or invent an unresolved delivery boundary:

| Field | Required content |
|---|---|
| Contract ID | Stable identifier used in assignments, reviews, and handoffs |
| Observable invariant | Public or owner-level behavior that must hold |
| Semantic owner | Component responsible for the invariant |
| Lifetime/bound/recovery | Applicable semantic boundaries, with inapplicable parts explained |
| Establishing delivery package | The one reviewed delivery package that establishes the complete contract ID |
| Named scenario | Portfolio entry that proves it |
| Evidence class | Deterministic repository, external compatibility, or observational telemetry |
| Status | Pending, accepted, unknown, or not-applicable |

Each invariant has one owning row. Delivery-package briefs, correction
messages, tests, documentation, and handoffs reference contract IDs rather
than restating the requirement. Update the row only after parent acceptance.

## Define work package and delivery package terms

This reference owns the delivery-package record and map consumed by the
entrypoint. The caller's normalized contract matrix remains the sole
requirement authority; this terminology describes how that authority is
delivered, not a second set of contracts.

- A **work package** is the complete caller-authorized scope passed to this
  skill. It may contain one or more ordered delivery packages.
- A **delivery package** is an independently acceptable delivery boundary
  inside the work package. It establishes one or more complete contract IDs
  and leaves a useful owner-level or public behavior if later packages never
  arrive.
- A **design checkpoint** records a decision needed by later work but need not
  produce behavior. Its acceptance does not make it a delivery package.
- An **internal step** is implementation work inside one delivery package. It
  may receive focused parent evidence, but it is not a separately gated
  delivery package by default.

Every contract ID has exactly one establishing delivery package, and every
delivery package establishes at least one complete contract ID. No checkpoint,
internal step, helper, representation, or temporary boundary may take partial
or temporary ownership of a contract. If accepted behavior genuinely reaches
two independently useful stopping points, stop and route a contract split to
the named product authority; continue only after the new contract rows and a
reviewed plan assign the resulting package IDs.

## Keep the realization disposition current

For each stable contract ID in an admitted delivery package, keep one logical
**realization disposition** current from pre-edit completeness through
implementation handoff and parent acceptance. It is a relation between the
contract row and its owner operations, information/state, transaction behavior,
scenarios, assertions, and design dependencies. It is not a required new file,
table, durable registry, or private representation.

The disposition is complete only when every applicable dimension has both the
following evidence and a current decision:

| Dimension | Pre-edit completeness | Implementation and handoff evidence |
|---|---|---|
| Ownership and capability | A concrete feasible owner capability or operation is selected, with every required ownership partition it can observe and enforce. | Current source shows the owner operation and its partition behavior; focused assertions exercise the applicable partitions. |
| Required information | The producer, lifetime, consumer path, and required identity/provenance or other immutable information are identified. | Current source and assertions show production or persistence, lifetime, and consumption of every required information fact. |
| Transaction and recovery | The applicable ordered admission, mutation, commit/publication, abort, retry, poison/failure, recovery, and cross-owner handoffs are planned. | Current operations and assertions prove the applicable success and failure partitions; adjacent success cannot stand in for an unresolved order or recovery step. |
| Scenario and assertion | Each required scenario has its observable invariant, adversarial partitions, and assertions, with localization at the owning or public boundary. | The actual owner/public behavior and assertion-level evidence retain the same positive and negative decision power; names or broad pass status are insufficient. |
| Design dependency | Dependent owner-map, architecture, plan, scenario, and evidence claims are identified for the selected design. | The disposition records whether each dependency remains valid or is stale and the dependency-aware decision that resolves it. |

At pre-edit completeness, the disposition must contain a concrete feasible plan
for the applicable dimensions above. During implementation and handoff, planned
entries are replaced by actual source and assertion evidence. Missing or
unproved coverage remains visible and blocks the current pre-edit, handoff, or
parent-acceptance decision; an implementer summary, adjacent success, names,
or a broad gate cannot satisfy the row.

Carry the complete relation once in the initial assignment. Later corrections,
handoffs, and follow-ups carry only changed dispositions and the contract IDs
whose dependencies changed. An unchanged disposition remains current only when
its plan, owner, design, and evidence dependencies are unchanged.

When a design change reaches a dependent authority or evidence claim, mark the
affected disposition stale before continuing or accepting work. Resolve it with
a dependency-aware `retain-with-proof`, `strengthen`, `replace`, or `delete`
decision. An unresolved
stale disposition blocks the current decision. If the changed content is
plan-owning, the existing review-fixpoint identity and invalidation boundary
also applies; this reference does not create another result level or gate.

## Record and admit the delivery-package plan

The plan-level result and its identity come from the
[review-fixpoint contract boundary](../../review-fixpoint/references/contract-and-evidence-boundary.md).
This skill consumes that durable decision and owns the final edit-admission
check; it does not create a fixed-point vocabulary, select a result level, or
infer plan readiness from a checkpoint.

Before spawning an implementer or permitting production edits, require all of
the following:

1. The latest durable review result is exactly
   `implementation-plan-fixed-point`, not merely `contract-fixed-point`, and
   includes the plan identity.
2. The identity is current under the review-fixpoint boundary's identity and
   invalidation rules for unchanged plan-owning content and the dependencies
   that determine the delivery relation, package records, closure fields, and
   dependency order.
3. Every plan cell is cleared and the delivery map is complete in both
   directions. Refuse admission and do not spawn when the result is missing,
   contract-only, stale, invalidated, changed, or has any unknown plan cell.
4. The map has been checked against the record below before the first edit.

The complete delivery-package record is:

| Field | Required closure |
|---|---|
| Package ID and useful outcome | Name the behavior available if work stops after this package. |
| Establishing contract IDs | List one or more complete stable IDs; each ID appears in exactly one package. |
| Semantic owner and physical boundary | Name the semantic authority and the current or proposed physical surface without equating layout with ownership. |
| Prerequisites and dependency order | Name only earlier accepted contracts, decisions, and packages actually consumed. |
| State and lifetime | Close ownership, durability, rebuildability, mutation, and the smallest correct lifetime. |
| Transaction and recovery closure | Close admission, mutation, commit, abort, retry, poison/failure, recovery, and cross-owner handoffs that the package needs. |
| Public, skill, and ABI surface | Name the real consumer-facing composition and any skill, guest, engine, embedding, or external boundary. |
| Focused evidence | Name deterministic owner/composition scenarios, adjacent boundaries, recovery partitions, and the package-level gate. |
| Safe deferred work | State what remains absent after this package and why that omission does not weaken its complete contracts. |
| Causal split/combine and acceptance-cost decision | Explain why adjacent work stays together or separates by semantic ownership, closure, useful stopping point, and decision value; place focused checks and canonical gates only where they decide something material. |

The map is not admissible when a package only supplies a design checkpoint,
mechanical move, helper, adapter, metric, or other non-useful intermediate. A
valid semantic boundary may coincide with a physical boundary, but physical
layout alone cannot justify a package. Do not invent an unresolved package
boundary locally; return the missing plan cell to the plan-review owner.

After the result, identity, and map pass these checks, admit the work package
before the first edit. Carry the complete accepted map and plan identity to the
first active implementation context once. Record the admission in the package
handoff and continue in dependency order only after the parent accepts the
admission boundary. The active context may continue into a later accepted
package, or SIL may renew it under
[implementer-continuity.md](implementer-continuity.md); a fresh context receives
the current plan identity and accepted delivery-package map with its next
package assignment once, and renewal does not change this map or its package
authority.

## Execute ordered delivery packages

For each admitted delivery package:

1. Confirm its prerequisites are accepted earlier packages or decisions and
   assign the complete package record and its contract IDs to the active
   implementation context. A fresh context may receive this assignment only
   after the preceding package is parent-accepted and SIL has verified the
   continuity handoff.
2. Build the useful owner/public behavior through its real composition path.
   Keep state, lifetime, transaction, recovery, public surface, and focused
   evidence closed around the package's primary reason to change.
3. Let the parent use focused checks for internal steps. Keep those steps
   inside their establishing package; they do not receive separate canonical
   gates or package IDs automatically.
4. Accept the package only when its complete contract IDs, stopping-point
   behavior, closure fields, evidence, deferred-work boundary, and causal
   split/combine decision are all resolved. A later package may extend behavior
   but may not repair an earlier package's incomplete semantics.
5. Send corrections within the admitted package to the active implementation
   context as delta-only follow-ups. Do not renew for an ordinary correction,
   resend the package map, or turn an internal step into a new package unless
   product authority accepts a contract split and a fresh reviewed plan assigns
   it. A verified continuity renewal is an allowed transition only after parent
   acceptance of the current delivery package; it starts the next admitted
   package and leaves this package record authoritative.

Package acceptance is distinct from `deterministic-fixed-point`; the latter's
result effects and exact-revision semantics remain with review-fixpoint. A
canonical gate is justified at an accepted package revision when it makes a
material decision, not merely to manufacture another internal checkpoint.

## Carry the behavioral goal record

Instantiate the package-level goal record from the shared
[behavioral design trace and rebaseline authority](../../evidence-efficient-review/references/behavioral-design-trace.md)
alongside the matrix. Mechanism rows reference its stable goal ID. Carry the
record through delivery-package assignments, corrections, handoffs, and
acceptance, and report its direct scenario's behavioral status separately from
mechanism status.

When literal specification choices or cumulative evidence challenge supporting
mechanisms, use that authority's aggregate comparison and rebaseline procedure.
The implementer supplies the trace and smallest faithful alternative; the
parent accepts mechanism-only correction within package scope, while product
authority accepts behavioral changes. Reconcile affected design dependencies
before resuming. Apply [economic actionability](../../evidence-efficient-review/references/economic-actionability.md)
when a defensive requirement would add or preserve product machinery or lasting
mechanism-coupled tests.

## Keep private mechanisms conditional

Put collection shape, fields, counters, diagnostic plumbing, helper names,
transaction decomposition, and numeric defaults in a conditional implementation
appendix. They are design inputs, not required package outcomes.

Promote a mechanism into a contract row only when changing it would violate a
public compatibility promise, eliminate the only sound semantic owner, or break
a named correctness invariant. State that reason. Ask whether a simpler
independently designed correct implementation can satisfy the row before
freezing representation or vocabulary.

## Profile design-sensitive owners

When one owner will receive a new design-sensitive responsibility or several
delivery packages, record a compact package-local structural baseline:

- relevant source units and major responsibility groups;
- state and collaborator boundaries;
- production and test separation; and
- the intended destination for each relevant delivery package.

Use module indexes, bounded outlines, and exact reads; do not load a complete
large owner merely to build the profile. Report material structural delta after
each relevant delivery package and compare the final owner with the baseline
before package acceptance. Inspect bounded history only when repeated placement across
earlier packages is material. The profile is implementation evidence, not a
public layout contract or permanent metrics ledger.

## Profile modularization roots

When the package contract explicitly includes modularization or physical
decomposition, inventory every material residual responsibility cluster in
each affected root before implementation and again at package acceptance:

```text
responsibility cluster
-> semantic owner
-> current physical representation
-> state and lifetime
-> transaction boundary
-> dependencies and callers
-> public or ABI surface
-> representative tests
-> smallest plausible complete private boundary
-> colocation invariant, when retained
-> extracted | retained-with-proof | unknown | not-applicable
```

`extracted` requires a cohesive private boundary with preserved behavior,
visibility, state, and dependency direction. `retained-with-proof` requires a
named causal invariant that the smallest plausible complete boundary would
break. Use `unknown` when required analysis is absent, contradictory, or tests
only a partial extraction. Use `not-applicable` for generated or
language-mandated regions, one cohesive algorithm, or another source-proven
absence of distinct responsibilities.

Record behavioral preservation and physical locality in separate evidence
lanes. Put passing APIs, ABIs, tests, and canonical gates in the preservation
lane; clear residual topology from the inventory and complete-boundary proof.
As acceptance backstops, an `unknown` residual cluster blocks the
modularization contract, while size and implementation effort only prioritize
the inventory.

## Define a small scenario portfolio

Record each scenario once:

```text
Scenario: <behavioral name>
Contracts: <stable IDs covered>
Observable invariant: <outcome at an owner or public boundary>
Evidence class: deterministic repository | external compatibility |
                observational telemetry
Capture helpers: <shared instrumentation>
Localization signal: <boundary identified when the scenario fails>
```

Prefer a few behavioral scenarios over an assertion inventory. Use shared
capture helpers for request shape, diagnostics, connection identity, and
cross-request contamination when relevant. Helpers may inspect private fields
for diagnosis, but their field layout does not become a public contract merely
because several scenarios reuse them.

## Separate evidence lanes and statuses

Keep the shared behavioral and mechanism progress statuses separate before
classifying the evidence that supports them. A completed owner suite or
mechanism path cannot establish the direct scenario's behavioral acceptance.

Keep these lanes independently reportable:

1. **Deterministic repository evidence:** owner-level and composed scenarios
   controlled by the repository. These must pass for delivery-package
   acceptance.
2. **Minimal external capability probe:** the smallest credentialed request
   that isolates provider or endpoint capability.
3. **Broader composed semantic scenario:** end-to-end product ownership and
   behavior, using the same capture helpers without being the sole proof of
   repository-controlled contracts.

The latter two are separate scenarios even when both use external compatibility
evidence. A failure must identify capability versus composition rather than
collapsing serialization, tools, diagnostics, transport identity,
contamination, and model output into one witness.

For each external scenario, carry the capability identity, freshness rule, and
one of the caller's evidence statuses: `current`, `reusable`, `stale`,
`unavailable`, `authentication-or-configuration-failure`,
`provider-or-infrastructure-failure`, `inconclusive-timeout`, or
`product-contract-failure`. Only the last proves the external contract false.
Missing credentials and other availability failures neither fail deterministic
acceptance nor count as an external pass. Required initial evidence remains
explicitly capability-unconfirmed.

Observational telemetry has no acceptance effect unless the contract names a
baseline, measurement method, direction, and regression threshold. Record
unthresholded bytes, token counts, cache tokens, and latency as observational.

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

Keep this tuple and its field layout private and disposable. They are diagnostic
evidence, not a public product contract.

Classify the failure as provider behavior, product behavior, evidence-harness
behavior, or still unknown.

If the first record is insufficient, improve the capture before one additional
run. A next run requires improved capture or a changed implementation. Never
rerun solely because summary output was truncated: preserve the complete
structured record in a temporary artifact and summarize it separately.

Once localized, add or strengthen deterministic owner and composition coverage
before another acceptance run.

## Justify exact limits

Before implementing a normative cap, timeout, retry count, or other numeric
limit, require:

| Field | Required justification |
|---|---|
| Correctness role | Invariant that changes or fails if the value changes |
| Workload basis | Observed or conservative workload the value must admit |
| Resource estimate | Memory, CPU, latency, connection, or storage cost it bounds |
| Boundary consequence | Behavior at exact and one-over values |
| Revision trigger | Production evidence, benchmark, or workload change that permits revision |

When correctness does not depend on the number, keep it as a private default in
the implementation appendix. Test it as mechanism evidence rather than making
it feature acceptance.

## Keep tests stable across redesigns

Classify affected tests as `retain`, `strengthen`, `replace`, or `delete`.
Contract tests protect stable public semantics, ownership, boundedness, and
recovery. Mechanism tests are disposable when their design simplifies.

Cover semantic partitions and reachable adjacent boundaries when they
distinguish behavior. Do not bypass an earlier public admission limit only to
exercise a later defensive ceiling. Test the earliest observable public
contract publicly and keep unreachable serializer or ABI limits owner-local.
A conformance label names evidence but does not replace the scenario's
observable invariant.

## Assign and hand off a delivery package

Use the existing map, contract matrix, and realization relation as the source
of assignment fields. Send them once, then carry changed dispositions and
affected IDs. A fresh authorized context receives the verified turnover
envelope and next package once; do not replay transcripts or raw logs.

### Initial assignment

Supply the work-package outcome, reviewed map and plan identity, current
package's owner/behavior, established prerequisites, exclusions, architectural
invariants, accepted behavior that must not regress, scenario portfolio,
realization disposition, focused completion checks, evidence locations, and
questions requiring a parent decision. Include base revision, commit authority,
selected configuration, continuity policy, and the progress envelope.

Include only applicable additions:

- structural baseline and intended source destination for changed owners;
- residual-topology inventory for physical decomposition;
- external evidence status and shared capture/localization helpers;
- architectural decisions and follow-up IDs, including ledger-write authority;
- the [glossary state's](../../clear-technical-writing/references/project-glossaries.md)
  opt-out marker alone, or selected source and material scope/term dispositions.

Keep representation and numeric defaults in the conditional implementation
appendix unless correctness requires them. The implementer chooses the internal
edits, compiler/import/fixture adaptation, and directly caused repairs. Require
a design or scope gap to be reported before expanding the package.

Set a completion or meaningful-checkpoint window, immediate blockers, decision
events, and the first credible stall deadline. The mailbox timeout is a generous
failsafe beyond the expected event, within the tool limit. Illustrative starting
points are about 30 minutes for substantial work, 45–60 minutes for long builds
or checks, and 10–15 minutes for smaller packages. Adjust to actual work; these
are not acceptance thresholds or instructions to leave work unbounded.

Instruct the implementer to inspect relevant owners and adjacent consumers,
avoid repeating context, use focused checks, and communicate concise deltas.
Keep verbose logs and intermediate evidence in its context or an accessible
temporary/authorized artifact. Economy does not waive owner analysis, cleanup,
required documentation, validation, or independent acceptance.

### Completion handoff

Report base revision and handoff SHA when committed, changed paths and owner
boundary, intended behavior/interface change (or none), established contract
IDs, goal and direct-scenario status, mechanism progress, focused checks with
pass/fail status, unresolved concerns, and the detailed-evidence location.
Replace planned realization entries with actual source/assertion evidence;
report changed entries and unresolved rows after the first complete relation.

Include material exceptions to mechanical equivalence and, when activated,
structural/residual-topology deltas, affected-test dispositions, external
evidence, architectural decisions and verified follow-up deltas. Carry material
terminology state under the shared glossary authority, not a copied glossary.

Distinguish expected pre-fix reproduction from final verification, observations
from hypotheses and execution witnesses, and the original failure from cleanup
failure. Zero selected tests, stale passes, and missing assertions remain
missing evidence. The implementer cannot accept its own work.

Before an authorized commit, settle editing/checking processes and validate the
coherent handoff. The message describes durable behavior and reason, with a
short useful validation summary; the inbox supplies SHA and transient evidence.
Label incomplete checkpoints unaccepted and retain the original package review
base. Parent acceptance covers the entire original-base-to-final range.

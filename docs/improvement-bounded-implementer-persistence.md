# Improvement Plan: Bounded Implementer Persistence

## Outcome summary

The BIP1-BIP9 matrix and NG1-NG8 non-goal table below are the sole normative
authority for this improvement. BIP2 is the desired bounded-persistence change;
BIP1 and BIP3-BIP8 constrain its direct SIL execution, while BIP9 owns outer
workflow composition. This summary and the decision rationale explain why
those IDs were selected without creating additional requirements.

Status: implementation present; BIP1-BIP9 accepted by the user;
`BIP-1-plan-r2` reached `implementation-plan-fixed-point` in independent
plan-level review. This plan
extends
[`improvement-delegation-context-locality.md`](improvement-delegation-context-locality.md)
and
[`improvement-efficient-subagent-polling.md`](improvement-efficient-subagent-polling.md).
Those plans keep work and evidence local to the implementer and avoid wasteful
parent polling. This plan addresses the different failure mode in which the
implementer's own retained history becomes too large to remain a reliable or
efficient working context.

Glossary disposition: `docs/glossary.md` is the selected source for recurring
repository terminology. The continuity terms introduced by this plan are
defined locally in the supervised-implementer-loop reference because they are
specific to this workflow; no glossary entry is added.

## Behavioral goal and direct scenario

```text
Goal ID: BIP-1
Behavioral goal: A long multi-package implementation may renew its
  implementer context only at an accepted delivery-package boundary while
  preserving exact caller authority and configuration, one active writer,
  parent acceptance, delta-only corrections, and independent review.
Direct scenario: Given four admitted delivery packages, after one accepted
  package shows concrete context pressure, the parent verifies a bounded
  turnover envelope, retires that context, and starts exactly one fresh
  authorized same-configuration implementer for the next package. No writers
  or Git writes overlap, and renewal adds no Tick.
Product authority: User-selected improvement; the parent accepts the
  mechanism while preserving the caller's requirements.
Owning contract: BIP2
Behavioral status: partial
Mechanism status: in-progress
```

The direct scenario is composed with BIP1 and BIP3-BIP9 as constraints on the
BIP2 boundary; BIP2 remains the one owning contract. Accepted plan identity:
`BIP-1-plan-r2`, at `implementation-plan-fixed-point`. This plan-level result
does not establish an accepted implementation revision, deterministic fixed
point, or completed behavioral scenario.

## Observed failure

The existing supervised workflow gives a capable implementer the complete
package once, then reuses the same identity with delta-only follow-ups. This is
effective for a bounded package. It becomes counterproductive when a work
package spans many semantic packages, days of execution, or hundreds of
turn-triggering follow-ups.

In the motivating session snapshot:

- the parent had compacted 27 times while the active implementer context had
  compacted 261 times;
- the implementer's latest replacement history contained approximately
  483,000 characters across 187 retained items;
- 181 retained messages came from the parent, including 138 turn-triggering
  new-task assignments; and
- individual unfinished implementer turns compacted repeatedly, including one
  turn with ten compactions before completion.

Delta-only messages made each follow-up smaller, but did not prevent the
retained prefix from growing. Repeated compaction was correlated with renewed
inspection, rediscovery, and incomplete semantic-closure claims. That
correlation is a context-health warning, not proof that compaction caused any
particular implementation defect.

The failure is therefore not persistence itself. It is **unbounded
persistence**: thread identity is treated as the only way to preserve
continuity even after accumulated history starts to obscure the accepted
package state it was meant to retain.

## Decision rationale

BIP2 uses the existing parent-accepted delivery package because the repository
already defines it as a complete, useful stopping point. BIP1 gives the
transition one-writer safety; BIP3 preserves caller authority and exact
configuration; BIP5-BIP7 preserve accepted state across the transition. BIP4
keeps context observations diagnostic, while BIP8 provides a separate recovery
route when ordinary boundary renewal is no longer trustworthy. BIP9 keeps
those leaf decisions from becoming duplicate outer-workflow mechanics.

## Scope and non-goals

This plan governs implementation-agent context lifetime inside mixed-work and
supervised-implementation workflows. These non-goals are normative alongside
BIP1-BIP9:

| ID | Non-goal | Related contract |
|---|---|---|
| NG1 | No numeric compaction limit or context-size acceptance threshold | BIP4 |
| NG2 | No weaker parent acceptance, repository verification, single-writer discipline, or serialized Git writes | BIP1, BIP2 |
| NG3 | No model, reasoning-effort, or normal/fast-mode substitution | BIP3 |
| NG4 | No agent rotation merely because work is long or one compaction occurs | BIP2, BIP4 |
| NG5 | No implementer handoff treated as independent review | BIP9 |
| NG6 | No change to persistent independent-reviewer policy | BIP9 |
| NG7 | No standalone context-management skill | BIP9 |
| NG8 | No inference that cheap implementer tokens imply unlimited context capacity | BIP4 |

## Authoritative contract and evidence matrix

These rows are the only normative outcomes. External compatibility evidence is
`not-applicable` for every row because the workflow does not depend on an
external provider capability.

| ID | Observable contract | Semantic owner | Public composition | Establishing delivery package | Deterministic evidence | External compatibility evidence | Telemetry | Status |
|---|---|---|---|---|---|---|---|---|
| BIP1 | **One active implementation writer.** Exactly one implementation context owns edits at a time; renewal never creates overlapping writers or Git operations. | `supervised-implementer-loop` | Direct SIL execution across a renewal | BIP-DP1 | Active-context and changed-path inventory before retirement and fresh assignment; serialized Git-write record | Not applicable: no external capability | Not applicable | Accepted |
| BIP2 | **Persistence has a delivery boundary.** Reuse the active context throughout one admitted delivery package and its corrections. Normal renewal is considered only after parent acceptance of that package; a generic owner checkpoint, design checkpoint, or internal step is not eligible. Mid-package continuity loss is exceptional stop-and-rebaseline. | `supervised-implementer-loop` with the delivery-package reference as boundary authority | SIL assignment, correction, acceptance, and next-package transition | BIP-DP1 | Accepted package map and packet; checkpoint/internal-step negative search; coherent-package and four-package scenarios | Not applicable: no external capability | Not applicable | Accepted |
| BIP3 | **Continuity authority is explicit.** Record whether continuity is `identity-persistent` or `role/model-persistent`. Never silently replace an explicitly named implementer or substitute its model, reasoning effort, or execution mode; a fresh context is allowed only when the runtime preserves the required configuration. | Caller requirement enforced by `supervised-implementer-loop` | Direct SIL execution | BIP-DP1 | Continuity record; named-identity and unavailable-exact-configuration scenarios | Not applicable: no external capability | Not applicable | Accepted |
| BIP4 | **Context health is observational and capability-aware.** Use available runtime, behavioral, and tree evidence to choose `continue`, `renew-at-boundary`, or `stop-and-rebaseline`. No individual context signal or invented telemetry threshold establishes failure, and correctness works without telemetry. After a missed event still supports `continue`, allow one bounded recovery turn; if that recovery fails its event or returns concrete degradation, treat the supervised communication channel as untrustworthy and stop-and-rebaseline. | `supervised-implementer-loop` | Direct SIL disposition and continuation or recovery | BIP-DP1 | Disposition-source audit; coherent-compaction, no-telemetry, successful-recovery, and exhausted-recovery scenarios | Not applicable: no external capability | Compaction, retained-prefix, message-topology, and token observations are observational only | Accepted |
| BIP5 | **Turnover preserves accepted state without a second ledger.** Before renewal, the parent verifies one compact turnover envelope that references the accepted delivery-package packet and includes the plan identity, current accepted delivery-package map, goal ID, exact revision or bounded dirty-tree state, continuity configuration, next admitted package, material unrecorded decisions, and shared evidence locations. | `supervised-implementer-loop` | Parent acceptance followed by fresh-context assignment | BIP-DP1 | Turnover read-back against tree and existing records; duplicate-ledger and package-map-identity negative searches | Not applicable: no external capability | Not applicable | Accepted |
| BIP6 | **Renewal externalizes required evidence.** Evidence needed after renewal is reachable from a shared accessible artifact or accepted record before the old context retires; successful raw logs need not be copied. | `supervised-implementer-loop` | Parent turnover verification and fresh-context consumption | BIP-DP1 | Shared-evidence reachability check; trapped-evidence scenario | Not applicable: no external capability | Not applicable | Accepted |
| BIP7 | **A fresh context receives one complete bounded assignment.** After authorized retirement, start exactly one fresh context with the verified envelope and next admitted package once, then use delta-only communication. Do not replay raw logs or reactivate or compare the old context in parallel. | `supervised-implementer-loop` | Sequential SIL delivery packages | BIP-DP1 | Agent-operation and message inventory; actual BIP-DP1 to BIP-DP2 fresh-context handoff | Not applicable: no external capability | Not applicable | Accepted |
| BIP8 | **Exceptional mid-package loss stops and rebaselines.** When concrete degradation invalidates the active course or the single bounded recovery turn fails, the parent stops further deltas, inspects the bounded dirty tree from the last accepted package, classifies accepted, complete-but-unaccepted, partial, and obsolete work without relying on an untrustworthy summary, preserves useful edits, and obtains required replacement authority before resuming. | `supervised-implementer-loop` | Direct SIL recovery | BIP-DP1 | Dirty-tree classification and exhausted-recovery scenarios; source audit of last-accepted-boundary routing | Not applicable: no external capability | Not applicable | Accepted |
| BIP9 | **Outer workflows consume rather than duplicate continuity.** `complex-work` carries material caller continuity requirements, consumes SIL dispositions, and replans only affected dependents; `review-fixpoint` consumes one accepted implementation result. Renewal creates neither a new outer unit nor a Tick and does not change persistent independent-review authority. | `complex-work` for mixed-work composition; `review-fixpoint` for phase/reviewer authority; SIL remains the leaf continuity owner | Non-trivial Tock and mixed-work routing | BIP-DP2 | Two-context Tock and affected-dependency scenarios; persistent-reviewer and exact-gate source audit; turnover-not-Tick negative search | Not applicable: no external capability | Not applicable | Accepted |

## Reviewed delivery-package plan

Plan identity: `BIP-1-plan-r2`, at `implementation-plan-fixed-point`. The
package relation is complete in
both directions: BIP1-BIP9 each have exactly one establishing package, and each
package establishes complete contract IDs. The independent plan review found
no required unknown or actionable plan defect in this exact relation.

### BIP-DP1: Direct supervised continuity

| Field | Planned closure |
|---|---|
| Package ID and useful outcome | `BIP-DP1`; direct SIL callers can preserve one active writer through a delivery package and either continue, renew safely after acceptance, or stop and rebaseline. |
| Establishing contract IDs | BIP1-BIP8 |
| Semantic owner and physical boundary | `supervised-implementer-loop`; its entrypoint plus `implementer-continuity.md`, with `contract-and-scenario-package.md` retaining delivery-boundary authority |
| Prerequisites and dependency order | Accepted BIP contracts and the existing reviewed SIL delivery-package authority; no BIP package prerequisite |
| State and lifetime | One active implementation context through one admitted package and corrections; accepted records and shared evidence survive a context retirement |
| Transaction and recovery closure | Assign once, correct by deltas, parent-accept, verify turnover, retire, then start one fresh context; continuity loss instead stops deltas and classifies the bounded tree |
| Public, skill, and ABI surface | Direct invocation of `supervised-implementer-loop`; no ABI or external provider surface |
| Focused evidence | BIP1-BIP8 source audit, relative-link and stale-phrase checks, direct renewal/no-telemetry/trapped-evidence scenarios, and the actual DP1-to-DP2 context handoff |
| Safe deferred work | Mixed-work and fixpoint integration remain absent; direct SIL behavior and its accepted package boundaries remain complete without them |
| Causal split/combine and acceptance-cost decision | Keep SIL mechanics and delivery authority together so direct invocation is useful. Stop before outer integration because it consumes this accepted interface and needs a separate cross-owner decision. Run focused structure checks and parent review here; defer the independent whole-scope review until BIP-DP2. |

### BIP-DP2: Outer-workflow integration

| Field | Planned closure |
|---|---|
| Package ID and useful outcome | `BIP-DP2`; mixed-work and fixpoint callers consume bounded SIL continuity without copying its mechanics or changing reviewer authority. |
| Establishing contract IDs | BIP9 |
| Semantic owner and physical boundary | `complex-work` carries caller authority and replans affected units; `review-fixpoint` retains Tick/Tock and persistent-reviewer authority; SIL remains the continuity owner |
| Prerequisites and dependency order | Parent-accepted BIP-DP1 and its unchanged SIL continuity interface |
| State and lifetime | Outer skills persist no new turnover state; they carry material caller requirements and consume the leaf disposition and accepted evidence |
| Transaction and recovery closure | Route to SIL, consume its accepted result or rebaseline disposition, preserve valid outer decisions, then continue ordinary mixed-work or exact-revision Tick/Tock sequencing |
| Public, skill, and ABI surface | `$complex-work` mixed packages and `$review-fixpoint` non-trivial Tocks; no ABI or external provider surface |
| Focused evidence | BIP9 source audit across both outer consumers, two-context Tock and affected-dependency scenarios, persistent-reviewer negative search, link/frontmatter checks, and independent whole-scope review |
| Safe deferred work | No BIP work is deferred; broader reviewer-context renewal remains explicitly outside scope |
| Causal split/combine and acceptance-cost decision | Keep the two outer consumers together because BIP9 requires their composition to preserve one leaf result and independent review. Keep them separate from BIP-DP1 so direct SIL is an independently useful stopping point. After parent acceptance, create the authorized coherent remediation commit, run the canonical deterministic gate on that exact clean revision, and only then perform one independent whole-scope Tick. |

Reviewed plan-cell evidence:

| Plan cell | Reviewed disposition |
|---|---|
| Contract-to-package coverage | BIP1-BIP8 map to BIP-DP1 and BIP9 maps to BIP-DP2; both packages establish at least one complete ID. |
| Useful stopping point | BIP-DP1 leaves direct SIL continuity usable; BIP-DP2 adds complete outer composition. |
| Cohesion and transaction closure | BIP-DP1 closes the implementation-context lifetime and turnover transaction; BIP-DP2 closes cross-workflow consumption without new state. |
| Dependency order | BIP-DP2 consumes the parent-accepted BIP-DP1 interface; BIP-DP1 has no BIP package prerequisite. |
| Package-size tradeoff | Splitting preserves a useful direct-SIL boundary; further splitting would create reference or caller checkpoints without a complete new behavior. |
| Acceptance-cost topology | Focused checks and parent acceptance follow each package. After BIP-DP2 acceptance, the authorized coherent remediation commit precedes the canonical gate on that exact clean revision, which precedes one independent whole-scope Tick. |
| Checkpoint/package distinction | Internal edits and correction turns remain inside their establishing package and never become renewal boundaries or package IDs. |

## Context-health disposition implementation (BIP4)

This section supplies conditional implementation detail for BIP4. The BIP4
matrix row remains the normative outcome.

Use three decision states:

- **continue:** current context remains coherent enough to finish the admitted
  package and ordinary corrections;
- **renew-at-boundary:** pressure is material, but semantic continuity remains
  trustworthy through parent acceptance of the current admitted delivery
  package; and
- **stop-and-rebaseline:** concrete behavior shows that accepted state can no
  longer be trusted or the current course is invalidated.

Relevant runtime observations include:

- multiple compactions during one unfinished turn;
- shortening intervals between compactions;
- a large post-compaction retained prefix relative to the active window;
- a high count of retained turn-triggering assignments;
- repeated broad reinspection of already accepted owners; and
- inability to complete the next meaningful package before another likely
  compaction.

Relevant behavioral observations include:

- contradicting an accepted owner or dependency decision;
- repeatedly asking for or reconstructing context already supplied;
- omitting adjacent contracts that were previously accepted;
- reporting closure that the current tree plainly does not establish; and
- losing the distinction between accepted work, partial work, and future
  scope.

These are diagnostic inputs. Compaction alone is not a defect, and a healthy
agent may compact several times while completing difficult work correctly.
Conversely, continuity can become unreliable even when the runtime exposes no
compaction telemetry.

## Execution protocol for BIP1-BIP8

This sequence realizes BIP1-BIP8 and the BIP-DP1/BIP-DP2 plan. It does not
redefine their observable outcomes.

### 1. Establish continuity policy

At package setup, record:

- the required model, reasoning effort, and normal or fast execution mode;
- whether continuity is identity-persistent or role/model-persistent;
- the admitted delivery packages and safe turnover boundaries;
- the evidence artifact location; and
- who may authorize replacement when the current context cannot continue.

Do not add a ceremony for a small package that is expected to finish in one
coherent implementation context.

### 2. Run one bounded persistence interval

Give one active implementer the complete accepted context for the current
admitted delivery package once. Reuse it for that package and all evidence-
based corrections. Keep detailed inspection, routine checks, and logs in its
context or the shared evidence artifact.

Carry later packages only as sequencing context. Assign one current
parent-acceptable package, and admit the next package only after the parent
accepts the current one.

Use queue-only messages for active-turn deltas. Trigger a new turn only after
the implementer is idle and the next substantive correction or accepted
boundary is ready. Batch related corrections instead of creating several small
status turns. Do not overlap implementation writers or Git writes.

### 3. Observe without imposing a threshold

When telemetry is available, record only observations relevant to the next
workflow decision. Do not poll solely to count compactions or context size.
Prefer the runtime's existing session data over self-reported estimates.

Select `continue`, `renew-at-boundary`, or `stop-and-rebaseline` from the
combined runtime and behavioral evidence. Explain the causal decision; do not
turn an arbitrary count into a language-independent constant.

After one missed event still supports `continue`, allow one bounded recovery
turn to restore the promised checkpoint or handoff. If that recovery misses its
event or returns concrete degradation such as unparsable source, broadened
failures, absent claimed evidence, or parent-owned implementation repair, select
`stop-and-rebaseline`. This is a communication-channel recovery budget, not a
context-size or implementation-correctness threshold.

### 4. Finish the useful boundary when trustworthy

When the disposition is `renew-at-boundary`, let the implementer finish the
current admitted delivery package whose acceptance leaves the repository better
off. Run focused checks and produce the ordinary acceptance packet. The parent
independently verifies the package boundary and accepts or corrects it before
turnover. A generic owner checkpoint or internal step is not sufficient.

Do not start the next delivery package in the old context after renewal has
been selected.

### 5. Produce and verify the turnover envelope

After parent acceptance, externalize every fact needed after renewal to an
accessible shared artifact or an existing accepted record. The outgoing
implementer may provide deltas, but the parent verifies the following compact
composition against the tree and authoritative package records:

```text
Turnover envelope
  goal ID and direct-scenario status
  plan identity and current accepted delivery-package map
  last parent-accepted delivery package and established contract IDs
  exact revision, or base revision plus bounded dirty-tree state
  continuity mode, required identity, role/model/reasoning/execution config,
  replacement authority
  next admitted delivery package and accepted prerequisites
  material decisions not represented in the package or plan records
  unresolved risks and shared evidence locations
```

The envelope references the existing delivery-package packet rather than
copying its contracts or closure fields. Successful raw logs need not be
copied. Evidence that remains only in the retiring context blocks renewal, and
an unverified outgoing summary does not establish continuity.

### 6. Renew without replay

When `role/model-persistent` renewal is authorized, retire the old context and
start exactly one fresh implementer with the same selected role, model,
reasoning effort, and execution mode. Give it the verified turnover envelope,
the current accepted package map, and the next admitted delivery package as
one complete bounded assignment. Later communication is delta-only.

The previous context remains historical evidence, not an active compatibility
path. Do not reactivate it, ask both contexts to implement, or compare the same
package in parallel. If the runtime cannot preserve the selected
configuration, renewal is unavailable and no silent substitution is allowed.

### 7. Handle lost continuity safely

For `stop-and-rebaseline`, stop issuing implementation deltas. The parent
inspects the bounded dirty tree and shared evidence without relying on an
untrustworthy outgoing summary. Starting from the last parent-accepted
delivery package, classify work as accepted, complete-but-unaccepted, partial,
or obsolete, and identify the last trustworthy delivery boundary. Preserve
useful edits and evidence; do not discard work merely to obtain a clean
conversational restart. Complete-but-unaccepted work is not accepted by
classification alone.

If explicit identity persistence applies, report the evidence and request
authorization before replacement. The parent records the invalidated
assumption, chooses the smallest recovery boundary, and obtains any required
configuration authority before a new complete assignment. A context problem
does not silently broaden replacement authority.

## Delivery realization

These physical edits realize the ID-keyed packages above; they are not
additional contract or delivery-package definitions.

### `complex-work`

Carries BIP3 requirements and consumes BIP4/BIP8 leaf results while realizing
the BIP9 outer composition in BIP-DP2.

- Carry material continuity policy, required configuration, safe renewal
  boundaries, and replacement authority separately from the optional execution-
  cost profile.
- Treat the implementation leaf's context-health disposition and any renewal
  unavailability that affects dependent units as a coordination replanning
  signal, parallel to existing primary-context and polling signals.
- Replan affected units from the leaf's accepted disposition without copying
  the supervised-implementer-loop's turnover or recovery mechanics. The leaf
  owns implementation continuity; this coordinator owns cross-unit ordering
  and replan decisions.

### `supervised-implementer-loop`

Realizes BIP1-BIP8 in BIP-DP1 and supplies the leaf interface consumed by
BIP-DP2.

- Replace indefinite whole-work-package context reuse with exactly one active
  implementation writer and bounded persistence through the current admitted
  delivery package.
- Add continuity mode and context-health disposition to package setup, with
  renewal eligible only after parent acceptance of that delivery package.
- Define the verified turnover envelope, evidence externalization, and
  fresh-context assignment under the SIL-owned reference.
- Preserve delta-only correction, parent acceptance, serialized Git writes,
  and the prohibition on silent model substitution.
- Keep ordinary corrections in the active context; renewal is not routine agent
  churn and does not make an internal step or checkpoint a package.

### `evidence-efficient-review`

BIP9 leaves this skill unchanged.

No implementation-lifecycle change is required. Its compact dossier and
coverage-ledger principles remain useful evidence formats, but implementer
turnover does not become independent review.

### `review-fixpoint`

Realizes the outer BIP9 composition in BIP-DP2.

No reviewer-policy change is required. A Tock may internally use more than one
authorized bounded implementer context while retaining one active implementer
at a time and one accepted remediation result. The subsequent Tick remains
independent and reviews the exact accepted revision.

Do not add a standalone context-lifecycle skill. Keep package coordination in
`complex-work`, implementation continuity in `supervised-implementer-loop`,
and review independence in the existing review owners.

## Validation scenarios

External compatibility is `not-applicable` to every scenario. Compaction and
token measurements remain observational even when deterministic source rules
govern the resulting action.

| Scenario | Contracts | Observable invariant | Evidence class | Capture and localization signal |
|---|---|---|---|---|
| Two-slice package completes coherently | BIP1, BIP2 | One context completes internal slices and corrections without renewal ceremony. | Deterministic repository | Assignment/message inventory; failure localizes to within-package persistence. |
| Four admitted delivery packages exceed one useful context lifetime | BIP1-BIP9 | Parent selects normal boundary renewal from observational pressure, accepts the current package, preserves exact configuration, verifies turnover and externalized evidence, retires the old context, starts one fresh context, and leaves exceptional recovery and Tick authority unchanged. | Deterministic repository with observational trigger | Package packets, disposition/configuration record, agent topology, turnover/evidence read-back, message inventory, and phase inventory; failure localizes to disposition, acceptance, authority, retirement, fresh assignment, or outer composition. |
| Several compactions occur but the implementer remains coherent | BIP2, BIP4 | Compaction pressure alone does not force renewal or failure. | Observational telemetry plus deterministic policy | Runtime compaction observations and disposition record; failure localizes to threshold-free disposition. |
| Implementer contradicts an accepted ownership decision mid-package | BIP4, BIP8 | Parent stops deltas and classifies the bounded tree from the last accepted package before continuation. | Deterministic repository | Accepted-boundary record, dirty-tree inventory, and invalidated assumption; failure localizes to recovery admission. |
| User explicitly requires the existing named implementer | BIP3 | No replacement occurs without explicit authority. | Deterministic repository | User instruction, continuity record, and agent-operation inventory; failure localizes to replacement authorization. |
| Exact requested configuration is unavailable | BIP3, BIP7 | Renewal stops without model, reasoning, or execution-mode substitution. | Deterministic repository | Requested/available configuration comparison and spawn decision; failure localizes to fresh-context admission. |
| Active implementer needs a correction | BIP1, BIP2 | Parent queues one batched delta without replacement or a status-only turn. | Deterministic repository | Active-state and message-operation inventory; failure localizes to interaction routing. |
| Idle implementer receives the next small correction | BIP2 | Parent triggers substantive follow-up work and retains the context inside the current package. | Deterministic repository | Idle-state and follow-up inventory; failure localizes to within-package persistence. |
| Cheap implementer context is saturated | BIP3, BIP4 | Cost preference does not override context reliability, semantic closure, or exact configuration. | Observational telemetry plus deterministic policy | Cost/context observations and disposition record; failure localizes to authority or health selection. |
| Tock uses two sequential implementer contexts | BIP1-BIP7, BIP9 | After an accepted delivery boundary and exact-configuration turnover with shared evidence, one fresh writer continues the Tock; parent accepts one result and the persistent independent reviewer performs the ordinary exact-revision Tick. | Deterministic repository | Tock package/configuration/turnover/evidence records, agent inventory, phase inventory, and reviewer identity; failure localizes to boundary admission, turnover trust, single-writer continuity, or SIL-to-fixpoint composition. |
| SIL is invoked directly without `complex-work` | BIP1-BIP8 | SIL preserves one writer and renews or recovers without outer-coordinator mechanics. | Deterministic repository | Direct assignment, agent inventory, and continuity disposition; failure localizes to SIL ownership. |
| Runtime exposes no context or compaction telemetry | BIP4 | Behavioral, accepted-package, shared-evidence, and bounded-tree evidence decide the disposition without a timer. | Deterministic repository | Telemetry-absent run record and disposition evidence; failure localizes to telemetry independence. |
| First missed event recovers coherently | BIP2, BIP4 | One bounded recovery turn produces the promised checkpoint or handoff, after which ordinary package execution and acceptance continue. | Deterministic repository | Missed-event record, recovery assignment, and resulting event; failure localizes to recovery admission or event delivery. |
| Bounded recovery also fails | BIP4, BIP8 | The parent sends no further correction to that context, settles the writer, preserves and classifies the tree, and either finishes a small bounded correction locally or respawns the same authorized configuration from the verified rebaseline. | Deterministic repository | Recovery event, agent topology, settlement evidence, dirty-tree classification, and next-owner decision; failure localizes to recovery-budget enforcement or rebaseline admission. |
| Required evidence exists only in the retiring context | BIP5, BIP6 | Renewal stops until required evidence becomes reachable in a shared artifact or accepted record. | Deterministic repository | Evidence reachability read-back; failure localizes to turnover verification. |
| Outgoing context is behaviorally untrustworthy mid-package | BIP4, BIP8 | Parent ignores its summary as authority, preserves useful edits, classifies work, and records a rebaseline before a fresh assignment. | Deterministic repository | Tree/evidence inspection and rebaseline record; failure localizes to exceptional recovery. |

## Acceptance backstop for BIP1-BIP9

- Is there exactly one active implementation writer at every point?
- Does persistence last through ordinary corrections and end only after parent
  acceptance of an admitted delivery package or a concrete loss of continuity?
- Is the user's identity, model, reasoning, and execution-mode requirement
  explicit and preserved?
- Are compaction and token observations diagnostic rather than invented pass or
  failure thresholds?
- After a missed event, does the workflow allow no more than one bounded
  recovery turn before failed recovery forces stop-and-rebaseline?
- Can the parent verify the accepted state from the turnover envelope and
  current tree without replaying the complete transcript?
- Does a fresh implementer receive one complete bounded assignment followed by
  deltas?
- Is required post-renewal evidence reachable outside the retiring context?
- Are partial dirty-tree edits classified and preserved rather than silently
  abandoned?
- Does renewal leave parent acceptance, authorization, single-writer safety,
  and independent review unchanged?
- Would the workflow remain correct when the runtime exposes no context or
  compaction telemetry?

Accept the improvement when the affected skills preserve useful persistence,
permit authority-safe renewal at meaningful package boundaries, and distinguish
context pressure from actual loss of semantic continuity without imposing an
arbitrary numeric cutoff.

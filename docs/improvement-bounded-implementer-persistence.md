# Improvement Plan: Bounded Implementer Persistence

## Outcome

Keep one supervised implementer long enough to preserve useful local reasoning,
accepted decisions, and efficient delta-only correction, but do not require one
conversation context to survive an arbitrarily long multi-package effort.

Persistence should be bounded by a meaningful delivery-package or owner-level
acceptance boundary. At that boundary, the workflow may renew the implementer
context while preserving the selected model and reasoning mode, the accepted
semantic state, single-writer discipline, parent acceptance, and any explicit
user requirement for a particular agent identity.

Status: proposed. This plan extends
[`improvement-delegation-context-locality.md`](improvement-delegation-context-locality.md)
and
[`improvement-efficient-subagent-polling.md`](improvement-efficient-subagent-polling.md).
Those plans keep work and evidence local to the implementer and avoid wasteful
parent polling. This plan addresses the different failure mode in which the
implementer's own retained history becomes too large to remain a reliable or
efficient working context.

## Observed failure

The existing supervised workflow gives a capable implementer the complete
package once, then reuses the same identity with delta-only follow-ups. This is
effective for a bounded package. It becomes counterproductive when a work
package spans many semantic packages, days of execution, or hundreds of
turn-triggering follow-ups.

In the motivating session snapshot:

- the parent had compacted 27 times while the persistent implementer had
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

## Decision

Use one active implementer at a time and preserve it through the current
delivery package and ordinary correction loop. Treat completion and parent
acceptance of a meaningful delivery package as a context-renewal boundary.

At that boundary, the workflow may either:

1. continue with the same implementer when its context remains useful and
   trustworthy; or
2. begin the next package with a fresh implementer context after a verified
   turnover packet preserves the accepted state.

This is **bounded implementer persistence**. It preserves continuity where it
has semantic value and permits renewal only where the repository already has a
useful stopping point.

Context renewal is not model substitution, reviewer substitution, a second
implementation pass, or permission to abandon unfinished work. The package
record must distinguish:

- **identity-persistent:** the user requires the same agent identity; replacing
  it requires explicit authorization; and
- **role/model-persistent:** the user requires the same implementation role,
  model, reasoning effort, and execution mode, but permits a fresh context at
  an accepted boundary.

When the requirement is absent or ambiguous, do not silently infer permission
to replace a named implementer.

## Scope and non-goals

This plan governs implementation-agent context lifetime inside mixed-work and
supervised-implementation workflows. It does not:

- introduce a numeric compaction limit or context-size acceptance threshold;
- weaken parent slice acceptance, repository verification, or single-writer
  rules;
- authorize a model, reasoning-mode, or fast-mode substitution;
- rotate agents merely because a task is long or one compaction occurred;
- make an implementer handoff into an independent review;
- change the persistent independent-reviewer policy;
- add a standalone context-management skill; or
- treat cheap implementer tokens as evidence that context capacity is
  unlimited.

## Authoritative contract and evidence matrix

| ID | Observable contract | Workflow owner | Named evidence | Status |
|---|---|---|---|---|
| BP1 | **One active implementer.** Exactly one implementation agent owns edits at a time; renewal never creates overlapping writers or Git operations. | `supervised-implementer-loop` | active-agent inventory; changed-path and Git-write record | Proposed |
| BP2 | **Persistence has a semantic boundary.** Reuse the current implementer throughout one admitted delivery package and its corrections. Consider renewal only at parent acceptance of a useful delivery-package or owner boundary, except when continuity has already become untrustworthy. | `supervised-implementer-loop` | admitted package map; acceptance packet; parent decision | Proposed |
| BP3 | **Continuity authority is explicit.** Record whether continuity is identity-persistent or role/model-persistent. Never silently replace an explicitly named implementer or substitute its model, reasoning effort, or execution mode. | `complex-work` for package policy; `supervised-implementer-loop` for execution | user instruction and package record | Proposed |
| BP4 | **Context health is observational.** Use available compaction, retained-prefix, message-topology, and behavioral evidence to decide whether to prepare renewal. No individual signal or invented number establishes failure. | `complex-work` | context-health disposition with cited observations | Proposed |
| BP5 | **Turnover preserves accepted state.** Before renewal, create and parent-verify one compact turnover packet covering exact tree state, accepted invariants, current owner boundary, checks, risks, and detailed evidence location. | `supervised-implementer-loop` | turnover packet and parent read-back | Proposed |
| BP6 | **The new context receives one complete bounded assignment.** Give the fresh implementer the accepted package state and next admitted boundary once, then resume delta-only communication. Do not replay raw logs, complete files, or superseded discussion. | `supervised-implementer-loop` | initial assignment and subsequent message inventory | Proposed |
| BP7 | **Turn triggering remains decision-bearing.** Queue deltas to an active implementer; trigger an idle turn only for substantive work. Do not use new-task turns for polling or fragmented status requests. | `supervised-implementer-loop` | collaboration-operation inventory | Proposed |
| BP8 | **Exceptional mid-package renewal stops and rebaselines.** If accepted decisions are contradicted, repeatedly rediscovered, or no longer carried reliably, stop implementation, inspect the dirty tree, classify completed and partial work, and obtain required replacement authority before resuming. | parent acceptance authority under `complex-work` | bounded dirty-tree inventory; invalidated assumptions; rebaseline decision | Proposed |
| BP9 | **Outer workflows do not duplicate the mechanism.** `review-fixpoint` consumes the accepted implementation package normally; implementer renewal neither adds a Tick nor changes independent-review authority. | `complex-work` composition; existing leaf owners | phase and role inventory | Proposed |

## Context-health disposition

Use three decision states:

- **continue:** current context remains coherent enough to finish the admitted
  package and ordinary corrections;
- **renew-at-boundary:** pressure is material, but semantic continuity remains
  trustworthy through the next accepted owner boundary; and
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

## Execution protocol

### 1. Establish continuity policy

At package setup, record:

- the required model, reasoning effort, and normal or fast execution mode;
- whether continuity is identity-persistent or role/model-persistent;
- the admitted delivery packages and safe turnover boundaries;
- the evidence artifact location; and
- who may authorize replacement when the current context cannot continue.

Do not add a ceremony for a small package that is expected to finish in one
coherent implementation context.

### 2. Run one bounded persistence epoch

Give the implementer the complete accepted package context once. Reuse it for
the admitted delivery package and all evidence-based corrections. Keep detailed
inspection, routine checks, and logs in its context or the evidence artifact.

Use queue-only messages for active-turn deltas. Trigger a new turn only after
the implementer is idle and the next substantive correction or accepted
boundary is ready. Batch related corrections instead of creating several small
new-task records.

### 3. Observe without imposing a threshold

When telemetry is available, record only observations relevant to the next
workflow decision. Do not poll solely to count compactions or context size.
Prefer the runtime's existing session data over self-reported estimates.

Select `continue`, `renew-at-boundary`, or `stop-and-rebaseline` from the
combined runtime and behavioral evidence. Explain the causal decision; do not
turn an arbitrary count into a language-independent constant.

### 4. Finish the useful boundary when trustworthy

When the disposition is `renew-at-boundary`, let the implementer finish the
smallest already-admitted owner package whose acceptance leaves the repository
better off. Run focused checks and produce the ordinary acceptance packet.
The parent independently verifies the owner boundary and accepts or corrects
it before turnover.

Do not start the next delivery package in the old context after renewal has
been selected.

### 5. Produce the turnover packet

The outgoing implementer records:

- package goal and plan identities;
- exact revision, or exact dirty-tree and changed-path state;
- accepted delivery packages and the invariants they established;
- the current semantic owner, physical boundary, and dependency direction;
- non-mechanical decisions and rejected approaches that must not return;
- focused checks and results, without raw successful logs;
- unresolved risks, blockers, and the next admitted dependency; and
- the detailed evidence location.

The parent verifies material claims against the current tree. An unverified
summary does not establish continuity.

### 6. Renew without replay

When role/model-persistent renewal is authorized, start one fresh implementer
with the same selected model, reasoning effort, and execution mode. Give it the
verified turnover packet, the current accepted package map, and the next
admitted boundary once. Later communication is delta-only.

The previous agent remains historical evidence, not an active compatibility
path. Do not ask both agents to implement or compare the same package.

### 7. Handle lost continuity safely

For `stop-and-rebaseline`, stop issuing implementation deltas. The parent
inspects the bounded dirty tree, classifies work as accepted, complete but
unaccepted, partial, or obsolete, and identifies the last trustworthy owner
boundary. Preserve useful edits and evidence; do not discard work merely to
obtain a clean conversational restart.

If explicit identity persistence applies, report the evidence and request
authorization before replacement. A context problem does not silently broaden
the replacement authority.

## Skill changes

### `complex-work`

- Extend the execution-cost profile with continuity policy, safe renewal
  boundaries, and replacement authority when delegated work is expected to
  span several substantial packages.
- Treat delegated-context growth without retained decision value as a
  coordination replanning signal, parallel to existing primary-context and
  polling signals.
- Own the cross-package decision to continue, renew at a boundary, or stop and
  rebaseline without copying the implementation leaf's handoff mechanics.

### `supervised-implementer-loop`

- Replace indefinite whole-work-package identity reuse with exactly one active
  implementer and bounded persistence through the current admitted delivery
  package.
- Add continuity mode and context-health disposition to package setup.
- Define the verified turnover packet and fresh-context assignment.
- Preserve delta-only correction, parent acceptance, serialized Git writes,
  and the prohibition on silent model substitution.
- Keep ordinary corrections in the same context; renewal is not routine agent
  churn.

### `evidence-efficient-review`

No implementation-lifecycle change is required. Its compact dossier and
coverage-ledger principles remain useful evidence formats, but implementer
turnover does not become independent review.

### `review-fixpoint`

No reviewer-policy change is required. A Tock may internally use more than one
authorized bounded implementer context while retaining one active implementer
at a time and one accepted remediation result. The subsequent Tick remains
independent and reviews the exact accepted revision.

Do not add a standalone context-lifecycle skill. Keep package coordination in
`complex-work`, implementation continuity in `supervised-implementer-loop`,
and review independence in the existing review owners.

## Validation scenarios

| Scenario | Expected behavior |
|---|---|
| Two-slice package completes coherently | The same implementer completes both slices and corrections; no renewal ceremony is added. |
| Four large owner packages exceed one useful context lifetime | The parent accepts the current owner package, verifies a turnover packet, and begins the next package in one fresh authorized context. |
| Several compactions occur but the implementer remains coherent | Compaction is recorded as observational pressure; work continues to the next meaningful boundary. |
| Implementer contradicts an accepted ownership decision mid-package | Parent stops the loop, inspects the dirty tree, invalidates affected assumptions, and rebaselines before any replacement or continuation. |
| User explicitly requires the existing named implementer | The workflow does not replace it automatically; it reports the context-health evidence and requests authorization at the safe boundary. |
| User requires Luna Max normal mode but not a particular identity | An authorized renewal uses Luna Max normal mode in a fresh context and receives one verified bounded assignment. |
| Active implementer needs a correction | Parent queues one batched delta; it does not create a replacement or a status-only new task. |
| Idle implementer receives the next small correction | Parent triggers one substantive follow-up and retains the context because the current package has not reached a renewal boundary. |
| Implementer is cheap while its retained context is saturated | Cheap execution remains preferred, but cost asymmetry does not override context reliability or semantic closure. |
| Tock implementation used two sequential contexts | Parent accepts one coherent Tock result; the independent Tick reviews the exact revision and does not treat turnover as another review phase. |

## Acceptance questions

- Is there exactly one active implementation writer at every point?
- Does persistence last through ordinary corrections and end only at a
  meaningful accepted boundary or a concrete loss of continuity?
- Is the user's identity, model, reasoning, and execution-mode requirement
  explicit and preserved?
- Are compaction and token observations diagnostic rather than invented pass or
  failure thresholds?
- Can the parent verify the accepted state from the turnover packet and current
  tree without replaying the complete transcript?
- Does a fresh implementer receive one complete bounded assignment followed by
  deltas?
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

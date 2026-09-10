# Remediation: subagent semantic-edit guidance

This record maps the three improvement reports to the workflow implemented on
`main`. The reports are historical process evidence, not a fresh product or
repository acceptance review. The selected implementation uses native
subagent task messaging with one persistent implementer and event-driven waits;
it has no semantic MCP runtime.

## Adopted in supervised-implementer-loop

The following behavior is now owned by
[`supervised-implementer-loop`](../skills/supervised-implementer-loop/SKILL.md):

- The parent selects one specific semantic edit at a time. The assignment
  names the owner, required behavior or interface, accepted prerequisites,
  constraints, exclusions, and local completion evidence. One edit may span
  files; no numeric size or duration limit is imposed.
- The implementer resolves source details and performs adaptation and repairs
  directly caused by that edit. It does not choose later edits or expand the
  admitted package. Its compact result reports outcome, attributed changes,
  owner or interface delta, checks by evidence phase, and unresolved risks.
- Expected reproduction failures remain distinct from final verification.
  Assignment-start state establishes attribution, including inherited dirt,
  same-file edits, and ambiguous provenance. Local completion remains distinct
  from package acceptance.
- The parent trusts a successful result as a working premise between edits and
  avoids routine implementation-detail rereads. Targeted parent reads are
  discouraged for routine detail but permitted for a concrete design,
  acceptance, attribution, or contradiction question.
- Before package-acceptance corrections, the parent performs one bounded,
  consolidated inspection of changed owners, affected consumers, and material
  residual topology, then sequences corrections from the complete finding set.
  A repeated architectural mismatch requires a concrete design checkpoint
  covering ownership, information flow, state and lifetime, transaction or
  ordering, failure and recovery, and decisive evidence.
- A wait timeout or caller interruption is not writer settlement. Direction
  changes require settlement evidence, current-state inspection, and
  classification of preserved work before a replacement assignment. Partial
  work is preserved and unresolved work is never replayed or overlapped.
- A verified milestone commit is allowed only under existing caller or
  repository commit authority, after the writer settles and attributable,
  coherent, locally checked state is verified. It preserves the original review
  and package base and map, is recorded as **verified-but-unaccepted**, and does
  not establish acceptance or fixed point. Interrupted, partial, unverified,
  or ambiguous work is not checkpointed; without commit authority it remains
  dirty state.

These rules address the bounded-edit, evidence-integrity, and convergence
findings in the [granularity report](improvement-semantic-edit-granularity-and-control.md),
the [M3 field learnings](improvement-semantic-edit-m3-field-learnings-2026-09-09.md),
and the [convergence-control report](improvement-implementation-convergence-control.md).

## Retained existing authority

The reports do not replace the surrounding workflow:

- [`complex-work`](../skills/complex-work/SKILL.md) remains the coordinator for
  mixed work packages, capability boundaries, package admission, and ownership
  of outer scope and commit policy.
- [`review-fixpoint`](../skills/review-fixpoint/SKILL.md) retains the Tock/Tick
  loop, phase lifecycle, exact-revision gate, persistent independent reviewer,
  and fixed-point decision. SIL package acceptance is not a Tick or fixed point.
- [`evidence-efficient-review`](../skills/evidence-efficient-review/SKILL.md)
  retains the contract-and-evidence model, sequential owner and seam review,
  residual-topology coverage, behavioral versus mechanism evidence, and
  economical final verification.

Plan readiness, delivery-package admission, independent acceptance, canonical
gates, review-artifact commits, and whole-scope fixed-point decisions stay at
their existing owning boundaries. The reports supply process corrections to
SIL; they do not create a second contract matrix, evidence ledger, or review
phase.

## Deliberately retired proposals

The semantic-edit reports proposed or described capabilities for a semantic MCP
runtime: semantic inspection operations, operation-status and result schemas,
automatic changed-file provenance, MCP cancellation or steering, backend
settlement controls, transport-specific state reconciliation, and MCP plugin or
server packaging. Those proposals are retired for this implementation.

Native subagent task messaging supplies the reusable implementer context,
follow-up deltas, completion mailbox, and event-driven waiting used here. SIL
therefore expresses the behavioral contract and recovery rules without naming
MCP operations, adding a semantic server, requiring an adapter, or claiming
runtime telemetry that native subagents do not provide. No automatic model
replacement, universal timeout, token-saving threshold, or transport-specific
steering behavior is inferred from the reports.

## Validation scenarios

Run these scenarios against the native subagent workflow before treating the
remediation as operationally validated:

1. Build one delivery package through multiple specific edits. Choose each
   next edit from the prior compact result, reuse the implementer, and avoid
   routine parent rereads while retaining targeted reads for concrete questions.
2. Introduce inherited and same-file dirt, an out-of-scope write, and ambiguous
   attribution. Confirm that only attributable changes are credited and that
   ambiguity blocks acceptance.
3. Produce expected-red and final-green checks, zero selected tests, stale
   green evidence, and a missing required assertion. Confirm that only the
   required final evidence establishes local completion.
4. Create original and cleanup failures around a transaction. Identify the
   mutation, failure, owner, and commit boundaries before deciding whether
   rollback is required; preserve both failures and distinguish facts,
   hypotheses, and runtime witnesses.
5. Repeat one architectural mismatch across corrections. Confirm that the
   parent pauses design-sensitive work until the concrete design checkpoint
   and decisive evidence are accepted.
6. Exercise completion, timeout, interruption, settlement, and partial-state
   recovery. Confirm that waiting or interruption alone does not start a
   second writer or authorize replay.
7. Exercise a verified milestone with existing commit authority and verify the
   preserved review/package base, verified-but-unaccepted status, and complete
   later package review. Repeat without authority and with interrupted or
   ambiguous work; confirm that no checkpoint is created.
8. Complete package acceptance, then run the existing exact-revision gate and
   independent Tick separately. Do not credit an edit result, checkpoint, or
   SIL acceptance as fixed point.

These scenarios establish workflow behavior only. They provide no token-saving,
latency, or throughput claim until a later controlled comparison supplies that
evidence.

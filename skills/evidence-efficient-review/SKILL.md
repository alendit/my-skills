---
name: evidence-efficient-review
description: >-
  Review implementation, architecture, or specification against an explicit
  target using compact evidence and sequential coverage. Use for broad reviews,
  specification audits, post-remediation reviews, and rebaselining. Not for
  implementing fixes or narrow diff acceptance.
---

# Evidence-Efficient Review

The caller owns scope, target, severity policy, artifact destination, commits,
and remediation decisions. This skill produces findings and a coverage decision
from current source or behavior.

## 1. Establish The Review Contract And Independence

Recover the scope, reviewed revision, authoritative requirements and non-goals,
architecture owners, previous review and baseline, required evidence, and
requested result format. Carry the existing behavioral goal and direct public
scenario, keeping mechanism progress separate. Resolve or consume material
[glossary state](../clear-technical-writing/references/project-glossaries.md#resolve-glossary-state-in-order).
Report missing review authority rather than inventing domain policy.

If the primary authored or supervised the work, use one independent read-only
reviewer. Otherwise the primary may review directly. Reuse an outer workflow's
persistent reviewer and review contract cells sequentially. Supply facts and
source, not expected findings. The primary verifies material candidates instead
of duplicating the full review. Add a reviewer only for a concrete unresolved
dispute, ambiguous cross-owner evidence, or an explicitly requested challenge.

## 2. Select Coverage And Target Mode

Use **incremental review** when trustworthy whole-scope coverage exists and the
change remediates explicit findings. Audit their closure first, invalidate
changed dependencies, and carry forward unaffected evidence.

Use **rebaseline review** when coverage is untrusted, the target or architecture
changed materially, a zero-finding decision was overturned, or impact is
uncertain. Cover the complete selected contract. File count alone does not
choose the mode; first widen the affected owner or contract cells.

For specifications, begin with [normalization and required specification cells](references/specification-review.md).
Separate current facts, accepted contracts, and proposed intent. Select contract
or implementation-plan review level; contract-level success may leave downstream
plan unknowns and never implies implementation readiness.

For implementation, use [promised closure and contract-cell review](references/implementation-review.md).
Read its residual-topology procedure when decomposition is in scope and its
seam/test sections as the reviewed behavior requires. When supporting mechanisms
are proposed or challenged, apply [behavioral design trace](references/behavioral-design-trace.md).

## 3. Collect A Compact Dossier

Gather the target contract, relevant diff and changed owners, prior finding IDs,
public entry points, focused tests, and current evidence. Start with known-term
searches or outlines, then read the ranges that answer a live question. Keep raw
logs, complete files, and remediation narratives outside the dossier unless
needed for a concrete decision.

Use the [review record](references/review-record.md#build-the-dossier) for
conditional fields and the existing incremental-review evidence budget.
Implementer inventories and normalized comparisons can locate questions; verify
them against source or behavior before crediting them as independent proof.

## 4. Review And Record Each Required Cell

Inspect the semantic owner and a realistic public composition, challenge the
applicable seams, record evidence and its decision, then move on. In incremental
mode, disposition every prior finding before broad new-defect exploration.

Maintain the compact [coverage record](references/review-record.md#record-coverage)
with four statuses:

- **cleared:** sufficient current evidence supports the contract;
- **candidate:** a concrete possible defect still needs proof or disposition;
- **unknown:** required review work remains;
- **not-applicable:** the dimension does not apply.

Unknown is not cleared. Invalidate evidence when its target, owner, consumer,
evidence source, or dependency changes. Widen invalidation when impact is
uncertain. For design changes, classify affected tests through the target-mode
reference rather than preserving obsolete mechanism assertions.

When architectural impact or deferral is claimed, or a concrete architecture
signal appears, use [architectural classification review](references/implementation-review.md#audit-architectural-scope-classifications).
The reviewer audits evidence and classification; it does not approve scope,
select remediation, accept deferral, or mutate follow-up records.

For a delegated review lasting several minutes, send a compact checkpoint after
material cell clusters and before the final gate: coverage status, active
command, and next question. A checkpoint is not a finding or final decision.
Return available candidate dispositions promptly; a status request does not
justify repeating completed coverage.

## 5. Prove Candidates And Verify

For each candidate, establish source proof or a minimal reproducer, the accepted
contract violation and public impact, supported defect history, owning correction,
and why a tempting workaround fails. If remediation would add or preserve a
defense, apply [economic actionability](references/economic-actionability.md).
Source-level possibility alone does not establish operational importance.
Have the primary verify material claims and severity.

Run focused checks to prove candidates and clear consequential cells. Perform
one required final gate at a meaningful checkpoint; green tests cannot negate
a concrete reproducer or prove unexamined architecture. Keep verbose output in
a temporary log and report revision, command, exit status, concise counts, and
only needed failure detail. Use the [verification procedure](references/review-record.md#verify-within-the-evidence-budget)
for execution and budget handling.

## 6. Return The Decision

Use the caller's artifact format and the [result fields](references/review-record.md#return-the-review-result):
reviewed scope/revision, prior-finding dispositions, confirmed findings with
proof and owner, coverage and unknowns, and verification. For locally repairable
specification defects, provide exact replacement or insertion text.

Accept a whole-scope zero-finding result only when prior findings are closed,
all required cells are cleared or not applicable, and the caller's complete
evidence gate passes. For specifications, apply this to the selected level and
report downstream plan unknowns separately. Do not invent lower-value findings
or relabel required unknowns as optional follow-ups to finish.

Apply one [clear-writing pass](../clear-technical-writing/SKILL.md) after findings,
severity, evidence, and correction semantics stabilize. Return the decision to
the caller; it owns review numbering, commits, remediation, repetition, and the
outer stop condition. Implementation handoff acceptance does not replace this
independent whole-scope review.

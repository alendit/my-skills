---
name: evidence-efficient-review
description: >-
  Review an implementation, architecture, or specification against an explicit
  target with one evidence model and minimal repeated context. Use for broad
  codebase reviews, pre-implementation specification audits, post-remediation
  audits, fixed-point review phases, and rebaselining. Do not use for
  implementing fixes or narrow diff acceptance.
---

# Evidence-Efficient Review

Review an implementation against an explicit target with one coherent evidence
model. Preserve breadth through contract coverage and adversarial seam analysis,
not by assigning several agents overlapping subsystem scans.

This skill owns review mechanics. The caller owns the surrounding workflow,
scope, target, severity policy, artifact location, commit policy, and decision
about whether findings trigger remediation.

## Establish The Review Contract

Before reading broad source, identify:

- the exact scope and reviewed revision;
- target-authoritative requirements and explicit non-goals;
- current architecture, ownership, dependency, and public-contract authorities;
- the latest relevant review and its reviewed baseline, when one exists;
- required evidence and canonical verification;
- severity and finding policy; and
- the requested result or review-artifact format.

Do not infer domain policy from this skill. If these inputs cannot be recovered
from the request and repository, report the missing review contract instead of
inventing one.

The reviewed target may be current implementation or proposed specification.
For a proposed target, distinguish accepted preceding contracts, current
implementation facts, future intent, and explicit non-goals; do not treat the
proposal's own wording as proof of feasibility or necessity.

## Choose The Review Mode

Use **incremental review** when a trustworthy prior whole-scope review exists
and the current work remediates its explicit findings. This remains the default
even when the remediation diff is large: audit each promised closure, invalidate
the contract evidence affected by its owner changes, and carry forward evidence
whose dependencies remain unchanged.

Use **rebaseline review** when no trustworthy coverage exists, the target or
architecture changed materially, a prior zero-finding decision was overturned,
or the impact cone is uncertain. Cover the complete selected contract
sequentially; do not replace rebaselining with several overlapping reviewers.

Rebaseline because prior coverage or dependency impact is untrustworthy, not
merely because many files changed. When uncertain, widen the affected owner or
contract cells first. A narrow diff cannot prove a whole-scope decision when
unreviewed inherited behavior remains possible.

## Review Specifications Before Implementation

For architecture notes, stage overviews, or slice contracts, read
[references/specification-review.md](references/specification-review.md) before
building the dossier. Its normalization is the required first review operation:
create one authoritative contract-and-evidence matrix, then review its contract
rows and required specification cells sequentially. Do not begin by accepting
the proposal's section structure or expanding every conceptual entity into a
private representation.

Keep durable observable contracts separate from a conditional implementation
appendix. Require mechanisms and exact limits to state why correctness depends
on them. Classify every named proof as a deterministic release gate, external
compatibility evidence, or observational telemetry, and preserve the distinct
status and completion effect defined in the reference.

Review ordered documents one at a time. Carry cleared cells forward so later
documents build on accepted earlier decisions. Reopen an earlier decision only
when a downstream join or current-source fact concretely invalidates it.

When wording is defective, provide explicit replacement or insertion text. For
duplicate authority, name the owning matrix row and the copies to delete or
replace with ID references. Do not report vague findings such as "improve
clarity" or "strengthen the transaction description."

## Build A Compact Review Dossier

Create one neutral dossier before detailed reasoning. Prefer deterministic,
compact evidence:

- status, history, baseline-to-current diff, and changed symbols;
- outlines of changed owners and adjacent consumers before exact range reads;
- the authoritative contract matrix, architecture ownership, and public entry
  points;
- prior finding identifiers and dispositions;
- relevant architectural-scope decision records, the selected durable ledger
  authority, and follow-up deltas;
- changed, added, and contract-named tests, classified as contract or mechanism
  evidence; and
- cheap searches for forbidden paths, duplicated authorities, compatibility
  branches, or other target-specific negative constraints.

Use fast search for known terms and an available structural outline tool before
broad file reads. Keep raw gate logs, complete source files, historical review
bodies, and remediation narratives out of the dossier unless a concrete
question requires them.

Keep dossier commands query-sized. Search a patch for filenames, symbols, and
hunk headers instead of loading a large patch body. When changed symbols or
exact ranges are already known, read those ranges directly rather than
outlining an entire large owner. Cap outlines and source reads to the smallest
result that can answer the current question; do not combine several large
ranges in one tool call.

Treat tool output as review cost. For an incremental post-remediation review,
default to at most 20 evidence-producing tool calls before the final gate when
the caller supplies no tighter budget. Keep individual source/outline results
under roughly 200 lines. If required coverage cannot be completed within the
budget, return the remaining cells as unknown instead of expanding context
without bound. Do not read every target document again when the prior review
already records its contract; reopen only changed authorities and sections
needed for a live closure question.

The dossier supplies facts and routing, not the remediation author's suspected
answer.

## Audit Promised Closure First

For implementation review, read
[references/implementation-review.md](references/implementation-review.md).
In incremental mode, apply its promised-closure proof and remediation-delta
audit before broad new-defect exploration. Disposition every prior finding
individually; neither a nearby mechanism nor a green named regression proves
that the owning boundary moved.

## Preserve Independence Without Reviewer Fan-Out

Use one reviewer for the complete review whenever delegation is needed. Reuse
that reviewer across the review's sequential contract cells; do not split the
same scope among subsystem agents merely for breadth.

- If the primary authored or supervised the implementation, use one fresh
  read-only reviewer when delegation is available.
- If the primary is independent of the implementation, it may apply this
  method directly.
- Never use the implementation author as the sole fixed-point reviewer.
- Give a delegated reviewer the neutral dossier and source tree, not expected
  findings or remediation reasoning.
- The primary verifies material candidate findings rather than duplicating the
  complete review.

Use another reviewer only for a concrete unresolved dispute, ambiguous
cross-owner evidence, or an explicitly requested independent challenge. Scope
that pass to the uncertainty instead of restarting the review.

## Review Contract Cells Sequentially

For implementation review, apply the contract-cell, seam, and test-evidence
rules in the linked implementation reference. For specification review, apply
the required cells and scenario portfolio in the specification reference.
Inspect the semantic owner and a realistic public composition, record the cell,
then move to the next; do not replace sequential coverage with one broad scan.

## Audit Architectural Scope Classifications

When the reviewed work claims architectural impact or defers an architectural
correction, read
[the architectural scope decision authority](../supervised-implementer-loop/references/architectural-scope-decision.md)
completely. Use it only to audit evidence and classification. A reviewer never
selects remediation, accepts a deferral, creates or mutates a follow-up record,
or authorizes package scope.

Require causal source, dependency, state, or test evidence before accepting a
non-local impact as an architecture signal; effort, file count, inherent public
composition, and implementation friction are insufficient. Audit the recorded
proper-correction bound without expanding it into a redesign.

For a claimed deferral, independently verify current-contract satisfaction,
every applicable non-worsening disposition, stable semantic identity and
deduplication, authorized durable read-back, current lifecycle state, activation
state, and handoff visibility. Report records created, updated, closed, stale,
or unchanged-but-relevant as observed deltas; never perform those mutations.

Classify a source-proven current contract violation, unresolved P0-P3 defect,
worsening correction, valid external `product-contract-failure`, or activated
follow-up as a current finding under the caller's severity policy. Keep missing
required evidence `unknown`. An evidenced improvement outside the current
contract is not a P2 merely because it is attractive: report it as a non-gating
architectural improvement only when the linked authority qualifies it, and
otherwise omit it or retain the concrete unanswered question. Never relabel a
current finding or unknown as a follow-up to produce a zero-finding decision.

## Maintain A Coverage Ledger

Keep compact external state so later cells do not require reconstructing prior
reasoning. Each cell records:

```text
Contract: <stable identifier and single normative source>
Revision: <reviewed revision>
Dependencies: <owners and consumers actually inspected>
Dimensions: <applicable seams challenged>
Evidence class: deterministic gate | external compatibility |
                observational telemetry | not-applicable
Evidence: <source proof, scenario, focused test, reproducer, or measurement>
Evidence status: <pass/fail; external freshness/failure state; or observational>
Decision role: <what this evidence can establish or block>
Test kind: contract | mechanism | not-applicable
Review classification: current finding | required unknown |
                       non-gating architectural improvement | not-applicable
Architectural decision: <record identity and audited branch, or not-applicable>
Follow-up state: <stable ID, durable read-back, lifecycle/activation state,
                  observed delta, or not-applicable>
Status: cleared | candidate | unknown | not-applicable
Next question: <only when unresolved>
```

For external compatibility evidence, record capability identity, freshness
window, evidence age, and reuse decision. For telemetry, record its baseline and
threshold or mark it observational. For a specification, also record the
required specification-cell dispositions from the linked reference; they are
coverage, not optional commentary.

The statuses have distinct meanings:

- **cleared:** sufficient current evidence supports the selected contract;
- **candidate:** a concrete possible defect needs proof or disposition;
- **unknown:** required review work remains;
- **not-applicable:** the dimension genuinely does not apply.

Unknown is not cleared. Zero confirmed findings with unknown required coverage
is an incomplete review, not a fixed point.

Use `candidate` while a possible current defect still needs proof. A confirmed
finding is a review result backed by its cell evidence, not a new cleared
status. Use `non-gating architectural improvement` only when the current
contract is cleared and the improvement's causal qualification is evidenced.
That classification does not approve deferral or substitute for an authorized
durable follow-up.

For incremental review, invalidate a cell when its target, owner, relevant
consumer, evidence, or dependency contract changed. Prefer symbol-level impact
when reliable; invalidate the wider owner when extraction or dependency impact
is uncertain.

When the specification changed, record the disposition of affected tests as
`retain`, `strengthen`, `replace`, or `delete`. Treat replacement or deletion of
obsolete mechanism evidence as design correction, not regression. Require
adjacent boundary evidence where applicable: exact/one-over, success/failure,
first/repeated invocation, and clean retry after abort. Repetition must cross a
known or derived failure threshold when the assertion is meant to distinguish
local settlement from end-of-entry cleanup.

## Escalate Only Concrete Candidates

Spend redundant reasoning on candidate findings, not on every cleared area.
For each candidate:

1. Prove it through a minimal reproducer or exact source invariant.
2. Establish public impact when the contract is externally observable.
3. Classify it as new, recurrent, inherited, or incomplete prior closure when
   history supports that distinction.
4. Name the owning correction and explain why tempting local workarounds would
   preserve the defect.
5. Have the primary independently verify material claims and severity.

Report only reproduced or source-proven findings. Keep speculative concerns as
unknown review questions rather than inflating the finding list.

Do not assign P2 or any other severity solely because an unrelated improvement
would be valuable. Severity requires a current target violation and the impact
required by the caller's policy. An unactivated follow-up is not a current
target merely because its ledger record is visible.

Do not implement remediation during the review. Temporary diagnostic probes
must stay within authorization, remain clearly disposable, and not become
unreviewed production changes.

## Verify Economically

Run focused checks while proving candidates or clearing high-risk cells. Defer
the complete canonical gate to one meaningful final checkpoint unless the
review contract requires otherwise. Automated checks are evidence; green gates
cannot negate a concrete reproducer or establish unexamined architecture.

Keep successful gate output out of model context: write verbose output to a
temporary log and retain only the command, exit status, concise test counts, and
failure tail when needed. Do not rerun an overlapping complete gate merely to
obtain another presentation of the same evidence.

Run each final gate in the foreground and wait on that execution instead of
starting background jobs and polling their logs. Final verification should add
at most three tool calls beyond the evidence budget unless a gate fails and its
failure needs bounded diagnosis.

Record revision-dependent evidence as such. Do not treat counts, identities,
timings, or a clean worktree from another revision as current facts.

## Return A Structured Review Result

Return or draft the caller's requested artifact with:

- decision, scope, and reviewed revision;
- disposition of every prior finding;
- confirmed findings with severity, proof, owner, and principled fix direction;
- exact proposed wording when the reviewed target is a specification and the
  defect can be corrected locally in prose;
- the authoritative contract-matrix delta and required specification-cell
  dispositions when the target is a specification;
- coverage ledger or a compact coverage summary;
- architectural-scope classification and observed follow-up-ledger delta,
  including stable IDs, read-back/lifecycle state, and any laundering rejection;
- unresolved unknowns, if any;
- focused and complete verification evidence; and
- progress toward the explicit target and applicable architecture self-check.

A whole-scope zero-finding decision requires every required cell to be cleared
or not applicable on the reviewed revision, every prior finding to be closed,
and the caller's complete evidence gate to pass. Stop rather than inventing
lower-value findings.

## Interaction With Outer Workflows

When called by a fixpoint orchestrator, this skill performs only the review
phase and returns its decision. The orchestrator owns review numbering,
commits, remediation selection, repetition, and the final stop condition.

When findings trigger a supervised implementation package, that package's
slice-level acceptance checks are not a substitute for this independent
whole-scope review.

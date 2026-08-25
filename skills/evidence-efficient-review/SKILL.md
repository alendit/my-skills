---
name: evidence-efficient-review
description: Review an implementation, architecture, or specification against an explicit target with one evidence model and minimal repeated context. Use for broad codebase reviews, pre-implementation specification audits, post-remediation audits, fixed-point review phases, and rebaselining. Do not use for implementing fixes or narrow diff acceptance.
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

For architecture notes, stage overviews, or slice contracts, normalize every
material conceptual entity into this chain:

```text
owner -> physical representation -> lifetime -> transaction boundary ->
public surface -> metric definition -> named evidence
```

Require each link to be concrete enough to implement and test. Mark a link not
applicable only with a reason. Check joins to accepted earlier contracts and
planned downstream consumers, but do not force future detail into the current
slice merely to fill the chain.

Challenge the specification itself:

- distinguish a semantic requirement from one possible transaction, counter,
  field, capability, or test vocabulary;
- require a separate resource dimension or metric only when it enforces a
  genuinely distinct bound or has an operational consumer;
- reject circular admission plans, impossible representations, owner gaps, and
  evidence that cannot observe the stated contract;
- prefer one cohesive owner over parallel subsystems created only to mirror
  documentation classifications; and
- permit simplification when it preserves the project goal, stable public
  semantics, boundedness, ownership, and recovery.

Review ordered documents one at a time. Carry cleared cells forward so later
documents build on accepted earlier decisions. Reopen an earlier decision only
when a downstream join or current-source fact concretely invalidates it.

When wording is defective, provide explicit replacement or insertion text (or
an equally concrete formulation). Do not report vague findings such as
"improve clarity" or "strengthen the transaction description."

## Build A Compact Review Dossier

Create one neutral dossier before detailed reasoning. Prefer deterministic,
compact evidence:

- status, history, baseline-to-current diff, and changed symbols;
- outlines of changed owners and adjacent consumers before exact range reads;
- target requirements, architecture ownership, and public entry points;
- prior finding identifiers and dispositions;
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

In an incremental post-remediation review, complete prior-finding disposition
before broad new-defect exploration:

1. Extract each prior finding's violated invariant, reproducer, semantic owner,
   and required owning correction into a compact checklist.
2. For each finding, trace the original negative scenario through the current
   owner, including the exact order of admission, mutation, commit, abort, and
   cleanup operations when applicable.
3. Compare the implemented boundary with the required correction. A nearby new
   mechanism, updated documentation, or green named regression does not prove
   that the required boundary moved or became exact.
4. Re-run the original reproducer or a smaller equivalent when source ordering
   alone does not establish closure.
5. Mark the finding closed only after owner evidence and its public composition
   agree. Otherwise report incomplete closure before searching for unrelated
   defects.

Record this compact closure proof before declaring the disposition complete:

```text
Prior finding: <identifier>
Required boundary: <invariant and owning correction from the prior review>
Current proof: <exact source order/range or rerun reproducer>
Disposition: closed | incomplete | recurrent | unknown
```

Do not batch several findings into a generic “repairs are present” conclusion.
For a temporal or transactional finding, `Current proof` must spell out the
actual ordered calls and name where the exact admission capability is acquired
relative to mutation and commit. Tests or documentation alone cannot supply
that proof.

After disposition, challenge interactions among the changed owners and sample
the highest-risk invalidated contract cells. Carry unchanged cleared cells from
the prior review instead of reconstructing them from the full source tree.

Before branching into unrelated latent defects, audit the changed transaction
itself. Enumerate every operation newly inserted, removed, or reordered between
admission and the first irreversible mutation. For each operation, prove that
its failure modes and resource costs are covered by the acquired capability or
remain rollback-safe. This delta audit takes precedence over exploring an
unchanged downstream limit: a credible new defect does not compensate for
missing a defect introduced by the remediation under review.

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

Derive review cells from the selected target: supported behaviors, ownership
boundaries, public routes, resource policies, failure contracts, performance
bounds, and negative constraints. For each applicable cell:

1. State the target claim and semantic owner.
2. Trace the owner through adapters and representative public consumers.
3. Inspect only the source ranges needed to answer the current question.
4. Challenge the applicable seams below.
5. Check owner evidence and at least one realistic composed boundary when the
   contract is public or cross-component.
6. Record the result before moving to the next cell.

Use these adversarial dimensions when relevant, without forcing every dimension
onto every contract:

- authority and dependency direction;
- admission before mutation;
- begin, commit, abort, drop, recovery, and retry completeness;
- ownership, transfer, reclamation, and state lifetime;
- exact, one-over, partition, schedule, or scaling boundaries;
- expected-error placement versus unexpected-error surfacing;
- identity and provenance across representations or bridges;
- substitutability across selected variants and routes;
- owner behavior versus public composition;
- hidden physical ceilings or duplicated policy;
- obsolete fallback, compatibility, or silent downgrade paths; and
- complexity accounting against real work rather than timing alone.

For test evidence, apply these additional checks:

- A contract test should protect stable public semantics, ownership,
  boundedness, or recovery. Prefer focused semantic partitions and adjacent
  boundaries over one heroic catch-all witness.
- Ask whether a simpler independently designed correct implementation could
  pass the test. If not, the test freezes mechanism unless that mechanism is an
  explicit stable contract.
- Compare each test name with its actual assertions; do not credit a broader
  claim than the assertions establish.
- Prove that a boundary witness can reach its claimed owner without violating
  an earlier admission bound. Do not raise or bypass the earlier bound merely
  to exercise a later defensive mechanism. Keep the stable public test at the
  earliest observable contract and test an otherwise unreachable serializer or
  ABI ceiling locally as disposable mechanism evidence.
- Do not credit a conformance label without an assertion-level coverage
  description.
- Challenge internal metrics that have no operational consumer, and assertions
  tied to field layout, counter vocabulary, or the current transaction
  decomposition.
- Challenge spec-induced accidental complexity. When a simpler owner or
  contract still advances the explicit project goal, recommend correcting the
  specification rather than implementing evidence vocabulary literally.

Inspect history only when it answers a live question such as regression
classification, incomplete prior closure, or the intended invariant. Do not
front-load repository archaeology.

## Maintain A Coverage Ledger

Keep compact external state so later cells do not require reconstructing prior
reasoning. Each cell records:

```text
Contract: <target claim or identifier>
Revision: <reviewed revision>
Dependencies: <owners and consumers actually inspected>
Dimensions: <applicable seams challenged>
Evidence: <source proof, focused test, or reproducer>
Test kind: contract | mechanism | not-applicable
Status: cleared | candidate | unknown | not-applicable
Next question: <only when unresolved>
```

The statuses have distinct meanings:

- **cleared:** sufficient current evidence supports the selected contract;
- **candidate:** a concrete possible defect needs proof or disposition;
- **unknown:** required review work remains;
- **not-applicable:** the dimension genuinely does not apply.

Unknown is not cleared. Zero confirmed findings with unknown required coverage
is an incomplete review, not a fixed point.

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
- coverage ledger or a compact coverage summary;
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

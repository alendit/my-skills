# Semantic-edit M3 field learnings and improvement proposals

## Status and evidence boundary

This note records observations from the 2026-09-09 Clojure-WASM M3 session and
its side conversation. It proposes changes to semantic-edit tooling and skill
guidance; it does not implement them or change the active delivery plan.
Evidence below comes from the supplied session record, not a fresh audit of
the running operation or repository. Later parent-thread progress is unknown.

At the observed boundary, focused tests had passed for several named-type
behaviors, including diagnostics, identity and hashing, admission, accessor
retirement, and metadata dispatch. M3 remained incomplete and unaccepted.
A same-form extension followed by a throw still exposed missing rollback.
An operation to attach private publication undo information had started; its
outcome was not available. Package verification and independent review were
still pending. Passing local checks must not be described as M3 completion.

The user raised three useful process questions: whether the implementation
request was too large, why waiting required frequent checks, and whether
intermittent commits would make progress easier to inspect. The proposals
below incorporate all three.

This note supplements [edit granularity and execution control](improvement-semantic-edit-granularity-and-control.md),
[efficient waiting](improvement-efficient-subagent-polling.md), and
[implementation convergence control](improvement-implementation-convergence-control.md).
Terminology for independent review (Tick) and remediation (Tock) follows the
[project glossary](glossary.md). A checkpoint commit below means a proposed
recovery and progress record, with no implication of acceptance.

## Observations and proposed improvements

### 1. Validate the tool with a bounded operation

Request 017 combined diagnostic emission, runtime bindings and rendering,
manifests or profiles, documentation, and tests. That was too broad for the
immediate goal of validating semantic-tool operation. Cancellation eventually
left a terminal partial result, a resumable context, and changes in 13 files.
Cancellation stopped further writing; it did not roll back completed edits.

Later requests were easier to assess: 018 addressed equality admission in two
files, 019 added an identity/hash-key test in one file, and 020 addressed a
canonical-name guard across three files. These examples support bounded
semantic requests, not a universal file-count or duration limit.

Proposed skill sequence: establish tool status, perform a bounded read-only
inspection, then request one useful edit with a named owner, completion
condition, exclusions, and prerequisites. Keep the delivery package separate
from the edits used to build it. A small edit should still establish meaningful
behavior; splitting work into arbitrary textual fragments does not solve the
control problem. Inspect missing cross-owner facts before authorizing mutation.

Validation: cancel an operation after a partial edit, confirm the writer has
settled, preserve the result, and resume with a narrow correction. The parent
must be able to identify completed and remaining work from the terminal report.

### 2. Wait for completion without repeated reassurance

The parent repeatedly resumed the outer transport wait at roughly minute
intervals and posted updates with no new result. These were transport waits,
not repeated semantic operation-status queries. That distinction explains the
mechanism but does not make the commentary useful.

Proposed adapter and skill behavior: use completion-driven waiting where the
harness supports it. Where the transport requires explicit continuation,
continue silently unless a new result, blocker, decision, or required status
update warrants a message. Query backend status when it can resolve an actual
uncertainty, such as a disconnected call or cancellation outcome. Do not claim
that every transport automatically wakes the parent, or equate stopping an
outer wait with stopping the writer.

Validation: a long successful operation should produce its result without
redundant backend probes or repeated no-change commentary; a lost connection
should still allow bounded status recovery.

### 3. Derive changed files from operation provenance

Request 021 failed result validation because its reported changed-files list
included an already-dirty `image.rs`. The operation's actual delta affected
`named_type_values.rs` and `tests/stage2_slice07.rs`. Inspection recovered the
distinction, and a focused test subsequently passed.

Proposed runtime change: derive the operation delta from before/after state.
Report inherited dirty paths, operation changes, and authorized package scope
separately. Retain a model-report discrepancy as diagnostic evidence without
discarding the useful semantic report. Scope violations must still block
acceptance; machine-derived provenance should strengthen that check.

Validation: begin with unrelated dirty files, modify a permitted file, and
verify the report attributes only the operation delta. Also exercise unrelated
edits in the same file, an actual out-of-scope write, and concurrent changes.
Ambiguous provenance must remain explicit rather than being attributed by guess.

### 4. Separate expected reproduction failures from final checks

Request 030 reproduced a null-callable trap and fixed it. Its report included
both the failed pre-fix check and the passing post-fix check. Result validation
rejected it with `APPLIED requires passing checks and no unresolved issues`.
The parent recovered the compact model result and independently reran the
focused regression successfully.

This is a different reporting failure from request 021. The observed record
supports one changed-files mismatch and one verification-classification
failure, not two changed-files mismatches.

Proposed result schema: attach purpose or phase, inspected state, expected
outcome, and actual outcome to each check. Decide final success from the
required checks on the resulting state. A reproduced pre-fix failure is useful
history; a failing required final check still prevents `APPLIED`.
Expose a compact rejected report alongside the validation reason so recovery
does not require log archaeology or a test rerun solely to recover schema data.

Validation: distinguish expected-red/green, unexpected final failure, stale
green evidence, and a missing required final check.

### 5. Make local completion evidence explicit

Request 027 reported `APPLIED` for a retirement primitive but returned an
accessor-collision regression and a diff check, without the requested
retirement-specific commit/abort proof. The parent correctly retained that
gap. Elsewhere, a test filter selected zero tests before request 038 corrected
the full path. A test name mentioning revisions was not itself evidence that
revision behavior was asserted.

Proposed contract: each request names its local evidence obligations; the
result records which are covered and which remain unproved. Include executed,
failed, and ignored test counts. `APPLIED` should satisfy the selected local
completion condition, not silently substitute an adjacent passing test.
Preserved changes with missing required evidence need an explicit partial or
blocked result. This should not grow into an independent review after every
edit: parent acceptance still assesses accumulated semantic and architectural
evidence at the chosen slice boundary.

Validation: reject zero-test success as proof of a required regression and
detect a result that supplies a neighboring test instead of the requested
commit/abort partition.

### 6. Preserve original failures and distinguish facts from hypotheses

A retirement failure initially surfaced as a secondary frame-abort error and
poisoned state. Request 029 captured the original trap at function 138, offset
`0x9548`. Inspection first suspected a host producer, then traced immediate
guest callers that intentionally supplied a null staged root. A subsequent
inspection incorrectly concluded that the nullable reference test and cast
handled null safely. The direct regression in request 030 demonstrated the
trap; a non-null guard corrected it.

Proposed runtime diagnostics: preserve both the original failure and cleanup
failure, with artifact identity and source or instruction mapping where
available. Proposed inspection guidance: separate source facts, inferred
causes, and runtime witnesses. When a claim conflicts with observed execution,
trace the concrete operand and caller or request a bounded probe. Repeating
the intended behavior does not resolve the contradiction.

Validation: a cleanup failure must not erase the first trap, and a supplied
counterexample must reopen a contradicted inspection conclusion.

### 7. Keep local repairs with the implementer; escalate real design gaps

Request 035 normalized a `FIELD_AT` operand but left the field-array read on
the original wrapper, then described the remaining defect as out of scope.
Request 036 completed that same local substitution and passed. By contrast,
the test-only request 032 correctly stopped at a discovered metadata dispatch
bug; a separately authorized implementation request fixed lookup while
preserving the original method receiver.

Proposed guidance: repair incomplete substitutions and directly caused local
implementation failures within the authorized edit. Preserve test-only scope.
Raise a design checkpoint for a missing owner, impossible contract, or new
semantic decision. Explain the missing decision and evidence, rather than
using an unresolved local implementation detail to broaden the package.

The retirement work also showed a useful checkpoint: an operation stopped
when safe post-settlement unlinking was unclear. Inspection found an existing
success boundary and distinguished nested expansion behavior before mutation
continued. Preserve that control point; do not replace it with speculative
global state or a generic transaction framework.

### 8. Locate the transaction boundary before requiring rollback

Request 039 expected an extension from an earlier top-level form to disappear
when a later form threw. Inspection established that the loader's outer
identity boundary did not make all top-level forms one semantic transaction.
Request 040 moved the extension and throw into the same `do` form. Revision
state still remained changed, exposing a genuine missing rollback contract.

Proposed test design: name the mutation, failure point, owning transaction,
and commit boundary before specifying recovery. Distinguish failure before
allocation, after staging, before commit, and in a later committed top-level
form. Do not repair a test by weakening a valid same-transaction requirement,
or repair the runtime to undo behavior that the accepted contract makes durable.

The subsequent publication-undo operation was still pending at the evidence
boundary. Its proposed use of an existing private carrier is not a validated
result or an architecture endorsement in this note.

## Proposal: checkpoint commits for inspectable progress

Intermittent commits would provide stable comparison and recovery points while
a package accumulates many semantic edits. They would make it easier to answer
what has been completed, what remains dirty, and which checks apply to which
state. Commit count alone would not measure progress or prove correctness.

The observed M3 plan commits the accepted complete package before its canonical
gate and independent Tick. Adding internal checkpoints therefore requires an
explicit workflow adjustment. This note proposes that adjustment; it does not
authorize or perform it in the active parent session.

Suggested sequence:

1. Choose a coherent internal milestone with useful local evidence. Do not
   commit after every tool call or on an arbitrary timer.
2. Wait until the writer has settled. Confirm the precise repository state
   and attribute the accumulated changes, including preserved partial results.
3. Inspect and stage only the intended package changes. Preserve unrelated
   user edits, including those sharing a file. Serialize every Git write.
4. Commit a concise record of the included behavior and operation IDs, checks
   and their inspected state, known failures or missing evidence, and the
   package's unaccepted status. Prefer milestones with passing local checks.
   If an interrupted-work checkpoint is allowed, label it explicitly and
   retain its failed or pending evidence.
5. Reconcile the semantic tool's expected state through its supported commit
   boundary before the next operation. Preserve the persistent context and
   stale-state protection; do not bypass a mismatch by substituting a token.
6. Continue from that checkpoint. Keep the package's original review base so
   later acceptance includes all unaccepted changes, including committed ones.
7. At completed package acceptance, retain the existing exact-revision gate
   and independent Tick. A checkpoint is neither a Tock completion nor a Tick,
   and does not establish fixed point. Do not run the full gate after every
   internal checkpoint merely because a commit exists.

No pushing, squashing, or history rewriting is implied. Recovery commits and
accepted delivery commits must remain distinguishable in progress reporting.

Validation should demonstrate continuation in the same semantic context after
a checkpoint, rejection of stale expected state, preservation of unrelated
same-file edits, and review of the entire package across multiple checkpoints.
It should also demonstrate that a running writer prevents checkpoint creation
and that an interrupted checkpoint cannot be presented as a validated milestone.

## Suggested ownership and evaluation

| Change | Owning boundary | Evidence of improvement |
|---|---|---|
| Bounded requests and design checkpoints | Supervised implementation guidance | Useful local completion without silent scope growth |
| Completion-driven waiting | Harness adapter plus caller guidance | Fewer empty continuations or probes without lost completion or recovery |
| Change provenance and verification phases | Semantic-edit runtime and result schema | Accurate deltas and final-state decisions in the scenarios above |
| Original failure preservation | Execution diagnostics | Original and cleanup errors remain independently inspectable |
| Checkpoint commits | Delivery workflow plus tool state reconciliation | Safe resume and complete review coverage across committed milestones |

Prioritize result integrity and writer/state reconciliation before expanding
checkpoint automation. Guidance alone cannot correct a runtime schema that
misclassifies valid evidence. Conversely, a schema cannot decide the correct
transaction contract or replace the parent's design authority.

The session demonstrated useful tool execution, resumable partial work, and
several successful bounded corrections. It also required parent intervention
for scope, misleading evidence, and design decisions. There is no controlled
baseline here for token savings, throughput, or latency. A future comparison
should record operation scope, latency, parent continuations, repeated checks,
repair loops, context reuse, and accepted behavior. Treat these as observations,
not invented acceptance thresholds; separate waiting time from reasoning cost.

## Evidence locators

- The observed workflow is Codex session `01a08cbd-b8e5-75f1-ba59-e7d9fea022f1`.
- Requests 017-021 provide the bounded-request, cancellation, and provenance
  observations.
- Requests 027-030 provide the local-evidence, zero-selection, original-failure,
  cleanup-failure, and contradicted-hypothesis observations.
- Requests 032, 035, and 036 provide the test-only, local-repair, and design-gap
  distinctions.
- Requests 038-040 provide the test-selection and transaction-boundary
  observations.
- The evidence boundary ends while the publication-undo operation is pending;
  later package acceptance and independent-review outcomes are outside this
  report.

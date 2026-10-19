---
name: supervised-implementer-loop
description: >-
  Implement a non-trivial code work package through ordered delivery packages
  with one persistent implementer and parent acceptance. Use when delegated
  exploration, editing, and focused validation are useful. Keep prose-heavy
  specification, design, and skill authoring with the parent unless explicitly
  delegated. Not for review-only work or small direct edits.
---

# Supervised Implementer Loop

The parent owns scope, design decisions, sequencing, and acceptance. One active
implementer owns routine code investigation, edits, and focused checks. Accept
coherent owner-level or public behavior, letting the implementer complete its
internal edits without a separate assignment for each function or file.

## 1. Establish And Admit The Package

Inspect the request, repository guidance, current tree, and existing changes.
State the outcome, non-goals, acceptance evidence, and authorization boundaries;
preserve unrelated work. Keep prose-heavy authorship with the parent. For mixed
work, delegate the admitted code package and its directly supporting tests,
fixtures, comments, and documentation.

Inspect enough to establish scope and the admission route. Trace owners only
for the first delivery package, and stop once you can name its outcome, owner,
and acceptance check; later packages are traced when assigned. Assign routine
owner tracing, adjacent-consumer inspection, and focused evidence gathering to
the implementer with the code package. If missing facts block a design
decision, before or between packages, assign the implementer a bounded
investigation checkpoint first; the parent decides from its findings before
dependent edits begin.

Select [admission depth](references/contract-and-scenario-package.md#choose-admission-depth)
before spawning. For bounded work with established behavior, ownership, and
checks, the parent accepts a compact delivery brief. Use the formal matrix and
reviewed plan when required by the caller/repository or when material contract,
architecture, recovery, or delivery dependencies remain unresolved. Preserve
existing review requirements and return invalidated decisions to their owner.

For bounded delivery, carry the brief's outcome and direct scenario, reusing
goal/contract IDs only when they already exist. Formal or design-sensitive work
uses [the goal record](references/contract-and-scenario-package.md#carry-the-behavioral-goal-record).
Keep behavior separate from mechanism progress. When shared terminology is
material, resolve or consume [glossary state](../clear-technical-writing/references/project-glossaries.md#resolve-glossary-state-in-order)
once and carry only material changes thereafter; otherwise omit the payload.

At setup, select the relevant package-reference sections: “Profile
design-sensitive owners” for changed responsibilities; “Profile modularization
roots” when physical decomposition is in scope; and “Define a small scenario
portfolio” through “Keep tests stable across redesigns” for evidence planning.
Use the external-scenario and exact-limit procedures only when they apply.

## 2. Select And Assign One Implementer

Use [implementer selection](references/implementer-continuity.md#select-the-implementer)
to select the configured role and any explicit overrides. Default to
`role/model-persistent` continuity: spawn and respawn within the authorized work
without asking again. Honor explicit identity restrictions and use normal
execution unless fast mode is explicitly requested. Keep one implementation
writer active through the delivery package, corrections, and parent acceptance.

Send the [initial assignment](references/contract-and-scenario-package.md#assign-and-hand-off-a-delivery-package)
once: accepted brief or formal map and current package, owner and behavior, prerequisites,
exclusions, ordered implementer-owned checkpoints with focused evidence,
decision boundaries, base revision, and commit
authority. Start with no parent conversation history; in Codex, explicitly set
`fork_turns: "none"` on every spawn or respawn. Supply a self-contained brief and
relevant artifact pointers instead of the parent transcript or orchestration
references. Record starting paths and diff only when inherited dirt or
overlapping changes make attribution uncertain. Keep verbose working evidence
with the implementer or in a referenced artifact.
Carry the full package map only as sequencing context. Admit only the current
parent-acceptable package; future packages remain unassigned until the parent
accepts the current package.
Checkpoints guide execution inside that package: the implementer verifies them
before dependent work and continues without routine parent approval. They do not
create delivery packages, canonical gates, or independently shippable states.

Before spawning, choose an append-only progress-log path in a shared location that
both agents can read and write without approval, such as a task directory under
`/private/tmp` when it is writable for both. Pass its absolute path in the
assignment and have the implementer create the log and verify access. Only the
implementer appends dated progress entries; the parent reads only the range
requested by the child and replies directly. Preserve the log across turns and
compaction. The implementer writes milestones, changed evidence, blockers, and
`DONE` there.
Child-local commentary is not delivery.
Use the [compact agent-message transport](references/compact-agent-messages.md)
for log entries and exceptional direct messages after the self-contained
assignment. Directly message the parent only when a parent-owned decision is
needed or progress cannot continue efficiently. If direct messaging is
unavailable, use a final-channel handoff at that boundary and resume the same
child; do not add status-only turns. Completion uses the log and the child's
final response, not a separate direct `DONE` message.
Bound the work up front with an expected completion or checkpoint window,
milestones, immediate blocker conditions, and a credible stall deadline. Every
child message and final handoff specifies `log-read: none` when self-contained,
or `log-read: <absolute-path>:<start-line>-<end-line>` with 1-based line numbers
when context is needed. Select a mailbox timeout up to the stall deadline within
the runtime's limit; completion interrupts the wait.
Use the reference's duration examples as starting points, not work limits or
acceptance thresholds.

## 3. Wait For An Event

Let the implementer investigate, edit, and run focused checks. Before the first
wait, state the send time and stall deadline as absolute times in the parent's
update so they survive compaction. Until that deadline, silence and an
unchanged tree or log are normal: do not inspect them for progress, and never
resend the package assignment. Corrections and replies stay deltas.

Do independent work when it advances the authorized request, such as a pending
design decision or parent-owned prose drafted outside the implementer's tree
(for example, beside the progress log). Otherwise wait. Prefer waiting to broad
exploration of future packages merely to occupy the interval; delegate that
routine work when its package is assigned. Avoid mirroring source, diff, and successful-log reads. While a
package is active, make no edits in the implementer's tree, even to files it
does not own; its checks and commit would absorb them. Apply parent edits
between packages, after acceptance and before the next assignment. Serialize
Git writes.

1. On an empty timeout before the agreed stall deadline, wait again directly.
   At that deadline, use the stall procedure; do not automatically read the log.
   After compaction or resume, recover the send time and deadline before
   reacting to silence. If they are lost, check the child's status once
   (`list_agents` in Codex); if it is still running, start a fresh stall window.
2. On a child decision or blocker message, follow its `log-read` instruction
   and reply directly to the child. If that instruction is missing and more
   context is needed, ask the child for the range. Use `send_message` for an active
   child or `followup_task` to resume the same idle child with the decision. The parent
   writes no log entries. Never return directly to waiting after a message;
   wait again only after delivering the response and establishing the child's
   next action with no parent action remaining.
3. On child completion, follow its `log-read` instruction, then begin acceptance.
4. If a promised event misses its stall deadline, or concrete safety, scope,
   or lifecycle evidence changes the decision, use the [stall procedure](references/implementer-continuity.md#handle-a-missed-event).
   Timeout count alone is not a stall signal. If the first recovery turn fails,
   apply [bounded recovery](references/implementer-continuity.md#bound-recovery-attempts):
   stop issuing deltas and rebaseline instead of returning the same context to
   another correction cycle.

The Codex plugin's session hook supplies a developer-level waiting exception
for implementers, reviewers, and long-running verification commands. Verify
that it is active before using the extended wait window. Keep routine command
polling inside the executor or an existing cheaper capable worker; use the
[gate waiting procedure](../evidence-efficient-review/references/review-record.md#verify-within-the-evidence-budget)
without transferring parent acceptance.

## 4. Inspect, Correct, Or Accept

Apply the [delivery execution and closure rules](references/contract-and-scenario-package.md#execute-ordered-delivery-packages)
to each package: its prerequisites must already be accepted, and it must close
useful behavior without relying on a later package to repair incomplete semantics.

1. Consume the compact `DONE` [handoff](references/contract-and-scenario-package.md#assign-and-hand-off-a-delivery-package):
   base/head or settled diff, behavior and owner changes, established contracts,
   focused results, unresolved questions, and detailed-evidence location. Planned
   claims must now have current source and assertion evidence. Formal packages
   carry the realization relation; bounded briefs need only their applicable
   behavior and owner evidence.
   Reference the implementer's checkpoint evidence; record the parent's
   acceptance decision and any new evidence without copying the report into
   another status file.
2. Treat successful handoffs as the working premise until this acceptance
   boundary. Independently inspect the changed owners and a few consequential
   seams; select risk probes that add evidence beyond the implementer's checks.
   Prefer narrow ranges, inventories, normalized comparisons, and focused
   witnesses. Expand reads for concrete contradictions, missing evidence,
   attribution, design, scope, safety, or acceptance questions. A summary alone
   does not establish acceptance.
   Before an expensive rerun, name the unresolved question or invalidated
   dependency. In the existing brief or handoff, distinguish changed executable
   behavior, build recipe/toolchain, artifact identity/admission, and prose.
   Reuse unaffected evidence with its original revision and a current
   equivalence check; exercise the actual consumer of changed manifests or
   identities. A manifest-only refresh need not replay unrelated behavior or
   performance suites, while backend or recipe changes invalidate the checks
   that depend on them. Keep required exact-candidate gates and defer fresh
   reconstruction until their inputs settle unless an earlier result is needed
   for a concrete decision.
3. Consolidate defects into one ordered correction set: evidence, violated
   invariant, owning boundary, required result and proof, and any invalid local
   workaround. Finish the bounded inspection before dispatching that set; let
   the implementer resolve related internal edits and checks without per-edit
   approval unless a design or scope decision blocks them. Send a compact
   `CORRECTION` delta to the same implementer and repeat this step. Before
   requiring rollback or cleanup, identify the mutation, failure, transaction,
   and commit/publication boundaries; distinguish an uncommitted failure from
   cleanup after an earlier commit.
4. For non-local impact, uncertain ownership, mechanism-coupled tests, hidden
   responsibilities, or a recurring failed design assumption, pause dependent
   changes and use the [architectural decision process](references/architectural-scope-decision.md).
   The parent accepts the decision; a contract change returns to product
   authority. Resume from the accepted boundary, preserving unaffected evidence.
5. Accept only when every required contract has current realization evidence,
   the direct scenario and applicable structural checks pass, and feedback is
   resolved. For modularization, inspect extracted and residual responsibilities;
   preservation alone does not establish locality. Required unknowns block
   acceptance.

Use a coherent locally validated handoff commit as the review anchor when
authorized; otherwise use the settled attributable diff. Commits describe the
durable behavior change and reason; the shared log carries the SHA and transient
evidence. A commit is not acceptance. Preserve the original review base across
unaccepted checkpoints, and accept the full original-base-to-final range. Avoid
per-function commits and commit polling; stage only attributable changes.

## 5. Continue And Finish

After acceptance, send the next admitted delivery package as a delta. Reuse the
context while it remains trustworthy. When context pressure or continuity loss
requires a decision, follow [continuity and recovery](references/implementer-continuity.md#executable-continuity-sequence).
Ordinary renewal occurs only after parent acceptance; replacement requires the
old writer and its subprocesses to be settled, not merely an interrupt receipt.

Run focused checks during iteration and required complete gates at meaningful
package checkpoints. Unless the contract requires it earlier, start the broad
suite after focused package acceptance. Run a required clean-revision gate once
on the accepted checkpoint rather than duplicating it before and after commit.

Before returning the work package, check:

- every contract and direct public scenario is accepted, with mechanism status
  and any external capability status reported separately;
- applicable structural, architectural-decision, and authorized follow-up
  evidence is complete, including residual topology when activated;
- required gates pass and no partial work, unresolved feedback, overlapping
  writer, or unintended dirty state remains; and
- the handoff identifies accepted packages, verification, commits or pending
  changes, material terminology state, and real remaining limitations.

Apply one [clear-writing pass](../clear-technical-writing/SKILL.md) after those
decisions stabilize. Return to the caller: delivery acceptance during a Tock
does not replace the independent Tick. Continue remaining work in the authorized
request; finish at the accepted requested outcome, a user-directed boundary,
or a concrete blocker requiring input.

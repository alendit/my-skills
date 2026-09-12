# Proposal: restore the baseline workflow and retain measured lessons

Status: design proposal; workflow, branches, and installed plugin have not been
changed by this proposal. The parent authors the proposal and all implementation
edits. An independent reviewer may review the proposal or completed changes.

Baseline: `a4dc591a6598021653cbdebba5c23d0d591a63c5`.
Sources compared: `75ea3c64f8550f2c9bf0342dd795d8381c5b8c78`,
`b8c783017d5e02482e1a6964b8bb29e2f98f72f4`, the experimental branch, the
skills-only plugin source, and the two recorded session trees below.

## Intended outcome and evidence

Restore delegation of coherent code implementation to one persistent, cheaper
capable implementer. The parent owns design, scope, ordering, integration, and
acceptance; the implementer owns routine source exploration, edits, local
adaptation, and focused checks inside the assigned boundary. The parent writes
specifications, skill text, design proposals, and other prose-heavy artifacts
directly, using the relevant writing skill. Independent review remains separate.

Use delivery-package boundaries already admitted by the baseline. Internal
steps are implementer work, without a mandatory parent turn per function or
semantic edit. Progress messages resume a parent decision only when needed.

The baseline-era M2 tree is rooted at
`01a07a22-7b2e-7822-b7eb-7aca5652904a`; the later native-subagent tree is rooted
at `01a09018-760e-7743-b15b-f06b8598c2d5`, containing implementer
`01a0901a-e50d-71d2-8f0f-84f57b37722c`.

| Observation | Baseline-era tree | Later tree |
|---|---:|---:|
| Recorded elapsed hours | 51.47 | 16.11 |
| Parent share of raw input | 11.6% | 28.2% |
| Parent shell commands per elapsed hour | 16.4 | 95.0 |
| Parent follow-ups and sent messages per elapsed hour | 1.7 | 15.3 |
| Empty waits followed immediately by another wait | 228/266 | 147/440 |
| Empty waits followed by parent `exec` | 33/266 | 253/440 |
| Recorded outcome | Independent fixed point | Usage limit; acceptance pending |

These are different workloads and observation windows, not an A/B experiment or
proof of savings. Raw input includes cached input; elapsed time includes waits.
The data supports reducing parent coordination and repeated inspection. It does
not isolate plugin packaging as a cause, justify universal slice sizes, or
establish that every proposed safeguard saves tokens. Evidence and settlement
safeguards also address concrete field reports. Parent prose ownership and long
failsafe waits are explicit user choices for the revised workflow.

Preserve analysis commit `3f3da25` unchanged. Its two standalone Python scripts
and tests remain development utilities, outside the plugin's skill/tool surface.
The follow-on wait-outcome figures above came from transcript inspection; the
current scripts reproduce tree totals and call counts, not that classification.

## Changes against baseline owners

Line numbers in this table refer to the immutable baseline, not the current
experimental checkout. Modify the existing process at these locations; avoid a
second general-guidance section or a duplicate evidence ledger.

| File and baseline location | Existing behavior | Proposed delta |
|---|---|---|
| `skills/supervised-implementer-loop/SKILL.md`: description, lines 3–12; Select The Implementer, line 111 | Can attract any substantial dependent implementation | Route code-heavy implementation here; keep prose-heavy authorship with parent. |
| Same: Give The Initial Assignment, line 149 | Full context, progress envelope, commit authority once | Bound coherent work up front, delegate internal steps, specify event/checkpoint and commit handoff. |
| Same: Run Each Delivery Package, line 250 | Package assignment, compact packet, independent acceptance | Add conditional provenance/evidence distinctions; consolidate corrections; use commit anchors. |
| Same: Route Architectural Scope Decisions, line 229 | Existing authority and rebaseline branches | Repeated mismatch triggers the existing design decision before further dependent edits. |
| Same: Keep The Loop Economical, line 363; Event-Driven Progress And Stall Protocol, line 386 | Longest permitted wait; risk-triggered reads | Define state-to-action sequence, long failsafe horizons, and empty-timeout behavior. |
| Same: objective, lines 21–28; closing lines 464–465 | Ends the assigned package, returns to fixpoint caller | Explicitly return control to the outer request and continue remaining authorized work. |
| `skills/supervised-implementer-loop/references/implementer-continuity.md`: Exceptional stop and rebaseline, line 168 | Classifies dirty work after stopping deltas | Establish writer/subprocess settlement before inspection, replay, or replacement. |
| `skills/complex-work/SKILL.md`: Assign Leaf Owners, line 90; delegation and waiting, lines 150–178 | Cost-based delegation and broad implementation routing | Classify prose/code units first; consume SIL waiting process instead of duplicating it. |
| Same: installation, lines 182–185; final handoff, line 235 | Standalone skill links and integrated delivery | Dispatch installation according to selected distribution; add outer completion decision. |
| `skills/review-fixpoint/SKILL.md`: Tock routing, lines 18–21 and 192–211 | Routes non-trivial remediation through SIL | Parent remediates prose; SIL handles suitable code packages; preserve independent reviewer. |
| Same: phase-commit rule, lines 38–45 | Requires creating a remediation commit after acceptance | Reuse an eligible accepted handoff commit or create the required phase commit, then gate that exact clean revision. |
| Same: Optional Goal Persistence, lines 432–454 | Runtime-goal workflow embedded in review | Remove automatic goal workflow; retain behavioral goal/evidence records and outer completion. |
| `skills/review-fixpoint/references/phase-mechanics.md`: Verify each Tock, lines 50–78 | Accepted phase commit and exact-revision gate | Reuse an eligible accepted handoff commit; checkpoints do not replace phase acceptance. |

Leave contract mapping, reviewed-plan admission, modularization coverage,
glossary authority, context-renewal boundaries, and independent Tick semantics
at their baseline owners. A checkpoint does not authorize renewal or change the
admitted package map. Prose routing must not accidentally impose a production
implementation-plan gate on writing the specification that precedes that plan.

## Proposed process text and decisions

### 1. Choose the author before delegating

At routing, identify the unit's main work. For specifications, plans, skills,
design prose, and editorial remediation, the parent authors and revises the
artifact using its specialized skill. For code-heavy work, select the existing
authorized cheaper capable implementer and use the supervised loop. In mixed
work, keep design/specification authorship with the parent and delegate the
admitted code unit; source comments, fixtures, tests, and documentation directly
needed to explain that code may stay with its implementer. Classify by work,
not file extension. Explicit user delegation overrides this default.

Following a specialized skill does not itself require another agent. Review
ownership is independent of authorship: a reviewer can evaluate parent prose.
For this implementation request, the parent also edits packaging scripts.

Suggested SIL description:

> Implement a non-trivial code work package through ordered, dependent delivery
> packages with one persistent implementer and parent acceptance. Use when code
> exploration, editing, and focused validation benefit from delegated execution.
> Keep prose-heavy specification, design, and skill authoring with the parent
> unless the user explicitly requests delegation.

### 2. Assign a coherent boundary once

Start with the baseline assignment and admitted map. Name the current owner or
observable behavior, accepted prerequisites, exclusions, focused completion
checks, and questions requiring a parent decision. Let the implementer choose
and complete internal edits, compiler/import/fixture adaptation, and repairs
directly caused by this work. Report a material scope or design gap before
expanding it. Do not require a parent assignment for each internal edit.

When inherited dirt, same-file overlap, or another actor makes attribution
uncertain, record the assignment-start commit and relevant dirty paths/diff.
Resolve ambiguous attribution before acceptance. An ordinary clean assignment
uses its base SHA; it needs no extra per-edit provenance ceremony.

### 3. Agree on events and then wait

Use this sequence in place of the existing overlapping waiting advice:

1. At assignment, agree on an expected completion or meaningful checkpoint
   window, the first credible stall deadline, and immediate blocker/decision
   events. The bound describes useful work; elapsed time does not force a tiny
   edit or an artificial commit.
2. Set a failsafe timeout slightly beyond the expected event window, within the
   tool's actual limit. Prefer a generous horizon because inbox events return
   early. Illustrative starting points are 30 minutes for substantial work,
   45–60 minutes for known long builds/checks, and 10–15 minutes for clearly
   smaller work. Adjust to actual work and platform limits; these are examples,
   not performance thresholds or mandatory time bands.
3. While the writer owns the unit, wait on its inbox. Independent useful work
   outside the writer-owned scope may continue; generic preparation is not a
   reason to reread the same source, diff, or successful logs.
4. An empty timeout within the agreed envelope leads directly to another wait.
   It carries no new repository or lifecycle evidence. A missed promised event
   past the agreed stall deadline can justify one narrow lifecycle check or
   status request. A first timeout is not automatically ignored if that agreed
   deadline has already passed; repeated timeout count alone is not the rule.
5. On a progress-only event, retain the updated expectation and wait again. On
   a blocker or decision request, answer the named question with the smallest
   necessary evidence. On completion, enter the acceptance process below.
6. If a higher-priority harness instruction caps waits or requires periodic
   commentary, honor it with a minimal update and resume waiting. Do not turn
   that wakeup into inspection or a new assignment. Record the harness limit
   as a limitation of the requested long-wait behavior.

Current harness instructions include a 60-second commentary requirement and
advice against blocking waits longer than 60 seconds. Skill text cannot override
them. The proposed 30–60 minute behavior requires a compatible harness policy;
the skill can still eliminate timeout-driven rechecks under the current policy.
No transport, timer tool, scheduler, or Codex source change is part of this patch.

### 4. Deliver compact evidence with a stable revision

The implementer completes focused checks, settles its processes, and sends one
inbox handoff. Extend the baseline packet rather than introducing a new schema:
outcome, owner/interface delta, attributable paths, base/head SHA when committed,
focused final checks and results, and unresolved risks or decisions. Keep large
logs and evidence at referenced locations.

Distinguish expected pre-fix reproduction from final verification when both
occur. Report zero selected tests, stale passes, or absent required assertions
as missing evidence. When diagnosis is uncertain, distinguish observations,
hypotheses, and execution witnesses; preserve the original failure separately
from any cleanup failure. These fields apply when relevant, not as an empty
checklist repeated after every operation.

At a coherent, locally validated handoff or useful recovery boundary, use a
commit if existing authority permits it. The initial assignment identifies the
Git owner. Delegate commits only with clear attribution and serialized Git
writes; the implementer must settle editing/checking processes before committing.
When inherited dirt or integration makes staging ambiguous, the parent selects
and commits the attributable change after writer handoff. Never sweep unrelated
work into a commit merely because it shares the file.

Use the commit message for the durable behavior change and its reason, plus a
short validation summary when useful. Use the inbox for notification, SHA, and
transient risks or questions. Reference durable content instead of copying a
second report. A commit marks a reviewable revision; acceptance is a separate
parent decision. Avoid per-function commits and commit polling.

When authority allows a checkpoint before full package acceptance, preserve the
package/review base and label the checkpoint unaccepted in the handoff. Later
acceptance covers the entire base-to-final range, including every checkpoint.
An unaccepted commit never becomes the next acceptance base by accident. With
no commit authority, use the settled diff and the same compact handoff.

### 5. Accept once, then correct from the combined findings

Use a successful progress/result summary as the working premise until the
meaningful acceptance boundary. Parent reads remain available for a concrete
design decision, contradiction, attribution, scope, safety, or acceptance
question; routine mirroring of implementer exploration is discouraged.

At a completed delivery package, examine the compact packet and revision/range
summary, then inspect the consequential owner/consumer boundaries and select
independent risk probes as the baseline already requires. Consolidate findings
from that bounded inspection before dispatching corrections. Give the same
implementer one ordered correction set with evidence, violated invariant, and
required result. On return, recheck affected evidence and seams; expand only
when new evidence justifies it. Neither a SHA nor a green summary self-approves.

If rollback or cleanup is implicated, first locate mutation, failure, transaction
ownership, and publication/commit boundaries. Correct according to whether the
failure precedes publication or follows an earlier commit. If the same accepted
architectural assumption fails again, pause dependent changes and invoke the
existing architecture/rebaseline owner with the intended owner, information
flow, lifetime, ordering, failure path, and decisive evidence. Resolve that
decision before another local patch.

At phase acceptance, reuse the final handoff commit if it already represents
exactly the accepted phase and repository policy permits. Otherwise make the
required phase commit. Run the existing exact-revision gate once at its required
boundary and preserve the independent Tick; no empty acceptance commit or
duplicate full gate is needed solely to mark approval. Update both the
review-fixpoint entrypoint phase-commit rule and its phase-mechanics reference
so neither still requires a redundant new remediation commit.

### 6. Settle invalidated work and finish at the correct boundary

When direction is invalidated, stop dependent assignments and request writer
interruption. Before inspection/replay/replacement, obtain lifecycle evidence
that the active turn and writer-owned subprocesses or cleanup have settled.
Classify preserved work under the existing accepted/complete-but-unaccepted/
partial/obsolete process. A timeout or interrupt acknowledgement alone does not
prove settlement. If settlement cannot be established, do not overlap writers.

After acceptance, return control to the caller and choose the next unmet step
in the authorized request. Finish when the full requested outcome is accepted,
the user chooses another boundary, or a concrete blocker requires input. Keep
this decision short at outer completion points. Remove baseline Optional Goal
Persistence and do not port the later runtime-goal reference; explicitly
requested platform goals remain governed by the tool contract. Existing
behavioral goals and their acceptance evidence remain intact.

## Restore the branch and preserve plugin distribution

Repository state observed for this proposal:

- This checkout is on `semantic-edit-tool` at analysis commit `3f3da25` and has
  untracked experiment and plugin files.
- `main` is checked out cleanly at `b8c7830` in
  `/private/tmp/my-skills-main-20260910`; `origin/main` is still `a4dc591`.
- Neither `.codex-plugin/plugin.json` nor `scripts/export_variants.py` has a
  commit in the inspected history. The working manifest describes `my-skills-b`.
- `/Users/dimitrivorona/plugins/my-skills/.codex-plugin/plugin.json` is the
  existing skills-only `my-skills` manifest. Its `SOURCE_REVISION` records
  `b8c7830`. That is the distribution template to recover, not its newer skills.
- The personal marketplace entry is named `my-skills` with source path
  `./plugins/my-skills`. Resolve that path through the configured plugin loader
  before selecting the update destination; the template path alone does not
  prove which source the active installation uses.

Execute restoration as a separate first implementation step:

1. Recheck both worktrees and refs. Preserve current main and experimental tips
   with named recovery refs, including the committed proposal and analyzers.
   Archive the untracked experiment files outside the restored worktree and
   verify their inventory/content before relocating conflicting files. Preserve
   any newly discovered dirty work as well; do not use blanket cleanup.
2. Detach the clean secondary worktree at its preserved main tip, move local
   `main` to `a4dc591`, and switch the primary checkout to `main`. Serialize all
   ref/index writes. Verify the tracked baseline before adding any improvements.
   This is a local restoration; no remote history rewrite or push is required.
3. Cherry-pick analysis commit `3f3da25` and the proposal commit independently.
   Do not cherry-pick `75ea3c6` or `b8c7830` wholesale. Parent applies the scoped
   process edits above against the baseline.
4. Recover only the plugin infrastructure below in a separate commit. Because
   it is uncommitted/external today, this is a selective file/logic port rather
   than a literal cherry-pick of an existing plugin commit.

Plugin infrastructure to include:

- Add `.codex-plugin/plugin.json` with the existing `my-skills` identity and
  `skills: ./skills/`, neutral engineering description, and a stable base
  version. Do not carry machine-specific cachebuster state into source control.
- Adapt the existing exporter’s safe staging, file inventory, and reference
  validation into one small `scripts/export_plugin.py`. Export a selected
  committed revision to a new `my-skills` directory, with all eight skills,
  transitive local reference closure, revision provenance, and file hashes.
  Reject escaping/broken references and protected or existing destinations.
  Do not export unrelated reports, session data, or experiment code. Include
  necessary documentation reached by skill references, including references
  outside `skills/`; validate the resulting closure recursively.
- Add focused exporter tests and a repository README covering build, install,
  update, and verification. Preserve the existing personal marketplace identity
  and source mapping. Use the supported plugin-creator update/cachebuster and
  reinstall flow; do not add another installer framework or hand-edit marketplace
  configuration. Initial setup uses its scaffold flow when no entry exists.
- Stage and validate the complete package before touching the installed source.
  Inventory/back up the previous source, synchronize only this plugin's selected
  contents, remove obsolete plugin-owned files through that bounded replacement,
  reinstall, and verify revision plus skill/reference hashes in the resolved
  cache. Account separately for the expected cachebuster manifest delta. Preserve
  other plugins and use a fresh session to test discovery.

Exclude the semantic server, MCP manifests, portable experiment `plugin.json`,
A/B variant output, runtime dependencies, steering/status/inspection tools, and
machine paths. The plugin adds distribution of skills, with no tool surface.

## Implementation order and acceptance

Commit independently: (1) recovery/baseline plus preserved analysis/proposal;
(2) parent-authored workflow edits; (3) skills-only plugin infrastructure.
Validate the final committed source before replacing the installed package.
The parent owns all edits for this request; one independent reviewer may assess
the proposal and final patch. Reuse that reviewer for corrections if available.

Check the final diff against `a4dc591` for concrete routing or decision changes,
not merely wording additions. Every new operational instruction should occur in
the process step that uses it. Use the following scenarios as acceptance checks:

| Scenario | Expected decision or evidence |
|---|---|
| Long specification or skill revision | Parent authors it; reviewer may review it; no implementer merely because it is long. |
| Code package with several dependent internal edits | One coherent assignment; implementer adapts and validates internally. |
| Mixed spec and code | Parent owns spec decisions; admitted code unit can be delegated with its local supporting artifacts. |
| Empty timeout inside agreed window | Next action is another wait; no repository/status probe. |
| Completion arrives before timeout | Inbox resumes acceptance promptly; no fixed sleep delays it. |
| One-minute harness communication cap | Minimal update then wait; record limit; do not claim long waits were achieved. |
| Promised checkpoint exceeds stall deadline | One narrow lifecycle/status probe; no routine diff review or assumed dead writer. |
| Progress-only message | Carry expectation forward; do not initiate acceptance or another internal edit. |
| Dirty same-file work at handoff | Attribute against starting state; stage only owned changes or use a settled diff. |
| Expected-red, zero selected tests, final-green checks | Distinguish phases and missing evidence; accept only required current assertions. |
| Several defects across one package | Consolidate owner/seam findings, send one ordered correction set, recheck affected evidence. |
| Failure before versus after commit | Determine transaction/publication boundary before prescribing rollback. |
| Repeated owner/design mismatch | Resolve the concrete architecture decision before another dependent correction. |
| Interrupted writer with child process still running | Preserve partial work and wait for settlement; no replacement writer or replay. |
| Several unaccepted checkpoints | Final acceptance covers the original package base through the final SHA. |
| Handoff commit already represents accepted Tock | Reuse it if policy permits; run exact-revision gate and independent Tick as required. |
| Package accepted while outer work remains | Continue the next authorized unit; no runtime-goal polling added. |
| Export/install/update | Complete closed package, correct identity/revision, no semantic runtime/tools, fresh-session discovery. |
| Failed export, invalid reference, or destination conflict | Existing source/cache remains intact; report actionable failure. |

Run skill frontmatter validation for changed entrypoints, link/reference checks,
the preserved analyzer tests, plugin exporter tests, and the plugin manifest
validator. Review realistic scenario decisions independently where useful; text
matching and simulated scenarios do not establish token savings.

After a later real code task, compare parent share, empty-timeout next actions,
parent duplicate reads, handoff frequency, cache-aware usage, and accepted
outcomes using the preserved analyzers and targeted transcript evidence. Report
the workload/window and any harness communication constraint. Do not invent a
savings threshold or attribute improvement to packaging alone.

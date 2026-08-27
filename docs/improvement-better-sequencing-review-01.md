# Better Fixpoint Sequencing — Review 01

## Decision

**Changes requested** on exact revision
`db92c5e85a703cd2c6cd4b0e9723575a067f512b`.

This independent rebaseline implementation Tick found one P2 defect. BS2-BS7
and M1-M6 are cleared, but BS1 and D1 do not clear because the generalized
`review-fixpoint` entrypoint still directs Tock to apply “breaking-cleanup
rules.” That retained imperative conflicts with the new repository-controlled
compatibility and cleanup owner, so the package has not reached deterministic
fixed point.

Reviewed scope:

- `docs/improvement-better-sequencing.md` as the sole BS1-BS7 authority;
- baseline `ae02e60492613244a021ce6e4b03ce2911cab55e` and its nine-file delta to
  the reviewed revision;
- `review-fixpoint`, `supervised-implementer-loop`, and
  `evidence-efficient-review`, including every changed one-level reference and
  the `review-fixpoint` interface prompt; and
- `docs/glossary.md` and the semantic sources for its material terms.

Review mode was rebaseline because no prior whole-scope Better Sequencing
implementation review exists.

## Prior Findings

None. This is the first numbered review for this package.

## BS1-BS7 Coverage

| Contract | Status | Evidence |
|---|---|---|
| BS1 repository-neutral outer workflow | **Candidate; D1 failed through Finding 01.** | The entrypoint, interface prompt, evidence boundary, and phase policy otherwise obtain artifact, compatibility, and gate policy from repository guidance (`review-fixpoint/SKILL.md:13-75`; `agents/openai.yaml:1-4`; `contract-and-evidence-boundary.md:27-41`; `phase-mechanics.md:12-20,50-68`). The remaining caller at `review-fixpoint/SKILL.md:185-187` still names unconditional breaking-cleanup rules. |
| BS2 diagnostic versus authoritative acceptance | **Cleared.** | `review-fixpoint/SKILL.md:279-310` orders deterministic owner proof, exact-commit gate, independent repository Tick, one authoritative attempt, evidence update, and bounded evidence-owner Tick. It invalidates material owner changes and keeps availability separate from deterministic failure. |
| BS3 bounded delegated progress | **Cleared.** | `supervised-implementer-loop/SKILL.md:220-241` requires pre-command disclosure and periodic checkpoints, lets an active completion handoff finish, and gives silence exactly one request, one additional bounded wait, and at most one interrupt before same-agent delta-only resumption. |
| BS4 localize before rerunning | **Cleared.** | `contract-and-scenario-package.md:98-124` requires the provider-neutral diagnostic tuple, keeps its field layout private, permits a next run only after improved capture or implementation change, and rejects truncation-only reruns. |
| BS5 control-only durable identity | **Cleared.** | `implementation-review.md:99-110` makes this a conditional review seam and requires a truthful, resolvable, response-owned event across success, preparation failure, repetition, reopen, and branch or fork. |
| BS6 effective external evidence identity | **Cleared.** | `implementation-review.md:112-128` traces effective native requests or metadata, challenges defaults, overrides, mismatches, mixed requests, and partial capture, and invalidates evidence without rewriting the execution result. |
| BS7 delegated review checkpoints | **Cleared.** | `evidence-efficient-review/SKILL.md:171-187` assigns checkpoint content and status communication to the correct owners, preserves independence, surfaces candidates promptly, and prohibits status-triggered cell reruns. |

## D1 And M1-M6 Evidence

All seven scenarios are deterministic repository evidence. “Workflow packet”
and “review packet” describe the controlled input form, not additional evidence
classes.

| Scenario | Result | Controlled evidence and localization |
|---|---|---|
| D1 repository-neutral source audit | **Fail.** | A package-wide search found no unconditional Rust, Clojure, ABI, Clippy, stage, or artifact-layout assumption; the only numbered-review reference is explicitly conditional on repository convention. The remaining phrase `breaking-cleanup rules` localizes the failure to the Tock caller at `review-fixpoint/SKILL.md:185-187`. |
| M1 diagnostic-to-acceptance sequence | **Pass.** | An early live failure remains diagnostic and ledger-ineligible; only an exact accepted implementation commit proceeds through repository Tick to one authoritative attempt. A changed request, response, identity, capture, or finalization owner invalidates the record and returns defects to Tock (`review-fixpoint/SKILL.md:281-310`). |
| M2 implementer schedules | **Pass.** | Active long work reports its command and checkpoints without interruption; completed work hands off normally; silent idle work receives process/diff inspection, one request, one 60-second follow-up wait, and at most one interrupt before same-agent resumption (`supervised-implementer-loop/SKILL.md:220-241`). |
| M3 external-failure localization ladder | **Pass.** | The failed-scenario packet records effective request, external presentation and action, semantic-owner state, resulting identity, and invariant. An unchanged run is rejected until capture or implementation changes; incomplete summary output is preserved separately rather than used as a rerun reason (`contract-and-scenario-package.md:98-124`). |
| M4 control-only provenance challenge | **Pass.** | A broken packet whose control-only durable record names the preceding event cannot satisfy the response-owned-event proof. A corrected packet clears only when success, preparation failure, repetition, reopen, and branch/fork all retain a truthful resolvable event (`implementation-review.md:103-110`). |
| M5 declared/effective identity challenge | **Pass.** | A profile-derived passing record is rejected when an omitted default, backend override, mixed per-request identity, or partial capture disagrees with the recorded identity. The execution result remains intact while evidence becomes invalid or unavailable (`implementation-review.md:112-128`). |
| M6 multi-cell delegated-review trace | **Pass.** | This Tick reported compact cleared/candidate/unknown/not-applicable checkpoints after material cell clusters and before its final gate, exposed the BS1 candidate immediately, retained reviewer independence, and did not rerun completed cells in response to status requests. |

## Specification-Cell Status

| Cell | Status | Evidence |
|---|---|---|
| Single normative authority | **Cleared.** | The plan declares BS1-BS7 its sole authority; later prose and packets implement or evidence those rows without creating another requirement table. |
| Durable contract boundary | **Cleared.** | Checkpoint intervals are orchestration defaults, diagnostic tuple fields are private, and BS5-BS6 are conditional review questions rather than application mechanisms. |
| Scenario diagnosability | **Cleared.** | D1 and M1-M6 each name an observable invariant and localization signal (`improvement-better-sequencing.md:298-308`). |
| Evidence topology | **Cleared.** | Every package scenario is deterministic repository evidence; external capability and telemetry remain separate and non-gating where unavailable or unthresholded. |
| External freshness | **Cleared for the design; execution not applicable.** | BS2 leaves scenario identity and freshness with the feature contract and invalidates records after material owner changes. This package requires no live provider evidence. |
| Telemetry decision power | **Not applicable.** | The package claims no telemetry threshold; token, elapsed-time, checkpoint, and call counts remain explicitly observational (`improvement-better-sequencing.md:323-327`). |
| Exact-limit justification | **Cleared.** | The 60-second interval is expressly a replaceable orchestration default, while BS3's stable contract is one bounded wait and at most one interrupt. No performance or acceptance claim depends on the number. |
| Workflow boundary | **Not applicable as a specification-review cell.** | The selected artifact is itself the repository workflow authority. Cross-package inspection found no second prose pass, evidence class, gate owner, or review owner. |

## Confirmed Finding

### P2 — The Tock caller still mandates breaking-cleanup rules

**Violated contract:** BS1, observed by D1.

**Proof:** BS1 requires compatibility and cleanup policy to come from repository
guidance (`improvement-better-sequencing.md:53`). The remediation moves that
authority into repository guidance at `review-fixpoint/SKILL.md:32-35` and
`phase-mechanics.md:12-20`. However, the Tock path still imperatively says
“Apply the breaking-cleanup rules” at `review-fixpoint/SKILL.md:185-187`.
For a repository that requires source, wire, persisted, or deployment
compatibility, that caller can direct the opposite behavior from the linked
owner.

**History:** New S1 regression from incomplete owner propagation. The phrase
was valid under the baseline's repository-specific breaking-cleanup policy but
became contradictory when S1 generalized its owner.

**Owning correction:** Replace the Tock caller with an instruction to apply the
repository compatibility and cleanup policy in `phase-mechanics.md`. The
entrypoint and reference must name the same owner. Adding a caveat elsewhere or
restoring a generic breaking-cleanup list would preserve the conflicting
authority and is not an acceptable plaster.

## Unknowns

None. Every BS row, named scenario, required specification cell, changed owner,
and negative constraint was either cleared, made not applicable, or converted
to Finding 01.

## Architecture And Follow-Up Disposition

S1 exposed one repository-coupling property across four package owners: the
entrypoint, interface prompt, phase policy, and review-evidence boundary. The
bounded `correct now` branch fits the accepted package and correctly removes
the Clojure/Rust/toolchain and fixed artifact-layout coupling without adding a
dependency, state lifetime, compatibility shim, fallback, public external
interface, or mechanism-coupled test. The retained Tock caller is an incomplete
application of that accepted branch, not a reason to widen its correction.

Follow-up delta: created none; updated none; closed none; stale none;
unchanged-but-relevant none. No finding was relabeled as a follow-up.

## Evidence-Lane Status

| Lane | Status | Decision effect |
|---|---|---|
| Deterministic repository | Mechanical gate passed, but D1 failed through Finding 01. | Blocks deterministic fixed point. |
| External compatibility | **Not applicable.** | No live provider capability is required or claimed by this package. |
| Observational telemetry | **Not applicable.** | No measurement has acceptance power. |

## Glossary And Terminology

The selected glossary is `docs/glossary.md`. Its entries for **Tick**, **Tock**,
**deterministic fixed point**, **capability unconfirmed**, and **semantic owner**
were read directly. Their meanings agree with `review-fixpoint`, its
contract-and-evidence boundary, and GL3: review remains independent, Tock owns
remediation and its exact commit, deterministic fixed point excludes required
unknowns and product-contract failures without claiming external capability,
and technical owners outrank explanatory terminology. No new term or glossary
change is needed.

## Independent Gate Evidence

The final implementation gate ran once while the worktree and index exactly
matched `db92c5e85a703cd2c6cd4b0e9723575a067f512b`:

- all three changed skill packages passed `quick_validate.py`;
- `review-fixpoint/agents/openai.yaml` parsed and contained its required
  interface prompt;
- all 14 relative Markdown links in the nine-file package resolved;
- all three `SKILL.md` files remained below 500 lines;
- every changed reference over 100 lines contained `## Contents`;
- the baseline-to-reviewed-revision diff passed `git diff --check`; and
- the tracked and untracked tree was clean before this review artifact was
  created.

These mechanical checks cannot negate D1's source-proven semantic failure.

## Clear-Writing Pass

Applied once after the finding, evidence, owner, severity, and decision were
fixed. The pass did not add, remove, close, or downgrade a finding.

## Fixed-Point Result

- `deterministic-fixed-point`: **not reached**;
- current P0-P3 findings: **one P2**;
- required unknowns: **none**;
- external capability: **not applicable**; and
- package `Done`: **not reached**.

A bounded Tock must correct the stale caller at its existing BS1 owner, pass the
exact-revision gate, and return to this persistent reviewer for Review 02.

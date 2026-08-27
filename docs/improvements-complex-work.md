# Improvement Plan: Repository-Owned Complex Work Orchestration

## Decision

Integrate `complex-work` into this repository as a compact outer orchestrator,
not as a copy of the current devtools/Tavern skill. Preserve its useful
evidence-driven sequencing and affected-unit replanning, but route
artifact-specific work to this repository's existing leaf owners.

The installed `~/.agents/skills/complex-work` is currently a standalone copy.
Its broad trigger overlaps several repository skills, its code path names
unavailable Tavern specializations, and its generic phase instructions claim
implementation, review, delegation, commit, and prose responsibilities already
owned elsewhere. The repository-owned replacement must remove those conflicts
and become the installed source after deterministic acceptance.

This document is the sole normative authority for the CW1-CW8 contracts below.
Later sections provide rationale, scenarios, and an implementation sequence;
they do not add independent requirements.

## Scope and non-goals

The work adds one repository skill that coordinates a mixed work package across
multiple artifact types or specialized skills when no existing skill owns the
outcome end to end.

It does not:

- replace the implementation, review, fixed-point, documentation, architecture,
  or prose mechanics owned by existing skills;
- make every multi-file edit, review, research request, or plan invoke an outer
  workflow;
- mandate subagents, commits, pushes, deployments, messages, or other external
  writes;
- preserve Tavern or devtools skill names as compatibility aliases; or
- define a new project term that belongs in `docs/glossary.md`.

## Authoritative contract-and-evidence matrix

| ID | Observable contract | Semantic owner and public composition | Slice | Named deterministic evidence | Status |
|---|---|---|---|---|---|
| CW1 | **Trigger only for mixed ownership.** Invoke `complex-work` for a non-trivial work package spanning multiple artifact types, capability boundaries, or specialized skills when no single skill owns the outcome end to end. Bypass it for a small bounded edit and when one specialized skill fully owns the requested result. | `complex-work` owns its trigger boundary; skill selection is observable through the loaded skill set and chosen workflow. | S1 | E1 trigger-routing scenarios | Proposed |
| CW2 | **Keep one outer owner.** The primary agent owns the package outcome, scope, cross-unit ordering, shared constraints, authorization boundaries, and final integrated handoff. A selected leaf owner retains its substantive decisions and validation mechanics. | `complex-work` owns outer coordination; each selected repository skill owns its declared leaf behavior. | S1 | E2 ownership and composition audit | Proposed |
| CW3 | **Ground and decompose economically.** Recover relevant primary evidence, state material unknowns or assumptions, and decompose the package into ordered units only as far as needed for observable acceptance. Keep uncertain choices local and reversible. | `complex-work` owns package discovery and unit ordering; source owners and repository guidance own facts and policy. | S1 | E3 package-shape scenarios | Proposed |
| CW4 | **Route without duplicating leaf mechanics.** Route review-only work to `evidence-efficient-review`, review/remediation repetition to `review-fixpoint`, dependent supervised implementation to `supervised-implementer-loop`, technical-note series to `technical-note-series`, architecture documentation to `project-architecture-doc`, reusable architecture policy to `add-architectural-guidances`, and final engineering prose to `clear-technical-writing`. Do not restate those skills' procedures. | `complex-work` owns routing; the named leaf skills own execution after selection. | S1 | E2 ownership and composition audit | Proposed |
| CW5 | **Adapt at the invalidated boundary.** When new evidence contradicts the route, invalidate the affected assumption, unit, or ordering decision; return to the latest broken boundary; and preserve accepted units whose dependencies remain valid. Do not continue a disproved route or restart unaffected work. | `complex-work` owns cross-unit dependency invalidation; leaf owners decide whether their own evidence remains valid. | S1 | E4 contradiction and carry-forward scenarios | Proposed |
| CW6 | **Delegate through explicit ownership.** Do not require the primary to delegate all actual work or fan out merely because a task is large. Delegate when the user requests it, a selected leaf skill requires it, or packages are genuinely independent. Preserve the primary agent as integration and acceptance authority. | `complex-work` owns outer delegation choice; selected leaf skills own implementer or reviewer topology. | S1 | E5 delegation scenarios | Proposed |
| CW7 | **Preserve authorization and repository state.** Discover and carry user and repository policy for commits, external writes, publication, destructive actions, and unrelated worktree state. Checkpoint only under that policy; never turn a reviewable unit into implicit authorization. | The user and repository own authorization; `complex-work` carries the boundary across units. | S1 | E6 authorization scenarios and source audit | Proposed |
| CW8 | **Verify proportionally and finish once.** Run focused checks when they can cheaply disprove a unit, defer expensive complete gates to meaningful package checkpoints, use the selected leaf owner's acceptance rules, and apply any final clear-technical-writing pass exactly once after substantive decisions stabilize. Report accepted units, evidence, unresolved unknowns, and pending authorized actions. | Leaf skills and repository guidance own checks; `complex-work` owns package-level evidence aggregation and handoff. | S1 | E7 verification and handoff scenarios | Proposed |

External compatibility evidence is not applicable: the skill coordinates local
workflow and has no credentialed provider contract. Telemetry is not
applicable: no runtime metric participates in acceptance. No normative numeric
limit is introduced; the authoring guideline that the entrypoint should remain
compact is an implementation preference, not a behavioral contract.

## Ownership and routing

`complex-work` fills only the outer-workflow gap. Use the narrowest owner that
can complete a unit:

| Work shape | Owner |
|---|---|
| Broad implementation or specification review | `evidence-efficient-review` |
| Repeated independent review and remediation | `review-fixpoint` |
| One ordered, dependent implementation package requiring supervised delegation | `supervised-implementer-loop` |
| Educational technical-note series | `technical-note-series` |
| Repository architecture document | `project-architecture-doc` |
| Durable reusable architecture guidance | `add-architectural-guidances` |
| Final reader-facing engineering prose | `clear-technical-writing` |
| Cross-owner outcome spanning several rows | `complex-work` |

When a request is entirely owned by one row above, invoke that leaf directly.
When the package spans rows, `complex-work` selects and sequences the leaves,
retains shared constraints, and integrates their accepted results without
performing their work a second time.

## Scenario portfolio

### E1 — Trigger routing

- A mixed feature, migration, documentation, and validation request invokes
  `complex-work` because no leaf owns the complete outcome.
- A broad review invokes `evidence-efficient-review` directly.
- A technical-note request invokes `technical-note-series` directly.
- A small single-file edit stays inline.

Failure localizes to the `complex-work` description or its trigger section.

### E2 — Ownership composition

Given a mixed package containing implementation and independent review, the
outer skill states the shared outcome and ordering, then routes implementation
and review to their existing owners without copying their slice, dossier,
reviewer, finding, or stop mechanics. Failure localizes to the ownership map or
a duplicated instruction in `SKILL.md`.

### E3 — Package shape

Given a design task with incomplete repository context, the workflow recovers
available source facts, identifies a material assumption, and defines only the
units and observable exit conditions needed to decide the requested outcome.
It does not manufacture a file, commit, subagent, or four-phase ceremony for
its own sake. Failure localizes to package establishment instructions.

### E4 — Contradiction and carry-forward

Given three ordered units where new evidence invalidates the second unit's
assumption, the workflow replans the second and dependent third unit while
retaining the first unit when its dependency remains sound. Failure localizes
to dependency invalidation and replanning.

### E5 — Delegation

- A dependent package selected for `supervised-implementer-loop` uses that
  skill's one persistent implementer and parent acceptance model.
- A review selected for `evidence-efficient-review` follows its independent
  reviewer policy.
- A large task without either condition does not automatically delegate all
  work.

Failure localizes to outer delegation wording or a leaf routing violation.

### E6 — Authorization

Given reviewable units in a dirty worktree, the workflow preserves unrelated
changes and does not commit, push, publish, deploy, send, delete, or overwrite
without the applicable user and repository authority. Failure localizes to the
authorization boundary or checkpoint wording.

### E7 — Verification and handoff

Given an implementation unit with a cheap focused check and an expensive
complete gate, the workflow uses the focused check while the unit is unstable
and runs the complete gate at the leaf or package checkpoint required by
repository policy. The final handoff applies one prose pass and reports the
actual evidence without claiming unavailable checks. Failure localizes to the
verification sequence or handoff contract.

## Implementation

### S1 — Add the repository-owned skill

Create `skills/complex-work/SKILL.md` and
`skills/complex-work/agents/openai.yaml`.

The entrypoint must:

- use `complex-work` as both directory and frontmatter name;
- use a concise, imperative, user-intent description with the CW1 trigger and
  bypass boundaries;
- remain client-neutral and name only skills present in this repository;
- define outer ownership, package establishment, leaf routing, affected-unit
  replanning, delegation, authorization, verification, and handoff;
- avoid scripts and references unless implementation reveals information that
  cannot remain compact in the entrypoint; and
- avoid automatic side effects so model invocation can remain enabled.

The interface metadata should present the skill as mixed-work orchestration,
not as the default owner of every non-trivial task.

### S2 — Make this repository the installed source

After S1 reaches deterministic fixed point, replace the standalone installed
`~/.agents/skills/complex-work` directory with a symlink to
`skills/complex-work`, preserving the old file in a recoverable temporary
location until the new link and readable `SKILL.md` are verified.

This installation step changes no skill semantics. Its evidence is an exact
source inventory, the resolved symlink target, and a readable linked
`SKILL.md`.

## Deterministic acceptance

Accept the package only when:

1. the CW1-CW8 matrix is fully implemented without a competing normative
   definition;
2. the description distinguishes mixed work from small or end-to-end leaf work;
3. every named leaf exists and retains its documented ownership;
4. no Tavern/devtools-only skill, client-specific planning tool, blanket
   integration-test preference, forced fan-out, implicit commit, or delayed-all-
   validation rule remains;
5. the skill satisfies the repository's canonical skill-authoring checklist;
6. E1-E7 are dispositioned against the final source;
7. repository status contains only the accepted package and required immutable
   review artifacts; and
8. the installed entry resolves to the accepted repository source and exposes a
   readable `SKILL.md`.

## Handoff

Report the accepted CW contracts, created files, deterministic checks,
independent review decision, installation read-back, and any remaining
capability or authorization boundary. Do not claim a fixed point until the
independent implementation Tick reviews the exact committed result.

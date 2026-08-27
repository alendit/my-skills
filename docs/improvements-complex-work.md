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

| ID | Observable contract | Semantic owner and public composition | Slice | Named evidence | Status |
|---|---|---|---|---|---|
| CW1 | **Trigger only for mixed ownership.** Invoke `complex-work` for a non-trivial work package spanning multiple artifact types, capability boundaries, or specialized skills when no single skill owns the outcome end to end. Bypass it for a small bounded edit and when one specialized skill fully owns the requested result. | `complex-work` owns its trigger boundary; a user request evaluated against the loaded skill set is the public composition. | S1 | D1 source audit; E1 trigger routing | Proposed |
| CW2 | **Keep one outer owner.** The primary agent owns the package outcome, scope, cross-unit ordering, shared constraints, authorization boundaries, and final integrated handoff. A selected leaf owner retains its substantive decisions and validation mechanics. For a unit whose complete outcome matches no available specialized skill, the primary remains that unit's leaf owner under carried repository and authorization policy; it does not invent a leaf, force delegation, or bypass an applicable specialized owner. | `complex-work` owns outer coordination; named leaf skills and the primary-owned fallback compose under one mixed user request. | S1 | D1 source audit; E2 ownership composition | Proposed |
| CW3 | **Ground and decompose economically.** Recover relevant primary evidence, state material unknowns or assumptions, and decompose the package into ordered units only as far as needed for observable acceptance. Keep uncertain choices local and reversible. | `complex-work` owns package discovery and unit ordering; a repository-backed design or investigation request is the public composition. | S1 | E3 package shape | Proposed |
| CW4 | **Route without duplicating leaf mechanics.** Route review-only work to `evidence-efficient-review`, review/remediation repetition to `review-fixpoint`, dependent supervised implementation to `supervised-implementer-loop`, technical-note series to `technical-note-series`, architecture documentation to `project-architecture-doc`, reusable architecture policy to `add-architectural-guidances`, final engineering prose to `clear-technical-writing`, and unmatched units through the CW2 primary-owned branch. Do not restate leaf procedures or retain unavailable Tavern/devtools aliases, client-native planning tools, a blanket integration-test preference, forced fan-out, implicit commits, or a delayed-all-validation rule. | `complex-work` owns routing; the installed repository skill set and the selected leaf's declared interface form the public composition. | S1 | D1 leaf and forbidden-source audit; E2 ownership composition | Proposed |
| CW5 | **Adapt at the invalidated boundary.** When new evidence contradicts the route, invalidate the affected assumption, unit, or ordering decision; return to the latest broken boundary; and preserve accepted units whose dependencies remain valid. Do not continue a disproved route or restart unaffected work. | `complex-work` owns cross-unit dependency invalidation; a package with accepted, invalidated, and dependent units is the public composition. | S1 | E4 contradiction and carry-forward | Proposed |
| CW6 | **Delegate through explicit ownership.** Do not require the primary to delegate all actual work or fan out merely because a task is large. Delegate when the user requests it, a selected leaf skill requires it, or packages are genuinely independent. Preserve the primary agent as integration and acceptance authority. | `complex-work` owns outer delegation choice; the primary, a supervised implementer, and an independent reviewer are representative compositions. | S1 | D1 source audit; E5 delegation | Proposed |
| CW7 | **Preserve authorization, repository state, and installed-source identity.** Discover and carry user and repository policy for commits, external writes, publication, destructive actions, and unrelated worktree state. Checkpoint only under that policy; never turn a reviewable unit into implicit authorization. For an authorized S2 transition, inventory the exact installed destination, preserve the standalone source recoverably until read-back, link the installed entry to the accepted repository package, and verify the resolved target and readable `SKILL.md`. | The user and repository own authorization; `complex-work` carries it across units, and the installed skill loader composes with the accepted repository source. | S1, S2 | D2 authorization source audit and installed-link read-back; E6 authorization behavior | Proposed |
| CW8 | **Verify proportionally and finish once.** Run focused checks when they can cheaply disprove a unit, defer expensive complete gates to meaningful package checkpoints, use the selected leaf owner's acceptance rules, and apply any final clear-technical-writing pass exactly once after substantive decisions stabilize. Report accepted units, evidence, unresolved unknowns, and pending authorized actions. | Leaf skills and repository guidance own checks; a multi-unit package handoff is the public composition aggregated by `complex-work`. | S1 | D1 source audit; E7 verification and handoff | Proposed |

Repository-deterministic evidence covers frontmatter and YAML validity, package
and relative-link structure, existence of every CW4 leaf, absence of forbidden
identifiers and client-native planning tools, single-authority source checks,
revision whitespace checks, and the installed symlink read-back. E1-E7 are
controlled model-behavior evidence. For each run, record the exact skill
revision, model and runtime identity, outer prompt, loaded skill set, repository
dossier, captured output and tool trace, scoring rule, and the owning CW
boundary to which failure localizes. Initial evidence is fresh only for that
exact identity and is not reused. An unavailable run leaves the capability
unconfirmed; only a valid run that contradicts a CW contract is a
product-contract failure.

Telemetry is not applicable: no runtime metric participates in acceptance. No
normative numeric limit is introduced; compactness is an implementation
preference, not a behavioral contract.

## Ownership and routing

CW1, CW2, and CW4 define the complete routing contract. The implementation may
use this non-normative file map to locate their current owners:

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

## Scenario portfolio

### D1 — Repository skill package audit

- **Contracts:** CW1, CW2, CW4, CW6, CW8
- **Observable invariant:** the package has valid frontmatter and interface
  metadata, every named leaf exists, relative links resolve, one source owns
  each instruction, and forbidden identifiers or policies are absent.
- **Evidence class:** deterministic repository gate.
- **Capture and scoring:** record the exact revision, validation commands, exit
  status, leaf inventory, forbidden-source search, and CW mapping.
- **Localization signal:** package structure, trigger, ownership, routing,
  delegation, or verification source defect.

### D2 — Authorization and installed-source audit

- **Contracts:** CW7
- **Observable invariant:** source wording preserves authorization and unrelated
  state; after an authorized installation, the exact destination resolves to
  the accepted repository package and its `SKILL.md` is readable while the
  previous standalone source remains recoverable until read-back.
- **Evidence class:** deterministic repository and local installation gate.
- **Capture and scoring:** record the exact repository revision, pre-mutation
  destination inventory, recovery location, resolved symlink target, readable
  file result, and post-mutation status.
- **Localization signal:** authorization wording, preservation, symlink target,
  or loader-readability defect.

### E1 — Trigger routing

- **Contracts:** CW1
- **Observable invariant:** mixed feature, migration, documentation, and
  validation work invokes `complex-work`; broad review and technical-note work
  select their leaf directly; a small single-file edit stays inline.
- **Evidence class:** controlled model behavior.
- **Capture and scoring:** use the common exact-identity record above and score
  the selected skill set and stated bypass reason for each prompt.
- **Localization signal:** description or trigger-boundary failure.

### E2 — Ownership composition

- **Contracts:** CW2, CW4
- **Observable invariant:** a mixed package routes dependent supervised
  implementation and independent review to their existing owners without
  copying leaf mechanics; a second mixed package keeps an unmatched ordinary
  implementation or analysis unit primary-owned while routing its specialized
  sibling to the applicable leaf.
- **Evidence class:** controlled model behavior. D1 separately audits static
  duplication and named leaf existence.
- **Capture and scoring:** use the common record and score owner assignment,
  ordering, and absence of duplicated leaf procedure.
- **Localization signal:** outer ownership, primary-owned fallback, or leaf
  routing failure.

### E3 — Package shape

- **Contracts:** CW3
- **Observable invariant:** with incomplete repository context, the workflow
  recovers available facts, identifies a material assumption, and defines only
  the units and observable exits needed for the outcome.
- **Evidence class:** controlled model behavior.
- **Capture and scoring:** use the common record and score source grounding,
  named assumptions, unit necessity, and lack of invented ceremony.
- **Localization signal:** package-establishment failure.

### E4 — Contradiction and carry-forward

- **Contracts:** CW5
- **Observable invariant:** when evidence invalidates the second of three units,
  the workflow replans it and its dependent third unit while retaining the
  independent accepted first unit.
- **Evidence class:** controlled model behavior.
- **Capture and scoring:** use the common record and score dependency
  invalidation, carry-forward, and the revised route.
- **Localization signal:** invalidation or replanning failure.

### E5 — Delegation

- **Contracts:** CW6
- **Observable invariant:** a supervised dependent package and an independent
  review retain their leaf topology, while size alone does not delegate all
  work.
- **Evidence class:** controlled model behavior.
- **Capture and scoring:** use the common record and score chosen topology,
  retained primary acceptance, and absence of blanket fan-out.
- **Localization signal:** outer delegation or leaf-topology failure.

### E6 — Authorization

- **Contracts:** CW7
- **Observable invariant:** reviewable units in a dirty worktree preserve
  unrelated changes and do not commit, push, publish, deploy, send, delete, or
  overwrite without applicable authority.
- **Evidence class:** controlled model behavior. D2 separately audits source
  wording and the authorized installed-link transition.
- **Capture and scoring:** use the common record and score proposed or executed
  mutations against supplied authority and preserved state.
- **Localization signal:** authorization or checkpoint-boundary failure.

### E7 — Verification and handoff

- **Contracts:** CW8
- **Observable invariant:** the workflow uses a cheap focused check while a unit
  is unstable, runs the expensive complete gate at the required checkpoint, and
  reports actual evidence after one final prose pass.
- **Evidence class:** controlled model behavior. D1 separately audits source
  constraints and package structure.
- **Capture and scoring:** use the common record and score check timing,
  leaf-acceptance use, prose-pass count, and evidence claims.
- **Localization signal:** verification sequence or handoff failure.

## Implementation

### S1 — Add the repository-owned skill

Create `skills/complex-work/SKILL.md` and
`skills/complex-work/agents/openai.yaml`.

Implement CW1-CW6 and CW8 in the entrypoint, and the source-auditable portion of
CW7. Use `complex-work` as both directory and frontmatter name. Keep the
entrypoint client-neutral and compact; add no script or reference unless the
implementation cannot satisfy the CW contracts without it. Record the resolved
source of the selected `$skill-authoring` authority in the implementation
dossier rather than copying its checklist into this plan. Interface metadata
should identify mixed-work orchestration.

### S2 — Make this repository the installed source

Implement the installed-source portion of CW7 after the accepted repository
implementation passes its named deterministic package checks and the caller
authorizes the installed-source mutation. Record the exact source inventory and
installed-link read-back. `$review-fixpoint` owns Tick/Tock selection,
review-artifact lifecycle, exact-revision timing, and the fixed-point decision
for the selected package.

## Deterministic acceptance

Accept the package when CW1-CW8 are implemented, D1-D2 pass, E1-E7 have current
controlled-model dispositions, and the selected `$skill-authoring` authority
finds no checklist violation. A valid E1-E7 product-contract failure returns to
implementation; unavailable execution remains capability-unconfirmed and
prevents a claim of `Done`. `$review-fixpoint` owns the fixed-point decision and
review-artifact lifecycle.

## Handoff

Report the accepted CW contracts, created files, deterministic checks,
independent review decision, installation read-back, and any remaining
capability or authorization boundary.

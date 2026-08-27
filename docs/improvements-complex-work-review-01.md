# Repository-Owned Complex Work Orchestration — Review 01

## Decision

**Changes requested** on exact revision
`29802a7cc142f1e8d687c3c53bf751297a4e8a17`.

This fresh rebaseline specification Tick finds one P1 and three P2 defects.
The proposed outer-orchestrator boundary is appropriate for this repository,
the named repository skills retain their existing leaf ownership, and CW1-CW8
preserve the useful parts of the installed skill without carrying forward its
Tavern names, forced fan-out, implicit checkpoints, or delayed validation.
However, the evidence plan treats model-mediated routing as deterministic, the
matrix omits required installation and authoring-authority outcomes while later
sections restate contracts, ordinary primary-owned work has no explicit route,
and S2 copies a partial fixed-point sequence into the feature plan. The
specification has not reached deterministic fixed point.

Reviewed scope:

- `docs/improvements-complex-work.md` as the proposed specification;
- the current repository skills named by CW4;
- the installed standalone `complex-work` as the source being replaced;
- the installed `skill-authoring` skill as the checklist actually available to
  the package; and
- the live installed-source boundary at `~/.agents/skills/complex-work`.

There is no previous numbered review for this package.

## CW1-CW8 coverage

| Contract | Status | Evidence and decision |
|---|---|---|
| CW1 Trigger only for mixed ownership | **Contract cleared; evidence finding** | The trigger distinguishes mixed ownership from small work and work already owned end to end by one skill (`improvements-complex-work.md:42`). It corrects the installed skill's broad triggers for nearly every implementation, review, plan, and investigation (`~/.agents/skills/complex-work/SKILL.md:4-16,36-64`). E1 is model routing, not deterministic source evidence. Finding 01 applies. |
| CW2 Keep one outer owner | **Finding** | Outer outcome, ordering, constraints, authorization, and integrated handoff have one owner, and leaf substantive decisions remain local (`:43`). The row does not say who owns a unit for which no repository skill applies, even though the glossary permits the caller to be a leaf owner. Finding 03 applies. |
| CW3 Ground and decompose economically | **Contract cleared; evidence finding** | The contract requires primary evidence, explicit material unknowns, observable unit acceptance, and reversible uncertainty without prescribing a four-phase representation (`:44`). E3 still asks a model to make those choices and cannot be proved by source inspection. Finding 01 applies. |
| CW4 Route without duplicating leaf mechanics | **Finding** | The seven named skills exist and the proposed mappings agree with their current descriptions and ownership statements. The row covers only dependent implementation that selects `supervised-implementer-loop`; mixed ordinary implementation, research, or analysis has no explicit primary-owned route. Its routing contract is also repeated in lines 57-76. Findings 02 and 03 apply. |
| CW5 Adapt at the invalidated boundary | **Contract cleared; evidence finding** | Replanning only the invalidated unit and its dependents preserves accepted evidence whose dependencies remain valid (`:46`). This is the useful behavior retained from the installed skill. E4 is model behavior and needs controlled execution evidence. Finding 01 applies. |
| CW6 Delegate through explicit ownership | **Contract cleared; evidence finding** | The row removes the installed skill's rule that a sufficiently large task delegates all actual work and leaves reviewer or implementer topology with the selected leaf (`:47`; installed skill `:77-81`). E5 correctly distinguishes the two leaf policies, but model compliance is not a deterministic source result. Finding 01 applies. |
| CW7 Preserve authorization and repository state | **Finding** | The authorization contract correctly prevents a reviewable unit from creating commit, external-write, destructive-action, or dirty-worktree authority (`:48`). The required S2 installed-source transition and its read-back are not assigned to CW7 or any other matrix row even though installation is package acceptance criterion 8. Finding 02 applies. |
| CW8 Verify proportionally and finish once | **Contract cleared; evidence finding** | Focused checks, meaningful complete checkpoints, leaf acceptance, one final prose pass, and evidence-honest handoff agree with current leaf ownership (`:49`). E7 contains model choices and output behavior in addition to source-auditable constraints. Finding 01 applies. |

## Ownership and feasibility

The proposed repository fit is sound where it is explicit:

- `evidence-efficient-review` owns broad review mechanics;
- `review-fixpoint` owns Tick/Tock selection, phase commits, and the
  fixed-point decision;
- `supervised-implementer-loop` owns a dependent package implemented by one
  persistent implementer, but explicitly does not own an outer completion
  process;
- `technical-note-series` owns research, reader journey, series structure,
  drafting, coherence, and publication validation;
- `project-architecture-doc` owns `docs/architecture.md` production;
- `add-architectural-guidances` owns durable AGENTS architecture policy; and
- `clear-technical-writing` owns one final prose transformation without taking
  substantive authority from the leaf artifact.

The package shape is feasible: a compact `skills/complex-work/SKILL.md` and
standard `agents/openai.yaml` match existing repository packages, and no script
or reference is currently necessary. The installed destination is source-proven
to be a physical directory containing one `SKILL.md`, while the repository's
other installed skill packages use symlinked sources. The `skill-authoring`
checklist is available, but it is not repository-owned: the installed entry
resolves to
`/Users/dvorona/projects/agents/dvorona-agentic-skills/dialects/wenyan/repo-skills/skill-authoring`.
The specification must identify that selected external authority accurately
instead of referring to a nonexistent repository checklist.

## Confirmed findings

### Finding 01 — P1 — E1-E7 cannot be deterministic proof of model routing and orchestration

**Proof.** Every CW row names E1-E7 as deterministic evidence
(`docs/improvements-complex-work.md:40-49`), and acceptance requires those
scenarios to be dispositioned only “against the final source” (`:173-189`). E1
asserts that a request invokes or bypasses a skill (`:80-88`); E3 requires the
workflow to recover facts, identify a material assumption, and choose economical
units (`:98-104`); E4 requires dependency-aware replanning (`:106-111`); E5
requires topology selection (`:113-122`); and E7 requires validation timing and
an evidence-honest generated handoff (`:131-138`). These are model decisions and
outputs. Static source inspection can prove that instructions exist, but not
that a model follows them.

The global statement that external compatibility is not applicable because
there is no credentialed provider contract (`:51-55`) does not resolve this.
The required capability is that the selected model/runtime follows the skill
under the loaded-skill and outer-instruction context. The scenario records also
omit the required common capture/scoring helper, exact model identity, freshness
rule, and explicit evidence class. A green source audit could therefore claim
CW1-CW8 behavior without executing any behavior.

**Owning correction:** keep repository-deterministic checks for package
structure and source constraints, and reclassify model behavior. Insert this
evidence boundary after the matrix:

> Repository-deterministic evidence covers frontmatter and YAML validity,
> package and relative-link structure, existence of every CW4 leaf, absence of
> forbidden Tavern/devtools identifiers and client-native planning tools,
> single-authority source checks, revision whitespace checks, and the installed
> symlink read-back. E1-E7 are controlled model-behavior evidence. For each run,
> record the exact skill revision, model and runtime identity, outer prompt,
> loaded skill set, repository dossier, captured output and tool trace, scoring
> rule, and the owning contract boundary to which failure localizes. Initial
> evidence is fresh only for that exact identity and is not reused. An
> unavailable run leaves the capability unconfirmed; only a valid run that
> contradicts a CW contract is a product-contract failure.

Update each E1-E7 entry to state `Contracts`, `Observable invariant`, `Evidence
class`, `Capture and scoring`, and `Localization signal`. Split E2 and E7 where
their static duplication or package checks can pass independently from model
behavior. Deterministic fixed point may establish that the package and
evaluation definitions implement the specification, but it must not claim
unexecuted model behavior or `Done`.

### Finding 02 — P2 — The CW matrix is not the complete single normative authority

**Proof.** The document declares CW1-CW8 to be the sole normative authority
(`:17-19`), but every row is assigned only to S1 (`:42-49`). S2 then adds a
required installed-source outcome, preservation rule, and read-back
(`:162-171`), and acceptance criterion 8 makes that outcome gating (`:188-189`).
No CW row owns it. The non-goal prohibiting Tavern/devtools compatibility aliases
(`:35`) and acceptance criterion 4's forbidden paths (`:181-183`) likewise have
no exact owning row; CW4 names positive routes but does not own those negative
constraints.

The routing table and its following rules (`:57-76`) repeat CW1, CW2, and CW4
instead of referencing them. S1's requirement to define the eight orchestration
concerns (`:147-157`) and acceptance criteria 2-4 and 7-8 repeat or add more
normative outcomes. Most matrix owner cells name an owner but not the required
public composition. Finally, criterion 5 cites “the repository's canonical
skill-authoring checklist” (`:184`), but this repository contains no
`skills/skill-authoring`; the checklist inspected by this Tick is an installed
symlink into another repository.

**Owning correction:** keep CW1-CW8 as the requested authority and amend their
rows rather than adding parallel prose:

- Make CW4 own both the positive routing set and the prohibition on unavailable
  Tavern/devtools aliases, client-native planning tools, and duplicated leaf
  procedures.
- Amend CW7 so its observable state-integrity outcome includes an authorized S2
  transition: inventory the exact destination, preserve the standalone source
  recoverably until read-back, link the installed entry to the accepted
  repository package, and verify the resolved target and readable `SKILL.md`.
  Assign CW7 to S1 and S2 and name the installed skill loader as its public
  composition.
- Add a representative public composition to every remaining matrix owner cell.
- Replace lines 57-76 and the contract-like S1 and acceptance copies with CW ID
  references plus only section-specific file shape, execution order, and
  evidence recording.
- Replace “the repository's canonical skill-authoring checklist” with “the
  selected `$skill-authoring` authority,” record its resolved source in the
  implementation dossier, and keep checklist rules out of this plan.

### Finding 03 — P2 — Mixed packages with an ordinary primary-owned unit have no route

**Proof.** CW1 intentionally selects packages spanning several artifact or skill
boundaries (`:42`). CW2 assigns the primary only outer coordination and assigns
substantive decisions to a selected leaf (`:43`). CW4 names a code implementation
owner only when the package is ordered, dependent, and requires supervised
delegation (`:45,66`). CW6 simultaneously says large work does not by itself
require delegation (`:47`). E2 nevertheless assumes a mixed implementation and
review package can route both units to existing owners (`:92-96`).

A mixed package containing an ordinary inline implementation plus an
architecture-document update therefore has two incompatible readings: force
`supervised-implementer-loop` despite CW6, or leave the implementation unit
without a substantive owner. The selected glossary defines a leaf owner as an
artifact-specific skill **or caller**, but the matrix and scenario do not carry
that branch into routing.

**Owning correction:** append this wording to CW2 and reference it from CW4:

> For a unit whose complete outcome matches no available specialized skill, the
> primary agent remains that unit's leaf owner and executes it under the carried
> repository and authorization policy. Do not invent a leaf, force delegation,
> or bypass an applicable specialized owner.

Extend E2 with one mixed package containing a primary-owned implementation or
analysis unit plus one specialized leaf, and keep the existing dependent
implementation case as the separate `supervised-implementer-loop` composition.

### Finding 04 — P2 — S2 embeds a circular partial fixed-point sequence

**Proof.** S2 may run only “After S1 reaches deterministic fixed point”
(`:162-167`), while package acceptance requires S2's installed read-back
(`:175-189`). The handoff then says fixed point requires an independent Tick of
the exact committed result (`:191-196`), and acceptance criterion 7 requires
immutable review artifacts (`:186-187`). The feature plan has therefore copied
partial fixed-point timing, review-artifact lifecycle, and exact-revision stop
mechanics from `review-fixpoint`. Under that workflow's contract, fixed point
applies to the selected package; this plan does not define a separate S1 package
or explain how an uncommitted external symlink mutation can be part of the
already reached S1 decision.

**Owning correction:** keep only feature ordering and authorization in the plan:

> Run S2 after the accepted repository implementation has passed its named
> deterministic package checks and the caller authorizes the installed-source
> mutation. Record the exact source inventory and installed-link read-back.
> `$review-fixpoint` owns Tick/Tock selection, review-artifact lifecycle,
> exact-revision timing, and the fixed-point decision for the selected package.

Remove acceptance criterion 7's review-artifact lifecycle rule and the final
exact-committed-Tick sentence; replace both with one reference to
`$review-fixpoint`. The outer workflow can then decide whether S2 is an
authorized package step or a post-fixed-point installation action without this
feature specification defining a second stop procedure.

## Required specification-cell dispositions

| Cell | Disposition |
|---|---|
| Single normative authority | **Finding.** S2 installation, forbidden compatibility paths, repeated routing, and acceptance prose sit outside or duplicate CW1-CW8. Finding 02 owns the matrix and deletion correction. |
| Durable contract boundary | **Finding.** CW1-CW8 otherwise permit equivalent private designs, but most semantic-owner cells omit a representative public composition, and the selected authoring authority is not identified accurately. Finding 02 applies. |
| Scenario diagnosability | **Finding.** E1-E7 provide useful behavioral examples and broad localization, but do not name common capture/scoring helpers or evidence identities; E2 also lacks the ordinary primary-owned branch. Findings 01 and 03 apply. |
| Evidence topology | **Finding.** Static package checks and model-mediated behavior are combined as deterministic evidence. Finding 01 supplies the split. |
| External freshness | **Finding.** Controlled model behavior has no identity or freshness rule because it is incorrectly marked not applicable. Finding 01 supplies a fresh, exact-identity initial rule. |
| Telemetry decision power | **Not applicable.** No runtime metric is named and no unthresholded measurement is used for acceptance. |
| Exact-limit justification | **Not applicable.** The specification introduces no normative cap, timeout, retry count, or resource number; compactness is explicitly an implementation preference. |
| Workflow boundary | **Finding.** S2, acceptance criterion 7, and the handoff copy partial fixed-point sequence, review-artifact lifecycle, and exact-revision timing. Finding 04 applies. |

## Evidence status

- **Exact source revision:** `git rev-parse HEAD` and `git show` both resolved to
  `29802a7cc142f1e8d687c3c53bf751297a4e8a17` before this artifact was written.
- **Specification hygiene:** `git diff --check
  b309047ed48c5ef51b83125cfa5ca4859d01f3bb
  29802a7cc142f1e8d687c3c53bf751297a4e8a17` passed.
- **Leaf inventory:** all seven skills named by CW4 exist under `skills/`, and
  their inspected ownership statements support the proposed routing where the
  route is explicit.
- **Installed-source inventory:** `~/.agents/skills/complex-work` is a physical
  directory containing one standalone `SKILL.md`; installation has not changed
  in this Tick.
- **Future package evidence:** the repository-owned `complex-work` package does
  not exist at the reviewed revision, so authoring, routing, forbidden-source,
  scenario, and installed-link checks were not executed as implementation
  evidence.
- **Controlled model behavior:** E1-E7 were not run and remain
  `capability-unconfirmed`; no model result is classified as a pass or product
  contract failure.
- **Observational telemetry:** not applicable.

## Glossary and writing status

`docs/glossary.md` is the selected glossary. `Leaf owner`, `semantic owner`,
`Tick`, `Tock`, `deterministic fixed point`, and `capability unconfirmed` were
read directly and kept subordinate to their linked semantic sources. No new
shared project term is required. The specification uses `leaf owner`
consistently but must carry the glossary's caller-owned branch into CW2 as
described in Finding 03.

One `clear-technical-writing` pass was applied after the findings, severities,
owners, and corrective wording stabilized. It did not change their technical
dispositions.

## Architectural scope, unknowns, and fixed-point status

No separate architectural-scope decision or durable follow-up is justified.
The integration remains a bounded repository-skill package; the findings
correct its evidence and ownership boundaries without expanding product scope.
No required review cell remains merely unknown: the four candidates above are
source-proven findings.

`deterministic-fixed-point` is **not reached** at
`29802a7cc142f1e8d687c3c53bf751297a4e8a17`. CW2, CW4, CW7, the evidence
topology, single-authority, scenario, freshness, and workflow-boundary cells
require remediation before the persistent reviewer's next Tick.

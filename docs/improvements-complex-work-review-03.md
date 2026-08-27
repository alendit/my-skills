# Repository-Owned Complex Work Orchestration — Review 03

## Decision

**Changes requested** on exact remediation revision
`81e3f8b7229261df07bb5d5a935d8254839a7224`.

Review 02 Findings 01 and 03 are closed. Finding 02 is substantially
remediated—the duplicate ownership table is gone—but one P2 incomplete closure
remains: the unchanged `Scope and non-goals` section still restates positive
and negative CW routing, delegation, and authorization requirements without CW
references. Every other CW row and required specification cell is cleared or
not applicable. The specification has not yet reached deterministic fixed
point.

Reviewed scope:

- `docs/improvements-complex-work.md` at the exact revision above;
- immutable Reviews 01 and 02 and their prior finding contracts;
- the unchanged repository leaf interfaces named by CW4;
- the specification evidence classes and fixpoint result vocabulary; and
- the live installed-source identity relevant to future D2.

## Prior finding dispositions

| Review 02 finding | Disposition | Exact evidence |
|---|---|---|
| 01 — Controlled model evidence class and result | **Closed** | Every E1-E7 scenario is now explicitly `external compatibility evidence; controlled model behavior` (`improvements-complex-work.md:103-188`). Package acceptance separately defines `capability-confirmed`, `capability-unconfirmed`, and `external-contract-failed`, reserves `Done` for deterministic fixed point plus confirmed capability, and leaves fixed-point ownership with `review-fixpoint` (`:214-230`). |
| 02 — Duplicate routing table | **Partially closed; incomplete prior closure** | The work-shape table is removed and the remaining navigation sentence references CW1, CW2, and CW4 plus actual `skills/<skill-name>/SKILL.md` paths (`:69-72`). The unchanged scope section still repeats those contracts and CW6-CW7 without ID references (`:23-38`), despite Review 02's explicit condition that it remain only if it references the CW rows. Finding 01 below remains. |
| 03 — S2 ordered after its own acceptance | **Closed** | The opening decision now orders package checks, caller authorization, S2, D2, and package acceptance consistently (`:10-17`). S2 repeats only its section-specific implementation order and delegates workflow mechanics (`:205-212`). |

Review 01 Finding 03 remains closed: CW2, CW4, and E2 retain the explicit
primary-owned fallback (`:45,47,113-126`). No closed prior finding recurs.

## CW1-CW8 coverage

| Contract | Status | Evidence and decision |
|---|---|---|
| CW1 Trigger only for mixed ownership | **Finding through duplicate authority** | The matrix row, public composition, D1, and E1 are sound (`:44,76-86,102-111`). Scope lines 23-34 restate the mixed/end-to-end/small trigger instead of referencing CW1. Finding 01 applies. |
| CW2 Keep one outer owner | **Cleared** | Outer ownership, leaf authority, and the primary-owned fallback are complete and exercised by E2 (`:45,113-126`). |
| CW3 Ground and decompose economically | **Cleared** | The row is implementation-independent, names its composition, and E3 has an observable invariant, external evidence class, capture/scoring, and localization (`:46,128-138`). |
| CW4 Route without duplicating leaf mechanics | **Finding through duplicate authority** | CW4 owns the full positive and negative route and matches every current leaf interface (`:47`). Scope lines 31-37 separately repeat bypass, leaf-mechanics, external-write, and forbidden-alias outcomes. Finding 01 applies. |
| CW5 Adapt at the invalidated boundary | **Cleared** | The invalidation and carry-forward contract, public composition, and E4 evidence record are complete (`:48,140-150`). |
| CW6 Delegate through explicit ownership | **Finding through duplicate authority** | CW6 and E5 correctly reject size-only fan-out and retain leaf topology (`:49,152-161`), but scope line 35 repeats the no-subagent mandate. Finding 01 applies. |
| CW7 Preserve authorization, repository state, and installed-source identity | **Finding through duplicate authority** | CW7 owns authorization and S2 installation, with D2 and E6 covering source, live read-back, and model behavior (`:50,88-100,163-173`). Scope lines 35-37 repeat external-write and compatibility prohibitions. Finding 01 applies. |
| CW8 Verify proportionally and finish once | **Cleared** | The row and E7 keep focused and complete checks, leaf acceptance, one prose pass, and evidence-honest handoff in one owner (`:51,175-185`). |

## Confirmed finding

### Finding 01 — P2 — Scope and non-goals remain a second CW authority

**Proof.** The document declares the CW1-CW8 matrix to be the sole normative
authority (`docs/improvements-complex-work.md:19-21`). The preceding scope
section nonetheless says when mixed work is selected (`:23-27`), says broad
multi-file edits, reviews, research, and plans do not automatically select the
outer workflow (`:31-34`), prohibits replacing leaf mechanics (`:31-32`),
prohibits mandated subagents and external writes (`:35-36`), and prohibits
Tavern/devtools aliases (`:37`). Those are the observable trigger, routing,
delegation, and authorization outcomes already owned by CW1, CW4, CW6, and CW7
(`:44,47,49-50`).

Review 02 explicitly permitted scope/non-goal prose to remain only if it
referenced the owning CW rows rather than introducing another positive or
negative route. Removing the later ownership table does not remove these
earlier copies. A future edit can still change a scope bullet without changing
its matrix owner, defeating D1's single-authority invariant.

**Owning correction:** replace lines 23-38 with purpose-specific references,
for example:

> This package adds one repository skill and its installed-source transition.
> CW1-CW8 own its trigger, ownership, routing, replanning, delegation,
> authorization, verification, and handoff behavior; S1 and S2 implement those
> contracts. CW4 owns the compatibility-alias boundary. The glossary
> disposition below records that no new term is required.

Alternatively, remove the section. Do not retain prose that independently
defines when the skill triggers, which leaf mechanics it may own, or which
mutations it may perform.

## Required specification-cell dispositions

| Cell | Disposition |
|---|---|
| Single normative authority | **Finding.** Scope and non-goals duplicate CW1, CW4, CW6, and CW7. Finding 01 applies. |
| Durable contract boundary | **Cleared.** Every CW row names an observable result, semantic owner, representative public composition, and replaceable private implementation. |
| Scenario diagnosability | **Cleared.** D1-D2 and E1-E7 name contracts, invariants, evidence classes, capture/scoring, and localization. |
| Evidence topology | **Cleared.** D1-D2 are deterministic; E1-E7 are external compatibility evidence using controlled model behavior; telemetry remains separate. |
| External freshness | **Cleared.** The common record captures exact skill, model/runtime, prompt, loaded skills, dossier, output/tool trace, scorer, and owner; initial evidence is exact-identity and non-reusable (`:53-63`). |
| Telemetry decision power | **Not applicable.** No runtime metric participates in acceptance. |
| Exact-limit justification | **Not applicable.** No normative numeric limit is introduced; compactness is non-contractual. |
| Workflow boundary | **Cleared.** S2 carries only feature ordering and evidence; `review-fixpoint` owns phase, artifact, exact-revision, and fixed-point mechanics (`:205-212,214-230`). |

## D/E evidence status

- **Exact revision:** `git rev-parse HEAD` and `git show` resolved to
  `81e3f8b7229261df07bb5d5a935d8254839a7224` before this artifact was written.
- **Revision hygiene:** `git show --check --oneline
  81e3f8b7229261df07bb5d5a935d8254839a7224` passed.
- **Remediation scope:** the revision changes the proposed specification and
  commits immutable Review 02; repository leaf interfaces are unchanged.
- **D1 package audit:** not executed because `skills/complex-work` is not yet
  implemented. The remaining duplicate-authority finding would currently keep
  its single-authority cell open.
- **D2 installation audit:** not executed. The live installed `complex-work`
  remains a readable standalone directory, not the planned repository symlink.
- **E1-E7 model evidence:** not executed and `capability-unconfirmed`; there is
  no valid product-contract failure.
- **Observational telemetry:** not applicable.

## Glossary and writing status

`docs/glossary.md` remains the selected glossary. `Leaf owner`, `semantic
owner`, Tick, Tock, deterministic fixed point, and capability status remain
consistent with their linked semantic sources. No new term or glossary write is
required.

One `clear-technical-writing` pass was applied after the finding, evidence, and
dispositions stabilized. It did not change the decision or severity.

## Architectural scope, unknowns, and fixed-point status

No architectural-scope decision, durable follow-up, or required unknown
remains. Finding 01 is a bounded normalization correction.

`deterministic-fixed-point` is **not reached** at
`81e3f8b7229261df07bb5d5a935d8254839a7224`. Remove or ID-reference the
remaining duplicate scope authority before the next independent Tick. E1-E7
remain `capability-unconfirmed`, so the package cannot claim `Done`.

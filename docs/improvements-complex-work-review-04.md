# Repository-Owned Complex Work Orchestration — Review 04

## Decision

**Accepted for specification design** at exact revision
`8a9f1b6c142ebb877e1240478448a584f38697f8`.

This incremental Tick verifies exact closure of Review 03 Finding 01 and
retains every earlier closure. The scope section now references CW1-CW8 and
CW4 instead of defining another trigger, routing, delegation, or authorization
contract. The specification has no remaining P0-P3 finding or required
unknown. This decision accepts the design document; it does not claim that the
future repository skill exists, that D1-D2 pass, that E1-E7 confirm model
capability, or that the installed source has changed.

Reviewed scope:

- `docs/improvements-complex-work.md` at the exact revision above;
- immutable Reviews 01-03 and all prior finding contracts;
- CW1-CW8, D1-D2, E1-E7, S1-S2, package acceptance, and handoff;
- the unchanged repository leaf interfaces named by CW4; and
- the live installed-source identity relevant to future D2.

## Prior finding dispositions

| Prior finding | Disposition | Evidence |
|---|---|---|
| Review 03: scope and non-goals remain a second CW authority | **Closed** | The section now says the package adds one repository skill and installed-source transition, assigns all behavior to CW1-CW8, assigns implementation to S1-S2, references CW4 for compatibility aliases, and records only the glossary disposition (`improvements-complex-work.md:23-29`). It no longer repeats any trigger, owner mapping, delegation rule, or mutation boundary. |
| Review 02: controlled model evidence lacked the external class and complete result | **Remains closed** | E1-E7 are external compatibility evidence using controlled model behavior (`:93-179`). Package acceptance separately reports `capability-confirmed`, `capability-unconfirmed`, and `external-contract-failed`, and reserves `Done` for deterministic fixed point plus confirmed capability (`:205-216`). |
| Review 02: duplicate routing table | **Remains closed** | The only routing navigation now references CW1, CW2, and CW4 and resolves named owners at `skills/<skill-name>/SKILL.md`; no work-shape mapping remains (`:60-63`). |
| Review 02: S2 ordered after its own acceptance | **Remains closed** | The decision and S2 consistently order repository package checks, caller authorization, installed-source mutation, D2 read-back, and package acceptance (`:10-17,196-203`). |
| Review 01: primary-owned units had no route | **Remains closed** | CW2, CW4, and E2 retain the unmatched primary-owned branch without forcing delegation or bypassing an applicable leaf (`:36,38,105-118`). |

## CW1-CW8 coverage

| Contract | Status | Evidence and decision |
|---|---|---|
| CW1 Trigger only for mixed ownership | **Cleared** | The row owns mixed-work selection and direct-leaf/small-work bypass, names the public request composition, and maps D1/E1 (`:35`). No second trigger definition remains. |
| CW2 Keep one outer owner | **Cleared** | Outer package ownership, leaf substantive authority, and the primary-owned fallback are explicit and exercised by E2 (`:36,105-118`). |
| CW3 Ground and decompose economically | **Cleared** | Primary evidence, visible assumptions, economical ordered units, reversible uncertainty, public composition, and E3 are implementation-independent (`:37,120-130`). |
| CW4 Route without duplicating leaf mechanics | **Cleared** | One row owns every current leaf mapping, the primary-owned route, and all forbidden legacy or duplicated mechanics (`:38`). Every named repository leaf exists and retains that interface. |
| CW5 Adapt at the invalidated boundary | **Cleared** | The row and E4 preserve accepted independent units while invalidating the contradicted unit and its dependents (`:39,132-142`). |
| CW6 Delegate through explicit ownership | **Cleared** | Delegation follows user, selected-leaf, or genuine-independence ownership rather than task size; E5 preserves primary acceptance and leaf topology (`:40,144-154`). |
| CW7 Preserve authorization, repository state, and installed-source identity | **Cleared for specification** | CW7 owns authorization and the S2 state transition; D2 and E6 separately cover deterministic source/install read-back and controlled model behavior (`:41,79-91,156-167`). Future live D2 evidence remains unexecuted. |
| CW8 Verify proportionally and finish once | **Cleared** | The row and E7 preserve focused checks, meaningful complete gates, leaf acceptance, one prose pass, and evidence-honest handoff (`:42,169-179`). |

## Required specification-cell dispositions

| Cell | Disposition |
|---|---|
| Single normative authority | **Cleared.** CW1-CW8 are the sole behavior authority. Scope, navigation, scenarios, implementation, acceptance, and handoff now add only ID references, evidence mechanics, work order, result effects, or artifact-specific reporting. |
| Durable contract boundary | **Cleared.** Every CW row names an observable result, semantic owner, representative public composition, and replaceable private implementation. |
| Scenario diagnosability | **Cleared.** D1-D2 and E1-E7 name contracts, observable invariants, evidence classes, capture/scoring, and localization. |
| Evidence topology | **Cleared.** D1-D2 are deterministic repository/local gates; E1-E7 are external compatibility evidence using controlled model behavior; telemetry is separate and not applicable. |
| External freshness | **Cleared.** Model evidence records exact skill revision, model/runtime, prompt, loaded skills, dossier, output/tool trace, scorer, and owning boundary; initial evidence is exact-identity and non-reusable (`:44-54`). |
| Telemetry decision power | **Not applicable.** No runtime metric participates in acceptance. |
| Exact-limit justification | **Not applicable.** No normative numeric limit is introduced; compactness is explicitly an implementation preference. |
| Workflow boundary | **Cleared.** S2 contains feature ordering and evidence only; `review-fixpoint` owns phase selection, artifact lifecycle, exact-revision timing, and the fixed-point decision (`:196-203,205-216`). |

## Findings and unknowns

None. No actionable P0-P3 defect or required specification-review unknown
remains. Future implementation and external evidence are unavailable because
the planned skill does not yet exist; they are not missing review coverage for
this design.

## D/E evidence status

| Lane | Current status | Decision effect |
|---|---|---|
| Specification review | **Passing on exact revision.** `git show --check --oneline 8a9f1b6c142ebb877e1240478448a584f38697f8` passed, the remediation diff was inspected, and every CW/specification cell was dispositioned. | Establishes the specification-design fixed point. |
| D1 repository skill package audit | **Not implemented or run.** `skills/complex-work` does not exist at this revision. | Does not block design acceptance; remains required for future package fixed point. |
| D2 authorization and installed-source audit | **Not run.** The live installed source remains a readable standalone directory rather than the planned repository symlink. | Does not block design acceptance; remains required after authorized S2. |
| E1-E7 controlled model compatibility | **`capability-unconfirmed`.** No model trial ran in this Tick, and no product-contract failure is claimed. | Does not make the design review red; prevents future package `Done` until confirmed. |
| Observational telemetry | **Not applicable.** | No effect. |

## Glossary and writing status

`docs/glossary.md` remains the selected glossary. `Leaf owner`, `semantic
owner`, Tick, Tock, deterministic fixed point, and capability statuses remain
consistent with their linked semantic sources. The normalized scope correctly
records that no new project term or glossary change is needed.

One `clear-technical-writing` pass was applied after coverage and the
zero-finding decision stabilized. It did not change any contract or evidence
disposition.

## Architectural scope and fixed-point result

No architectural-scope decision, durable follow-up, or finding laundering is
present.

- specification design `deterministic-fixed-point`: **reached**
- future skill package `deterministic-fixed-point`: **not reached; S1 and D1-D2 are not implemented**
- controlled model behavior: **`capability-unconfirmed`**
- installed-source transition: **not performed**
- future package `Done`: **not reached**

The accepted design is ready for supervised implementation.

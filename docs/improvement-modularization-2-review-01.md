# Improvement: Modularization 2 — Review 01

## Decision

**Contract result: `contract-fixed-point`. Plan result: `implementation-plan-fixed-point`.**

These results apply only to the exact normalized contract and delivery plan in this review, using proposal blob `5a638a0a34481e90c692e8a826bc137a0975afc4` and the dependency blobs listed under Evidence. This review is the sole current MD2 contract-and-plan authority; the proposal remains its rationale and historical input. A material change to the goal, MD2 rows, scenarios, package record, owner routing, or an identity-bearing dependency invalidates the affected result.

There are no P0–P3 specification or plan findings and no required unknowns. Two bounded implementation deltas remain. The architectural-scope authority qualifies a physical-decomposition defect but does not yet make that qualification activate the residual-topology lane. Separately, `complex-work` must carry the repository's always-on, lightweight physical-boundary constraint outside its current same-owner-overlap special case. Existing residual-inventory, EER, review-fixpoint, and architecture-guidance mechanics remain adequate and should not be expanded.

This result does not authorize an edit, select a Tock, prove an implementation, or establish an exact-revision gate. The caller supplied clean baseline HEAD `7ad2b4219aa4c12453651ec5bdc2a0f611900fd0`; Git operations were prohibited, so this review did not independently verify that HEAD or cleanliness.

## Normalized goal and scope

**Goal ID — MD2-G1.** Every ordinary design-sensitive implementation and review makes a lightweight, cohesive physical-boundary disposition for each new or materially changed responsibility. An explicit modularization package, or a source-proven and qualified physical-decomposition defect, instead activates the dedicated complete-topology mechanics, where required unknowns block completion.

The product authority is the user-authorized rebaseline supplied with this review. It preserves the accepted meanings of MD2-1 through MD2-6 while separating two costs:

1. Ordinary design-sensitive work names the semantic owner, selected source boundary, and cohesion reason for the affected responsibility. It does not inventory an entire root.
2. Explicit modularization or a qualified physical-decomposition defect routes the affected scope through complete-boundary, residual-topology, preservation/locality, and fixed-point mechanics.

Direct acceptance scenarios:

- **Ordinary path:** Given an ordinary design-sensitive change that places one responsibility cohesively, the workflow records a lightweight physical-boundary disposition and does not require a whole-root residual inventory.
- **Escalated path:** Given an explicit modularization package or source/dependency/state/test evidence that qualifies a physical-decomposition defect, the workflow routes the affected scope to the dedicated full residual-topology mechanics, and a required unknown blocks completion.
- **Negative boundary:** File size, file count, non-local work, or several units touching one source owner can prompt a lightweight placement check; none alone proves a physical-decomposition defect or activates complete-topology review.

## Sole MD2 contract-and-evidence matrix

| ID | Stable contract | Contract owner | Current source disposition | Establishing package | Deterministic evidence |
|---|---|---|---|---|---|
| MD2-1 | Modularity is an always-on architecture consideration for design-sensitive work. For each new or materially changed responsibility, identify its semantic owner, selected physical boundary, and cohesion reason. Semantic ownership does not require physical colocation, and this ordinary disposition does not require a whole-root inventory. | Authority: `add-architectural-guidances/references/guidance-contract.md`. Carrier: `complex-work`. | The guidance authority already defines this rule. `complex-work` carries it only inside its several-units/same-owner special case, leaving the planned coordinator delta. | MD2-P2 | MD2-D1, MD2-D4 |
| MD2-2 | Explicit modularization, or a physical-decomposition defect qualified from source, dependency, state, or test evidence, activates complete-boundary and residual-topology mechanics for the affected roots. Caller authority must make the correction scope explicit; without that authority or required analysis, the coverage remains `unknown` and blocks acceptance. Ordinary local placement and unqualified signals do not activate these mechanics. | `supervised-implementer-loop/references/architectural-scope-decision.md` | The authority already qualifies and bounds physical-decomposition defects, but it does not route a qualified defect into the residual-topology lane. MD2-P1 adds that missing transition without duplicating leaf mechanics. | MD2-P1 | MD2-D2, MD2-D3, MD2-D4 |
| MD2-3 | Implementation review checks affected-owner placement through a lightweight seam in ordinary work. For explicit modularization or an MD2-2-qualified affected scope, it separately proves preservation and locality and covers residual topology. | `evidence-efficient-review/references/implementation-review.md` | The existing general placement seam and conditional whole-scope rule are adequate once MD2-P1 activates physical-decomposition scope; no EER change is planned. | MD2-P1 | MD2-D1, MD2-D2, MD2-D3 |
| MD2-4 | Supervised implementation profiles an owner receiving a new design-sensitive responsibility compactly. Explicit modularization and an MD2-2-qualified affected scope use the existing full residual-root profile at parent acceptance. | `supervised-implementer-loop/SKILL.md` and `references/contract-and-scenario-package.md` | The existing lightweight owner profile and conditional modularization-root profile are adequate once MD2-P1 makes the selected physical-decomposition contract explicit; no SIL entrypoint or package-reference change is planned. | MD2-P1 | MD2-D1, MD2-D2, MD2-D3 |
| MD2-5 | Fixpoint review applies general architecture no-worsening coverage to ordinary work. Explicit modularization and an MD2-2-qualified affected scope require full residual dispositions; required unknown coverage blocks the existing result. | `review-fixpoint/SKILL.md` | The existing general routing and selected-physical-decomposition fixed-point rule are adequate once MD2-P1 activates that scope; no review-fixpoint change is planned. | MD2-P1 | MD2-D1, MD2-D2, MD2-D3 |
| MD2-6 | When architecture documentation or a glossary is independently in scope, distinguish semantic ownership, current physical placement, and accepted topology; descriptive placement does not create normative topology. No glossary work is required when no shared terminology changes. | The target repository's architecture-documentation authority; glossary authority only when independently triggered. | The proposal introduces no new shared terminology, so glossary work is not applicable to this package. | MD2-P2 | MD2-D5 |

This table is bidirectionally complete: MD2-1 through MD2-6 each map to exactly one establishing package, MD2-P1 and MD2-P2 each establish at least one contract, and there is no unmapped package or contract.

## Deterministic contract fixtures

These are source-and-contract fixtures, not claims about model behavior:

| Evidence ID | Fixture and required result | Covers |
|---|---|---|
| MD2-D1 | An ordinary change adds or materially changes one responsibility. The composed workflow names the owner, source boundary, and cohesion reason, without requesting full residual topology. | MD2-1, MD2-3, MD2-4, MD2-5 |
| MD2-D2 | The selected contract explicitly requests modularization. SIL inventories all affected residual roots, EER separates preservation from locality, and review-fixpoint blocks on a required unknown. | MD2-2, MD2-3, MD2-4, MD2-5 |
| MD2-D3 | Direct source/dependency/state/test evidence qualifies a physical-decomposition defect. Before affected-package acceptance, the scope authority either obtains caller authority for an explicit physical-decomposition contract and activates full residual inventory plus separate preservation/locality and fixed-point evidence, or records required coverage as `unknown` and selects scope stop. A partial helper rejection is not a substitute. | MD2-2, MD2-3, MD2-4, MD2-5 |
| MD2-D4 | A large file, non-local task, or same-owner overlap appears without qualifying structural evidence. The workflow performs the ordinary placement disposition but does not activate whole-root mechanics. | MD2-1, MD2-2, MD2-3, MD2-4, MD2-5 |
| MD2-D5 | Documentation describes current placement. It is not treated as accepted topology, and no glossary update is requested because this package adds no shared term. | MD2-6 |

## Minimal delivery-package map

| Order | Package | Establishes | Depends on |
|---|---|---|---|
| 1 | MD2-P1 — Qualified-decomposition escalation | MD2-2, MD2-3, MD2-4, MD2-5 | Accepted normalized matrix above and the exact existing SIL, EER, and review-fixpoint blobs under Evidence |
| 2 | MD2-P2 — Always-on modularity routing | MD2-1, MD2-6 | Accepted MD2-P1 and the exact architecture-guidance and `complex-work` blobs under Evidence |

### MD2-P1 — Qualified-decomposition escalation

- **Useful outcome and stopping point:** A source-proven, qualified physical-decomposition defect can no longer remain in the ordinary placement lane. The affected package either receives caller authority for explicit physical-decomposition scope and uses the existing complete residual mechanics or stops with required unknown coverage. Explicit modularization behavior remains unchanged. This is useful independently of coordinator integration.
- **Owner and edit boundary:** Change only `skills/supervised-implementer-loop/references/architectural-scope-decision.md`, which owns qualification, correction bounds, branch selection, and scope-stop effects. Do not copy residual inventory, implementation admission, review evidence, or fixed-point tables into it.
- **Prerequisites:** The user-authorized rebaseline, this exact normalized matrix, and unchanged SIL, EER, and review-fixpoint dependencies.
- **State, lifetime, and consumers:** Add no state or artifact. The qualification lives for the affected architectural-scope decision. SIL consumes it for package scope and acceptance, EER for required evidence, and review-fixpoint for result eligibility.
- **Transaction and failure behavior:** A qualified physical-decomposition defect transitions to explicit caller-authorized physical-decomposition scope before implementation continues. If authority or required residual analysis is absent, preserve it as required `unknown` coverage and select the existing scope-stop branch. Do not silently expand scope or credit ordinary no-worsening deferral as clearing the defect.
- **Public composition:** The architectural-scope authority points to the existing SIL residual profile and leaves EER and review-fixpoint conditions in their owners.
- **Acceptance evidence:** Exercise MD2-D2, MD2-D3, and MD2-D4; validate the SIL package, relative links, the explicit/unqualified polarity, and absence of duplicated mechanics.
- **Deferred work:** No target-repository decomposition is selected. Model efficacy and external validation remain outside this package.
- **Split/combine decision:** Qualification-to-scope transition is one concern in one authority. Splitting the transition from its failure effect would leave a non-useful half-rule; editing consumers would duplicate their already-correct selected-scope mechanics.
- **Acceptance-cost topology:** One focused source review, one SIL validator, link and polarity checks, and parent acceptance. The result is a useful working-tree stopping point but not an exact-revision fixed point.

Exact owning insertion direction: in `skills/supervised-implementer-loop/references/architectural-scope-decision.md`, immediately after the physical-decomposition qualification guidance and before test-locality qualification, add:

```markdown
Once source, dependency, state, or test evidence qualifies a physical-
decomposition defect, carry required physical-decomposition coverage for the
affected roots into branch selection. Before an affected package can be
accepted, either obtain caller authority that makes physical decomposition
explicit in the package contract and apply the
[residual-topology profile](contract-and-scenario-package.md#profile-modularization-roots)
plus its existing review and fixed-point rules, or retain the required residual
coverage as `unknown` and select scope stop. Do not use the ordinary lightweight
placement disposition or a no-worsening deferral to clear the qualified defect,
and do not silently broaden caller-approved scope.
```

### MD2-P2 — Always-on modularity routing

- **Useful outcome and stopping point:** Every design-sensitive `complex-work` unit receives the lightweight physical-boundary disposition. Explicit modularization and qualified physical-decomposition defects continue to use the existing full leaf mechanics. On acceptance, the complete two-tier workflow is available; no follow-on production package is required.
- **Owner and edit boundary:** Change only `skills/complex-work/SKILL.md`, which owns shared-constraint routing. Do not move inventory, qualification, review evidence, implementation admission, or fixed-point semantics out of their existing owners.
- **Prerequisites:** Accepted MD2-P1, the user-authorized rebaseline, this exact normalized matrix, and the identity-bearing dependency blobs listed below.
- **State, lifetime, and consumers:** No new persistent state or artifact. `complex-work` carries the constraint while establishing and assigning units; EER, SIL, architectural-scope, and review-fixpoint remain the consumers and operational owners.
- **Transaction and failure behavior:** Use the ordinary local disposition by default. Escalate only when the contract explicitly includes modularization/physical decomposition or qualifying source evidence exists. Missing required evidence in an activated leaf remains an unknown and blocks that leaf's existing acceptance/fixed-point result. No new phase, role, gate, or retry state is introduced.
- **Public composition:** `complex-work` links to and routes through the architecture-guidance and SIL architectural-scope authorities; the leaf skills retain their public contracts.
- **Acceptance evidence:** Exercise MD2-D1, MD2-D3, MD2-D4, and MD2-D5 as deterministic source fixtures; validate the changed skill package, relative links, wording polarity, and the negative constraints below. Later exact-revision acceptance requires the existing canonical gate and an independent Tick.
- **Deferred work:** Model efficacy, target-repository architecture changes, and architecture-documentation or glossary changes not otherwise in scope. No leaf-owner edit is deferred because none is required for this contract.
- **Split/combine decision:** One shared routing concern in one file is cohesive. Splitting it creates a checkpoint without an independently useful outcome; adding leaf edits duplicates established authorities and increases acceptance cost.
- **Acceptance-cost topology:** One focused source review, one package validator, link/structure checks, and parent acceptance cover the implementation candidate. The later authorized commit and exact-revision independent Tick remain distinct. External capability and telemetry are not applicable; no push is in scope.

Exact owning replacement direction: in `skills/complex-work/SKILL.md`, replace the paragraph beginning `For a mixed package in which several units affect the same source owner,` with:

```markdown
For every design-sensitive unit, carry the repository's
[architecture-guidance authority](../add-architectural-guidances/references/guidance-contract.md)
and its semantic-authority/physical-decomposition orthogonality rule as a shared
constraint. Ask the leaf to give a lightweight physical-boundary disposition for
each new or materially changed responsibility: name the semantic owner, the
selected source boundary, and why the placement keeps one cohesive reason to
change without unrelated context. This ordinary disposition does not require a
whole-root residual-topology inventory or a complete-boundary challenge for
unrelated clusters.

When the user-selected contract explicitly includes modularization or physical
decomposition, or source/dependency/state/test evidence qualifies a
physical-decomposition defect under the
[architectural-scope authority](../supervised-implementer-loop/references/architectural-scope-decision.md),
route the affected unit through that authority and the existing leaf mechanics.
Require the implementation or review leaf to report the activated-scope result,
residual-topology coverage, separate preservation and locality evidence, and
fixed-point eligibility for that affected scope. Several units touching the
same source owner are a signal to check the lightweight disposition; overlap
alone does not activate the full topology mechanics. Leave activation,
inventory, qualification, and fixed-point rules to their existing owners.
```

The wording is normative at the contract level, not a required verbatim implementation. A semantically equivalent smaller edit is acceptable if MD2-D1 through MD2-D5 still pass.

## Required specification-cell dispositions

| Cell | Disposition |
|---|---|
| One product and contract authority | Clear: the user rebaseline is product authority; the matrix above is the sole normalized MD2 contract. |
| Behavioral trace and durable goal | Clear: MD2-G1, both direct paths, and the negative boundary are explicit. |
| Scenario and counterexample coverage | Clear: MD2-D1 through MD2-D5 cover ordinary, explicit, evidence-qualified, non-qualifying, and documentation paths. |
| Deterministic evidence | Clear: source/contract fixtures and repository validators are sufficient for mechanism review. |
| External capability | Not applicable. |
| Telemetry | Not applicable. |
| Exact limits | Not applicable; no numeric threshold is introduced. |
| Lasting defensive machinery | Clear and proportionate: expensive topology proof is activated only by selected scope or qualifying evidence. |
| Change locality and ownership | Clear: one scope-authority reference and one coordinator entrypoint change in separate packages; operational leaf authorities remain singular. |
| Workflow effects | Clear: existing phases, roles, result levels, and canonical gate are unchanged. |
| Contract/plan decision levels | Clear and reported separately. |
| Contract-to-package cardinality | Clear: four contracts map exactly once to MD2-P1 and two map exactly once to MD2-P2. |
| Useful stopping point | Clear: MD2-P1 completes qualified-defect escalation; MD2-P2 then completes the composed two-tier workflow. |
| Package cohesion | Clear: each package changes one concern in one owning file. |
| Dependency order | Clear: accepted leaves precede MD2-P1; MD2-P1 precedes its thin coordinator carrier MD2-P2. |
| Split/combine causality | Clear: splitting either owner transition creates a half-rule; combining them hides two independently useful outcomes and two owners. |
| Acceptance cost | Clear: two focused implementation reviews can share the one later authorized commit and exact-revision gate. |
| Checkpoint versus delivery boundary | Clear: no intermediate checkpoint is represented as a package. |

## Findings, unknowns, and status

- **P0–P3 findings:** none.
- **Required unknowns:** none at contract or plan level.
- **Planned mechanism deltas:** The architectural-scope authority does not yet transition a qualified physical-decomposition defect into the full residual lane; `complex-work` does not yet carry MD2-1 outside its same-owner-overlap special case. These are MD2-P1 and MD2-P2, respectively, not defects in the normalized specification or delivery plan.
- **Behavioral status:** `partial`. Explicit modularization is structurally supported. Qualified physical-decomposition defects are bounded but do not yet activate full residual coverage, and the ordinary path is not guaranteed through `complex-work` for every design-sensitive unit.
- **Mechanism status:** `in-progress`. Existing leaf mechanics are present; MD2-P1 and MD2-P2 are neither implemented nor admitted.
- **Exact-revision status:** pending implementation, an authorized commit, canonical-gate evidence, and a fresh independent Tick. Neither `deterministic-fixed-point` nor Done is claimed.
- **Model efficacy:** unproved and outside deterministic acceptance.

## Architecture and ownership self-check

The result keeps one authority per concern:

- architecture guidance owns the always-on semantic/physical rule;
- `complex-work` carries the shared constraint and stays thin;
- SIL owns implementation profiling, admission, and package execution;
- the SIL architectural-scope reference owns qualification, complete-boundary challenge, and the transition from a qualified defect to explicit affected-scope coverage or scope stop;
- EER owns implementation evidence and preservation/locality review;
- review-fixpoint owns fixed-point semantics and unknown-blocking effects;
- target-repository documentation owners describe architecture only when independently in scope.

The plan adds no competing policy surface and does not turn a local placement decision into a repository-wide modularization campaign.

## Evidence and checks

Identity-bearing inputs were read directly and their Git-blob SHA-1 values were independently recomputed from file bytes without invoking Git:

| Input | Blob |
|---|---|
| `docs/improvement-modularization-2.md` | `5a638a0a34481e90c692e8a826bc137a0975afc4` |
| `skills/add-architectural-guidances/references/guidance-contract.md` | `59e01130e97f89257dc406647d37c5a5d48e7dfd` |
| `skills/complex-work/SKILL.md` | `81b506218dbba40b4c722717a54119c4ec50cf18` |
| `skills/evidence-efficient-review/SKILL.md` | `29a3f7070e6edaf873c3bed8bd795546766616db` |
| `skills/evidence-efficient-review/references/implementation-review.md` | `1d709915850ddca63fec2c1d9ba76de0e1d13c93` |
| `skills/review-fixpoint/SKILL.md` | `fc78f0275ad221429cd9b1a813402855f78c7285` |
| `skills/supervised-implementer-loop/SKILL.md` | `a1a2618c4ed7a9455c66f09875f100530e77f360` |
| `skills/supervised-implementer-loop/references/contract-and-scenario-package.md` | `73ca67aa0d851aaf42e655ec540f92be4dab9f35` |
| `skills/supervised-implementer-loop/references/architectural-scope-decision.md` | `becd18023d5dfe6cdd2c49125f000018b8135332` |

Source audit results:

- architecture guidance contains the always-on physical-decomposition self-check;
- `complex-work` contains the rule only in the same-owner-overlap special case and lacks the general design-sensitive-unit route;
- the architectural-scope authority qualifies and bounds physical-decomposition defects but has no source rule that makes a qualified defect activate residual-topology coverage or stop with that required unknown;
- SIL contains both a lightweight design-sensitive-owner profile and a separately conditional full modularization-root profile;
- EER contains both a general affected-owner placement seam and a separately conditional whole-scope residual review;
- review-fixpoint applies general no-worsening coverage and conditions full residual fixed-point rules on selected physical decomposition;
- all 33 relative links inspected across the proposal and relevant skills resolved;
- `quick_validate.py` passed for `add-architectural-guidances`, `complex-work`, `evidence-efficient-review`, `review-fixpoint`, and `supervised-implementer-loop`;
- a bounded negative-mechanics search found no new line-count rule, one-module-per-term rule, mandatory phase, mandatory role, mandatory artifact, or mandatory gate.

## Non-goals and evidence limits

This package does not add a review phase, role, gate, mandatory artifact, line-count threshold, one-module-per-term rule, or universal whole-root inventory. It does not prescribe a target repository's architecture, require unrelated refactoring, edit a glossary, prove model behavior, validate external capability, collect telemetry, commit, or push.

Glossary work is **not applicable** because the normalized contract reuses existing architecture terms and authorities; no glossary was accessed, created, or updated. External capability and telemetry are **not applicable**. The clear-writing pass completed: the decision leads, ordinary and escalated paths remain distinct, owner verbs are explicit, and checks are presented as backstops rather than the process itself.

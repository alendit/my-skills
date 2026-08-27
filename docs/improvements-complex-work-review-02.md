# Repository-Owned Complex Work Orchestration — Review 02

## Decision

**Changes requested** on exact remediation revision
`2ccffcd79835eb72f41feecb7c8ec029986f2444`.

The remediation closes Finding 03 and most of Findings 01, 02, and 04. It now
defines the primary-owned fallback, separates source checks from controlled
model scenarios, maps S2 into CW7, names public compositions, identifies the
selected external authoring authority accurately, and delegates fixed-point
mechanics to `review-fixpoint`. Three P2 defects remain: the controlled model
lane is not assigned the repository's external-evidence class and complete
result vocabulary, the routing table still duplicates CW4, and the opening
decision retains the circular instruction to install only after deterministic
acceptance. This is an incomplete prior closure, not a new architectural scope.

Reviewed scope:

- `docs/improvements-complex-work.md` at the exact revision above;
- immutable Review 01 and all four prior corrective contracts;
- the unchanged repository leaf interfaces named by CW4;
- `evidence-efficient-review`'s specification evidence classes;
- `review-fixpoint`'s deterministic and external result vocabulary; and
- the live installed `complex-work` and selected `skill-authoring` source
  identities.

## Prior finding dispositions

| Review 01 finding | Disposition | Exact evidence |
|---|---|---|
| 01 — E1-E7 called deterministic | **Partially closed; incomplete prior closure** | Lines 51-61 separate repository-deterministic checks from E1-E7 controlled model behavior, add exact run identity, prohibit initial reuse, and distinguish unavailable execution from a valid contract contradiction. D1-D2 and E1-E7 now record invariant, evidence class, capture/scoring, and localization (`:85-192`). The E rows nevertheless call their class only `controlled model behavior`, and package acceptance does not use the complete external-capability result vocabulary. Finding 01 below remains. |
| 02 — CW matrix incomplete and duplicated | **Partially closed; incomplete prior closure** | CW4 now owns positive and forbidden routing (`:45`); CW7 owns the authorized installed-source transition and D2 (`:48`); every row names a public composition; S1 records the selected `$skill-authoring` source (`:201-207`). Lines 69-81 still reproduce CW1/CW4's work-shape-to-owner rules in a second table despite calling it non-normative. Finding 02 below remains. |
| 03 — Primary-owned units had no route | **Closed** | CW2 explicitly keeps unmatched units primary-owned without inventing a leaf or bypassing an applicable one (`:43`); CW4 references that branch (`:45`); E2 exercises both supervised and ordinary primary-owned compositions (`:122-135`). This matches the selected glossary's caller-inclusive `leaf owner`. |
| 04 — S2 embedded circular partial fixed-point sequence | **Partially closed; incomplete prior closure** | S2 now waits for named repository package checks and explicit installation authority, records link evidence, and assigns all Tick/Tock and fixed-point mechanics to `review-fixpoint` (`:209-216`). Package acceptance and handoff no longer copy review-artifact or exact-revision mechanics (`:218-231`). The opening decision still says the installed transition follows deterministic acceptance (`:10-15`), while D2 is required to obtain that acceptance (`:97-109,220-225`). Finding 03 below remains. |

## CW1-CW8 coverage

| Contract | Status | Evidence and decision |
|---|---|---|
| CW1 Trigger only for mixed ownership | **Contract cleared; evidence finding** | The mixed/end-to-end/small boundary and public request composition are stable (`:42`). D1 and E1 are separated, but E1's formal evidence classification and package result remain incomplete under Finding 01. |
| CW2 Keep one outer owner | **Cleared** | Outer ownership, leaf authority, and the unmatched primary-owned unit are explicit in one row (`:43`). E2 independently covers both specialized and fallback compositions. |
| CW3 Ground and decompose economically | **Contract cleared; evidence finding** | The observable contract and public repository-backed composition remain implementation-independent (`:44`). E3 is diagnosable, but its lane classification inherits Finding 01. |
| CW4 Route without duplicating leaf mechanics | **Finding** | The row now owns the complete positive and negative route (`:45`) and matches current leaf interfaces. The second work-shape table remains a competing copy. Finding 02 applies. |
| CW5 Adapt at the invalidated boundary | **Contract cleared; evidence finding** | Dependency invalidation, carry-forward, public composition, and E4 localization are complete (`:46,148-157`). Evidence result vocabulary remains under Finding 01. |
| CW6 Delegate through explicit ownership | **Contract cleared; evidence finding** | The row and E5 preserve leaf topology and reject size-only fan-out (`:47,159-168`). Evidence result vocabulary remains under Finding 01. |
| CW7 Preserve authorization, repository state, and installed-source identity | **Contract finding** | The row now owns S1/S2 authorization, preservation, installation, public loader composition, D2, and E6 (`:48,97-109,170-180`). The opening decision contradicts its D2-before-acceptance dependency. Findings 01 and 03 apply. |
| CW8 Verify proportionally and finish once | **Contract cleared; evidence finding** | The public handoff composition and split D1/E7 checks are complete (`:49,182-192`). Evidence result vocabulary remains under Finding 01. |

## Confirmed findings

### Finding 01 — P2 — Controlled model behavior is not assigned the external evidence class and complete package result

**Proof.** The remediation correctly removes E1-E7 from deterministic evidence
(`docs/improvements-complex-work.md:51-61`), but each scenario records its
evidence class only as `controlled model behavior` (`:117,130,143,154,165,176,
188`). The specification-review authority admits exactly three evidence
classes: deterministic release gate, external compatibility evidence, and
observational telemetry. The selected model/runtime's ability to follow the
skill is the required external capability; `controlled model behavior` is the
kind of probe, not a fourth evidence class.

The acceptance section requires “current controlled-model dispositions” and
names only `capability-unconfirmed`, `product-contract failure`, and `Done`
(`:218-225`). It does not state when a passing fresh run is
`capability-confirmed`, when a non-product execution failure remains
`capability-unconfirmed`, or when a valid contradiction yields
`external-contract-failed`. An implementation reviewer could therefore record
some current disposition without one of the result states that determines
whether the package is complete.

**Owning correction:** change every E1-E7 evidence-class field to:

> **Evidence class:** external compatibility evidence; controlled model
> behavior.

Replace the acceptance paragraph with:

> Accept deterministic implementation when CW1-CW8 are implemented, D1-D2
> pass on the accepted revision and installed state, the selected
> `$skill-authoring` authority finds no checklist violation, and no valid E1-E7
> product-contract failure remains unresolved. Separately report E1-E7 as
> `capability-confirmed` when fresh valid runs pass,
> `capability-unconfirmed` when a valid observation is unavailable because of
> stale identity, authentication or configuration, provider or infrastructure
> failure, or inconclusive timeout, and `external-contract-failed` when a valid
> run contradicts a CW contract. `Done` requires deterministic fixed point and
> `capability-confirmed`. `$review-fixpoint` owns the fixed-point decision and
> review-artifact lifecycle.

Rename the section to `Package acceptance` so its heading does not imply that
the separately reported model lane is deterministic.

### Finding 02 — P2 — The routing table remains a duplicate contract authority

**Proof.** CW1, CW2, and CW4 are declared the complete routing contract
(`:42-45,69-70`). The following table nevertheless repeats the exact
work-shape-to-owner mappings for review, fixpoint, supervised implementation,
technical notes, architecture documentation, architecture guidance, final
prose, and the outer orchestrator (`:72-81`). Calling this table
“non-normative” does not turn it into a file map: it contains no file paths and
can disagree with CW4 after either copy changes. This is the duplicate Review 01
explicitly required lines 57-76 to replace with CW ID references.

**Owning correction:** delete lines 67-81. If implementers need navigation,
replace them with a genuinely section-specific path statement:

> CW1, CW2, and CW4 own routing. Resolve each named skill at
> `skills/<skill-name>/SKILL.md`; do not maintain another work-shape mapping.

The scope/non-goal prose may remain explanatory only if it references the CW
rows rather than introducing another positive or negative route.

### Finding 03 — P2 — The decision still places S2 after the acceptance that requires D2

**Proof.** The opening decision says the repository-owned replacement becomes
the installed source “after deterministic acceptance” (`:10-15`). The package
acceptance section requires D1-D2 (`:218-225`), while D2 can pass only after the
authorized installation and link read-back (`:97-109`). S2 itself now gives the
correct order: repository implementation checks, authorization, mutation, and
read-back (`:209-216`). The stale opening sentence therefore preserves the
circular reading from Review 01 and competes with the corrected S2 authority.

**Owning correction:** replace the final sentence of the opening decision with:

> The repository-owned replacement must remove those conflicts. After its
> repository package checks pass and the caller authorizes installation, S2
> makes it the installed source and D2 verifies that state for package
> acceptance.

## Required specification-cell dispositions

| Cell | Disposition |
|---|---|
| Single normative authority | **Finding.** CW4 owns routing, but lines 67-81 retain a second work-shape mapping. Finding 02 applies. |
| Durable contract boundary | **Cleared.** Every row now names an observable result, semantic owner, and representative public composition without requiring a private representation. |
| Scenario diagnosability | **Cleared.** D1-D2 and E1-E7 name contracts, invariants, capture/scoring, and localization; E2 covers the previously missing primary-owned branch. |
| Evidence topology | **Finding.** Deterministic and model scenarios are separated, but the model scenarios are not assigned the required external compatibility class and complete result mapping. Finding 01 applies. |
| External freshness | **Cleared.** Each controlled model run records the exact skill, model/runtime, prompt, loaded skills, dossier, capture, and scorer; initial evidence is exact-identity and non-reusable (`:55-61`). |
| Telemetry decision power | **Not applicable.** No runtime metric participates in acceptance. |
| Exact-limit justification | **Not applicable.** No normative numeric limit is introduced; compactness remains explicitly non-contractual. |
| Workflow boundary | **Finding.** S2 and final acceptance now defer workflow mechanics correctly, but the opening decision retains the circular acceptance/install order. Finding 03 applies. |

## Evidence status

- **Exact revision:** `git rev-parse HEAD` and `git show` resolved to
  `2ccffcd79835eb72f41feecb7c8ec029986f2444` before this artifact was written.
- **Revision hygiene:** `git show --check --oneline
  2ccffcd79835eb72f41feecb7c8ec029986f2444` passed.
- **Remediation scope:** the revision changes only the proposed specification
  and commits immutable Review 01. The seven repository leaf interfaces are
  unchanged from the reviewed baseline.
- **D1-D2 implementation evidence:** not executed. The repository-owned
  `skills/complex-work` package does not yet exist, and the installed source is
  still the readable standalone directory rather than the planned symlink.
- **E1-E7 controlled model evidence:** not executed and
  `capability-unconfirmed`. No product-contract failure is claimed.
- **Selected authoring authority:** the installed `skill-authoring` entry still
  resolves outside this repository to the recorded
  `dvorona-agentic-skills/dialects/wenyan/repo-skills/skill-authoring` source.
- **Observational telemetry:** not applicable.

## Glossary and writing status

`docs/glossary.md` remains the selected glossary. The remediation correctly
uses the caller-inclusive `leaf owner`, preserves `semantic owner`, and leaves
Tick, Tock, deterministic fixed point, and capability status subordinate to
their linked workflow and evidence authorities. No new glossary term or
authorized glossary mutation is needed.

One `clear-technical-writing` pass was applied after the dispositions,
severities, evidence, and exact corrective wording stabilized. It did not alter
the review decision.

## Architectural scope, unknowns, and fixed-point status

No architectural-scope decision or durable follow-up is warranted. No required
cell remains merely unknown; the three remaining issues are source-proven
incomplete closures.

`deterministic-fixed-point` is **not reached** at
`2ccffcd79835eb72f41feecb7c8ec029986f2444`. Findings 01-03 must be remediated
before another independent Tick. Controlled model capability remains
`capability-unconfirmed` and cannot establish `Done`.

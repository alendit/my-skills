# Clear Technical Writing Integration — Review 03

## Decision

**Accepted for specification design** at exact revision
`54fb32098ab35c692e615f93f004cc50f642b84d`.

This fresh incremental Tick verified both Review 02 corrections and retained
the three Review 01 closures. The specification now defines the human
comprehension outcome once, uses that outcome to score V11, and replaces the
unsupported seven-day reuse threshold with non-reusable initial evidence. Its
contract, scenario, evidence, and completion boundaries have no remaining
P0-P3 finding or required unknown.

This decision applies to the design document. It does not claim that the future
skill package exists, that V9-V10 have run, that a model has passed V1-V8, or
that readers have confirmed V11.

Reviewed scope:

- `docs/improvement-clear-technical-writing.md` at the revision above;
- both findings and the disposition update in
  `docs/improvement-clear-technical-writing-review-02.md`;
- all Review 01 closures;
- `docs/improvement_avoid_repetition.md` and
  `docs/improvement-right-feedback.md` as composed authorities; and
- the changed CTW10, V11, freshness, completion, and adjacent contract and
  evidence cells.

## Prior finding dispositions

| Prior finding | Disposition | Evidence |
|---|---|---|
| Review 01: artifact visibility and nested consumers do not select one writing authority | **Remains closed.** | CTW2 routes by artifact purpose and factual owner, selects one transformation authority for an overlap, assigns one pass to the substantive leaf owner, and prohibits a second outer-orchestrator pass (`improvement-clear-technical-writing.md:37-43,70,80-103`). The review route gives prose ownership to `evidence-efficient-review` and leaves mechanics to `review-fixpoint` (`:94`). |
| Review 01: the deterministic suite cannot prove model-generated writing behavior | **Remains closed.** | CTW10 assigns only static repository properties to deterministic gates and assigns V1-V8 to controlled model evidence (`:78`). S5, S6, and the scenario portfolio preserve that separation, capture runtime identity, and score observable output without inferring private planning (`:188-231`). |
| Review 01: V11 does not isolate the skill effect | **Remains closed.** | The paired comparison fixes the task, source packet, outer instructions, model/runtime configuration, generation policy, and exposed settings while changing only skill presence. It also predeclares scoring and randomizes or counterbalances presentation (`:231,249-259`). |
| Review 02: V11 references an absent comprehension contract | **Closed.** | CTW10 now defines the five reader outcomes once (`:78`). V11 references that authority, derives its answer key from each source packet before generation, and maps both scorers to those questions (`:231`). No second question list competes with CTW10. |
| Review 02: the 168-hour freshness gate lacks a workload and cost basis | **Closed.** | The exact calendar threshold is gone. Initial V1-V8 and V11 evidence cannot be reused and is current only for its commissioning acceptance review while every recorded identity remains unchanged (`:261-269`). A later reuse proposal requires observed model volume, token use, elapsed time, human effort, rerun cost, and independent acceptance under the composed exact-limit policy (`:271-278`). |

## CTW1-CTW10 coverage

| Contract | Status | Evidence |
|---|---|---|
| CTW1 Preserve substantive authority | **Cleared; V1 specified.** | Source and specialized skills retain facts and decisions; the prose pass returns uncertain meaning to them. V1 compares severity, status, evidence, and requested correction and names the failed owner boundary (`:69,221`). |
| CTW2 Route one prose pass | **Cleared; V2 specified.** | Purpose and factual source distinguish engineering evidence from general prose, including public artifacts. Leaf ownership and explicit overlap handling select one pass. V2 observes the invocation trace and localizes a routing mismatch (`:37-43,70,82-103,222`). |
| CTW3 Derive reader and purpose | **Cleared; V3 specified.** | The actual artifact audience takes precedence over the uninvolved-developer fallback. V3 compares the information required by PR, local-comment, and operator audiences (`:71,223`). |
| CTW4 Use adaptive effort | **Cleared; V4 specified.** | Compact work gets a compact pass, dependent claims get a private question/evidence map, and sentence simulation is diagnostic only. V4 scores visible compactness, prerequisite order, and support without claiming private planning occurred (`:72,224`). |
| CTW5 Explain terminology and relationships | **Cleared; V5 specified.** | Necessary repository terms remain allowed after definition, while compressed wording must expose the relevant actor, operation, object, condition, and consequence. V5 scores that observable result (`:73,225`). |
| CTW6 Ground claims and measurements | **Cleared; V6 specified.** | The contract distinguishes source truth, unknowns, exact correctness values, and decision-sized observational precision. V6 names a source-field comparator and separates fidelity from measurement treatment (`:74,226`). |
| CTW7 Match structure and detail | **Cleared; V7 specified.** | Information relationships select prose, lists, steps, tables, or a useful diagram; reader need governs deletion. V7 scores structure and prerequisite preservation without imposing a universal template (`:75,227`). |
| CTW8 Revalidate later edits | **Cleared; V8 specified.** | The invalidation boundary covers dependent claims, transitions, title, summary, conclusion, and evidence, and scales the reread to the semantic impact. V8 compares changed source with the affected complete prose boundary (`:76,228`). |
| CTW9 Keep one compact authority | **Cleared; V9 specified.** | The entrypoint owns trigger, precedence, adaptive process, and final questions; one-level references hold supporting detail; consumers link instead of copying. V9 checks substantive ownership, one invocation point, one concise link, and duplicate authority (`:77,105-127,229`). |
| CTW10 Separate observable evidence lanes | **Cleared; V9-V11 specified.** | Repository structure, controlled model behavior, human comprehension, and observational telemetry have separate owners and decision effects. CTW10 defines the five human outcomes, V11 has a controlled paired protocol, and completion preserves unconfirmed external capabilities (`:78,219-231,233-293`). |

## Required specification-cell dispositions

| Cell | Disposition |
|---|---|
| Single normative authority | **Cleared.** CTW1-CTW10 are the declared package authority. Routing, slices, scenarios, and completion add mappings, work order, evidence mechanics, and status effects without restating a second prose contract. |
| Durable contract boundary | **Cleared.** Observable meaning, ownership, reader outcomes, evidence, and revision behavior are normative. Private drafting representation and equivalent one-level package layouts remain replaceable (`:24-35,69-78,105-127`). |
| Scenario diagnosability | **Cleared.** V1-V8 share identity capture and each names an observable scorer and contract boundary. V9-V10 name static checks. V11 distinguishes factual preservation from comprehension failure (`:207-231`). |
| Evidence topology | **Cleared.** V9-V10 are deterministic repository gates; V1-V8 are controlled model compatibility evidence; V11 is separate human evidence; unthresholded measurements are observational (`:78,219-231,233-284`). |
| External freshness | **Cleared.** Initial evidence has exact identity, collection time, age, and an event-bounded current period but no reuse. Completion of the commissioning review or any later claim requires a new run. Future reuse cannot be introduced until measured cost and an independently accepted freshness record exist (`:261-278`). |
| Telemetry decision power | **Cleared.** Word count, tokens, latency, reading time, preference, and edit size cannot establish or block acceptance without a baseline, method, direction, and threshold (`:280-284`). |
| Exact-limit justification | **Cleared.** The unsupported seven-day normative limit was removed. Any future reuse interval must satisfy the imported exact-limit policy after a full run supplies workload and resource observations (`:271-278`). The 100-line reference guidance remains package-authoring guidance rather than a product-correctness gate (`:122-127`). |
| Workflow boundary | **Cleared.** The feature plan requires an independent review but leaves Tick/Tock mechanics, phase commits, reviewer selection, and repetition to `review-fixpoint` (`:199-205`). |

## Findings

None. No actionable P0-P3 defect was found in the remediated specification or
its composition with the two authoritative improvement plans.

## Unknowns

None for specification design. Every CTW row, both Review 02 corrections, all
Review 01 closures, and every required specification cell were inspected.

The following future evidence is unavailable rather than unknown review
coverage: V9-V10 package results, V1-V8 controlled model results, V11 human
results, and rollout-cost telemetry. The design explicitly schedules and
classifies those results.

## Architectural scope and follow-up disposition

No AF1 architectural-scope decision is required. The remediation changes only
the comprehension and external-evidence contracts already owned by CTW10. It
does not add a dependency, split semantic authority, move state, create a public
compatibility surface, or defer a current contract defect.

Follow-up deltas:

- created: none;
- updated: none;
- closed: none;
- stale: none; and
- unchanged-but-relevant: none.

No finding was relabeled as a follow-up.

## Evidence lanes and current status

| Lane | Current status | Acceptance effect |
|---|---|---|
| Specification review evidence | **Passing on exact revision.** The target revision exists, `git show --check` passes, both composed plan links resolve, and the complete changed evidence boundary was inspected. | Supports the specification-design fixed point. |
| Future deterministic package evidence, V9-V10 | **Not implemented or run.** | Does not block acceptance of this design document; remains required before the future package can claim `deterministic-fixed-point`. |
| Future controlled model behavior, V1-V8 | **`model-capability-unconfirmed`.** No trial was run in this Tick. | Does not turn the design review red and cannot be reported as passing. It remains required for future `Done`. |
| Future blinded human comparison, V11 | **`human-comprehension-unconfirmed`.** No pilot was run in this Tick. | Does not turn the design review red and cannot support an improvement claim. It remains required for future `Done`. |
| Observational telemetry | **None collected.** | No unthresholded measurement affected this decision. Future cost observations inform, but do not themselves set, a reuse interval. |

## Fixed-point result

- specification design `deterministic-fixed-point`: **reached**
- future package `deterministic-fixed-point`: **not reached; package and V9-V10 do not exist**
- controlled model behavior: **`model-capability-unconfirmed`**
- human comprehension improvement: **`human-comprehension-unconfirmed`**
- future package `Done`: **not reached**

The design is ready to enter implementation. The implementation must still
create the package, integrate the six consumers, run V9-V10, and obtain current
passing V1-V8 and confirmed V11 evidence before making the stronger package or
capability claims.

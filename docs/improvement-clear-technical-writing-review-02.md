# Clear Technical Writing Integration — Review 02

## Decision

**Changes requested** on revision
`f1d21cf3306fcabd23a95979acd9fd2874c2bd65`.

## Current disposition after Tock

The remediation following this historical review addresses both findings:

| Finding | Current disposition |
|---|---|
| Missing V11 comprehension contract | Addressed by defining the five reader outcomes once in CTW10 and requiring V11 to derive its source-packet answer key and scorers from those outcomes. |
| Unsupported 168-hour freshness gate | Addressed by removing the calendar gate. Initial external evidence is non-reusable and current only for its commissioning acceptance review. A future reuse interval requires measured trial volume, human effort, elapsed time, and rerun cost under the imported exact-limit policy. |

These dispositions preserve the original decision below. A fresh Tick must
verify the remediated revision before any fixed-point claim.

This incremental Tick independently verified the three Review 01 findings and
then audited the changed evidence and routing boundaries. The remediation
correctly assigns one prose pass to the substantive leaf owner and separates
repository checks, controlled model behavior, human comprehension evidence, and
observational telemetry. It also removes the unobservable private-plan claim
from V4 and gives V11 a causally matched baseline.

Two P2 specification defects remain. V11 invokes five comprehension questions
that the remediated authority no longer defines, so its required human gate is
not reproducible. The new seven-day evidence boundary is exact but is supported
only by an asserted rollout duration and an unquantified rerun cost, contrary to
the imported exact-limit contract. CTW10 and the external-freshness evidence
cell therefore remain open. This specification design has not reached
deterministic fixed point.

Reviewed scope:

- `docs/improvement-clear-technical-writing.md` at the revision above;
- the Review 01 findings and the remediation diff;
- `docs/improvement_avoid_repetition.md` and
  `docs/improvement-right-feedback.md` as composed authorities;
- the installed general `writing` skill; and
- the six planned consumers, only at their prose-authority and nested-workflow
  boundaries.

## Review 01 finding dispositions

| Prior finding | Disposition | Evidence |
|---|---|---|
| Artifact visibility and nested consumers do not select one writing authority | **Closed.** | CTW2 now routes by artifact purpose and factual source rather than publication visibility, assigns the pass to the substantive leaf owner, and prohibits an outer orchestrator from applying a second pass (`improvement-clear-technical-writing.md:37-43,70`). The routing table assigns review prose to `evidence-efficient-review` and leaves only outer mechanics to `review-fixpoint` (`:82-103`). This composes with the installed `writing` skill's broader documentation/report scope by selecting one transformation authority for an overlap. |
| The deterministic suite cannot prove model-generated writing behavior | **Closed.** | CTW10 limits deterministic evidence to repository-owned package and fixture properties and moves V1-V8 to controlled model trials (`:78`). S5-S6 and the portfolio preserve that split (`:188-231`). V4 now scores only output compactness, prerequisite order, and supported claims; it makes no assertion about private planning (`:224`). |
| V11 does not isolate the skill's effect or define reusable evidence age | **Partially closed.** | The paired baseline now fixes task, source packet, outer instructions, model/runtime configuration, generation policy, and exposed settings while changing only skill presence; presentation is randomized or counterbalanced and scoring is predeclared (`:231,249-259`). Identity and an exact age boundary now exist (`:261-275`). The age boundary is not justified to the standard imported by this plan, so the freshness part remains open as Finding 02 below. |

## CTW1-CTW10 coverage

| Contract | Status | Evidence |
|---|---|---|
| CTW1 Preserve substantive authority | **Cleared; V1 specified** | The contract keeps facts, decisions, findings, severity, and evidence status with their existing owners. V1 compares those observable fields and names the owning boundary on failure (`:69,221`). |
| CTW2 Route one prose pass | **Cleared; V2 specified** | Purpose-and-source routing distinguishes engineering evidence from general prose, including public artifacts, while leaf-versus-orchestrator ownership selects one pass (`:37-43,70,80-103`). V2 captures invocation and localizes a mismatch (`:222`). |
| CTW3 Derive reader and purpose | **Cleared; V3 specified** | The actual artifact audience takes precedence over the uninvolved-developer fallback, and V3 compares the information required by three audiences (`:71,223`). |
| CTW4 Adaptive drafting | **Cleared; V4 specified** | Compact, dependent-claim, and difficult-passage effort are bounded. Private planning is explicitly excluded from acceptance, while V4 observes output order and cost separately (`:72,224`). |
| CTW5 Explicit terminology and relationships | **Cleared; V5 specified** | Necessary stable terms remain allowed after an ordinary-language definition, while hidden actors, operations, conditions, and results must be exposed. V5 scores that observable relationship (`:73,225`). |
| CTW6 Ground claims and measurements | **Cleared; V6 specified** | Source fidelity, unknowns, exact boundaries, and decision-sized observational precision remain distinct, with a source-field comparator named in V6 (`:74,226`). |
| CTW7 Structure and deletion | **Cleared; V7 specified** | Structure follows the information relationship and deletion follows reader need. V7 scores both properties without imposing a fixed template (`:75,227`). |
| CTW8 Revalidate later edits | **Cleared; V8 specified** | Dependency invalidation reaches affected claims, transitions, summaries, conclusions, and evidence. V8 compares the changed source packet with the complete affected prose boundary (`:76,228`). |
| CTW9 One compact authority | **Cleared; V9 specified** | The proposed package keeps one short entrypoint, one-level references, research outside the invocation path, and consumer links rather than copied process. V9 checks leaf ownership and duplicate authority (`:77,105-127,229`). |
| CTW10 Separate observable evidence lanes | **Candidate.** | Repository checks, model trials, human evidence, and telemetry now have distinct decision roles (`:78,233-289`). V11 is not runnable as written because its referenced five questions are absent from CTW10 and elsewhere in the current document. The exact freshness boundary also lacks the required cost and evidence basis. See Findings 01 and 02. |

## Confirmed findings

### P2 — V11 references a comprehension contract that no longer exists

V11 requires audience-matched readers to answer “the five CTW10 questions”
(`docs/improvement-clear-technical-writing.md:231`). The remediated CTW10 row no
longer states those questions (`:78`), and no other current section defines
them. The previous wording asked readers to explain what happened before, what
changes, why the behavior is correct or deliberately different, what evidence
matters, and what action is requested. Removing that wording while retaining
the reference leaves the human scorer without a stable observable contract.

“Predeclared factual and comprehension scorers” does not close the gap. A future
implementation could choose different questions after interpreting the broad
phrase “understand the artifact,” and two valid-looking V11 runs could measure
different capabilities. Because V11 is required for `Done` (`:283-290`), this
is a blocking specification defect rather than editorial cleanup.

**Owning correction:** define the comprehension outcome once. The smallest
correction is to restore the five observable reader questions to CTW10 and have
V11 reference them. The V11 protocol should derive an answer key from each
source packet and map its factual and comprehension scorers to those questions.
Do not define a second question list in the scenario or future reference.

### P2 — The 168-hour freshness gate has no adequate workload or cost basis

External evidence becomes stale at exactly 168 hours
(`docs/improvement-clear-technical-writing.md:261-275`). That boundary decides
whether V1-V8 and V11 may support a capability claim, so it is a normative
numeric limit. The plan expressly imports the exact-limit contract from
`improvement_avoid_repetition.md` (`:12-16`). That authority requires an
observed or conservative workload, an estimated resource cost, exact/one-over
behavior, and evidence that permits revision
(`evidence-efficient-review/references/specification-review.md:62-75`).

The new record supplies a clear expiry instant and revision trigger, but its
workload basis only asserts that a rollout is expected to finish within a week
and that the suite is “small enough to rerun” (`:271-275`). It does not state the
planned trial volume, human-reader workload, elapsed evaluator effort, model
cost, or other conservative rerun estimate. It also gives no causal reason that
evidence is trustworthy at 167 hours and stale at 168 hours. The exact value is
therefore a convention, not an evidence-backed gate.

**Owning correction:** either make initial capability evidence non-reusable
until measured rollout duration and rerun-cost data support a freshness window,
or supply conservative numerical estimates for the V1-V8 trial volume, V11
reader effort, and complete rerun cost and use them to justify the selected
window. Preserve the existing exact stale boundary and invalidation triggers
only after that basis exists. Do not let an arbitrary calendar value decide
acceptance merely to satisfy the presence of an age field.

## Required specification-cell dispositions

| Cell | Disposition |
|---|---|
| Single normative authority | **Cleared.** CTW1-CTW10 remain the declared package authority. Routing, slice, scenario, and completion text add artifact mappings, implementation work, scoring mechanics, or status effects without creating a contradictory contract. |
| Durable contract boundary | **Cleared.** The prose contracts constrain observable meaning and reader outcomes while allowing equivalent private drafting methods. The package layout is explicitly an implementation proposal. |
| Scenario diagnosability | **Candidate.** V1-V10 name capture/scoring and a failure boundary. V11 cannot be scored consistently until its referenced comprehension questions exist. See Finding 01. |
| Evidence topology | **Cleared.** V9-V10 are repository deterministic checks, V1-V8 are controlled model behavior, V11 is separate human-comprehension evidence, and unthresholded cost remains observational. No external availability failure is promoted to a deterministic failure. |
| External freshness | **Candidate.** Identity, age, invalidation, and status effects are explicit, but the exact age was not selected under the imported limit contract. See Finding 02. |
| Telemetry decision power | **Cleared.** Word count, tokens, latency, reading time, preference, and edit size are observational unless a protocol adds a baseline, method, direction, and threshold (`:277-281`). |
| Exact-limit justification | **Candidate.** The 168-hour normative freshness boundary lacks a conservative resource estimate and evidence-based threshold rationale. See Finding 02. |
| Workflow boundary | **Cleared.** The feature plan requires independent review and names its owner without copying Tick/Tock numbering, commit policy, reviewer selection, or repetition mechanics. |

## Unknowns

None. The prior findings, invalidated CTW2/CTW4/CTW8-CTW10 cells, changed
scenarios, adjacent prose authority, and six consumer ownership boundaries were
inspected. The two confirmed findings replace the remaining candidates; no
required review work is merely unknown.

## Architectural scope and follow-up disposition

No AF1 architectural-scope decision is required. Both findings are bounded
corrections to CTW10 evidence design. They do not change the proposed skill's
semantic owner, dependency direction, public compatibility surface, or the six
consumer responsibilities.

Follow-up deltas:

- created: none;
- updated: none;
- closed: none;
- stale: none; and
- unchanged-but-relevant: none.

No current finding was relabeled as a follow-up.

## Evidence status

All revision-dependent source evidence in this review was collected against
exact revision `f1d21cf3306fcabd23a95979acd9fd2874c2bd65` before this review
artifact was created.

- **Deterministic specification evidence:** `HEAD` matched the reviewed
  revision, `git show --check` passed, both composed relative links resolved,
  and the changed routing/evidence cells were inspected against their owners.
  The future skill package and V9-V10 do not exist and were not run.
- **Controlled model behavior:** V1-V8 are future implementation trials. No
  current or reusable run exists, so model behavior is
  `capability-unconfirmed`; this is not a product failure.
- **Human comprehension:** V11 is a future pilot and was not run. Human
  comprehension improvement is `capability-unconfirmed`; this is not a product
  failure.
- **Observational telemetry:** none was collected for this specification Tick,
  and no unthresholded measurement affected the decision.

## Fixed-point result

- specification `deterministic-fixed-point`: **not reached**
- controlled model behavior: **capability-unconfirmed**
- human comprehension improvement: **capability-unconfirmed**
- future package `Done`: **not reached**

Findings 01 and 02 require bounded CTW10 remediation. A fresh independent Tick
must review the corrected specification before deterministic fixed point can be
claimed. Future model trials and the human pilot remain capability work; this
review does not present them as executed.

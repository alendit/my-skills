# Improvement Right Feedback — Review 01

## Decision

**Changes requested** on revision
`d21bfcc90ab3a2b144478cf1ee0f7206f87f9db3`.

This fresh rebaseline Tick found one P2 defect. AF2–AF7 are cleared, but the
independent-review trigger does not fully implement AF1 and AF8, so G1 and G9
do not clear and the package has not reached deterministic fixed point.

Reviewed scope:

- `docs/improvement-right-feedback.md` composed with
  `docs/improvement_avoid_repetition.md`;
- `supervised-implementer-loop`, `review-fixpoint`,
  `evidence-efficient-review`, and `add-architectural-guidances`;
- the explicit not-applicable consumers `project-architecture-doc` and
  `technical-note-series`; and
- the Feature 88 `addendum2.org` motivating fixture.

## Prior findings

None. This is the first numbered review for this package.

## AF1–AF8 coverage

| Row | Status | Evidence |
|---|---|---|
| AF1 Causal signal qualification | **Candidate; G1 failed** | The shared authority requires causal owner, dependency, state, or test evidence and rejects file count, effort, inherent composition, and difficult test editing as proof (`architectural-scope-decision.md:18-43`). `review-fixpoint` routes signals exposed during either remediation or review (`SKILL.md:83-103`). However, the independent review skill loads this authority only when the reviewed work already claims impact or deferral (`evidence-efficient-review/SKILL.md:163-175`), leaving a missing or misclassified Tock record outside the mandatory AF1 path. See Finding 01. |
| AF2 Smallest proper correction | **Cleared; G2 passed** | The shared bound follows owners, representative consumers, stable contracts, dependencies, state and cleanup, compatibility, evidence, documentation, and obsolete-path removal; it rejects both current-diff bounding and full-system redesign (`architectural-scope-decision.md:45-64`). Tick independently audits the bound. |
| AF3 Correct now | **Cleared; G3 passed** | A bounded correction that fits caller-approved scope updates the one owning contract, reclassifies tests, corrects the owner, removes the obsolete path, and resumes; non-locality is not a deferral reason (`architectural-scope-decision.md:66-80`). |
| AF4 Non-worsening deferral | **Cleared; G4 and G5 passed** | Safe deferral requires current-contract satisfaction, all nine dimensions to be evidenced as improved, unchanged, or reasoned not-applicable, and an authorized durable follow-up. Any worsened dimension routes to reevaluation (`architectural-scope-decision.md:88-106`). Slice acceptance and Tick both require durable read-back rather than a proposed record. |
| AF5 Reevaluate or stop | **Cleared; G6 passed** | Worsening ordinary containment is rejected. The intermediate correction must prevent new reliance on the defect and not raise later removal cost; otherwise production changes stop for explicit scope authority (`architectural-scope-decision.md:70-86`). Neither implementer nor Tick may self-authorize expansion. |
| AF6 Durable ledger | **Cleared; G7 passed** | One existing project ledger owns ledger-issued IDs. Semantic dedupe identity, record fields, create/update/dedupe/close/stale/supersede lifecycle, activation, authorization, read-back, and five-way handoff deltas are explicit (`architectural-scope-decision.md:108-160`). Review remains read-only and reports observed deltas only (`evidence-efficient-review/SKILL.md:177-181`). |
| AF7 No finding laundering | **Cleared; G8 passed** | Current violations, P0–P3 defects, required unknowns, worsening corrections, valid external product-contract failures, and activated follow-ups remain gating. The fixed-point rule permits only current-contract-satisfying, non-worsening, durably recorded, unactivated follow-ups (`review-fixpoint/SKILL.md:239-272`). |
| AF8 Responsibility routing | **Candidate; G9 failed through AF1 owner** | Supervision owns branch acceptance and ledger proposals; fixpoint owns Tock/Tick phase use; review is read-only; compact AGENTS guidance contains one short policy rule and one self-check. The two inspected consumers correctly remain non-owners. The under-inclusive review trigger prevents `evidence-efficient-review` from completely performing its AF1 audit responsibility; see Finding 01. |

## Feature 88 scenario composition

The Feature 88 addendum demonstrates why AF1 cannot depend on the remediation
author declaring a signal. Its live older-clean-anchor test composes request
serialization, tool execution, anchor admission, diagnostics, connection
identity, and contamination checks, while the surrounding plan records
connection-ledger and timer mechanisms. That breadth is evidence to inspect,
not proof by line count or editing difficulty.

The shared authority correctly separates the possible dispositions:

- ordinary harness-to-adapter propagation and genuinely end-to-end semantics do
  not qualify by themselves;
- a test that rejects an independently designed correct implementation because
  it freezes private decomposition does qualify;
- the proper bound follows the actual owner and representative composition,
  such as reusable capture infrastructure, rather than expanding to Feature 88
  as a whole;
- a bounded correction is done now, a current-contract-satisfying neutral
  containment can be durably deferred, a worsening shim is reevaluated, and an
  unavailable bounded safe route stops for explicit scope; and
- the 256-entry ledger limits, credentialed evidence, telemetry, and embedded
  workflow mechanics remain governed by the imported R1–R8 authority rather
  than being redefined here.

The composition fails only at independent discovery: if the Feature 88 Tock
does not label the broad test or local patch as architectural, the review skill
does not unconditionally enter the AF1 qualification path.

## Confirmed findings

### P2 — Independent review routes only author-declared architecture signals

AF1 assigns the independent Tick authority to audit architecture-signal
classification, and AF8 assigns `evidence-efficient-review` the AF1 audit
responsibility (`docs/improvement-right-feedback.md:55,62`). This must include
an absent or incorrect Tock classification; otherwise the remediation author
controls whether the independent reviewer applies the new safeguard.

`review-fixpoint` has the correct broad trigger: it routes when remediation
**or review exposes** non-local impact, uncertain ownership,
mechanism-coupled tests, or a local fix that may preserve an architectural
problem (`skills/review-fixpoint/SKILL.md:83-90`). The actual review mechanic is
narrower. It reads the shared authority only when “the reviewed work claims
architectural impact or defers an architectural correction”
(`skills/evidence-efficient-review/SKILL.md:163-170`). A Tock that omits the
record—or incorrectly treats a mechanism-frozen Feature 88 test as mere
friction—therefore avoids the mandatory qualification and correction-bound
audit in a directly invoked review. General seam inspection may notice the
symptom, but it does not supply the required AF1 record, branch, or missing-
evidence classification.

**Owning correction:** in `evidence-efficient-review`, make the routing trigger
symmetrical with the shared authority and `review-fixpoint`: read and apply the
authority when the reviewed work claims or defers architectural impact **or
when the review itself encounters** non-local impact, uncertain ownership,
mechanism-coupled tests, or a local fix that may preserve an architectural
problem. Require an absent decision record to remain a candidate or required
unknown according to the source evidence; do not synthesize a branch or ledger
mutation. This preserves reviewer read-only authority while closing the
author-omission escape hatch. Do not add a second decision table or copy the
ledger schema.

## Specification-cell dispositions

| Cell | Disposition |
|---|---|
| Single normative authority | **Cleared.** AF1–AF8 are the package authority; the shared runtime reference owns the reusable decision detail and consumers link it instead of copying its tables. |
| Durable contract boundary | **Cleared.** The contracts govern decision evidence, ownership, branch eligibility, authorization, and lifecycle rather than prescribing a private software representation. |
| Scenario diagnosability | **Cleared.** Six scenarios isolate cohesive correction, safe containment, worsening shims, unrelated improvements, laundering, and test-locality evidence. |
| Evidence topology | **Cleared.** G1–G9 are deterministic document/behavior fixtures. External capability evidence is not applicable to this skill-package revision. |
| External freshness | **Not applicable.** The Feature 88 endpoint is a motivating fixture; this revision makes no provider-capability claim. |
| Telemetry decision power | **Not applicable.** No measurement is acceptance evidence for this package; imported R4 continues to govern telemetry. |
| Exact-limit justification | **Not applicable.** This package adds no normative numeric resource limit; imported R6 governs the Feature 88 values. |
| Workflow boundary | **Cleared.** The feature addendum remains unchanged, while `review-fixpoint` retains numbering, phase commits, reviewer selection, repetition, and stop mechanics. |

## Architectural decision and follow-up ledger

The reviewed package itself did not require an AF1 decision. Its four changed
skills have distinct responsibilities and their multi-file composition is
intentional owner propagation, not evidence of wrong ownership. No safe
deferral was selected, so AF4 read-back is not applicable.

Relevant follow-up IDs:

- created: none;
- updated: none;
- closed: none;
- stale: none; and
- unchanged-but-relevant: none.

No finding was relabeled as a follow-up. Finding 01 remains a current P2.

## Unknowns

None. Every required AF row and specification cell was either cleared, made not
applicable, or converted to the confirmed finding above.

## Gate evidence

All revision-dependent evidence was collected on exact revision
`d21bfcc90ab3a2b144478cf1ee0f7206f87f9db3`.

- all six in-scope `quick_validate.py` checks passed;
- all directly referenced Markdown targets resolved;
- every skill reference over 100 lines contained `## Contents`;
- AF1–AF8 each have an owner, slice, and named G1–G9 witness;
- the Feature 88 scenario was checked against its current addendum rather than
  inferred from the feedback summary;
- `HEAD` exactly matched the reviewed revision;
- tracked working-tree and index state matched the reviewed revision before
  this review artifact was created; and
- whitespace checks passed for the reviewed package and this artifact.

## Fixed-point result

- `deterministic-fixed-point`: **not reached**
- required external capability: **not applicable**
- `Done`: **not reached**

G1 and G9 remain open through Finding 01. A fresh independent Tick is required
after its owning correction; the current review cannot accept or implement that
remediation.

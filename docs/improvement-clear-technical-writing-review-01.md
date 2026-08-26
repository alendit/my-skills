# Clear Technical Writing Integration — Review 01

## Decision

**Changes requested** on revision
`a4c5f9bf29bc21d4241003b1973746d844891d2c`.

## Current disposition after Tock

The remediation following this historical review addresses all three findings:

| Finding | Current disposition |
|---|---|
| Artifact visibility and nested ownership | Addressed by routing on artifact purpose and factual owner, choosing one prose authority for overlaps, and assigning exactly one invocation to the leaf substantive owner. Outer orchestrators only verify or report that pass. |
| Model behavior called deterministic | Addressed by limiting deterministic gates to package and fixture structure, moving V1-V8 to controlled model evidence with shared capture and scoring, and removing the unobservable private-plan assertion from V4. |
| Human pilot baseline and freshness | The paired baseline and predeclared scoring remain addressed. Review 02 rejected the initial seven-day reuse boundary; the next Tock replaces it with non-reusable initial evidence and requires measured cost and duration before any reuse interval may be proposed. |

These dispositions do not alter the original decision below. A fresh Tick must
verify the remediated revision before any fixed-point claim.

This fresh rebaseline specification Tick found one P1 and two P2 design
defects. The proposed skill has a sound substantive writing contract, bounded
research rationale, adaptive effort, and dependency-aware revision. It does not
yet define an unambiguous trigger boundary with the installed general writing
skill, and its evidence plan treats model-generated behavior as deterministic
while the human pilot cannot isolate or durably reuse an improvement claim.
CTW2, CTW4, CTW8-CTW10 and V1-V11 therefore remain open. The specification has
not reached deterministic fixed point.

Reviewed scope:

- `docs/improvement-clear-technical-writing.md`, composed with
  `docs/improvement_avoid_repetition.md` and
  `docs/improvement-right-feedback.md`;
- the six planned consumers: `technical-note-series`,
  `project-architecture-doc`, `add-architectural-guidances`,
  `evidence-efficient-review`, `review-fixpoint`, and
  `supervised-implementer-loop`;
- the installed general `writing` skill as an adjacent prose authority; and
- the installed `skill-authoring` skill as package-authoring authority.

## Prior findings

None. This is the first numbered review for this package.

## CTW1-CTW10 coverage

| Contract | Status | Evidence |
|---|---|---|
| CTW1 Preserve substantive authority | **Cleared; V1 contract sound** | The row leaves behavior, scope, architecture, findings, severity, evidence status, and workflow with their existing owners and requires uncertain meaning to return to that authority (`improvement-clear-technical-writing.md:66`). The routing table keeps each specialized artifact owner in place (`:82-90`). |
| CTW2 Route reader-facing engineering prose | **Candidate; V2 not decidable** | The direct engineering triggers and specialized-skill-first rule are useful, but `general/public prose` conflicts with both public repository artifacts and the installed writing skill's actual documentation/report scope. The review/fixpoint composition also lacks a one-pass owner. See Finding 01. |
| CTW3 Derive reader and purpose | **Cleared; V3 specified** | The row selects the actual code maintainer or operational recipients where available and uses an uninvolved repository developer only as a fallback (`:68`). This composes with the six consumers' more specific audiences rather than replacing them. |
| CTW4 Adaptive drafting | **Contract cleared; V4 evidence candidate** | Compact, dependent-claim, and difficult-passage effort levels are bounded and the private plan is explicitly non-evidence (`:69`). V4 nevertheless asks acceptance to establish that a private question/evidence plan exists while saying private notes are not observed (`:195`). See Finding 02. |
| CTW5 Explicit terminology and relationships | **Cleared; V5 specified** | The row permits a necessary stable term after an ordinary-language definition and requires hidden actor, operation, condition, and consequence to be expanded (`:70`). It corrects overloaded vocabulary without imposing a categorical terminology ban. |
| CTW6 Claims and measurements | **Cleared; V6 specified** | Source fidelity, comparison base, existing-versus-added evidence, facts versus unknowns, exact contractual values, and decision-sized observational rounding remain distinct (`:71`). No universal precision rule or unsupported performance claim is introduced. |
| CTW7 Structure and deletion | **Cleared; V7 specified** | Structure follows the information relationship, relevance determines retention, and punctuation and voice remain contextual (`:72`). This is compatible with the installed writing skill's medium routing and non-ban treatment of punctuation and passive voice. |
| CTW8 Revalidate later edits | **Contract cleared; V8 evidence candidate** | The dependency invalidation rule reaches claims, transitions, title, summary, conclusion, and evidence and scales the reread to impact (`:73`). This directly addresses the supplied late-patching blind spot. Its live behavioral proof is misclassified under CTW10; see Finding 02. |
| CTW9 One compact authority | **Candidate through CTW2 composition** | The proposed one-level package, short entrypoint, on-demand research, reference TOC rule, and optional-script threshold match `skill-authoring` (`:74,92-114`). The six consumers are instructed to link instead of copying. The adjacent-skill and leaf-versus-orchestrator precedence still needs one exact owner; see Finding 01. |
| CTW10 Prove outputs, not private process | **Candidate; V1-V11 evidence invalid** | The output-facing goal and telemetry separation are correct, but V1-V8 are model-behavior scenarios, not repository-deterministic checks, and the human comparison lacks a causally matched baseline and time-based freshness rule. See Findings 02 and 03. |

## Consumer and authority composition

The six existing skills have legitimate, distinct technical ownership:

- `technical-note-series` owns its experienced-newcomer audience, reader
  journey, examples, series coherence, and publication review;
- `project-architecture-doc` owns the architecture document's structure,
  source-backed component model, and architecture discussion;
- `add-architectural-guidances` owns the compact AGENTS policy contract;
- `evidence-efficient-review` owns finding decisions, severities, coverage, and
  evidence status;
- `review-fixpoint` owns Tick/Tock mechanics and phase completion; and
- `supervised-implementer-loop` owns slice/package handoffs and their accepted
  technical evidence.

CTW1 preserves those boundaries. The planned final prose pass is therefore a
cohesive consumer integration, not a new technical authority. The unresolved
composition is narrower: a public engineering artifact can match both proposed
prose skills, and `evidence-efficient-review` plus its outer
`review-fixpoint` caller can both see the same review artifact as ready for a
final pass. That ambiguity is a trigger/ownership defect, not evidence that the
six-skill integration itself is architecturally misplaced.

## Confirmed findings

### P2 — Artifact visibility and nested consumers do not select one writing authority

CTW2 directly triggers for PR descriptions, design documents, reports, status
updates, and technical explanations, but excludes `general/public prose`
(`docs/improvement-clear-technical-writing.md:67`). The routing table likewise
routes PRs to the new skill and all general/public prose to the installed
writing skill (`:82-90`). Publication visibility cannot decide between those
rules: a PR in a public repository, a public developer design document, or a
public operator report is both reader-facing engineering prose and public
prose.

The adjacent skill does not use the proposed boundary. Its description covers
documentation and long-form reader-facing prose, and its medium routing
explicitly covers specifications, reports, and technical writing
(`/Users/dvorona/.agents/skills/writing/SKILL.md:3,44-50`). The proposed
description repeats the overlap by naming design documents and technical
reports while excluding general public prose
(`docs/improvement-clear-technical-writing.md:116-127`). Saying that precedence
will be clear when both are installed (`:37-40`) does not define the decision.

Nested ownership has a related ambiguity. S4 says each of the six consumers
states when its substantive work is ready for the pass (`:165-170`), while the
artifact table assigns review content to `evidence-efficient-review` and outer
mechanics to `review-fixpoint` without saying which one invokes the single pass
(`:88`). An implementation can therefore apply the new skill twice to one
review artifact or leave both consumers expecting the other to apply it.

**Owning correction:** revise CTW2 and the routing table to route by the
artifact's purpose, audience, and factual owner rather than whether it is
public. Repository engineering artifacts whose claims depend on code, diffs,
tests, or operational evidence use `clear-technical-writing`, even when they
are publicly visible. Editorial, marketing, customer communication, and other
general prose use `writing`. For a genuine overlap, select one prose authority;
do not run both automatically. Also assign the leaf substantive artifact owner
one final pass. An outer orchestrator may require or report that pass but must
not apply a second pass. State how an explicit user request to use both skills
is reconciled without weakening truth or the specialized artifact contract.

### P1 — The deterministic suite cannot prove model-generated writing behavior

CTW10 says deterministic repository gates prove trigger boundaries, source
fidelity, authority preservation, required distinctions, and late-change
behavior (`docs/improvement-clear-technical-writing.md:75`). S5 calls V1-V10
deterministic behavioral fixtures and says source packets plus an observable
reader contract are enough (`:172-177`). The completion section then claims
that this suite can prove the implemented package follows CTW1-CTW10 (`:204-208`).

The proposed package is an instruction skill, not a deterministic text
transformer. Structural checks can prove frontmatter, links, reference shape,
fixture schema, and the absence of copied authority. They cannot prove that a
model preserves severity in V1, chooses the audience in V3, expands overloaded
terminology in V5, or rebuilds affected prose in V8. If V1-V8 invoke a model,
their result depends on the skill revision, model, outer instructions, runtime
configuration, and generated output and is external behavior evidence under the
imported R3 evidence topology, not a deterministic repository gate.

V4 also contradicts CTW4 and CTW10. It requires the multi-claim handoff to
`have ordered reader questions and evidence` but immediately says acceptance
does not observe private notes (`:195`). The output may demonstrate coherent
ordering and supported claims; it cannot prove that a private record existed.
Finally, the V1-V8 rows do not consistently identify a capture/scoring helper
or failure-localization signal, as required by the imported scenario contract.

**Owning correction:** split CTW10 evidence into three lanes.

1. Keep repository-deterministic checks for skill validation, links, reference
   TOCs, package/routing declarations, fixture schema, static example
   invariants, duplication searches, and whitespace.
2. Run V1-V8 as controlled model-behavior evaluations. Record skill revision,
   model and runtime identity, outer prompt, source packet, trial policy,
   output-scoring helper, and the contract boundary to which each failure
   localizes. Evaluate only observable output; replace V4's private-plan claim
   with output ordering, evidence support, and separately reported cost.
3. Preserve the human-comprehension comparison as a separate external lane.

Deterministic fixed point may establish that the package and fixtures implement
the specification, but it must not claim that an unexecuted or externally run
model follows the skill. Apply the imported external-status vocabulary to the
controlled model evaluation and keep unavailable execution distinct from a
valid behavior failure.

### P2 — V11 does not isolate the skill's effect or define reusable evidence age

V11 asks blinded readers to compare baseline and candidate artifacts and
requires no factual regression plus a material comprehension benefit
(`docs/improvement-clear-technical-writing.md:202`). S6 records the skill
revision, model family, source packet, artifact type, evaluator audience, and
result (`:179-186`). The completion rule predeclares sample, scoring, and a
threshold and reuses evidence while the skill contract, prompt shape, model
family, artifact suite, and audience remain applicable (`:210-218`).

Nothing requires the baseline and candidate to use the same source packet,
task instructions, model/runtime configuration, or generation policy with only
the skill context changed. A valid-looking result could therefore measure a
model or prompt change rather than the skill. Blinding the readers to the
process does not correct that confound. The plan also supplies no randomized or
counterbalanced presentation rule, so order and within-reader exposure can
affect the answers. Finally, the imported external-evidence contract requires
identity **and age** rules, but V11 has only identity/applicability conditions;
old evidence can remain reusable indefinitely.

**Owning correction:** define the baseline as the same task, source packet,
outer instructions, model/runtime configuration, and generation policy with
the candidate skill absent (or the exact current production baseline when that
is the product claim). Change only the skill condition. Predeclare artifact
assignment, randomized or counterbalanced order, factual-scoring rules,
comprehension scoring, sample, and decision threshold before candidate results
are examined. Record an explicit maximum evidence age or a justified no-expiry
policy plus invalidation triggers. Report `current`, `reusable`,
`capability-unconfirmed`, or a valid skill-behavior failure without treating
missing evaluators or an inconclusive sample as success or failure.

## Research-source audit

The research rationale stays within the sources inspected for this Tick:

- the reader-expectation article supports known context before dependent new
  information and sentence linkage while warning against rigid guarantees;
- PLANET, PAIR, and Re3 support planning/refinement only in their evaluated
  long-form generation tasks, which the plan explicitly does not generalize to
  short engineering artifacts or current coding agents;
- the discourse and model-criticism papers support separating local fluency
  from high-level coherence, not the proposed workflow;
- the two verbosity papers support separating length or preference from
  correctness, not treating brevity as accuracy;
- the code-review and PR-description studies support orientation, rationale,
  purpose, change explanation, testing evidence, and context-sensitive feedback
  requests; and
- Google and Microsoft style guidance support clear actors and useful
  structure without establishing categorical bans.

No unsupported research inference was found. The future
`research-rationale.md` remains outside the default invocation path and is
correctly described as rationale rather than proof.

## Required specification-cell dispositions

| Cell | Disposition |
|---|---|
| Single normative authority | **Cleared.** CTW1-CTW10 are the single package authority. Routing, slices, scenarios, and completion add their distinct operational or evidence role rather than creating another writing contract. |
| Durable contract boundary | **Cleared.** The rows specify observable prose, authority, evidence, and revision outcomes while allowing equivalent private drafting processes. Sentence-level simulation is optional diagnostic work, not a required representation. |
| Scenario diagnosability | **Candidate.** V1-V8 name useful behaviors but lack consistent scoring/capture helpers and localization, and V4 asks for unobservable private planning. Finding 02 owns the correction. |
| Evidence topology | **Candidate.** Model-generated behavior is incorrectly assigned to the deterministic lane. Controlled model behavior, human comprehension, structural package checks, and observational cost need independent statuses. See Finding 02. |
| External freshness | **Candidate.** V11 records identity changes but no evidence age or no-expiry justification. The controlled model-behavior lane also needs an identity and reuse rule. See Findings 02 and 03. |
| Telemetry decision power | **Cleared.** Word count, tokens, latency, reading time, preference, and edit size remain observational unless a protocol supplies baseline, method, direction, and threshold (`:220-224`). |
| Exact-limit justification | **Not applicable.** The document adds no normative resource cap or timeout. The 100/200-line package guidance is imported from `skill-authoring` or explicitly advisory, not a product correctness limit. |
| Workflow boundary | **Cleared.** The plan requires an independent review but does not copy review numbering, phase commits, reviewer selection, remediation repetition, or stop mechanics into the feature contract. |

## Unknowns

None. Every CTW row, required specification cell, consumer boundary, adjacent
authority, and cited research group was inspected. The three confirmed findings
replace the open candidates; no required review work remains merely unknown.

## Architectural-scope and follow-up disposition

No AF1 architectural-scope decision is required. The findings are bounded
contract corrections in CTW2 and CTW10: trigger ownership and evidence topology
already belong to the proposed skill package. They do not require a new
dependency, state owner, public compatibility surface, or cross-repository
ledger.

Follow-up deltas:

- created: none;
- updated: none;
- closed: none;
- stale: none; and
- unchanged-but-relevant: none.

No current finding was relabeled as a follow-up.

## Evidence status

All revision-dependent source evidence was collected against exact revision
`a4c5f9bf29bc21d4241003b1973746d844891d2c` before this review artifact was
created.

- **Deterministic gate:** the reviewed revision existed, `HEAD` matched it, the
  specification was the only changed file in its commit, relative plan links
  resolved, and the document had no whitespace error before this artifact was
  added. The proposed V1-V10 suite has not been implemented or run.
- **External compatibility:** no controlled model-behavior evaluation or V11
  human-comprehension pilot exists. Both capabilities are unconfirmed rather
  than passed or failed.
- **Observational telemetry:** none was collected for this specification Tick;
  no unthresholded metric affected the decision.

## Fixed-point result

- `deterministic-fixed-point`: **not reached**
- controlled model behavior: **capability-unconfirmed**
- human comprehension improvement: **capability-unconfirmed**
- `Done`: **not reached**

Findings 01-03 require bounded specification remediation. A fresh independent
Tick must review the corrected authority before fixed point can be claimed.

# Improvement Plan: Contract-Centered Specifications and Fixpoint Reviews

## Purpose

Revise the six specification, implementation, architecture, and documentation
skills in this repository so they preserve the technical decisions of a feature
while producing a shorter, single-authority contract and evidence model. The
triggering case is
`~/projects/elisp/e/docs/feats/88-generational-context-ephemeral-frames/addendum2.org`;
the plan addresses the concrete failure modes visible there rather than treating
the feedback as a generic request to shorten documents.

The contract-and-evidence matrix below is the normative authority for this
package. Later sections organize and validate its rows; they do not restate the
requirements.

## Scope and non-goals

In scope are these six skills:

- `evidence-efficient-review`
- `review-fixpoint`
- `supervised-implementer-loop`
- `add-architectural-guidances`
- `project-architecture-doc`
- `technical-note-series`

The first three are high-impact behavior owners: they shape specifications,
fixed-point artifacts, and implementation evidence. The latter three are
structural and hygiene owners: they keep architecture and teaching documents
from recreating duplicate authorities or workflow prose.

This package does not rewrite the Feature 88 addendum, alter its accepted
semantic decisions, prescribe a universal document template, change the
repository's commit policy, or weaken the requirement for independent review.
It also does not make credentialed provider checks deterministic. It defines
how those checks contribute evidence without blocking unrelated release gates.

## Diagnosis of the reference specification

Line references are to `addendum2.org` as reviewed on 2026-08-26.

| ID | Observed failure mode | Concrete evidence in the addendum |
|---|---|---|
| R1 | Normative requirements have several competing homes. | The 600-second retention and fallback contract appears in **Goal** (lines 34-39), **Decisions** (48-55), **Scope** (72-78), **Semantic and transport protocol** (149-162), **Profile-owned socket retention** (203-220), **Implementation slices** (286-335), **Acceptance criteria** (486-519), **Performance contract/Risks and responses** (550-564, 580-597), and **Architecture self-check** (624-647). |
| R2 | Tests are specified as assertion inventories instead of a small scenario portfolio. | **Slice 1** enumerates sixteen narrow cases (252-269); **Slice 4** places nine distinct assertions in one credentialed scenario (314-324); **Acceptance criteria** enumerates the same mechanisms again (478-526). |
| R3 | Completion evidence is coupled to a credentialed private endpoint. | **Evidence baseline** makes credentialed evidence necessary (111-113), **Slice 4** requires it (314-335), and **Implementation handoff** reports it blocked by absent credentials (447-470) without a freshness or infrastructure-failure policy. |
| R4 | Measurements lack decision thresholds. | **Implementation handoff** records warm bytes and item counts with only a within-scenario warm-less-than-cold relation (390-395); live latency and token fields are requested there (396-404), in **Acceptance criteria** (521-526), and in **Performance contract** (550-555) without a prior baseline, regression allowance, or explicit non-gating label. |
| R5 | Durable semantics and private mechanisms share the normative contract. | **Connection-local response ledger** mandates fields, lookup/order structures, and scalar replacement (164-201), while **Ownership and material entities** mandates their representation (224-232); **Slice 1** and **Acceptance criteria** repeat those choices (243-269, 486-501). |
| R6 | Exact bounds are asserted without workload or cost justification. | The two 256-entry caps and FIFO behavior recur in **Connection-local response ledger** (191-197), **Ownership and material entities** (228), **Slice 1** (247, 261-265), **Acceptance criteria** (494-497), and **Performance contract** (556-560), but no section supplies a workload estimate, memory estimate, or revision trigger. |
| R7 | One live test has too many independent failure causes. | **Slice 4** simultaneously checks provider branching, literal serialization, tool execution, observation replacement, model-visible output, diagnostics, and durable-anchor admission (314-324); **Implementation handoff** adds timer and provider telemetry assertions (396-404), so a failure does not identify the broken contract boundary. |
| R8 | Product specification and development workflow are coupled. | **Fixed-point review protocol** embeds review numbering, Tick/Tock mechanics, remediation, operator status, and stop rules (599-623), even though those mechanics belong to the repository review workflow. |

## Authoritative contract-and-evidence matrix

| ID | Durable outcome | Owning skill(s) | Slice | Concrete skill change | Named validation |
|---|---|---|---|---|---|
| R1 | A specification has exactly one normative contract-and-evidence matrix; decisions, slices, risks, acceptance, and handoff reference contract IDs instead of paraphrasing them. | `evidence-efficient-review`, `review-fixpoint`; hygiene support from `project-architecture-doc` and `technical-note-series` | S2, S3, S5 | Make matrix normalization the first specification-review operation; add duplicate-authority as a required review cell; require Tock to update the owning authority once; require architecture and note artifacts to link to normative IDs rather than reproduce them. | V1 Single-authority fixture |
| R2 | Evidence is organized as a small portfolio of observable scenarios, with reusable capture/assertion helpers; assertion count and current field layout are not themselves coverage. | `evidence-efficient-review`, `supervised-implementer-loop` | S2, S4 | Require each scenario to name its observable invariant, covered contract IDs, capture helper, and localization signal; add helper categories for request shape, diagnostics, connection identity, and contamination; prefer semantic partitions over assertion inventories. | V2 Scenario-portfolio fixture |
| R3 | Deterministic gates and external compatibility evidence have separate status and completion effects; external evidence has a freshness/reuse rule and classified failure outcomes. | `evidence-efficient-review`, `review-fixpoint`, `supervised-implementer-loop` | S2-S4 | Add the evidence taxonomy and freshness record to review contracts, coverage ledgers, slice handoffs, and fixed-point decisions; require external failures to be classified before they can block deterministic acceptance. | V3 External-evidence state table |
| R4 | Every measurement is either a thresholded gate against a named baseline or explicitly observational and non-blocking. | `evidence-efficient-review`, `review-fixpoint`; guidance support from `add-architectural-guidances` | S2, S3, S5 | Add telemetry decision-power as a required review cell; prevent unthresholded telemetry from satisfying or blocking fixed point; require architecture guidance to label measurement role. | V4 Telemetry classification fixture |
| R5 | The durable contract states observable semantics, ownership, lifetime, bounds, and recovery; equivalent private representations remain permitted unless correctness depends on a mechanism. | `evidence-efficient-review`, `supervised-implementer-loop`; hygiene support from `add-architectural-guidances` and `project-architecture-doc` | S2, S4, S5 | Split durable contract from implementation appendix; replace the mandatory per-entity representation chain with a contract-first chain and conditional implementation detail; require mechanism prescriptions to name their correctness dependency. | V5 Alternate-implementation challenge |
| R6 | An exact cap or timeout is normative only with workload basis, estimated resource cost, operational consequence, and evidence that would justify changing it. | `evidence-efficient-review`, `supervised-implementer-loop`, `add-architectural-guidances` | S2, S4, S5 | Add exact-limit justification to review cells, accidental-complexity stops, and architecture guidance; otherwise convert the number to an implementation default in the appendix. | V6 Exact-limit fixture |
| R7 | External endpoint capability and composed product semantics are separate scenarios using shared instrumentation, so failures localize to provider capability or product composition. | `evidence-efficient-review`, `supervised-implementer-loop`, `review-fixpoint` | S2-S4 | Require a minimal endpoint-capability probe and a broader semantic scenario when both are necessary; prohibit a single live witness from being the sole evidence for unrelated contracts; carry independent scenario dispositions into Tick. | V7 Split-live-scenario fixture |
| R8 | Feature artifacts contain feature-specific review targets and evidence links, while general review numbering, commit mechanics, reviewer selection, and stop rules live only in the workflow skill. | `review-fixpoint`; hygiene support from `technical-note-series` and `project-architecture-doc` | S3, S5 | Define the fixed-point artifact boundary; make feature specs reference `review-fixpoint` mechanics; make documentation skills reject embedded workflow copies and link to the repository procedure. | V8 Workflow-boundary fixture |

## Ordered implementation slices

### S1 — Establish this plan

Create this document, verify every diagnosis anchor against the current
addendum, and make the matrix the package authority. No skill behavior changes
in this slice.

### S2 — Make specification review contract-centered

Update `evidence-efficient-review` for R1-R7. Keep the main workflow compact by
moving detailed templates or classification tables into a directly linked
reference when needed. Its coverage ledger must distinguish contract evidence,
external compatibility evidence, and observational telemetry.

### S3 — Make fixed-point status evidence-aware

Update `review-fixpoint` for R1, R3, R4, R7, and R8. Preserve independent Tick
review and phase ownership. A zero-finding Tick may establish the deterministic
fixed point while reporting external compatibility as current, reusable,
unavailable, infrastructure-failed, or product-failed according to the matrix
policy; it must not silently convert missing external evidence into a pass.

### S4 — Shape implementation around scenario contracts

Update `supervised-implementer-loop` for R2, R3, R5, R6, and R7. Slice
assignments must consume contract IDs and produce scenario-level evidence with
shared instrumentation. Keep the persistent-implementer and parent-acceptance
mechanics unchanged.

### S5 — Prevent duplicate authorities in supporting documents

Update `add-architectural-guidances`, `project-architecture-doc`, and
`technical-note-series` for their matrix rows. This is structural/hygiene work:
remove redundant instruction prose where practical, use stable links/anchors,
and move long reusable rubrics out of entrypoints without weakening behavior.
Do not duplicate the review or implementation workflows inside these skills.

### S6 — Validate the package as a composed workflow

Run V1-V8 against the finished skills, audit links and frontmatter, and inspect
the complete diff for new duplicated normative language. The final independent
Tick reviews the package against this matrix, not against remediation claims.

## Evidence policy

Each contract row and scenario records exactly one of these evidence classes:

| Class | Meaning | Acceptance effect | Required record |
|---|---|---|---|
| Deterministic release gate | Controlled, reproducible evidence owned by the repository. | Must pass on the accepted revision. | Command or scenario name, revision, result, and contract IDs. |
| External compatibility evidence | Credentialed provider or environment evidence outside deterministic repository control. | Required for initial capability confirmation when the contract depends on that capability; thereafter reusable only under the freshness rule below. | Endpoint/protocol/model/request-shape identity, evidence date and revision, result, and failure class. |
| Observational telemetry | Measurement without a decision threshold. | Neither establishes nor blocks acceptance. | Metric name, measurement context, and explicit `observational` label. |

External evidence may be reused when its recorded endpoint capability, protocol,
model family, and material request shape still match and its age is within the
feature's stated freshness window. Any mismatch or expired window makes the
evidence unavailable and schedules a refresh; it does not falsify the product
contract. A failed attempt is classified as one of:

- `product-contract-failure`: the provider ran the scenario and contradicted
  the required capability; blocks the dependent contract;
- `authentication-or-configuration-failure`: the scenario could not start;
- `provider-or-infrastructure-failure`: external service or transport health
  prevented a valid observation; or
- `inconclusive-timeout`: the observation did not finish within its declared
  bound.

The latter three leave external evidence unavailable and must remain visible in
handoff, but they do not turn a passing deterministic gate red. A feature that
has never obtained required initial capability evidence remains capability-
unconfirmed even if its deterministic fixed point is otherwise reached.

## Exact-limit justification policy

For R6, an exact limit record contains:

| Field | Question answered |
|---|---|
| Correctness role | What invariant fails if the value changes or disappears? |
| Workload basis | Which observed or conservatively estimated workload must fit? |
| Resource estimate | What memory, CPU, latency, connection, or storage cost does the value bound? |
| Operational consequence | What happens at exact and one-over boundaries? |
| Revision trigger | Which production evidence, benchmark, or workload change justifies revisiting it? |

If correctness does not depend on the number, place it in the implementation
appendix as a tunable private default. Its boundary tests are mechanism evidence,
not the durable feature acceptance contract.

## Fixed-point artifact boundary

Feature specifications own feature semantics, semantic owners, explicit
non-goals, contract IDs, feature-specific evidence, and unresolved external
capability status. They may state that independent review is required and link
to the repository workflow.

`review-fixpoint` owns Tick/Tock selection, numbered review creation, phase
commits, reviewer independence, gate timing, remediation repetition, and the
stop condition. Review artifacts own findings and their current dispositions.
Implementation handoffs own revision-specific commands and results. None of
those mechanics should be copied into a feature's normative contract.

## Scenario-level acceptance

The package is accepted through these composed scenarios:

1. **Specification normalization:** Apply the revised review skill to a compact
   fixture modeled on the addendum. V1, V4, V5, and V6 identify one authority,
   correctly classify telemetry, permit an equivalent private design, and
   reject an unjustified exact cap.
2. **Evidence portfolio design:** Convert a monolithic credentialed fixture into
   a portfolio. V2, V3, and V7 produce deterministic semantic coverage, a
   minimal external capability probe, a composed scenario using shared
   instrumentation, and independently reportable dispositions.
3. **Fixed-point handoff:** Run the revised workflow wording over a hypothetical
   passing deterministic revision with unavailable credentials. V3 and V8
   yield a deterministic fixed-point decision plus explicit capability-
   unconfirmed status, with workflow mechanics absent from the feature spec.
4. **Documentation composition:** Use the three supporting skills on a fixture
   that references the same contracts. V1 and V8 preserve links to the matrix
   and workflow authority without recreating either body.

No acceptance scenario is expanded into a list of implementation assertions in
this plan; the named validation catalog defines what reviewers inspect.

## Named validation catalog

- **V1 Single-authority fixture:** search a generated/reviewed fixture for each
  normative contract and verify one definition plus ID references elsewhere.
- **V2 Scenario-portfolio fixture:** verify each scenario names observable
  behavior, contract IDs, shared capture helpers, and a localization signal.
- **V3 External-evidence state table:** exercise current, stale, unavailable,
  infrastructure-failed, inconclusive, and product-failed evidence states and
  verify their distinct completion effects.
- **V4 Telemetry classification fixture:** verify a thresholded metric can gate,
  an unthresholded metric is labeled observational, and neither is mistaken for
  the other.
- **V5 Alternate-implementation challenge:** verify a simpler implementation
  preserving public semantics can satisfy the durable contract and that a
  required mechanism includes an explicit correctness reason.
- **V6 Exact-limit fixture:** review a justified limit and an arbitrary 256-entry
  limit; keep the first normative and route the second to an implementation
  appendix.
- **V7 Split-live-scenario fixture:** verify endpoint capability and composed
  semantics can fail and report independently while sharing capture helpers.
- **V8 Workflow-boundary fixture:** verify a feature artifact contains targets
  and links but no copied Tick/Tock numbering, commit, reviewer, or stop
  mechanics.

## Validation and handoff

After every slice, run the narrow checks named by its matrix rows. At S6, also
run the repository's available skill audit or structural validation, validate
all relative links, inspect `git diff --check`, and review the complete diff for
contradictory evidence classifications or duplicated authorities.

The implementer handoff for each slice records only changed files, matrix rows
addressed, named validation results, and unresolved concerns. The independent
reviewer records coverage against R1-R8 and the evidence class of each proof.
Completion requires all matrix rows cleared, V1-V8 passing, no unknown required
coverage, and a fresh independent review with no actionable P0-P3 finding.

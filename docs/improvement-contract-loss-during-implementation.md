# Improvement Note: Contract Loss During Implementation

Status: observed workflow failure and candidate interception points. This note
does not select or prescribe skill changes.

## Observation

The first Slice 7.1 implementation reached its independent Tick with a compact,
mostly coherent protocol kernel and passing canonical gates, but it had lost
several already accepted requirements between specification, design,
implementation, and evidence.

Review 98 inspected exact clean revision
`290e554b495e6391eff752574e17951a34f930c4`, using the accepted design revision
`13665a2c18b301127f16774a684c2ab0688d0b2e` as its baseline. It found two P2
functional and architectural defects and two P3 authority or evidence defects:

1. protocol definition reused arbitrary same-namespace Vars and overwrote their
   roots instead of admitting one complete owned generated group;
2. protocol descriptors and generated Vars omitted required canonical identity
   and definition provenance, publishing zero provenance instead;
3. active owner-map, architecture, and evidence text still required a discarded
   global cache representation after the implementation selected descriptor-
   local packed cells; and
4. an exact required negative-authority scenario was replaced by a differently
   named, weaker test whose assertions could not exclude host protocol
   authority.

The independent Tick caught the failure. The improvement opportunity is to
catch these defects before the expensive exact-revision gate and final review,
without adding repeated full reviews during implementation.

## Why This Was Not Primarily Underspecification

The stable semantic requirements were already explicit:

- `S7-PROTOCOL` required canonical name and provenance, complete generated-Var
  ownership, binding admission before mutation, and atomic group publication;
- the owner map required absent, matching-predeclared, same-owned-group, and
  foreign or colliding binding distinctions;
- the 7.1 design called for a narrow protocol-method-group operation rather
  than direct access to Var or publication records; and
- the evidence portfolio named both the stable protocol-group scenario and the
  negative-authority scenario, with assertion-level behavior rather than names
  alone.

Private storage remained deliberately conditional, but the observable owner,
information, transaction, and evidence requirements did not. The implementation
was therefore free to choose compact descriptor and cache storage; it was not
free to omit binding ownership or provenance.

The primary failure was loss of contract traceability during implementation.
Convenient existing operations were treated as sufficient even though they
could not observe group ownership, and a compact descriptor representation was
accepted without accounting for all immutable identity facts. The focused
tests exercised successful definition, redeclaration, rollback, dispatch, and
cache behavior, but did not challenge foreign ownership, cross-protocol reuse,
same-name collision, matching predeclaration, or provenance.

The remaining two findings show related trace failures. A design change did not
invalidate every active authority and evidence row that depended on the old
cache representation, and a required scenario name was treated as replaceable
without proving that the substitute assertions carried the same negative
power.

This is not usefully classified as implementer error alone. The implementer
made unsound local choices, but the package also passed through design
settlement, focused verification, parent acceptance, documentation settlement,
and a canonical gate without those choices being rejected. The workflow
retained the requirements but did not keep them decision-active at each
handoff.

## Candidate Interception Stages

The table identifies where future skill-improvement work should inspect the
workflow. It deliberately does not choose a new artifact, checklist, role, or
gate.

| Stage | Evidence already available | Failure signal that could have been noticed |
| --- | --- | --- |
| Specification review | The owner, immutable information, transaction, and named scenarios were explicit. | No defect for F98.1 or F98.2: this stage had already supplied the required semantics. Treating conditional layout as conditional behavior would have been a downstream misread. |
| Package and checkpoint design | The package map assigned generated-group ownership and provenance to 7.1; the design named a new narrow group-publication seam. | An exit check on the checkpoint could have asked whether the selected calls could distinguish foreign, predeclared, and same-group bindings and could carry real provenance. Ordinary name lookup and root staging plainly could not. |
| Implementer preflight | The implementer had the complete package, current owner operations, and named evidence portfolio. | A contract-to-operation and contract-to-persisted-information comparison would have exposed the missing ownership observation and absent provenance fields before production edits accumulated. |
| Focused scenario design | Collision classes, atomic retry, provenance, and negative host authority were stable observable partitions. | The planned assertions omitted the cases most likely to falsify the shortcut. Comparing scenario claims with assertions would also have rejected the weaker renamed negative test. |
| Implementation handoff | Changed owners, non-mechanical decisions, focused results, and unresolved risks were available for a compact handoff. | A package could not show how the group-ownership and provenance cells were satisfied. Successful rollback and broad checks were adjacent evidence, not proof of those cells. |
| Parent slice acceptance | The parent could inspect concise diffs, symbol and state inventories, forbidden-dependency searches, and a few independently selected probes. | A foreign-Var protocol definition probe exposed F98.1 immediately. A search for zero provenance at generated publication exposed F98.2. A search for the exact required scenario name exposed F98.4. |
| Design-change reconciliation | The descriptor-local cache decision named the superseded global-table mechanism. | Searching all active authorities and evidence rows for the removed capacity, insertion, revision, and reclamation model would have exposed F98.3 before the package gate. |
| Canonical deterministic gate | Formatting, builds, prior regressions, release checks, and the supplied focused tests all passed. | This gate could not prove assertions that did not exist. It correctly established broad preservation, not contract completeness; making it earlier or running it again would not have found the omissions. |
| Independent Tick | The exact clean revision and complete contract baseline were available to an independent reviewer. | Review 98 found all four defects. This stage worked, but only after the package incurred late rework and a canonical-gate cycle. |

The earliest practical detection point differed by finding. F98.1 and F98.2
could have been blocked when the just-in-time design was connected to concrete
owner operations, or by focused negative tests before implementation
acceptance. F98.3 belonged to dependency invalidation when the cache design
changed. F98.4 belonged to assertion-level evidence comparison as soon as the
required scenario was implemented under another name.

## Existing Workflow Surfaces To Examine

Future improvement work should examine the seams already owned by:

- the contract-first package matrix and scenario lifecycle in
  [`supervised-implementer-loop`](../skills/supervised-implementer-loop/references/contract-and-scenario-package.md);
- design-sensitive implementation, handoff, and parent slice acceptance in the
  [`supervised-implementer-loop` entrypoint](../skills/supervised-implementer-loop/SKILL.md);
- assertion-level coverage and implementation-seam challenges in
  [`evidence-efficient-review`](../skills/evidence-efficient-review/references/implementation-review.md); and
- phase selection, exact-revision gates, and final independent review in
  [`review-fixpoint`](../skills/review-fixpoint/SKILL.md).

The question is not simply which skill should gain another instruction. It is
where a normative cell stops being active, what compact evidence would reveal
that loss, and which existing acceptance decision should reject it without
duplicating another role's work.

## Questions For A Later Improvement Design

- What is the smallest trace that keeps each accepted owner, information,
  transaction, and evidence cell connected to concrete implementation and
  assertions?
- When should missing feasibility for a required narrow owner operation block
  implementation rather than become an implementer-local shortcut?
- How should a representation decision invalidate dependent architecture,
  owner-map, specification-evidence, and test claims without forcing broad
  document rewrites?
- Which adversarial partitions should the implementer derive, and which
  high-risk probes should parent acceptance select independently?
- How can a compact handoff expose an unproved contract cell without importing
  full source, test logs, or implementer reasoning into the primary context?
- How should the workflow distinguish a genuinely underspecified contract from
  a specified requirement that the implementation or evidence simply omitted?

## Non-Goals

- This note does not propose exact skill wording, new mandatory artifacts, or a
  new review phase.
- It does not prescribe the Slice 7 remediation or change the target
  repository's architecture.
- It does not assign the failure exclusively to the implementer, parent, spec
  author, or reviewer.
- It does not recommend earlier or repeated canonical gates; the observed gate
  lacked the missing assertions and could not decide these findings.
- It does not weaken reviewer independence. The final Tick remains the
  backstop that established the failure on an exact clean revision.

## Source Evidence

- `clojure-wasm/docs/stage2/review98.md`, especially F98.1-F98.4 and its
  contract ledger;
- `clojure-wasm/docs/stage2/07-user-types-and-protocols.md`, S7-PROTOCOL,
  identity rationale, and the required scenario portfolio;
- `clojure-wasm/docs/stage2/07-user-types-and-protocols-owner-map.md`, the 7.1
  owner map and evidence lifecycle; and
- `clojure-wasm/docs/stage2/07-1-protocol-kernel-design.md`, the selected
  cross-owner operations and checkpoint decisions.

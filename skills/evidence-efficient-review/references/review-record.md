# Review Record

Use the dossier section while collecting evidence, the coverage schema while
reviewing cells, and the result fields at handoff. Include conditional fields
only when they apply; reference existing records rather than creating parallel
requirements. Honor explicit caller budgets while sizing ordinary evidence work
to the actual review.

## Contents

- [Build the dossier](#build-the-dossier)
- [Record coverage](#record-coverage)
- [Verify within the evidence budget](#verify-within-the-evidence-budget)
- [Return the review result](#return-the-review-result)

## Build the dossier

Create one neutral dossier before detailed reasoning. Prefer deterministic,
compact evidence:

- status, history, baseline-to-current diff, and changed symbols;
- outlines of changed owners and adjacent consumers before exact range reads;
- any applicable structural baseline, intended placement, and material
  structural delta for a design-sensitive owner;
- the authoritative contract matrix, architecture ownership, and public entry
  points;
- material `local-only` or `opt-out` status, or for a selected glossary, its
  identity, declared-scope fit, and only the material term-to-semantic-source
  relationships and inherited unresolved candidates;
- prior finding identifiers and dispositions;
- relevant architectural-scope decision records, the selected durable ledger
  authority, and follow-up deltas;
- changed, added, and contract-named tests, classified as contract or mechanism
  evidence; and
- cheap searches for forbidden paths, duplicated authorities, compatibility
  branches, or other target-specific negative constraints.

Use fast search for known terms and an available structural outline tool before
broad file reads. Keep raw gate logs, complete source files, historical review
bodies, and remediation narratives out of the dossier unless a concrete
question requires them.

Keep dossier commands query-sized. Search a patch for filenames, symbols, and
hunk headers instead of loading a large patch body. When changed symbols or
exact ranges are already known, read those ranges directly rather than
outlining an entire large owner. Cap outlines and source reads to the smallest
result that can answer the current question. Batch independent narrow reads
when useful; avoid bundles whose output hides the evidence needed next.

Treat tool output as review cost. Plan compact evidence batches from scope,
known findings, and uncertain dependencies. Call counts and output size are
signals to improve evidence collection, not automatic stopping thresholds.
Continue while additional evidence is needed to complete required coverage.
Honor an explicit caller time/token/call budget; if it prevents completion,
report uncovered cells as unknown and state the budget boundary. Do not reread
every target document when prior review records its contract; reopen changed
authorities and sections needed for a live closure question.

The dossier supplies facts and routing, not the remediation author's suspected
answer. It may include concise implementer-produced inventories, normalized
comparisons, and references to detailed evidence when they efficiently locate
review candidates. Treat those as navigation facts, not as findings or proof
that a contract cell is cleared.

When a glossary is selected, require the independent reviewer to access each
material entry directly rather than receiving the remediation author's
interpretation. Treat that wording as explanatory input, never proof; verify
behavior, ownership, lifetime, and acceptance against their semantic sources.
When an inherited candidate affects reviewed terminology, verify it against its
semantic source without choosing an alias or deciding architecture. Under an
explicit opt-out, carry only the marker: require no glossary access or placement
question, scope-fit calculation, or candidate transfer, recovery, or reporting;
explain concepts locally when the reader needs them.

## Record coverage

Keep compact external state so later cells do not require reconstructing prior
reasoning. Each cell records:

```text
Contract: <stable identifier and single normative source>
Revision: <reviewed revision>
Dependencies: <owners and consumers actually inspected>
Dimensions: <applicable seams challenged>
Evidence class: deterministic gate | external compatibility |
                observational telemetry | not-applicable
Evidence: <source proof, scenario, focused test, reproducer, or measurement>
Evidence status: <pass/fail; external freshness/failure state; or observational>
Decision role: <what this evidence can establish or block>
Test kind: contract | mechanism | not-applicable
Review classification: current finding | required unknown |
                       non-gating architectural improvement | not-applicable
Economic actionability: <accepted observable violation, comparative decision,
                         required unknown, or not-applicable>
Architectural decision: <record identity and audited branch, or not-applicable>
Follow-up state: <stable ID, durable read-back, lifecycle/activation state,
                  observed delta, or not-applicable>
Status: cleared | candidate | unknown | not-applicable
Next question: <only when unresolved>
```

For external compatibility evidence, record capability identity, freshness
window, evidence age, and reuse decision. For telemetry, record its baseline and
threshold or mark it observational. For a specification, also record the
required dispositions from [specification review](specification-review.md); they are
coverage, not optional commentary.

Use the four coverage statuses defined in the [review process](../SKILL.md#4-review-and-record-each-required-cell).

Use `candidate` while a possible current defect still needs proof. A confirmed
finding is a review result backed by its cell evidence, not a new cleared
status. Use `non-gating architectural improvement` only when the current
contract is cleared and the improvement's causal qualification is evidenced.
That classification does not approve deferral or substitute for an authorized
durable follow-up.

For incremental review, invalidate a cell when its target, owner, relevant
consumer, evidence, or dependency contract changed. Prefer symbol-level impact
when reliable; invalidate the wider owner when extraction or dependency impact
is uncertain.

When the specification changed, record the disposition of affected tests as
`retain`, `strengthen`, `replace`, or `delete`. Treat replacement or deletion of
obsolete mechanism evidence as design correction, not regression. Require
adjacent boundary evidence where applicable: exact/one-over, success/failure,
first/repeated invocation, and clean retry after abort. Repetition must cross a
known or derived failure threshold when the assertion is meant to distinguish
local settlement from end-of-entry cleanup.

## Verify within the evidence budget

Keep temporary diagnostic probes authorized and disposable. Review does not
authorize lasting source changes, whether performed by the primary or a
delegated reviewer.

Run focused checks while proving candidates or clearing high-risk cells. Defer
the complete canonical gate to one meaningful final checkpoint unless the
review contract requires otherwise. Automated checks are evidence; green gates
cannot negate a concrete reproducer or establish unexamined architecture.

Keep successful gate output out of model context: write verbose output to a
temporary log and retain only the command, exit status, concise test counts, and
failure tail when needed. Do not rerun an overlapping complete gate merely to
obtain another presentation of the same evidence.

Run each final gate in the foreground. Keep routine polling inside the executor
or an existing cheaper capable worker and return completion, failure, a material
decision, or agreed milestone/stall evidence. The parent retains acceptance of
the exact revision, command, exit status, and material evidence. In Codex, use
the session hook's extended waiting exception within runtime limits. A live
exec cell does not eliminate model turns: avoid `yield_control()`, `notify()`,
recurring status output, and short outer exec/wait windows merely to report
that a process is running. Preserve user interruption and bound the wait by a
credible stall deadline. Reuse current equivalent gate evidence when its
revision and dependencies match. Additional calls should finish required
verification or diagnose a concrete failure, not reproduce an
already sufficient result. Respect an explicit caller budget without inventing
a separate final-gate call limit.

Record revision-dependent evidence as such. Do not treat counts, identities,
timings, or a clean worktree from another revision as current facts.

## Return the review result

Return or draft the caller's requested artifact with:

- decision, scope, and reviewed revision;
- disposition of every prior finding;
- confirmed findings with severity, proof, actionability evidence, owner, and
  principled fix direction;
- exact proposed wording when the reviewed target is a specification and the
  defect can be corrected locally in prose;
- the authoritative contract-matrix delta and required specification-cell
  dispositions when the target is a specification;
- the selected specification review level with separate contract-cell and
  delivery-plan-cell dispositions;
- coverage ledger or a compact coverage summary;
- architectural-scope classification and observed follow-up-ledger delta,
  including stable IDs, read-back/lifecycle state, and any laundering rejection;
- unresolved unknowns, if any;
- focused and complete verification evidence;
- material `local-only` or `opt-out` status, or for a selected glossary, its
  identity, declared-scope fit, and changed or still-material unresolved
  candidates; and
- the behavioral goal ID and direct scenario status, mechanism progress reported
  separately, and the applicable architecture self-check.

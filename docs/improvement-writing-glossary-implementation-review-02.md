# Clear-Writing And Glossary Implementation — Review 02

## Decision

**Not at deterministic fixed point.** This fresh independent Tick reviewed exact
revision `9759f528232154a1223a050d9e6802b3798bbf17` in **incremental
implementation mode** against Review 01, CTW10/S5, GL8/S5, and the accepted
clear-writing Review 03 and glossary Review 05 specification fixed points.

The four-file remediation adds the missing evaluation package and its single
V10 entrypoint. The exact deterministic command, synthetic self-test, installed
skill read-back, and `git show --check` all pass on the reviewed revision.
Review 01's P1 nevertheless remains incompletely closed. Two capture paths
accept records that do not establish their predeclared external protocols, and
the V10 package gate freezes filenames that CTW9 explicitly makes replaceable.
This review finds two P1 defects and one P2 architectural test-coupling defect.

Reviewed delta from parent `d4f70cb7ccebe360e2e454743d6cc4615043927f`
to the target revision:

- added `skills/clear-technical-writing/evals/fixtures.json`;
- added `skills/clear-technical-writing/evals/capture.schema.json`;
- changed `skills/clear-technical-writing/references/validation-scenarios.md`;
- added `skills/clear-technical-writing/scripts/validate_evidence.py`.

The unrelated untracked `docs/improvement-better-sequencing.md` was excluded and
left unchanged.

## Review 01 P1 Disposition

**Incomplete closure.** The original absence is substantially corrected:

| Required boundary | Current proof | Disposition |
|---|---|---|
| V1-V8 and M1-M8 source packets | `fixtures.json` contains exactly V1-V8 and M1-M8, each with artifact intent, reader, source packet, expected outcomes, forbidden regressions, scorer criteria, and a first-failure boundary. Removing M6 in a bounded manifest check is rejected by the exact fixture-ID check at `validate_evidence.py:25-30,265-270`. | Present and runnable. |
| V11 present and absent conditions | `fixtures.json:709-812` defines `V11-GLOSSARY-PRESENT` and `V11-GLOSSARY-ABSENT`; `validate_evidence.py:372-397` requires both conditions, the five answer fields, no factual regression, no default threshold, and pre-generation commissioning requirements. | Present; commissioning lifecycle is defective under P1-2. |
| Capture identity and lane status | `capture.schema.json:8-81` requires run, skill, model, runtime, outer-instruction, source-hash, settings, context, trial, timestamp, output, score, status, trace, and commissioning fields. `validate_evidence.py:807-937` checks identity, source hash, lane-compatible status, score state, and exact current package hash. | Present. |
| Scorer records and first-failure localization | Fixture criteria name observable fields, contracts, and boundaries. `validate_evidence.py:847-929` requires ordered complete decisions for scored records and checks the first false criterion against the reported contract and boundary. The helper correctly does not claim to judge natural-language quality (`validation-scenarios.md:58-65`). | Present; structured M7/M8 consistency is defective under P1-1. |
| One V10 entrypoint | The executable `scripts/validate_evidence.py` owns `validate-package`, `prepare-capture`, `validate-capture`, and `self-test`. `validation-scenarios.md:46-65` publishes one deterministic command. | Present and runnable. |

The prior finding required not only files but a sound capture and scoring
boundary. P1-1 and P1-2 leave that owning correction incomplete.

## Findings

### P1-1 — M7 and M8 captures do not bind actor identity or source access to the declared lifecycle

**Violated contracts:** GL7-GL8 and CTW10, through glossary S5's observable M7
and M8 delegation trace.

**Proof:**

- Glossary S5 requires actor and run identity, glossary source-access events,
  ordered dossier/work-package, assignment, correction, handoff, and final
  output checkpoints (`docs/improvement-glossary.md:136-143`). M7 specifically
  requires a fresh reviewer and that reviewer's direct access to every material
  entry (`:155`); M8 requires distinct parent/implementer continuity and the
  authorization branch (`:156`). Accepted glossary Review 05 cleared G4 on
  exactly those observable properties.
- The M7 fixture records `fresh reviewer distinct from remediation author`, two
  material entries, and `performed-directly-by-fresh-reviewer`
  (`fixtures.json:593-632`). The M8 fixture supplies separate parent and
  implementer roles, material mappings, and candidate/authorized cases
  (`:640-703`).
- `validate_trace` checks only that `actor_id` is non-empty, `run_id` equals the
  capture ID, required event names exist in order, forbidden event names are
  absent, and a selected `source_access.details.entries` value is truthy
  (`validate_evidence.py:746-804`). It never compares the actor with the
  required role or another actor, and it never compares the accessed entries
  with the case's material entries or term mappings.
- Bounded negative checks produced no validation errors after (1) changing all
  M7 source-access actors to `remediation-author` and their entries to
  `["unrelated term"]`, and (2) changing every M8 event actor to `one-actor`.
  Both records retained a complete manually supplied scorecard. These are
  mechanical trace contradictions, not prose judgments.

**Impact:** A structurally invalid M7 or M8 run can be recorded as `current`.
That erases the evidence needed to distinguish direct independent access from
an author's interpretation and a supervised two-actor lifecycle from one actor
self-reporting every checkpoint. A future external run could therefore receive
compatibility credit without proving GL7. No such run occurred in this review,
so current capability status remains unconfirmed rather than failed.

**Owner and correction:** The shared capture validator owns the correction.
Give each M7/M8 trace case the expected actor roles and exact material-access
set, then validate role identity and required distinctness, direct access by the
assigned actor, and exact selected entry or mapping coverage. Cross-check
mechanical authorization and lifecycle facts carried in trace details with the
corresponding scorecard evidence. Preserve manual scoring for natural-language
meaning; do not add exact-prose matching or infer private reasoning.

**History:** Incomplete closure of Review 01's P1 at the capture/scorer boundary.

### P1-2 — V11 can be prepared without the protocol that must precede generation

**Violated contract:** CTW10/S5-S6 and V11's pre-generation commissioning
protocol.

**Proof:**

- The accepted CTW authority requires both external protocols to be
  predeclared before candidate outputs are examined
  (`docs/improvement-clear-technical-writing.md:199-205`) and requires the V11
  answer key, scorers, metric direction, numeric threshold, reader sample, and
  presentation method to be recorded before generation (`:231,245-260`). The
  implementation reference repeats that requirement and supplies no default
  threshold (`validation-scenarios.md:118-130`).
- The fixture commissioning requirements correctly set `default_threshold` to
  `null` and name all required pre-generation fields
  (`fixtures.json:743-757,796-810`).
- The capture validator explicitly accepts a `prepared` V11 record when
  `commissioning_protocol` is `null` (`validate_evidence.py:687-700`). The CLI
  also permits direct creation of any status from new arguments rather than
  completing an identified prepared record (`:947-973,1249-1270`). A bounded
  check built `V11-GLOSSARY-PRESENT` in `prepared` state with no commissioning
  object and received no validation errors. The existing self-test rejects a
  missing threshold only after constructing a newly scored record
  (`:1187-1189`); it does not prove a prior commissioned record existed.

**Impact:** The package can begin or directly construct a V11 run without a
durable pre-generation threshold and answer key, then accept a later assertion
that those values were recorded earlier. That permits post-output threshold
selection, the bias the accepted paired protocol exists to prevent. V11 has not
run, so this is an implementation defect in the evidence mechanism, not an
external `product-contract-failure`.

**Owner and correction:** The capture lifecycle owns the correction. Require a
complete commissioning protocol when a V11 record first enters `prepared`, and
make later completion consume that same prepared record while preserving its
trial identity, source hash, `prepared_at`, and commissioning values. Reject
direct scored V11 creation without that predecessor. Add adjacent self-tests
for missing prepared commissioning, altered post-prepare threshold, and a valid
prepare-to-complete transition.

**History:** Incomplete closure of Review 01's P1 at the V11 capture-lifecycle
boundary.

### P2-3 — V10 freezes the proposed reference filenames as a correctness boundary

**Violated contracts:** CTW9's replaceable one-level package layout and CTW10's
stable deterministic evidence boundary.

**Proof:**

- CTW9 states that the listed filenames are an implementation proposal and
  that equivalent one-level references are acceptable
  (`docs/improvement-clear-technical-writing.md:105-120`).
- The new validator makes those exact paths required files and makes their
  exact link destinations and counts part of V10
  (`validate_evidence.py:52-87,502-515,549-557`). A conforming implementation
  that renamed or combined an equivalent one-level reference would fail before
  source review could assess CTW1-CTW10.
- The alternate-prose self-test does not challenge this decomposition. It
  creates the same six hard-coded target names and varies only their headings
  and wording (`validate_evidence.py:1135-1160`). It therefore proves resistance
  to exact prose, not resistance to source-layout coupling.

**Impact:** The deterministic gate rejects a simpler independently designed
conforming package and turns private file decomposition into a durable test
contract. This is the mechanism-coupled-test architecture property identified
by the architecture-scope authority. The current layout itself passes, but the
gate contradicts the accepted substitutability boundary and prevents a
whole-scope fixed-point decision.

**Owner and correction:** V10 package validation owns the correction. Validate
the stable one-level topology, required semantic roles, and rendered link
integrity without hard-coding proposal filenames as product contracts. A
package-owned structural manifest may map replaceable paths to stable roles, or
the gate may discover one-level references and leave semantic ownership to the
required independent D1/D2/V9 review. Retain the exact fixture-ID check so a
missing contract fixture still fails.

**History:** New regression introduced by the Review 01 remediation delta.

## Invalidated And Carried Contract Cells

| Cell | Disposition at `9759f52` | Evidence effect |
|---|---|---|
| CTW1-CTW8 | **Carried cleared.** None of their owners or consumers changed. Their new V1-V8 packets are concrete and structurally valid, but no external trial ran. | Existing implementation conformance remains cleared; model capability remains unconfirmed. |
| CTW9 | **Reopened only at the new V10 test-stability dependency; finding P2-3.** The package and consumer source remain unchanged and Review 01's V9 semantic decision carries. | Exact layout is incorrectly frozen by the new gate. |
| CTW10 | **Not cleared.** All evidence lanes and most capture mechanics now exist, but P1-1, P1-2, and P2-3 remain. | Blocks deterministic fixed point. |
| GL1-GL6 | **Carried cleared.** Their semantic owners and consumers did not change; M1-M6 packets are present. | Controlled behavior remains unexecuted. |
| GL7 | **Consumer implementation carried cleared; M7/M8 evidence dependency reopened and fails under P1-1.** | Direct reviewer access and supervised actor continuity cannot yet be credited from a validated capture. |
| GL8 | **Not cleared.** The shared suite exists, but its M7/M8 capture boundary is unsound. | Blocks deterministic fixed point. |
| D1 | **Carried cleared.** The four-file delta adds no glossary authority or standalone glossary skill. V10 reports zero standalone glossary packages but does not claim semantic clearance. | Independent Review 01 source decision remains valid. |
| D2 | **Carried cleared.** No consumer changed. V10 deliberately reports `requires-independent-source-review`. | Independent Review 01 source decision remains valid. |
| V9 | **Carried cleared.** No consumer or pass owner changed. V10 deliberately reports `requires-independent-source-review`. | Independent Review 01 source decision remains valid. |
| V10 | **Mechanical command passes, contract gate not cleared.** | Green output cannot override P1-1, P1-2, or P2-3. |

## Remediation-Delta Risk Audit

| Risk | Disposition |
|---|---|
| Exact prose, headings, or regexes as semantic proof | **Cleared except for P2-3's path decomposition.** Fixture keys explicitly prohibit target prose and expected headings (`validate_evidence.py:275-277`), and both wording-variant self-tests pass. The long-reference Contents check implements the explicit over-100-line package rule; rendered link parsing checks destinations, not prose meaning. |
| False claim that V10 clears D1, D2, V9, or an external capability | **Cleared.** V10 emits all three semantic gates as `requires-independent-source-review`, reports every external lane unconfirmed, and labels capture preparation/validation as non-aggregating (`validate_evidence.py:593-612,978-1005`). |
| Accepted status vocabulary and fixture-lane compatibility | **Cleared.** The schema defines prepared, current, product failure, lane-specific unconfirmed states, and their failure kinds (`capture.schema.json:30-81`); `compatible_states` and capture validation reject cross-lane states. The self-test covers both wrong-lane directions. |
| V11 threshold supplied only through pre-generation commissioning | **Finding P1-2.** Fixture defaults and scored-state validation are correct; the prepared-to-current lifecycle is not. |
| Complete scorer records without automatic prose judgment | **Cleared.** Every scored criterion must have a decision and observable evidence, current requires all true, product failure requires all decisions and exact first-failure localization, and the documentation disclaims prose judgment. This does not excuse the mechanically checkable M7/M8 inconsistency in P1-1. |
| M7/M8 actor/run identity, access, lifecycle, opt-out, authorization, and private-reasoning exclusion | **Partially cleared; finding P1-1.** Run identity, event order, opt-out forbidden events, authorization-path event presence, and forbidden private keys are checked. Actor role/distinctness and exact material source access are not. |
| Generated output location | **Cleared.** `default_output_path` uses the system temporary directory (`validate_evidence.py:940-944`). A real prepared V1 CLI record was written to `/private/tmp` and validated without adding a repository artifact. |
| Exact revision and installation | **Cleared mechanically.** The exact command reported repository revision `9759f528...`, skill hash `sha256:62bb9703077063390661bda4b37274b20388299d35101c897870f664058943af`, and the installed symlink resolved to `/Users/dvorona/projects/agents/my-skills/skills/clear-technical-writing`; its readable `SKILL.md` matched. `git show --check` passed. |
| Simpler conforming prose passes while a missing contract fixture fails | **Cleared for prose and fixture presence; failed for layout under P2-3.** Both alternate-wording self-tests pass. A bounded manifest check removing M6 fails the exact V1-V8/M1-M8/V11 fixture-set requirement. |

## Deterministic Verification

The repository-owned command ran from its absolute path on the exact reviewed
HEAD:

```text
/Users/dvorona/projects/agents/my-skills/skills/clear-technical-writing/scripts/validate_evidence.py \
  --repo-root /Users/dvorona/projects/agents/my-skills validate-package \
  --installed-skill /Users/dvorona/.agents/skills/clear-technical-writing
```

It exited 0 and reported V10 `pass`, 18 fixtures, 7 successful quick
validations, 34 rendered relative links, 10 long references with Contents, 18
declared structural links, and no standalone glossary skill. The exact
`self-test` command exited 0 with all 16 synthetic cases passing. A prepared V1
capture created and validated through the public CLI also exited 0 and made no
capability claim. `git show --check --oneline --no-renames
9759f528232154a1223a050d9e6802b3798bbf17` exited 0.

These results establish that the entrypoint runs and that its implemented
checks pass. They cannot clear the source-proven counterexamples above.

## Glossary Access And Semantic Sources

Selected glossary: `docs/glossary.md`. No opt-out applies. Only the two entries
material to this incremental review's result vocabulary were read directly;
their wording was used for terminology and not as proof.

| Material entry | Independent semantic source | Disposition |
|---|---|---|
| Deterministic fixed point | `skills/review-fixpoint/SKILL.md:255-276` and `skills/review-fixpoint/references/contract-and-evidence-boundary.md:45-70` | The source requires a fresh zero-finding Tick, all required deterministic cells cleared on the exact revision, no required unknown, and no unresolved product-contract failure or activated follow-up. External capability confirmation remains separate. This review cannot claim the term because three P0-P3 findings remain. |
| Capability unconfirmed | `skills/review-fixpoint/references/contract-and-evidence-boundary.md:53-70` | Missing or unavailable current external evidence is neither confirmation nor product-contract failure and does not itself fail deterministic gates. V1-V8, M1-M8, and V11 therefore remain unconfirmed. |

No glossary entry conflicts with its semantic source, no new term candidate was
introduced, and no glossary write was authorized or performed.

## External Evidence Status

| Lane | Status | Decision effect |
|---|---|---|
| V1-V8 controlled model behavior | `model-capability-unconfirmed` | Fixtures and capture preparation exist, but no generated output was scored. |
| M1-M8 glossary and delegation behavior | `capability-unconfirmed` | Fixtures exist, but no controlled model trial ran; P1-1 must be corrected before a validated M7/M8 record is reliable. |
| V11 blinded human comprehension | `human-comprehension-unconfirmed` | Both glossary conditions exist, but no paired pilot ran; P1-2 must be corrected before commissioning evidence is reliable. |
| Observational telemetry | None collected | No unthresholded measurement affects acceptance. |

No valid external output exists, so no lane has a
`product-contract-failure`. The passing deterministic command does not confirm
model behavior, glossary behavior, or improved human comprehension, and the
package is not `Done`.

## Architecture And Follow-Up Disposition

P1-1 and P1-2 are local defects in the already authorized shared capture owner.
They introduce no new semantic component, public compatibility surface, state
owner, or external dependency.

P2-3 qualifies as a mechanism-coupled-test architecture signal: a correct
alternative one-level decomposition fails because V10 freezes the current file
layout. The proper correction remains bounded to the validator's structural
contract and its alternate-implementation self-test. Because the current
contract is violated, the issue cannot be deferred or relabeled as a non-gating
improvement. No architecture decision or durable follow-up record was supplied;
this Tick reports the current finding and does not choose a remediation branch
or mutate a ledger.

Follow-up deltas: created none; updated none; closed none; stale none;
unchanged-but-relevant none.

## Fixed-Point Result

- implementation `deterministic-fixed-point`: **not reached**;
- Review 01 P1: **incompletely closed**;
- current findings: **two P1 and one P2**;
- required deterministic unknowns: **none; the failures are reproduced current
  defects rather than missing review coverage**;
- V10 command: **mechanically passing but not sufficient to clear CTW10/GL8**;
- external capabilities: **unconfirmed, with no external contract failure**;
- architecture follow-ups: **none**; and
- package `Done`: **not reached**.

The next remediation should stay inside the shared evaluation package: enforce
the M7/M8 trace's declared actors and source access, establish a real V11
prepare-to-complete commissioning lifecycle, and replace exact filename
assertions with stable structural-role validation. A fresh independent Tick is
required afterward.

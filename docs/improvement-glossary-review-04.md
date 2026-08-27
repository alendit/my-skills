# Glossary Integration Review 04

## Decision

**Changes requested: one P2 specification finding, with no additional required
unknowns.** This fresh independent incremental Tick reviews
`docs/improvement-glossary.md` at exact revision
`b51f4104a1e1eb8e84e7fef2b9fee3b238b0a02a` against its composed
`docs/improvement-clear-technical-writing.md` authority and Review 03.

The agent-to-agent extension preserves semantic ownership, leaf-level glossary
resolution, review independence, bounded mutation authority, and the single
clear-writing pass. Its new controlled evidence does not yet prove that
contract: the shared record has no observable delegated trajectory, M7 cannot
show that the fresh reviewer independently read the glossary, and M8 neither
carries explicit opt-out state into the assignment nor preserves GL6's
authorized-new-term branch. The normative GL7 owner is sound, but GL8's named
evidence must be corrected before the specification can return to fixed point.

## Review contract and mode

- **Mode:** incremental specification review from Review 03's accepted baseline
  `bd87c1e47000dd1bb22cb0cdedc3c4330ff08182` to exact revision
  `b51f4104a1e1eb8e84e7fef2b9fee3b238b0a02a`.
- **Impact cone:** GL1-GL8 were re-reviewed because the changed GL7 consumer
  ownership, M7/M8 evidence, and person-or-agent communication boundary affect
  their shared owners or consumers. No GL cell is carried merely because its
  row text is unchanged.
- **Authorities:** GL1-GL8 remain the sole glossary contract; CTW1, CTW2, CTW5,
  CTW8, CTW9, and CTW10 supply substantive-authority, single-pass, terminology,
  revalidation, package, and evidence composition. `review-fixpoint` supplies
  only the Tick evidence boundary and completion vocabulary.
- **Finding policy:** only source-proven P0-P3 contract, authority, evidence, or
  architecture defects are findings. Future unexecuted implementation evidence
  is reported by class, not converted into a specification defect.

## Prior-finding dispositions

| Prior finding | Disposition | Evidence |
|---|---|---|
| G1 placement contract | **Closed and not regressed.** GL2 retains the ordered opt-out, selected-source, selected-absent-path, unresolved-placement, and competing-source branches. Extending its trigger from prose to durable engineering communication does not change consent or acquire write authority. GL5 and M5 still own the non-persistent local-definition result. |
| G2 teaching-vocabulary authority | **Closed and not regressed.** GL7 still assigns project-wide identity, aliases, and concise meaning to the selected glossary while the technical-note series owns introduction order, reader-specific first use, series-only terms, and navigation. S4 and D2 still require coherent removal of the old competing authorities. |
| G3 authorization escape | **Closed at GL6; its agent-evidence composition has a new defect.** GL6 still limits glossary and dependent-prose writes to authorized location and edit scope and reports out-of-scope dependents. GL7 preserves the same three-part meaning/location/edit-scope condition. G4 concerns M8's contradictory scorer, not a reopened authorization escape in the owning rows. |

## Contract coverage

| Contract | Status | Evidence and decision |
|---|---|---|
| GL1 | Cleared | The workflow remains one reference under `clear-technical-writing`. Consumers receive only authority links or state-carry notes at their owning boundaries; CTW9/V9 still require one concise leaf link and D1-D2 reject copied procedure or a second pass. |
| GL2 | Cleared | The leaf owner resolves explicit opt-out, selected source, missing selected path, ambiguous candidates, and unresolved placement before glossary creation. Selection does not extend the task's mutation authority, and recoverable same-project state may cross the outer workflow. |
| GL3 | Cleared | Glossary identity and explanation remain subordinate to code, accepted contracts, architecture authorities, findings, package scope, and evidence. EER must read material entries independently but cannot treat them as review proof; supervised agents receive semantic-source context rather than mechanism authority. |
| GL4 | Cleared | Admission still requires a useful project distinction, aliases retain one concept owner, and entry representation remains replaceable. Agent communication does not create an automatic right or need to persist every newly used term. |
| GL5 | Cleared | Review dossiers, assignments, corrections, and handoffs may use glossary source material while retaining local prerequisite explanations for people or agents. Source preparation and terminology continuity do not introduce a second final prose pass. |
| GL6 | Cleared | Accepted semantic sources establish meaning, and writes require authorized location and scope. Out-of-scope or uncertain changes remain reports. M6 still diagnoses the direct update boundary; G4 requires M8 to preserve it in supervised delegation. |
| GL7 | Finding in named evidence | The normative owner split is coherent: EER resolves state before fresh review delegation and independently verifies semantics; the supervised parent resolves before spawning and carries only relevant terminology context; `review-fixpoint` carries state without another pass. M7/M8 do not yet observably establish all of those outcomes. |
| GL8 | Finding | D1-D2 remain correctly deterministic and CTW V11 remains separate human evidence. M7/M8 are correctly classified as controlled external model evidence, but their capture and scorer definitions are incomplete and M8 contradicts the authorized-write branch. G4 applies. |

## Finding

### G4 — P2 — M7/M8 cannot diagnose delegated continuity and M8 contradicts the authorized-term branch

**Proof.** GL7 requires EER to record the selected glossary or explicit opt-out
in its neutral dossier, use a fresh reviewer who independently reads material
entries, and preserve semantic authority. It separately requires the supervised
parent to put the selected source or opt-out and relevant term-to-semantic-source
relationships into the work package and initial assignment, preserve them in
corrections and handoffs, and report a new term as a candidate only unless its
meaning, location, and edit scope are authorized (`improvement-glossary.md`
line 55).

The shared M1-M8 record instead contains one undifferentiated `output` and no
actor/run identity, source-access event, assignment, correction, or handoff
sequence (lines 136-140). M7 therefore cannot distinguish an independently read
glossary from terms copied into a reviewer brief (line 152). M8 says only that
the parent resolves glossary state and sends relevant mappings; it does not
require the selected source or explicit opt-out to survive into the initial
assignment. It then requires every newly needed term to remain a candidate,
without the GL6/GL7 branch that permits a write when meaning, location, and edit
scope are all authorized, and localizes every lifecycle failure only to the
whole supervised-agent boundary (line 153). CTW's shared record likewise stores
one generated output and explicitly does not infer private activity
(`improvement-clear-technical-writing.md` lines 207-215).

**Impact.** A supervised implementation can lose an explicit opt-out during
delegation, ask another placement question, or attempt persistence while M8
still lacks the checkpoint needed to diagnose that defect. Conversely, a
conforming authorized glossary edit can be scored as a product-contract failure.
A final handoff that happens to use the right words can also conceal drift in an
earlier correction. For reviews, the same final-output-only record cannot
establish the required fresh reviewer's independent source read. The new GL7
communication contract therefore lacks evidence capable of establishing or
localizing its central behavior.

**Owner and exact replacement.** GL8 owns the evidence correction; GL7 should
remain unchanged. Replace the capture paragraph at lines 136-140 with:

> M1-M6 use CTW's shared single-output capture record and output scorer. M7-M8
> use the same model/runtime identity, freshness, failure, and scoring protocol,
> and additionally record an ordered observable delegation trace: actor and run
> identity; glossary-resolution state; glossary source-access events; neutral
> dossier or work package; initial assignment; applicable corrections; slice or
> review handoffs; and final output. The trace records external actions and
> artifacts, not private reasoning. Each checkpoint reports the first failed GL
> contract and the named lifecycle boundary.

Replace M7 with:

> **M7 — Controlled model behavior — Review delegation.** Before a fresh review
> is delegated, the neutral dossier records the selected glossary identity or
> explicit opt-out. The trace identifies the fresh reviewer and, when a glossary
> is selected, records that reviewer's access to each material entry rather than
> a remediation author's interpretation. The resulting findings and correction
> directions use the preferred terms while preserving severity, evidence, and
> semantic-source authority when an entry conflicts. An opt-out triggers no
> placement question or glossary access. A failure localizes to resolution,
> neutral handoff, independent source reading, semantic preservation, or final
> review communication under GL7.

Replace M8 with:

> **M8 — Controlled model behavior — Supervised delegation.** Before spawning
> the implementer, the parent resolves glossary state. The work package and
> initial assignment carry the selected source or explicit opt-out and only the
> material term-to-semantic-source relationships. Recorded corrections and
> handoffs preserve those meanings. Under an opt-out, no later placement
> question, glossary access, or persisted term occurs. A newly needed term is
> reported as a candidate when its meaning, location, or edit scope is not
> authorized; when all three are authorized, GL6 governs the bounded write. No
> glossary label creates a field, state, limit, or component. Each failure
> localizes to work-package resolution, assignment transfer, correction
> continuity, handoff continuity, authorization, or mechanism invention under
> GL7.

Keep both scenarios in CTW's existing external compatibility lane. The added
trace is observable instrumentation, not a new evidence class or a capture of
private reasoning.

## Required specification cells

| Cell | Status | Disposition |
|---|---|---|
| Single normative authority | Finding | GL7 and GL6 condition new-term persistence on meaning, location, and edit-scope authority, but M8 currently makes candidate-only handling unconditional. G4 restores GL7/GL6 as the sole owner. |
| Durable contract boundary | Cleared | Selected source or opt-out, terminology/semantic-source separation, continuity across delegation, bounded writes, and no mechanism invention are observable outcomes. The proposed trace is evidence instrumentation, not a prescribed production representation. |
| Scenario diagnosability | Finding | M7/M8 currently collapse several delegated boundaries into a single output and whole-boundary failure. G4 supplies ordered observable checkpoints and first-failed-boundary localization. |
| Evidence topology | Finding | The evidence classes remain separate, but the current single-output capture cannot establish the multi-actor lifecycle claimed by M7/M8. G4 extends CTW's controlled lane rather than promoting the behavior to a deterministic gate or creating a second suite. |
| External freshness | Cleared for specification | GL8 inherits CTW10's exact identity, event-bounded initial non-reuse, failure classes, and future interval-justification rule. The added run/actor identity becomes part of M7/M8's material request identity. |
| Telemetry decision power | Cleared | Entry counts, glossary size, lookup time, prompt tokens, prose length, and edit size remain observational until a protocol supplies a baseline and threshold. |
| Exact-limit justification | Not applicable | The delta introduces no normative count, timeout, retry, size, or calendar freshness limit. “Relevant” and “material” describe semantic selection, not numeric caps. |
| Workflow boundary | Cleared | The feature plan names leaf communication targets and evidence, but leaves reviewer selection policy, Tick/Tock numbering, commits, remediation repetition, and stop mechanics to `review-fixpoint`. Observable agent/run identity proves the scenario; it does not select the reviewer. |

## Single-pass, ownership, and architecture self-check

- CTW1 remains authoritative over substantive preservation: glossary wording
  cannot change findings, severity, evidence, package scope, code semantics, or
  architectural ownership.
- CTW2 remains the sole final-prose owner. Glossary resolution, independent
  source reading, and terminology-continuity checks prepare or verify source
  state; the leaf review or handoff artifact receives one clear-writing pass.
  `review-fixpoint` only carries and reports that state.
- The proposed consumer updates attach to existing owners: review contract,
  neutral dossier, and structured result for EER; work package, assignment,
  slice loop, and package handoff for supervised implementation. They neither
  add a glossary reviewer nor move acceptance authority to an agent or glossary.
- No standalone glossary skill, private glossary data structure, compatibility
  path, silent default location, automatic repository mutation, copied outer
  workflow, or justified architectural follow-up is introduced.

## Evidence status

- **Specification-source evidence:** the exact commit changes only
  `docs/improvement-glossary.md`. All changed GL rows, routing entries, slices,
  scenarios, and completion text were read against the complete material CTW
  authority, Review 03, and the current EER, supervised-loop, and fixpoint
  consumer sections.
- **Deterministic revision hygiene:** `git show --check
  b51f4104a1e1eb8e84e7fef2b9fee3b238b0a02a` passes.
- **Review-artifact hygiene:** `git diff --check` passes for the tracked tree.
  Because Review 04 is intentionally untracked, `git diff --no-index --check
  /dev/null docs/improvement-glossary-review-04.md` was also run; it emitted no
  whitespace diagnostics (its exit status 1 denotes the expected content
  difference).
- **Future deterministic implementation evidence:** D1-D2 and applicable CTW
  package gates were not executed. No future consumer or package implementation
  is credited by this specification review.
- **Future external compatibility evidence:** M1-M8 were not executed.
  Glossary-aware model and delegated-agent behavior remains
  `capability-unconfirmed`; no output is classified as passing or as
  `product-contract-failure`.
- **Future human evidence:** the glossary-conditioned CTW V11 pilot was not
  executed. Human comprehension remains `human-comprehension-unconfirmed`.
- **Observational telemetry:** no glossary, prompt, latency, prose, or edit-size
  measurements were collected; all remain non-gating.

## Follow-up and fixed-point result

There is no non-gating architectural follow-up, activated follow-up, or durable
ledger mutation. G4 is a current P2 specification finding and may not be
laundered into a follow-up.

Specification `deterministic-fixed-point` is **not reached** at
`b51f4104a1e1eb8e84e7fef2b9fee3b238b0a02a`. Prior G1-G3 remain closed and
there are no required unknowns, but G4 leaves GL7's named evidence, GL8, and
three required specification cells uncleared. The next revision should correct
the capture and M7/M8 wording, then receive a fresh independent Tick. Future
implementation, model, and human evidence remain separately unexecuted.

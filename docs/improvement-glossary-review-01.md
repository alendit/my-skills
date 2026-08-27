# Glossary Integration Review 01

## Decision

**Changes requested.** This is a fresh rebaseline review of
`docs/improvement-glossary.md` at exact revision
`4597dbf76a11edbf72bdef7440713ff341871ff9`.

The proposal correctly makes glossary support part of the planned
`clear-technical-writing` package, preserves one final prose pass, separates
terminology from semantic truth, and keeps model and human behavior outside
deterministic repository evidence. Three specification defects remain: the
missing-glossary placement rule has two normative formulations and an undefined
trigger, the technical-note integration leaves an existing competing vocabulary
authority intact, and dependent glossary updates can escape the authorized edit
scope.

No previous numbered glossary review exists to disposition. Future package,
model, and human evidence was not executed and is not treated as proof of this
specification.

## Contract coverage

| Contract | Status | Evidence and decision |
|---|---|---|
| GL1 | Cleared | Lines 5-7 and 47 put glossary behavior inside `clear-technical-writing` and prohibit a standalone glossary skill. The consumer design keeps artifact ownership with the existing skills. |
| GL2 | Finding | The matrix, placement protocol, S1, and M1-M2 do not state one exact applicability and precedence rule. Finding G1 applies. |
| GL3 | Cleared | Line 49 makes the glossary authoritative only for term identity and explanation, while code, accepted contracts, architecture authorities, and artifact owners retain semantic truth. M3 tests the conflict direction. |
| GL4 | Cleared | Line 50 limits entries to useful project distinctions, keeps aliases under one concept, and rejects unsupported paragraph and typography requirements. M4 observes that contract. |
| GL5 | Cleared | Line 51 preserves local prerequisite explanations, rejects vocabulary dumps, and defines a non-persistent fallback when glossary creation is declined. It composes with CTW2 and CTW5 rather than adding another pass. |
| GL6 | Finding | The required dependent revalidation is not bounded by the current authorization. Finding G3 applies. |
| GL7 | Finding | The proposed glossary/series split conflicts with the current `technical-note-series` authorities, and S4 does not require all of those authorities to change. Finding G2 applies. |
| GL8 | Cleared | D1-D2 are limited to static package and ownership checks. M1-M7 remain controlled model evidence and glossary cases extend CTW V11 instead of creating a second human-capability claim. Unthresholded counts and costs remain observational. |

## Findings

### G1 — P2 — GL2 has a duplicated and incomplete placement contract

**Proof.** GL2 says to ask whenever no glossary exists and “the user has not
chosen a location” (line 48), although the same row says repository guidance may
own placement. The placement protocol instead asks only when “glossary-aware
work is applicable” (lines 64-66), without defining that condition. It then adds
normative behavior absent from GL2: infer a project-local path after consent,
obtain an exact look-aside path and scope, and avoid writing a project pointer
(lines 67-72). S1 introduces a third trigger formulation, “unrelated writing
tasks for which durable project terminology is not applicable” (lines 119-122).
The matrix therefore is not the sole placement authority, and an implementation
cannot tell whether explicit repository guidance for a missing glossary resolves
placement or whether it must still ask.

**Impact.** The intended user-visible safeguard can be skipped for one reading
of “applicable,” repeated unnecessarily despite explicit repository placement,
or implemented differently by each consumer. It also leaves automatic path
selection governed by non-authoritative prose rather than GL2.

**Owner and replacement direction.** GL2 owns the correction. Replace its
placement outcome with one ordered rule:

> Before glossary-aware durable writing, inspect explicit user instructions and
> repository guidance. Use an existing selected glossary. If no glossary exists
> but either authority selects its location, treat placement as resolved while
> retaining the task's normal write-authorization boundary. If no glossary exists
> and neither authority selects placement, ask whether to create it inside the
> project or at a user-selected look-aside location, and do not create a file or
> persist a term until the user answers. This question applies when the requested
> durable engineering prose would use or establish shared project terminology;
> unrelated work does not trigger it. After a project-local answer, follow an
> established repository path or ask for the exact path; after a look-aside
> answer, obtain the exact location and scope. Never invent either location.

Reduce the placement protocol and S1 to GL2 references plus non-normative
examples. Extend M2 with the missing-file case where explicit repository
guidance already selects a path, so the scorer distinguishes resolved placement
from the required no-instruction question.

### G2 — P1 — GL7 does not actually resolve the teaching-vocabulary authority

**Proof.** GL7 assigns shared project term identity to the glossary and says
`technical-note-series` retains teaching order (line 53). Its routing row narrows
the series to series-specific teaching explanations (line 104). The current
consumer, however, makes the guide the sole authority for “teaching vocabulary”
in `skills/technical-note-series/SKILL.md` lines 39-44 and
`references/research-and-reader-journey.md` lines 118-136. Its coherence check
requires one guide-owned definition for every shared term in
`references/drafting-and-coherence.md` lines 91-96, and its review contract
repeats guide-owned teaching vocabulary in
`references/validation-and-review.md` lines 39-50. S4 requires only concise links
or invocation notes (lines 136-140), and D2 checks each changed consumer rather
than naming these existing authorities. Adding the planned link can therefore
leave both the project glossary and series guide canonical for the same shared
term.

**Impact.** A project-wide definition and a teaching guide can drift while each
claims authority. That is the duplicate teaching-vocabulary authority the
integration is supposed to remove, and it makes later glossary changes under
GL6 unable to identify their real dependents.

**Owner and replacement direction.** GL7 owns the cross-artifact split, while
`technical-note-series` retains pedagogy. State the split explicitly:

> The selected project glossary owns the preferred project-wide term, aliases,
> and concise project meaning. The technical-note guide owns introduction order,
> first-use explanations for its reader, and terms used only within the series.
> It may explain a project term locally for teaching, but links to the glossary
> instead of maintaining a second canonical project definition.

Expand S4 and D2 to require coherent updates to the consumer entrypoint and the
three references cited above. Replace absolute “teaching vocabulary” and
“guide-owned definition per shared term” wording with the split, and make D2
fail when an old canonical shared-term claim remains. Keep M7 focused on the
observable result: the project term has one canonical identity while the note
still introduces it where its reader needs it.

### G3 — P2 — GL6 can require edits outside the authorized documentation scope

**Proof.** GL6 correctly requires authorization for writing the glossary, but
then requires aliases, linked entries, and affected prose to be revalidated
whenever a semantic source or glossary definition changes (line 52). Its owner
cell assigns work to every affected artifact owner without saying how the
current task's edit boundary limits those changes. S3 repeats the broad
revalidation requirement (lines 130-134). M6 distinguishes authorized and
unauthorized glossary writes but does not cover an authorized glossary edit
with out-of-scope dependent artifacts (line 166). CTW8, the composed authority,
instead relies on the calling artifact skill to supply the changed source and
authorized scope.

**Impact.** An authorized glossary edit could be interpreted as authority to
rewrite every known dependent document. The opposite implementation could
silently ignore stale out-of-scope dependents. Neither result provides the
bounded, visible behavior needed for safe maintenance.

**Owner and replacement direction.** Amend GL6 so revalidation applies only to
the glossary and dependent artifacts inside the current authorized scope.
Known dependents outside that scope must be reported with their semantic source
and stale term; they are not edited or silently treated as current. Make S3
carry that boundary, and extend M6 with an authorized glossary update whose
linked dependent is outside scope. The passing output updates in-scope entries
and prose, reports the out-of-scope dependent, and performs no unauthorized
write.

## Required specification cells

| Cell | Status | Disposition |
|---|---|---|
| Single normative authority | Finding | GL2's protocol and S1 add or alter placement behavior outside the authoritative row. G1 supplies the matrix correction and deletion direction. |
| Durable contract boundary | Cleared | The contracts concern observable placement, authority, term use, update boundaries, and consumer composition. Entry format remains replaceable guidance; no unsupported private data representation is required. |
| Scenario diagnosability | Finding | M1-M2 do not cover the complete placement precedence, M6 omits out-of-scope dependents, and M7 does not reject the current competing series authority. G1-G3 define the missing localization cases. |
| Evidence topology | Cleared | Static package evidence, controlled model behavior, paired human comprehension, and observational measurements retain distinct decision roles. |
| External freshness | Cleared for specification | GL8 inherits CTW10's exact identity and event-bounded non-reuse rule. No glossary-specific external capability or freshness rule is invented. Future evidence remains unexecuted. |
| Telemetry decision power | Cleared | Entry count, size, lookup time, tokens, prose length, and edit size are explicitly observational without a baseline and threshold. |
| Exact-limit justification | Not applicable | The specification rejects the original paragraph cap and proposes no normative numeric cap, timeout, or retry count. |
| Workflow boundary | Cleared | The document names its feature-specific fixed-point target and defers review numbering, commits, reviewer selection, repetition, and stop mechanics to `review-fixpoint`. |

## Evidence status

- **Specification-source evidence:** `git show --check 4597dbf76a11edbf72bdef7440713ff341871ff9`
  passed. The reviewed document and
  composed authorities were read at that exact revision.
- **Future deterministic implementation evidence:** D1-D2 and applicable CTW
  package gates were not executed because the glossary integration and planned
  clear-writing package are not implemented by this specification revision.
- **Future model compatibility:** M1-M7 were not executed. Glossary-aware model
  behavior remains `capability-unconfirmed`; no output is classified as a
  product pass or failure.
- **Future human comprehension:** the glossary-conditioned CTW V11 pilot was not
  executed. Human comprehension remains `human-comprehension-unconfirmed`.
- **Observational telemetry:** not collected and non-gating.

## Unknowns and follow-ups

No separate required review unknown remains after the three findings above.
There is no justified non-gating architectural follow-up and no durable
follow-up-ledger mutation to report.

## Specification fixed-point decision

`deterministic-fixed-point` is **not reached** at
`4597dbf76a11edbf72bdef7440713ff341871ff9`. GL2, GL6, and GL7 and the associated
single-authority and scenario-diagnosability cells remain open. A remediation
must correct those owning rows and their scenario mappings before a fresh Tick
can witness a specification fixed point. Future D1-D2, M1-M7, and CTW V11
results remain explicitly unexecuted and cannot establish implementation
completion or `Done`.

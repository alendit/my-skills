# Compact Agent Messages

Use this transport for shared progress-log entries and exceptional direct
messages after the complete initial assignment. It reduces repeated prose while
retaining the facts needed for the next decision. It is not a user-facing
response mode, a contract ledger, or an instruction to compress code,
documentation, commit messages, or final prose.

## Contents

- Send One Decision-Useful Record
- Report Progress
- Request A Decision
- Send A Correction Delta
- Complete The Package
- Evaluate The Prototype

## Send One Decision-Useful Record

In the log, start with a timestamp and author, then the event type and existing
package or scope ID. Put one labeled fact on each following line. Reuse
established IDs instead of restating their
contracts. Preserve commands, error text, paths, revisions, and identifiers
exactly. Point to detailed evidence instead of pasting logs.

Use `-` for a known empty value and `?` for a required fact that remains unknown.
Omit optional fields only when they are inapplicable. Expand into normal prose
when compression would make scope, authority, safety, or the requested decision
ambiguous. Multi-line values are allowed when one line cannot preserve meaning.

The initial assignment remains self-contained. It names this reference and the
events expected for the package; it does not encode the package itself in this
format. Later messages carry only changed facts.

## Report Progress

Append a checkpoint to the shared log only at an agreed milestone or before its
expected time will be missed. Do not directly message the parent for routine
progress:

```text
CHECKPOINT <package-or-scope-id>
state: <investigating|editing|testing|settling>
done: <material completed result>
now: <active command or work>
next: <next decision-useful event>
due: <updated event window>
block: <->
evidence: <pointer|->
acceptance: unaccepted
```

Use `BLOCKED` instead when progress cannot continue efficiently. Append it to
the log, then directly message the parent with the entry pointer and the
specific need:

```text
BLOCKED <package-or-scope-id>
block: <concrete condition>
impact: <work that cannot continue>
need: <smallest parent or external action>
safe-work: <independent work that can continue|->
next: <event after resolution>
due: <window after resolution|?>
evidence: <pointer or exact failure>
acceptance: unaccepted
```

## Request A Decision

Append the decision request to the log, then directly message the parent. Ask
one material question and expose the consequence of delaying it:

```text
DECISION <package-or-scope-id>
need: <parent-owned decision>
why-now: <dependent work or invariant>
recommend: <choice and reason>
alternatives: <material alternatives and tradeoffs|->
safe-work: <independent work that can continue|->
evidence: <pointer>
authority: parent
```

The parent may answer in compact form when the decision is unambiguous. Use
normal prose for destructive actions, security or privacy questions, contract
changes, or any choice whose conditions would be lost in a fragment.

## Send A Correction Delta

The parent sends one consolidated correction record without replaying the
assignment:

```text
CORRECTION <package-or-scope-id>
violates: <contract, invariant, or accepted boundary>
evidence: <source or reproducer pointer>
required: <observable corrected result>
proof: <focused acceptance evidence>
scope-delta: <authorized scope change|->
authority-delta: <commit, publication, or side-effect change|->
```

An absent delta changes nothing. A `scope-delta` or `authority-delta` entry may
only report authority the parent already has; this record cannot create it.

## Complete The Package

Append one `DONE` record to the log before finishing the turn. The final response
points to it and notifies the parent; do not send a duplicate direct message:

```text
DONE <package-or-scope-id>
outcome: <useful behavior now available>
base: <revision>
head: <revision|settled-dirty-tree>
review-range: <base..head|bounded dirty paths>
changed: <paths and owner boundary>
behavior: <interface or behavior change|none>
contracts: <established existing IDs|->
checks: <command => PASS|FAIL with concise counts>
unknowns: <remaining concern|->
evidence: <detailed-evidence pointer|->
commit: <sha|none>
acceptance: parent-pending
```

Add activated formal realization, direct-scenario, mechanism, structural,
external, terminology, or test-disposition deltas after these core fields. Do
not manufacture absent IDs or omit a required unknown to shorten the record.
`DONE` means implementation handoff complete; only the parent can accept it.

## Evaluate The Prototype

Compare each compact record with the expanded message it replaces. Accept the
compact form only when both versions preserve the same event, package identity,
current state, evidence, next action, authority, and acceptance status. Record
word or token reduction as observational evidence; do not assume a fixed saving.

Prefer normal prose when a reader must reconstruct unstated causality, when a
field contains competing interpretations, or when the compact form becomes
longer than a direct explanation. Compression succeeds by removing repeated
context, not by deleting decision-bearing facts.

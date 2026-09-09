# Remediation: semantic edit granularity and control

The parent implements a slice by choosing and integrating specific edits. The
MCP realizes each selected edit. This remediation applies the
[early user feedback](improvement-semantic-edit-granularity-and-control.md) to
the existing skills while preserving summary-based composition and independent
acceptance of the complete slice.

## Decisions and owners

- **Supervised implementation:** the entrypoint makes the parent responsible
  for implementation sequence and integration reasoning. Each request has an
  owner, behavior, constraints, and local completion condition. A complete slice
  specification is background, including in an existing context.
- **Semantic operation contract:** owns the granularity examples and active-edit
  control procedure. Local adaptation and repairs stay within the selected edit;
  necessary expansion returns to the parent. Multiple files can serve one edit;
  no fixed size limit or extra acceptance gate is introduced.
- **Package and continuity references:** retain delivery boundaries and backend
  identity without treating either as permission to complete remaining work.
- **Complex-work and review-fixpoint:** route implementation and corrections
  through parent-selected edits. A review finding may need several edits. The
  existing slice acceptance and outer independent Tick retain their authority.

After each successful result, the parent retains the changed behavior, relevant
interfaces, checks, and unresolved questions as its abstract program state, then
chooses the next edit against remaining obligations. It does not replay patches,
logs, or tests. Independent source and behavior checks occur at slice acceptance.

For example, first add a typed diagnostic operation using an existing text-value
representation. Use that result to choose the next dispatch edit and its required
interface. Do not ask one continuation to finish diagnostics, dispatch, rollback,
rotation, tests, and documentation merely because the context knows the slice.

## Execution control and runtime boundary

The skill checks the installed control surface rather than inventing API names.
Supported steering must report whether and when the bounded correction took
effect. If steering requires stopping, supported cancellation must distinguish
requested cancellation from a stopped writer and preserve partial work, context,
evidence, and exact state. Completion racing cancellation uses the actual result.

Without the needed control, report its absence and use documented status/recovery
after writer settlement. An ended caller wait, `UNKNOWN` state, or busy worktree
does not establish cancellation. Interruption acknowledgment cannot stop a writer;
no second writer or lock bypass is authorized. Recovery is exceptional, not a
routine parent supervision loop.

This change implements skill guidance only. The current server registers
`realize_change`, `operation_status`, `slice_summary`, and
`acknowledge_interruption`; cancellation and steering remain runtime follow-up.
That follow-up must align tool descriptions, backend instructions, examples, and
runtime documentation with the same edit boundary. Its acceptance requires live
tests of cancellation before and after mutation, duplicates, completion races,
and steering applied, rejected, or requiring stop-and-resume, with writer
settlement and state-continuity evidence. Skill validation cannot establish those
runtime capabilities or behavior of an installed plugin snapshot.

## Validation boundary

Validate the modified skill frontmatter and relative references, inspect the
combined guidance for conflicting ownership, and simulate multi-edit composition,
uncertain interruption, control races, and aggregate acceptance. These checks
assess instructions; they do not measure token savings or demonstrate live
cancellation. Runtime and plugin implementation remain outside this commit.

Validation completed: all four affected skill entrypoints passed the skill
validator, local Markdown references resolved, and an independent agent simulated
the four decision paths above without calling a live MCP. That pass exposed an
ambiguous interrupted-request retry sentence; the contract now routes lost
responses through status recovery before any permitted identical resubmission.

The skill commit includes the pending semantic-MCP skill migration on which this
remediation depends. Unrelated runtime and packaging work remains in the worktree.

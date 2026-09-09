# Semantic edit granularity and execution control

## Decision and scope

The parent implements the slice by composing specific semantic edits. The MCP
is the editing tool used in that implementation. Each call should request one
specific edit: perhaps a function, an operation, or a small behavioral change.
The parent retains the implementation sequence and integration reasoning while
working at the level of abstract behavior without directly reading or outputting
the implementation code. The tools must supply the code facts the parent needs.

This records the user's correction during the 2026-09-09 Stage 2 M3 continuation
in `clojure-wasm`. It documents an observed misuse, guidance gaps, and requested
tool capabilities. It does not implement those capabilities, revise the M3
contracts, or claim that the installed skills already enforce this distinction.

The user's clarifications were:

> “this is a semantic editing tool, the scope of the calls should be a single
> specific edit, maybe a function, maybe a small change. Not the whole slice.”

> “Also the slice itself is being implemented by the parent, the tool is for edits”

## What went wrong

The parent resumed `m3-named-types-realize-003` in the preserved MCP context but
asked it to complete the entire remaining M3 package. The instruction included:

> “Return APPLIED only when the entire admitted M3 slice is ready for aggregate
> independent parent acceptance”

That delegated implementation of four contracts, their tests, lifecycle and ABI
integration, and documentation in one call. The request was a short continuation
delta, but its semantic scope was still the whole package. Prompt length and
context reuse did not make it a small edit.

When challenged, the parent initially explained that the skills permit one or
several operations per slice. That was an accurate reading of permissive wording,
but it missed the intended responsibility split. Keeping acceptance at the
whole-slice boundary does not justify handing slice implementation to the tool.

The loaded B-only skill snapshot and callable native MCP passed the startup
checks. This failure therefore occurred after the earlier legacy/B duplication
issue was resolved; plugin isolation alone did not prevent it.

## Intended working sequence

1. The parent establishes the slice's accepted behavior, architecture, and
   acceptance boundary, then chooses the next specific implementation edit.
2. The parent describes that edit's owning component, required behavior,
   constraints, and local acceptance condition. The tool receives enough context
   to realize the edit without taking over the remaining slice.
3. The MCP resolves concrete source details, makes the edit, runs appropriate
   local checks, and repairs local errors within that edit. A contradiction or
   necessary scope expansion returns to the parent for a decision.
4. The MCP returns a compact result describing the changed behavior, relevant
   interfaces, checks, and unresolved questions. The parent uses the result as a
   working premise and chooses the next edit.
5. The parent composes the edits into the slice and independently evaluates
   semantic evidence at the established acceptance boundary. Code inspection
   belongs behind tools or with the independent reviewer; the parent needs
   evidence sufficient to challenge the result without reading the code itself.
   The outer exact-revision gate and independent Tick remain separate.

The intended saving is removal of direct implementation-code processing from
the parent's workflow, including recovery, design questions, and acceptance. It does not transfer slice implementation responsibility.
The parent must retain enough abstract knowledge of the evolving program to
choose and integrate the next edit. Re-reading successful patches, logs, and
tests after every call would defeat this purpose.

An edit may touch several files when they implement the same specific behavior.
No fixed line count, file count, token limit, or one-function rule follows from
this correction. The controlling question is whether the parent selected one
concrete edit or delegated completion of a broader implementation package.
Several edits within one slice do not create extra slice reviews or gates.

For example, “add the typed diagnostic operation for named descriptors using
the existing text-value representation” is a semantic edit. “Finish named types,
dispatch, rollback, rotation, tests, and documentation” delegates a package.
These examples describe granularity, not a new M3 implementation plan.

## Guidance that needs correction

The [original proposal](improvement-semantic-edit-tool.md#calls-slices-and-acceptance)
already distinguishes operations from slices and describes the parent choosing
the next operation. However, “one or several semantic operations” permits the
whole-slice reading without stating the intended default edit granularity.

The [supervised implementation skill](../skills/supervised-implementer-loop/SKILL.md),
its [package reference](../skills/supervised-implementer-loop/references/contract-and-scenario-package.md),
the [complex-work coordinator](../skills/complex-work/SKILL.md), and the
[MCP documentation](semantic-edit-mcp.md) should consistently establish:

- The parent implements and integrates the slice; the MCP realizes individual
  semantic edits selected by the parent.
- A call's scope is one specific change, even when the persistent context
  already contains the complete slice specification.
- Tool-owned iteration means source adaptation and local repair for that edit.
  It does not authorize choosing or completing subsequent slice work.
- Successful operation summaries support the parent's next implementation
  decision. Aggregate acceptance retains its existing independent role.

Examples, tool descriptions, and backend instructions need the same distinction.
Changing only the outer skill would leave conflicting cues in the tool contract.

## Missing semantic inspection surface

The user subsequently clarified:

> “The idea to provide tools for the parent to avoid direct code reading altogether.”

The parent had read targeted source after cancellation and a design blocker,
then described those reads as an exception to the ordinary summary-based loop.
That exception also missed the intended design. Recovery and design questions
must obtain the necessary code facts through tools, rather than cause the
parent to reconstruct concrete implementation details.

The parent needs a semantic inspection capability that answers bounded questions
about existing behavior, interfaces, ownership, state, ordering, and failure
boundaries. It should return compact, source-grounded facts and explicit
uncertainty that the parent can use to choose an edit. It must distinguish
inspection from mutation and preserve independent acceptance: an editing tool's
self-report alone cannot prove correctness. An independent reviewer may inspect
code and provide evidence; the parent retains the decision and can challenge
specific claims through further tool questions.

The observed native MCP inventory has no dedicated semantic inspection tool.
That is a capability gap, not authorization for fallback direct source reads.
The proposed tools should cover parent information needs as well as edits and
execution control. Exact API names, result shapes, and implementation remain
unselected. Source-location references may support traceability without sending
raw code to the parent.

## Missing cancellation and steering

The native tool inventory in this session exposed `realize_change`,
`operation_status`, `slice_summary`, and `acknowledge_interruption`. It exposed
no operation to cancel an active edit or steer it while it was running.

After the user corrected the granularity, the parent terminated the outer
`functions.exec` wait. That did not establish that the backend had stopped:
`operation_status` returned `UNKNOWN` with `mutation: unknown` and
`observed_state: null`. A subsequent `slice_summary` was refused with
`worktree busy: another semantic operation is active`.

The [documented recovery path](semantic-edit-mcp.md#recover-an-interrupted-request)
requires exclusion of a live writer before interruption can be acknowledged.
Acknowledgment is recovery after execution stops; it is not cancellation.
Stopping a caller's wait must not be reported as confirmed backend cancellation.
Request 003 subsequently settled as `FAILED` with partial work preserved and
an exact result-state token. Its result reported incomplete implementation,
not confirmed cancellation. The parent could then resume the same context
with one bounded edit for the reported inline-callable publication defect.
This later recovery does not establish that terminating the outer wait
cancelled the backend.

The tool needs two explicit control capabilities:

- **Cancel an active edit.** Address the request being stopped, deliver the
  cancellation to its backend, and distinguish cancellation requested from
  writer stopped. Once stopped, return a recoverable outcome and exact current
  state. Preserve partial work, context identity, evidence, and writer exclusion;
  do not imply rollback or release the lock while mutation can continue.
- **Steer an active edit.** Deliver a bounded correction to the same execution
  context and report whether and when it took effect. Steering must not start a
  second writer or silently change an immutable request's recorded payload.
  If the backend cannot apply the correction safely in flight, make that outcome
  explicit and use cancellation plus a new bounded request after recovery.

These are required behaviors, not selected API names or a prescribed transport.
Ordinary edits should still return compact results without a supervision loop.
The control surface is needed when the user changes direction or the parent
detects an incorrect edit scope during execution.

## Verification for the follow-up

Demonstrate a parent implementing one slice through multiple specific edits,
choosing each next edit from the prior result without replaying low-level work.
Verify the complete slice separately at acceptance.

For execution control, exercise cancellation before mutation and after partial
mutation, duplicate cancellation, cancellation racing completion, and steering
that is applied, rejected, or requires stop-and-resume. Results must establish
writer settlement, partial-work preservation, state continuity, and no second
writer. A stopped UI wait alone is insufficient evidence.

This incident provides no measured token savings, general latency conclusion,
or M3 completion result. It establishes an incorrect scope choice and a missing
control surface. Existing unrelated work and the installed plugin snapshot are
outside this documentation change.


## Follow-up disposition

The later user clarification makes avoidance of direct code reads advisory,
not a prohibition. The historical observations and quotations above remain the
incident record. Targeted direct reads are permitted when useful; semantic
inspection is the preferred way to keep implementation detail out of the parent
context.

The [runtime remediation](remediation-semantic-edit-runtime-controls.md) implements
semantic inspection and request-specific cancellation. Its steering tool reports
that the CLI backend requires stop-and-resume; it does not claim in-flight delivery.
Source changes do not update an installed plugin snapshot automatically.

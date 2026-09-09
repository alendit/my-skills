---
name: supervised-implementer-loop
description: >-
  Implement a bounded work package by composing specific semantic edits through
  the MCP, with reused context and independent slice acceptance. Use for dependent
  implementation slices where the parent chooses and integrates each edit and
  the tool realizes it. Trust operation summaries between calls; inspect accumulated
  semantic evidence at slice acceptance. Prefer tool-supplied code facts over
  direct implementation reads. Does not own broader review convergence.
---

# Supervised Implementer Loop

Implement the slice by choosing and integrating specific semantic edits, then
independently accept the accumulated result. The parent owns design, scope,
implementation sequence, integration reasoning, and acceptance. The MCP resolves
source details and owns context reuse, local checks, repairs, and execution for
the current edit. A slice is an admitted delivery package; each call requests
one specific change within it. Complete slice context supplies constraints,
not authority for the tool to choose or finish subsequent work.

Use [the semantic operation contract](references/semantic-operation.md) for
calls, result meanings, and recovery. This skill describes the B workflow.
For an explicitly selected A experiment, load the frozen A plugin's complete
skill set instead; do not combine its supervision rules with this workflow.

## Establish The Work Package

Read [contract and scenario package](references/contract-and-scenario-package.md)
and consume the current independently reviewed implementation-plan result and
admitted delivery-package map. Keep stable contract IDs, the behavioral goal,
useful stopping points, and dependency order authoritative. Before production
edits, require applicable capability, information, transaction, scenario, and
design-dependency cells to have a concrete feasible plan. A missing or stale
plan returns to its owning review boundary.

Read user requirements and repository instructions. Obtain facts about design
owners and existing dirty implementation through semantic inspection. Preserve
unrelated edits. Carry the package outcome, non-goals, contract/plan references, material design decisions, applicable
structural profile, and authorization limits into the initial specification.
A tool-call boundary does not invent a slice or split a contract.

Consume [project glossary state](../clear-technical-writing/references/project-glossaries.md).
Under explicit opt-out, carry only that marker. Otherwise carry the selected
source and material term relationships or unresolved candidates once, then
only changes. Technical contracts retain meaning. Do not add glossary work to
each realization call.

For explicit modularization, carry the contract reference's residual-topology
inventory and intended complete responsibility boundaries. Ordinary work uses
only its applicable owner and physical-boundary profile.

## Bind The Realization Context

Confirm the semantic MCP is available for the intended repository and exact
implementer model, reasoning effort, and normal execution mode. Use current
user configuration and applicable preferences; do not silently substitute an
unavailable model or switch to fast execution. Configuration and writable
repository binding belong to the host setup, not portable skill defaults.

Read [implementer continuity](references/implementer-continuity.md) when identity,
recovery, or context lifetime matters. The MCP reuses its backend context;
the parent keeps only its opaque ID and returned state. Do not spawn an
implementation agent, manage its mailbox, or reconstruct its conversation.
If the MCP is unavailable, report the setup failure. Native supervision is an
explicitly selected alternative workflow, not a silent fallback for B.

## Design And Realize A Slice

1. Select the next admitted slice whose prerequisites have been accepted.
   Give the MCP its complete relevant contract/plan references and acceptance
   scenarios once as background. Keep the implementation sequence and evolving
   behavior/interface state with the parent; select the next specific edit.
2. Specify that edit's owner, required behavior, local completion condition,
   and exclusions. Include the interfaces, information flow, ordering,
   transaction/recovery guarantees, abstractions to reuse, and exclusions that
   constrain realization. State permitted freedoms. Concrete imports, fixture
   adaptation, and local compiler repairs stay with the realizer.
3. Call `realize_change` with a new stable request ID. Reuse the returned context
   ID and expected state on subsequent calls. A request may span files that
   implement the same specific behavior. Use the granularity guidance in
   [the semantic operation contract](references/semantic-operation.md#bound-one-edit).
4. On `APPLIED`, rely on the summary to compose the next operation. Avoid routinely
   rereading its patch, source, successful logs, or tests, or rerunning the
   realizer's checks merely to double-check it. Local iteration and detailed evidence remain inside
   the MCP until slice acceptance. Update the parent's abstract program state
   from the changed behavior, interfaces, checks, and unresolved questions;
   choose the next edit from that result and the remaining slice obligations.
5. On `BLOCKED`, resolve the returned semantic question at its owning boundary.
   Prefer semantic inspection for the needed code facts; use a targeted direct
   read when needed. The realizer can challenge a feasible but unnecessarily complex design; it cannot implement a changed
   design before acceptance of that decision. Invalidate affected plan or
   evidence dependencies, then send the accepted delta using the same context.
6. On `FAILED`, recover the recorded operation state under the semantic contract.
   A timeout does not authorize replay or imply unchanged files. Preserve partial
   work and evidence. Do not replace the implementer or issue speculative repair
   calls while another writer may still be active.
7. When the whole slice is ready, request its aggregate `slice_summary` and
   proceed to independent acceptance. Successful internal steps are trusted
   working premises; they are not separately accepted delivery packages.

The parent obtains implementation facts through
[semantic inspection](references/semantic-operation.md#obtain-semantic-facts),
including design questions, recovery, and acceptance, as the preferred workflow.
Avoid routinely reading or emitting implementation code. Direct reads remain
available when needed to resolve a concrete question; keep them targeted. Prefer
applying referenced source-inspection procedures behind tools or through an
independent reviewer. Transport waiting belongs to the tool call;
ordinary parent continuations should not manage status polls or milestones.
When the user changes direction or an active call exceeds its intended scope,
use [active-edit control](references/semantic-operation.md#control-an-active-edit).
Stopping the caller's wait is not evidence that the backend writer stopped.

## Reconcile Design And Scope

Apply [behavioral design trace and rebaseline](../evidence-efficient-review/references/behavioral-design-trace.md)
when literal mechanism choices or cumulative evidence expose a smaller faithful
alternative. The realizer returns evidence and a proposal; the parent accepts
mechanism changes within its authority. Behavioral changes return to the named
product authority. Update the owning decision once and preserve unaffected
accepted evidence.

For non-local impact or qualified architectural concerns, use
[architectural scope decisions](references/architectural-scope-decision.md).
Carry its branch and evidence through semantic feedback and slice acceptance.
Do not infer an architectural defect from effort, file count, or context size.
External follow-up ledger writes retain their separate authorization boundary.

Keep tests tied to behavior and meaningful owner invariants. Use
[economic actionability](../evidence-efficient-review/references/economic-actionability.md)
when defensive requirements would add lasting machinery or mechanism-coupled
tests. Accepted design changes classify affected tests as retained,
strengthened, replaced, or deleted rather than freezing obsolete mechanisms.

## Independently Accept The Slice

At this boundary, evaluate semantic evidence against complete slice contracts.
Select consequential owner boundaries and behavioral questions independently of
the realizer's choices. Have an independent reviewer inspect the resulting code
and assertions and return source-grounded claims, probe outcomes, state identity,
and explicit uncertainty, normally without raw code. Challenge incomplete or contradictory
claims through further bounded tool questions. The parent retains acceptance;
the editing context's self-report alone cannot establish it.

Require current source and assertion evidence for the applicable realization
dimensions; a tool summary alone does not establish independent acceptance.
Verify the direct scenario separately from mechanism progress. For activated
modularization, check cohesive ownership, removal of the extracted responsibility
from the root, material residual-cluster dispositions, and locality evidence.
Resolve applicable architecture decisions and authorized follow-up read-backs.

If a defect remains, send a semantic correction through `realize_change` in the
same context. Identify the evidence, violated invariant, owning boundary,
required behavior, and invalid workaround to avoid. Return the corrected slice
to acceptance with its evidence delta; do not add per-call inspections during
the correction. Carry forward evidence whose dependencies remain valid.

Have tools or the reviewer run required package checks at the meaningful
acceptance checkpoint and return semantic outcomes. Only then
begin the next slice. The MCP never accepts its own work; the parent records
acceptance under the existing package authority. Commit or other external-write
authority is separate. Serialize authorized Git writes outside active realization
and reconcile their resulting state before the next operation.

## Finish The Work Package

Map accepted slices to the complete contract matrix and behavioral goal. Resolve
required unknowns, partial work, and applicable structural and follow-up evidence.
Report verification, remaining limitations, selected glossary state, and pending
authorized actions. Apply one [clear technical writing pass](../clear-technical-writing/SKILL.md)
to the final handoff after substantive acceptance, not to every tool result.

Return an accepted remediation package to its outer workflow. Slice acceptance
does not establish an independent whole-scope Tick or deterministic fixed point;
never reuse the realizer as the sole fixed-point reviewer. Stop at the requested
package rather than inventing adjacent cleanup or broader review work.

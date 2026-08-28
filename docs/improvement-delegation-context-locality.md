# Improvement Plan: Cost-Aware Delegation and Context Locality

## Purpose

Keep detailed implementation work in the cheapest capable execution context
while preserving primary-agent ownership of scope, architecture, acceptance,
authorization, and final integration. This matters when model costs are
asymmetric: a persistent implementer may be effectively free while the primary
agent's context is scarce or expensive.

The objective is not to minimize total reasoning, tool use, or verification.
It is to prevent inexpensive work from being copied into an expensive context
without improving a decision.

## Observed failure

A supervised implementation can delegate the code change but still consume
most of its expensive context in the parent. Common examples are:

- the implementer inspects a large source region, moves it mechanically, and
  validates it, after which the parent streams the complete moved module;
- both implementer and parent run and display the same broad checks;
- small related edits become separate handoff, inspection, test, and acceptance
  cycles even though only their combined owner boundary is meaningful;
- implementer reports reproduce raw command output rather than a compact
  acceptance packet;
- the parent repeatedly reconstructs dependency context already held by a
  persistent implementer; and
- commentary narrates routine execution instead of material decisions,
  corrections, or blockers.

This is a **context-locality failure**. Delegation happened operationally, but
the evidence and working set did not remain with the delegated owner. Total
work may be appropriate while its placement is not.

## Decision

Add cost-aware context locality to mixed-work orchestration and supervised
implementation. When a cheaper persistent implementer is capable of doing the
mechanical work, exhaustive investigation, iteration, and routine verification
should remain there. The primary should consume only the information needed to
make or verify package-level decisions.

Model price alone does not determine authority. The primary still owns package
scope, dependency ordering, architectural decisions, authorization, parent
acceptance, and the integrated handoff. An independent reviewer still performs
independent review where required. Cost-aware delegation changes where work and
evidence are processed; it does not turn implementer self-review into an
independent Tick.

## Detection conditions

Treat context locality as an active concern when all of these conditions hold:

1. A persistent subordinate model is materially cheaper than the primary, or
   the user identifies it as effectively free.
2. That model is capable of inspecting the relevant repository, editing the
   artifact, running the required tools, and retaining package context.
3. A substantial part of the work is mechanical, iterative, or
   evidence-producing rather than a decision reserved for the primary.
4. The parent can accept the work from a bounded evidence packet plus a small
   number of independently selected risk probes.

The following signals indicate that the workflow is violating the concern:

- parent tool output is dominated by complete source files, long diffs, test
  logs, or command listings already examined by the implementer;
- parent and implementer repeat the same check without a distinct independence
  or risk-coverage purpose;
- the parent imports many tokens per accepted decision or correction;
- related mechanical moves are split into acceptance cycles whose individual
  stopping points add little value;
- a persistent implementer receives broad context repeatedly instead of
  delta-only follow-ups;
- large outputs truncate and are then reread in additional ranges;
- implementer findings are explained in prose when a normalized comparison,
  symbol inventory, or machine-readable result would be smaller and stronger;
  or
- routine progress commentary grows with elapsed work despite no new user
  decision, risk, blocker, or result.

These are diagnostic signals, not numeric acceptance thresholds. A large
parent read or repeated check can be justified when it supplies genuinely
independent evidence for a high-risk boundary.

## Exceptions

Do not compress or delegate away information needed for:

- an architectural or semantic decision the primary must make;
- independent review, where relying on the implementer's conclusions would
  defeat independence;
- authorization, destructive-action, security, privacy, or external-side-
  effect decisions;
- exact public behavior whose preservation cannot be established by bounded
  structural evidence and focused witnesses;
- a correction where the implementer's evidence is contradictory,
  incomplete, or implausible; or
- a package whose cheaper implementer lacks the required capability or cannot
  retain the relevant context.

The response to an exception is a targeted primary investigation, not an
automatic replay of the entire implementation process.

## Remediation protocol

### 1. Establish the execution-cost profile

At package establishment, record only the cost facts that affect routing: which
capable persistent implementer is preferred, whether its work is cheap enough
to favor exhaustive offloading, and which independent reviewer is required.
Do not invent provider prices or optimize around an unverified difference.

### 2. Give the implementer the complete package once

Provide the owner map, constraints, ordered dependencies, exclusions, and
acceptance targets in one initial handoff. Reuse the same implementer. Later
messages should contain only changed evidence, corrections, or the next
dependent boundary.

The implementer should own:

- broad source inspection and dependency analysis;
- mechanical edits and iterative corrections;
- normalized before/after comparisons;
- structural and forbidden-dependency searches;
- formatting, compilation, linting, and focused test selection;
- detailed logs and intermediate evidence; and
- drafting implementation-grounded documentation when it belongs to the same
  accepted package.

### 3. Keep detailed evidence local

Store verbose logs, comparison details, symbol inventories, and test output in
a temporary or explicitly authorized evidence artifact. Return a concise
acceptance packet containing:

- changed paths and the resulting owner boundary;
- material behavior or interface changes, or an explicit statement that none
  were intended;
- exceptions from mechanical equivalence;
- checks run with pass/fail status;
- unresolved risks or blockers; and
- the location of detailed evidence when the parent needs to inspect it.

Reports should not paste complete files or successful command logs by default.

### 4. Batch by meaningful acceptance boundary

Group related mechanical edits when their combined owner is the useful
stopping point. Do not create one ceremony per small guard, helper, or file
merely because each can be committed separately. Keep slices separate when a
later slice genuinely depends on parent acceptance of an earlier semantic or
architectural decision.

### 5. Make parent acceptance risk-directed

The parent should inspect the acceptance packet, the changed owner topology,
and the few boundaries where defects would be consequential. Prefer:

- normalized extraction comparisons over rereading moved bodies;
- symbol and visibility inventories over complete-file streaming;
- searches for forbidden dependencies or escaped state;
- concise diff summaries plus narrow changed ranges; and
- focused witnesses chosen independently from the implementer's test list.

The parent should not duplicate routine successful checks solely to demonstrate
activity. Its independent contribution is selecting and evaluating risk, not
replaying cheap execution.

### 6. Verify at package checkpoints

Use cheap focused checks while the package is unstable. Run broad deterministic
checks once the substantive package is assembled, and run expensive canonical
gates only at the exact checkpoint required by the owning workflow. Re-run a
broad gate only when later changes invalidate its evidence.

Run the required independent Tick once the Tock package is committed and clean.
If the Tick finds a defect, return a delta-only correction to the persistent
implementer and revalidate only the invalidated evidence before the next
required exact-revision gate.

### 7. Keep communication decision-dense

Commentary should report material scope decisions, accepted boundaries,
corrections, blockers, and checkpoint results. Omit routine narration that does
not help the user intervene or understand a changed outcome.

## Skill changes

### `complex-work`

- Carry an explicit asymmetric execution-cost profile when the user supplies
  one or current capabilities establish one.
- Route exhaustive mechanical and evidence-producing work to the cheapest
  capable persistent owner.
- Treat parent-context growth without decision value as a replanning signal.
- Aggregate related units at meaningful acceptance boundaries instead of
  multiplying leaf ceremonies.

### `supervised-implementer-loop`

- Add context locality to package setup and require one complete initial
  package handoff followed by delta-only messages.
- Define the compact acceptance-packet shape above.
- Keep verbose evidence with the implementer or in a referenced artifact.
- Replace complete moved-body rereads with normalized comparison and
  risk-directed parent probes when those establish preservation.
- Distinguish required parent acceptance from duplicated execution.

### `evidence-efficient-review`

- Permit an independent reviewer to consume repository state and concise
  factual dossiers without importing implementer conclusions as review
  findings.
- Keep reviewer independence explicit: cheap implementer evidence may locate
  candidates, but it cannot establish the Tick decision.

### `review-fixpoint`

- Preserve one independent Tick after the accepted exact-revision Tock rather
  than repeating review during mechanical implementation.
- Reopen only evidence invalidated by a finding or remediation.

No change is required merely to reduce prose length in
`clear-technical-writing`; the defect occurs earlier, in execution and evidence
placement.

## Validation scenarios

| Scenario | Expected behavior |
|---|---|
| Free persistent implementer extracts several mechanical modules | Implementer performs exhaustive inspection and checks; parent receives a compact packet and probes only high-risk boundaries. |
| Mechanical extraction moves a large function body unchanged | Normalized comparison and symbol/dependency evidence replace complete parent rereading. |
| A small migration changes an observable error contract | Parent investigates that exact boundary and returns a delta-only correction. |
| Several related transaction guards form one owner package | They may be implemented iteratively but are accepted together unless one introduces a dependent semantic decision. |
| Independent Tick is required | Reviewer inspects the exact clean revision independently; implementer self-checks do not substitute for it. |
| Security-sensitive external mutation | Primary retains the complete authorization and risk decision despite model-cost asymmetry. |
| Implementer report is inconsistent with the diff | Parent expands inspection only around the contradiction and invalidates affected evidence. |

## Acceptance

Accept the skill improvement when the affected skills:

- recognize asymmetric model cost without weakening ownership or independence;
- keep exhaustive cheap work and verbose evidence outside the primary context;
- produce a bounded acceptance packet;
- distinguish meaningful batching from dependency-sensitive slicing;
- preserve targeted parent acceptance and exact-revision gates; and
- pass scenarios that distinguish context locality from unsafe trust or
  superficial brevity.

Measure success by reduced expensive-context consumption per material decision,
not by reduced total tool calls, implementer tokens, or validation depth.

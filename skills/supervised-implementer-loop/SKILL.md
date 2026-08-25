---
name: supervised-implementer-loop
description: Implement one non-trivial work package through ordered, dependent slices using one persistent subagent while the main agent independently reviews, corrects, validates, and accepts each slice. Use when the user asks to reuse one implementer, review every implementation slice, make later work rely on accepted earlier fixes, or keep implementation token-efficient. Do not use for review-only work, small direct edits, or genuinely independent parallel packages.
---

# Supervised Implementer Loop

Complete one bounded work package through a repeated implement-review-correct
loop. The main agent is the acceptance authority; one persistent implementer
owns the edits and first-pass validation.

This skill ends when the requested work package is implemented and accepted.
It does not initiate broader reviews, invent adjacent work, or define an outer
project-completion process.

When an outer fixpoint workflow invokes this skill for remediation, return the
accepted package to that orchestrator. Slice-level acceptance proves the Tock
package, not an independent whole-scope Tick; do not reuse the implementer as
the fixed-point reviewer.

## Establish The Work Package

1. Inspect the current tree, user-supplied requirements, repository guidance,
   and existing changes. Begin at the first unmet requirement and preserve
   unrelated user work.
2. State the package outcome, architectural invariants, explicit non-goals,
   required evidence, and authorization or commit boundaries.
3. For every material conceptual entity, state its owner, physical
   representation, lifetime, transaction boundary, public surface, metric
   definition, and named evidence. Mark genuinely inapplicable links rather
   than inventing machinery to fill them.
4. Divide the package into coherent, ordered slices. Each accepted slice must
   leave the project in a useful state and establish invariants on which later
   slices may safely rely.
5. Keep uncertain decisions local and reversible. Ask only when a missing
   choice would materially change behavior, architecture, risk, or scope.

## Select The Implementer

Before spawning an implementer:

1. Consult available memory according to the environment's memory instructions
   for repository-, task-, and user-specific model and reasoning preferences.
   Keep the lookup narrow. Current user instructions override memory.
2. Confirm that the remembered or explicitly requested model is currently
   available and appropriate for the package. Do not silently substitute a
   different model.
3. If model or reasoning selection remains unclear, conflicting, stale, or
   unavailable, explicitly ask the user what configuration to use before
   spawning. Do not guess.
4. Prefer the leanest capable implementation model consistent with the clear
   selection, paired with enough reasoning effort for principled owner-level
   work. A lean model such as Luna with high or maximum reasoning can be an
   effective implementation choice when current availability and remembered or
   explicit preferences support it.
5. Use normal, non-fast execution by default. Enable fast mode only when the
   user explicitly requests fast mode for the current task; never infer it from
   memory, model choice, urgency, or token-economy instructions.

Spawn exactly one implementation subagent and reuse it for every slice and
correction in the package. If that agent becomes unavailable, report the loss
of continuity and ask before replacing it.

## Give The Initial Assignment

Give the implementer enough context once:

- the complete package outcome and ordered slice map;
- the current slice and its acceptance criteria;
- architectural owners, invariants, and dependency direction;
- accepted existing behavior that must not regress;
- explicit non-goals and prohibited plastering fixes;
- expected focused tests, their contract/mechanism classification, and
  reporting format; and
- whether the implementer may commit.

Explicitly instruct the implementer to use tokens economically without
weakening correctness: inspect only relevant owners and adjacent consumers,
avoid repeating supplied context, communicate concise deltas, run focused
checks during iteration, and report only changed files, verification, and
material unresolved concerns.

Use the smallest context fork that still carries the requirements and current
repository state. Do not repopulate the agent's context on later slices.

## Design Tests To Survive Simplification

Classify relevant tests before changing them:

- **Contract tests** protect stable public semantics, ownership, boundedness,
  and recovery. Split a semantic contract into focused partitions, and cover
  adjacent boundaries when applicable: exact/one-over, success/failure,
  first/repeated invocation, and clean retry after abort.
- **Mechanism tests** are temporary evidence for the current implementation and
  may be replaced or deleted when the design simplifies.

Apply the alternate-implementation check: could a simpler independently
designed correct implementation pass this test? If not, do not make it durable
unless the mechanism is an explicit stable contract. Avoid public metrics or
test machinery without an operational consumer.

Before constructing an exact/one-over witness, prove the target boundary is
reachable under every earlier public admission bound. Never raise or bypass an
upstream limit solely to reach a later defensive check. Test the earliest
observable public contract publicly and keep an otherwise unreachable
serializer or ABI ceiling in a disposable owner-local mechanism test. Repeat a
failure/recovery case far enough to distinguish local settlement from cleanup
that occurs only when the outer entry ends.

When the specification or design changes, require the implementer to list
affected tests as `retain`, `strengthen`, `replace`, or `delete`, then make the
corresponding edits. Replacing obsolete mechanism evidence is a design
correction, not a regression. Conformance labels must be accompanied by a
concise assertion-level coverage description; the label alone is not evidence.

## Stop For Spec-Induced Accidental Complexity

Do not implement documentation vocabulary literally when it creates several
owners, limits, public metrics, collision tables, failpoints, or transaction
states without distinct semantics or operational consumers. At that checkpoint:

1. identify the stable public behavior, ownership, boundedness, and recovery
   actually required;
2. propose the smallest cohesive owner that can satisfy them;
3. identify the exact specification wording and tests that must change; and
4. wait for the parent acceptance authority to approve the corrected contract
   before continuing that design-sensitive work.

Treat this as implementation feedback to the specification, not resistance to
the task. Preserve genuinely distinct limits and evidence when they protect
real work or public behavior.

## Run Each Slice

For every slice:

1. Send the slice to the existing implementer. After the initial assignment,
   use follow-up messages containing only new requirements, evidence, and
   corrections.
2. Let the implementer edit and run focused validation. Do not perform
   overlapping writes or Git operations in the shared workspace. Non-mutating
   preparation may continue, but formally review only a completed slice.
3. Require a compact handoff: changed files, behavior established, tests run,
   affected-test dispositions, assertion-level coverage, and any design
   concern. The implementer does not approve its own work.
4. Independently inspect the actual diff, owning code, adjacent consumers,
   tests, error placement, cleanup, state lifetime, documentation impact, and
   unintended compatibility or fallback paths. Do not accept the implementer's
   summary as evidence by itself.
5. When the review finds a defect, send corrective guidance to the same
   implementer. State:
   - the concrete evidence;
   - the violated invariant;
   - the owning boundary and required result;
   - the state or public behavior that must be proved; and
   - any tempting but invalid workaround to avoid.
6. Repeat implementation and parent review until the slice is correct. Do not
   advance because one narrow test passes.
7. Run independent validation proportional to the slice. Checkpoint accepted
   work according to user and repository policy, with all Git writes serialized
   by the main agent unless explicitly delegated.
8. Only then begin the next slice. Treat accepted earlier invariants as stable;
   do not rediscover or restate them unless new evidence challenges them.

## Keep The Loop Economical

- Reuse the same implementer; do not spawn a replacement for ordinary
  corrections or subsequent slices.
- Prefer concise follow-up tasks over full rewritten briefs.
- Read and test the smallest relevant surface during iteration.
- Run focused checks first and defer expensive complete gates to meaningful
  package checkpoints unless risk requires them earlier. When a repository
  requires a clean-revision gate, run it once on the accepted exact checkpoint
  instead of duplicating the same full suite before and after commit.
- Omit routine narration, unchanged-code summaries, generic reassurance, and
  repeated architectural background.
- Preserve required facts, evidence, constraints, and design reasoning before
  trimming explanation.
- Do not interpret token efficiency as permission to skip owner analysis,
  tests, cleanup, documentation, or independent review.
- If an implementer turn appears stalled, first check for an active tool or
  test process and inspect whether the shared diff is still changing. Send one
  concise status request and wait a bounded interval. If there is no active
  work or response, interrupt the turn rather than waiting indefinitely. Review
  any stable edits directly and either finish the narrow package at the parent
  boundary or resume the same implementer with a delta-only correction. Do not
  spawn a replacement merely to recover momentum; ask before replacing a lost
  persistent implementer.

## Accept The Package

After the final slice:

1. Map the resulting tree back to every package requirement.
2. Run the package-level verification required by the repository and the risk
   of the changes.
3. Confirm no partial implementer work, unresolved feedback, overlapping write,
   or unintended dirty state remains.
4. Report the accepted slices, important review corrections, verification,
   commits or pending changes, and any genuine remaining limitation.

Stop when this package is accepted. Do not continue into unrelated cleanup or
a broader review unless the user separately requests it.

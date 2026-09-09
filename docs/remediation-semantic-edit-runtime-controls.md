# Semantic inspection and execution-control remediation

Goal `SEM-CONTROL`: let the parent obtain implementation facts and correct an
active edit without handing over slice ownership or permitting concurrent writers.
The authority is the [user report](improvement-semantic-edit-granularity-and-control.md)
and the subsequent clarification that avoiding direct code reads is advisory.
Project terminology follows [the glossary](glossary.md).

| Contract | Owner and implementation | Evidence |
|---|---|---|
| C1: one selected edit | Backend prompt distinguishes current edit from slice background and returns scope expansion as BLOCKED. | Composition tests and prompt inspection |
| C2: cancellation with truthful settlement | Runtime owns a shielded backend task, one-shot cancellation, subprocess-spawn cleanup, and writer lock through final snapshot/journal. Early cancellation reports when no resumable thread exists. | Before/after mutation, duplicate, caller cancellation during cleanup, completion race, delayed spawn, other-server control |
| C3: change direction | Parent cancels and resumes a new bounded request. No separate steering tool is exposed without an in-flight delivery capability. | Partial-work stop/resume in the same durable thread, immutable edit retry, MCP transport |
| C4: semantic inspection | Fresh read-only backend, structured source references and uncertainty, exclusive state-bound observation. No editing-context reuse or acceptance authority. | Read-only arguments, fresh context, stale state, busy writer, malformed response, mutation detection, MCP transport |

C1–C4 form one runtime delivery package because they share execution lifecycle
and host binding. `runtime.py` owns that lifecycle and journal; `server.py` exposes
the capabilities. No app-server migration, automatic rollback, model replacement,
installed-plugin mutation, or measurement of token savings is included.

Independent implementation-plan review cleared the design after requiring safe
cancellation during subprocess creation and truthful handling of cancellation
before backend thread identity exists. Baseline validation passed 23 tests;
the expanded suite passed 30 tests using controlled subprocesses and real stdio
MCP calls. This demonstrates transport and lifecycle behavior, not live model
semantic correctness or in-flight steering support. Independent delta review and
live compatibility results are recorded below when available.


Final validation: 32 workspace tests passed. Independent delta review found one
inspection cancellation-cleanup gap; the fix and two new regression tests were
independently rechecked, with no remaining findings in the reviewed delta. The
live disposable Codex CLI inspection probe returned source-referenced observations,
inferences, and uncertainty with unchanged repository state. Reproduce it with
`uv run python scripts/smoke_semantic_inspection.py`; this uses local Codex auth
and the runtime's default configured model in a temporary repository.

The runtime commit includes its previously uncommitted base implementation and
Python package prerequisites. Separate plugin/export work remains uncommitted.
The full workspace test count includes those existing export tests; the committed
runtime test module is independently runnable. No installed plugin was refreshed.


Tool-surface review removed `steer_change`: it could only record an undelivered
correction and advise cancellation, adding no execution capability. Six tools
remain: edit, inspect, status, cancel, acknowledge interruption, and summarize a
slice. Status remains read-only; cancellation stops active work; acknowledgment
finalizes interrupted work only after writer exclusion. Keeping these distinct
avoids hiding mutation behind a read-oriented status call. Existing stored control
records are left untouched, but new databases no longer create that unused table.
Descriptions state selection purpose, key inputs, result meaning, and the relevant
scope or recovery boundary. No replacement tool or optional mode was added.

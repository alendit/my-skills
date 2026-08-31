# Improvement Plan: Efficient Subagent Waiting and Interaction

## Outcome

Long-running delegated work should remain event-driven. The parent waits for a
mailbox update with the longest useful bounded timeout, wakes immediately when
the subagent reports, and inspects progress only when a decision, blocker, or
credible stall signal requires it. Routine polling must not repeatedly replay a
large parent context merely to learn that the subagent is still working.

This proposal extends the context-locality direction in
`improvement-delegation-context-locality.md`. That note keeps detailed work and
evidence with the cheaper capable implementer. This note governs the otherwise
unbounded coordination cost while that work is in progress.

## Observed failure

A persistent implementer can be correctly delegated a large package while the
parent still spends substantial tokens on a loop like this:

1. wait for two to four minutes;
2. wake the parent model and learn that no message arrived;
3. run `git status`, `git diff --stat`, or another progress probe;
4. wake the parent model again to interpret an unsurprising result; and
5. start another short wait.

Each tool result can require another model continuation over the parent thread.
The stable prefix may be cached, but cached input still appears in raw token
usage, has non-zero execution cost, and must fit in the request context. The
small coordination messages and tool results also accumulate in the transcript.
A status probe after every timeout can nearly double the number of parent
continuations without producing a decision.

This is not an argument against monitoring. It is a distinction between:

- **completion waiting**, which should be event-driven;
- **progress evidence**, which should be requested at planned or risk-triggered
  checkpoints; and
- **stall diagnosis**, which should begin only after the expected progress
  envelope has been exceeded or contradictory evidence appears.

## Cost model

For a parent prefix of `P` input tokens and `N` model continuations, raw input
usage is approximately `P × N`, plus the growing suffix. Prompt caching changes
the price and latency of the reusable prefix; it does not make those requests
disappear or prevent new coordination records from growing the thread.

Track three quantities separately:

- raw input tokens, including cached input;
- cached reads, cache writes, and ordinary uncached input; and
- actual context growth from new messages, reasoning, tool calls, and results.

Do not describe a repeated cached read as free, and do not describe the whole
raw count as newly consumed context. If the runtime exposes usage details,
measure the cache-hit rate from cached input divided by total input rather than
inferring it from elapsed time.

Current OpenAI evidence provides a useful example, not a portable constant. For
GPT-5.6 and later, the default and currently supported prompt-cache lifetime is
30 minutes after the latest write or reuse, and reuse refreshes that lifetime.
Cached reads are charged at 0.1 times ordinary input and cache writes at 1.25
times ordinary input. A two-to-four-minute polling loop therefore normally
keeps the prefix warm but performs many avoidable cached reads. A bounded wait
near, but safely below, the known cache lifetime preserves reuse with far fewer
continuations. See the OpenAI
[prompt-caching guide](https://developers.openai.com/api/docs/guides/prompt-caching)
and [GPT-5.6 Sol model page](https://developers.openai.com/api/docs/models/gpt-5.6-sol).

Cache retention, prices, routing, model behavior, and host orchestration can
change. Skills should express the capability-driven rule and use a current
model-specific duration only after checking the active platform contract.

## Waiting protocol

### 1. Establish the progress envelope once

When assigning a non-trivial package, record:

- the expected class of duration, such as minutes or tens of minutes;
- milestones at which the implementer should report without being asked;
- conditions that require an immediate blocker message;
- the first time at which absence of progress becomes suspicious; and
- whether any later package depends on an intermediate parent decision.

This is a coordination estimate, not a delivery deadline or acceptance target.
An underestimated duration is not itself evidence that the implementer failed.

### 2. Wait for events, not reassurance

Use the collaboration wait mechanism with the longest useful bounded timeout.
It should return early on a mailbox update, so a longer timeout does not delay
handling a completion or blocker. Select the timeout from:

- the next real decision or progress checkpoint;
- the platform's maximum supported wait;
- any applicable user-communication requirement; and
- the verified cache lifetime, when retaining a costly prefix matters.

For the current GPT-5.6 cache contract, roughly 20 to 25 minutes is a reasonable
cache-aware waiting interval when no earlier checkpoint is needed. This is an
example configuration, not a permanent skill constant.

After a timeout with no message, wait again unless the progress envelope says
that diagnostic evidence is now warranted. Do not run a repository probe merely
to justify another wait.

### 3. Make progress probes decision-bearing

Inspect the shared tree while an implementer is running only when the result can
change an action. Examples include:

- a promised milestone or evidence artifact should now exist;
- a dependent architectural decision is blocked on the current state;
- the implementer reports a contradiction or asks for inspection;
- elapsed time has crossed the planned stall threshold; or
- there is evidence of runaway output, repeated failure, unsafe mutation, or
  work outside the authorized scope.

When a probe is justified, make it narrow and batch the evidence needed for one
decision. Prefer a changed-path summary, bounded diff statistic, process state,
or named artifact over streaming the working tree. Do not interpret ordinary
dirty state as progress quality while the writer is still active.

### 4. Use the correct interaction operation

- Use `send_message` to queue a delta or correction for an active subagent. It
  should receive the message at a safe turn boundary without restarting the
  package or repeating its context.
- Use `followup_task` when an idle persistent subagent must begin another turn.
  Do not use it as a polling mechanism.
- Use `wait_agent` to await mailbox updates or completion. A timeout means only
  that no update arrived during that interval.
- Use `interrupt_agent` only when the active work should actually stop or its
  current course is unsafe or invalidated. Do not interrupt merely to request a
  progress report that could wait for a checkpoint.
- Use `list_agents` for topology or lifecycle uncertainty, not as a periodic
  substitute for waiting.

Completion routing and queue/wake semantics are capabilities of the active
collaboration implementation. Check the current tool contract instead of
assuming that all messaging operations wake an idle recipient.

### 5. Keep messages delta-only

Give a persistent implementer the complete package context once. Later messages
should contain only:

- a changed decision or new constraint;
- a correction tied to concrete evidence;
- the next dependent boundary after parent acceptance; or
- a request for a compact checkpoint packet.

Do not resend the package, repeat successful logs, or ask the implementer to
summarize unchanged state. A useful checkpoint packet contains changed paths,
the owner boundary, non-mechanical exceptions, check results, unresolved risks,
and the detailed evidence location.

### 6. Report only material user-visible state

Before a long wait, tell the user what is running and what event or checkpoint
will wake the parent. Afterward, report completion, a material boundary decision,
a correction, or a blocker. Avoid commentary whose only information is that
the subagent remains active.

If the host requires periodic user updates, use the largest permitted interval
and keep the update in the same continuation as the next necessary action when
possible. Repository or runtime rules outrank token optimization.

## Cache-aware decision rule

When the active platform exposes a reusable-prefix lifetime:

1. determine the current lifetime and whether reuse refreshes it;
2. select a wait slightly shorter than that lifetime when the task is expected
   to continue and preserving the prefix is useful;
3. rely on early wake-up for prompt completion handling;
4. measure cached, cache-write, and ordinary input tokens when telemetry is
   available; and
5. re-establish the rule after compaction, model changes, tool-definition
   changes, or other prefix-invalidating events.

Do not poll every few minutes merely to keep a cache warm. Conversely, do not
choose a wait longer than a verified lifetime on the assumption that avoiding
all intermediate requests must be cheaper: one full cache miss and rewrite can
cost more than a small number of well-spaced cached continuations. Optimize the
measured request topology, not request count in isolation.

When cache behavior is unknown, prefer event-driven long waits and treat cache
status as unknown. Do not invent a retention duration.

## Skill changes

### `supervised-implementer-loop`

- Establish milestone, blocker, and stall-reporting expectations in the initial
  package handoff.
- Prefer long event-driven waits over short timeout loops.
- Treat timeout as absence of a message, not evidence of progress or failure.
- Permit progress inspection only when it can change a parent decision.
- Keep active-agent corrections queue-only and delta-only; wake idle persistent
  agents only for real follow-up work.
- Include cache-aware timing only as a verified runtime profile, not a fixed
  cross-platform number.

### `complex-work`

- Include coordination continuations in the execution-cost profile.
- Route long delegated units with explicit progress envelopes and meaningful
  checkpoints.
- Replan when parent activity is dominated by status polling rather than scope,
  architecture, acceptance, authorization, or integration decisions.

No new review phase or delivery package is required. This is an execution
discipline inside existing delegated work.

## Validation scenarios

| Scenario | Expected behavior |
|---|---|
| Implementer needs approximately 40 minutes | Parent waits on mailbox events with one or two cache-aware bounded waits, not ten short polls. |
| Implementer finishes two minutes into a 25-minute wait | Wait returns early and the parent handles the completion immediately. |
| Short wait times out with no message | Parent waits again; timeout is not converted into an unnecessary tree inspection. |
| Implementer promises a checkpoint artifact and misses the stall threshold | Parent performs one narrow diagnostic probe and decides whether to message, wait, or interrupt. |
| Parent has a very large stable context | Usage distinguishes raw, cached, cache-write, and newly appended tokens; successful status checks are not repeated. |
| Cache lifetime is unknown | Parent uses event-driven waits without claiming cache savings or inventing a timer. |
| Active implementer needs a correction | Parent queues one delta-only `send_message`; it does not restart the task or resend package context. |
| Idle persistent implementer receives the next accepted slice | Parent uses a turn-triggering follow-up with only the new boundary and accepted deltas. |
| User asks for frequent status reports | The workflow honors the request and combines each report with a meaningful checkpoint when possible. |

## Acceptance questions

- Can each parent wake-up change a decision or report a material event?
- Does waiting return early on subagent completion or blocker delivery?
- Are cache claims based on the active model and current telemetry?
- Are raw token replay, cache-adjusted cost, and transcript growth kept distinct?
- Are status probes triggered by evidence rather than elapsed curiosity?
- Does the persistent subagent receive full context once and deltas afterward?
- Are message, follow-up, wait, list, and interrupt operations used according to
  their queue and wake semantics?
- Would the workflow remain correct if prompt caching were unavailable?

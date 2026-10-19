---
name: session-audit
description: >-
  Audit long Codex session trees for outcome quality, failures, coordination
  overhead, rework, and evidence-backed improvements to skills. Use local rollout
  records and selected artifacts. Not a substitute for reviewing product code.
---

# Session Audit

Turn a large execution trace into a small set of supported workflow findings.
The output is an assessment and prioritized skill-change candidates, with enough
evidence and uncertainty for the user to assess them. Inspect the target without
steering its agents or changing its repository. Do not apply proposed skill
changes unless that work is requested.

## Index Before Reading

Use the bundled [session analyzer](../../scripts/codex_session_audit.py), which
requires only Python's standard library. Resolve its path relative to this skill
in an installed package. Create a fresh output directory outside the target repo:

```sh
python3 /path/to/scripts/codex_session_audit.py index SESSION_ID --output /tmp/audit-SESSION_ID
python3 /path/to/scripts/codex_session_audit.py overview /tmp/audit-SESSION_ID
```

Default discovery covers local active and archived rollouts. Repeat
`--sessions-root PATH` for other stores. Record missing stores, ambiguous lineage,
partial records, and files changing during the scan. A locally discovered tree
is not proof that all children survived. Separate parent, implementers,
reviewers, and automated approval agents; roles named `default` need inspection.
Check message visibility. Some rollouts preserve encrypted assignment or handoff
bodies while exposing only their headers. The analyzer marks these as opaque.
Do not judge their meaning, reporting compliance, or missing instructions from
the visible header; use a surviving authorized artifact or leave it unknown.

The index streams each selected file at its initial byte cutoff, records hashes,
and writes compact events with direct evidence locations. Keep these artifacts
local. Read the overview and query the index; do not dump full rollouts or the
entire event file into model context.

```sh
python3 /path/to/scripts/codex_session_audit.py events /tmp/audit-SESSION_ID --kind user_message --session SESSION_ID
python3 /path/to/scripts/codex_session_audit.py events /tmp/audit-SESSION_ID --kind patch_failure
python3 /path/to/scripts/codex_session_audit.py events /tmp/audit-SESSION_ID --query check-stage3.sh
python3 /path/to/scripts/codex_session_audit.py show /tmp/audit-SESSION_ID SESSION_ID:L123 --context 2
```

Queries search bounded excerpts and file-path anchors, not all transcript text.
Use `--skip` to page results and inspect the original source narrowly when an
omitted term matters. `show` verifies the indexed record's hash; adjacent context
is bounded and is not independently authenticated. Old snapshot evidence stays
old evidence even when the source has later messages.

## Reconstruct Decisions, Then Judge Them

Establish the requested outcome, accepted authorities and skill versions, scope
changes, delivery boundaries, and final claimed acceptance. Separate actual user
direction from injected environment, skill, and goal-continuation messages.
Segment at material user changes and accepted/rejected delivery boundaries;
calendar days alone do not define comparable work.

Use coverage across these questions rather than an invented overall score:

| Question | Evidence to inspect |
|---|---|
| Did it deliver the requested behavior? | Original outcome, final handoff, decisive witnesses, exact revision and remaining limitations |
| Did design risks surface soon enough? | First counterexample, prior assumptions, feasibility checks and subsequent rework |
| Did delegation reduce parent burden? | Ownership, assignments, handoffs, parent acceptance, repeated direction and child continuity |
| Did checking produce new information? | Change invalidating prior evidence, failed stage, diagnosis, scope of rerun and actual exit status |
| Where was avoidable work concentrated? | Repeated reads, truncations, failed patches, wait wakeups, retries, recovery and artifact churn |
| What made intervention necessary? | User corrections, preceding decisions, skill text actually available and response after correction |

Start with the outcome and scope changes. Weight workload by model price before
ranking efficiency leads: cheap local investigation and an expensive parent
round trip have different economics. Keep latency and machine-resource costs
visible separately. Read selected episodes around those leads, including
successful counterexamples.
Link trigger → decision → consequence → recovery. A pattern match, repeated
command, compaction, or long duration alone does not establish waste. Long wait
requests can return immediately on messages; requested timeout is not elapsed
waiting. Separate external interruptions and user-requested scope changes from
agent-caused rework. If skill versions are unavailable, leave attribution open.

Stop when the requested dimensions have supported findings or explicit unknowns
and further episodes are not changing the recommendations. Label sampling and
any unresolved high-impact question; indexing every record is not semantic
review of every record. Do not rerun costly product gates just to audit a session.

## Measure Cost Honestly

Prefer deduplicated per-response usage, attributed by the owning `thread_id` and
turn's model. A child's `session_id` may name the root. Never sum both native
usage records and their mirrored cumulative events. The analyzer labels legacy
cumulative peaks as lower bounds and reports accounting anomalies.

Report parent and whole-tree workload separately, and keep cached input,
uncached input, and output distinct. Reasoning output is part of output; do not
charge for it twice. Use dated, sourced rates for each actual model and service
tier before estimating price. If rates or attribution are missing, identify the
unpriced portion and report workload without a dollar estimate. API-equivalent
estimates are not subscription bills. Do not infer cost or progress from bytes,
message counts, or raw tokens alone.

The analyzer's `cost` command applies a supplied rate file to the indexed source
prefixes and verifies their hashes. For the supported GPT-6 pricing structure,
provide `as_of`, `source`, `basis`, `long_context_threshold`, and a `models` map
with `input`, `cached_input`, `cache_write`, and `output` rates per million tokens.
The command applies the full-request 2x input/cache and 1.5x output multipliers
above that threshold. Confirm those rules against the selected models' official
rates before use. It does not infer the service tier or price unknown models.

```sh
python3 /path/to/scripts/codex_session_audit.py cost /tmp/audit-SESSION_ID --rates /path/to/sourced-rates.json
```

Do not apply short-context rates to aggregated usage when some requests cross
the threshold. When the tier is unknown, label the assumed tier and examine a
relevant sensitivity. Use same-usage repricing to explain relative prices and
break-even workload reductions; it does not predict another model's token use,
quality, required supervision, or completion time. A cheap model's numerous
recoverable failures may be economical; prioritize failures that consume parent
decisions, invalidate useful work, or delay the outcome.

Compare only matched outcomes and acceptance boundaries. Mark comparisons across
different tasks, models, directions, and stopping conditions as observational.
A before/after snapshot within one changing task is not a causal experiment.

## Convert Findings Into Small, Testable Improvements

For each material finding, provide its observed consequence, source locations,
confidence, and attribution: missing/contradictory guidance, failure to follow
existing guidance, tool/environment failure, authorized scope change, or an
unresolved cause. Repetition of an existing instruction is not automatically a
useful skill fix.

Propose the smallest change to the owning skill, hook, or helper. Include the
activation condition, expected decision change, a realistic forward-test, and a
success measure such as fewer parent replayed commands per accepted unit or
earlier detection of a broken failure path. Preserve good behavior observed in
the same run. Rank by consequence and likely avoided work; do not invent savings.

Deliver a concise assessment with outcome, measured concentrations, supported
findings, positive evidence, prioritized changes, and coverage limits. Keep
verbose generated evidence in the index and cite only the needed episodes.

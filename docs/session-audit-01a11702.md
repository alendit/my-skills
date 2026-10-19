# Pilot session audit: S3-P2 implementation

Session `01a11702-c2a3-7ab0-a5b9-32901a958ed2` delivered a documented,
independently accepted result. Relative pricing supports its use of a cheap
implementer: Luna handled 93.84% of available input tokens for 48.06% of the
priced Standard API-equivalent estimate. The parent used 5.41% of input for
47.93% of priced cost. Improve the value of parent involvement first, retaining
checks that found real defects. Narrow evidence invalidation and reliable
failure reporting matter more economically than the raw count of cheap retries.

This is a first audit of selected episodes, not a new correctness review of the
compiler. Proposed changes below are candidates; existing production workflows
have not been edited as a result of these findings.

## Evidence and coverage

The [audit skill](../skills/session-audit/SKILL.md) and
[analyzer](../scripts/codex_session_audit.py) produced a local index at
`/private/tmp/session-audit-01a11702-20261019-final`. Reproduce it with:

```sh
python3 -B scripts/codex_session_audit.py index 01a11702-c2a3-7ab0-a5b9-32901a958ed2 --output /tmp/s3p2-audit-new
python3 -B scripts/codex_session_audit.py overview /tmp/s3p2-audit-new
```

The recorded snapshot covers 514,178 rows and 1,628,138,604 bytes across 82
locally available sessions: one parent, three implementers, two reviewers
identified from their paths, and 76 automated approval agents. Streaming and
indexing took 17.94 seconds on this machine; that measures preprocessing, not
the time needed for this assessment. The generated index is about 47 MB.

The parent spans October 7, 15:38 UTC through October 19, 05:23 UTC: about
11.6 elapsed days, including interruptions. Its 55,335-line snapshot SHA-256 is
`0ec5ea463dcdf37dd59108325f45d98bd9cbd1027a283e1a4b25a7e43bbaf9da`.
The analyzer SHA-256 is
`78d698d618acfd0d1e973781bb2b3ae0dcb1e27ea6b41e3153a2e184e74e78bd`.
No scanned source or analyzer changed during the final scan; no accounting or
malformed-record anomalies were detected.
That hash identifies the index-building version. The subsequent pricing pass
records its updated analyzer identity in `cost-standard-20261019.json` and
reconciles the same response totals against the original snapshot hashes.

Important limits:

- Earlier implementer contexts disappeared during continuation; some requested
  agent paths have no surviving local rollout in the discovered tree. These
  totals describe available recordings and may omit earlier work.
- All 1,753 parent assignment/message calls have opaque encrypted message
  bodies. Of 1,853 incoming agent messages, 1,569 contain encrypted content.
  Their meaning and exact reporting compliance cannot be judged from headers.
- The initial transcript names plugin version `0.1.0+codex.11f3705736e3`.
  Its cached `complex-work` matches this repository, but its supervised workflow
  differs from the current source. Current guidance must not be applied
  retrospectively where the versions differ.
- The whole trace was indexed. Semantic inspection sampled the original request,
  major user changes, failure and recovery episodes, output/patch failures,
  successful parent interventions, and final acceptance documents. No product
  gates were rerun; no agents or files in the target repository were changed.

## Outcome and workload

The original request was to implement the GC-backed syntax addendum, with
attention to relative parent/implementer pricing. The final
[handover](/Users/dimitrivorona/projects/rust/clojure-wasm/docs/stage3/implementation-handover.md:3)
and [independent review02](/Users/dimitrivorona/projects/rust/clojure-wasm/docs/stage3/reviews/s3p2-private-image-implementation-review02.md:3)
agree on accepted implementation `9dbd8c8ba2f19b3187a5e50ae918545d4e942dcd`:
673 release tests, four required artifact selectors, two fresh reconstructions,
and no remaining actionable review findings. Later status commit `4f89990f`
records acceptance. These are corroborating acceptance records, not a new
independent verification of every test result.

Available per-response usage, deduplicated by response identity and owning
thread, gives the following workload. Values are millions of tokens:

| Model | Uncached input | Cached input | Output |
|---|---:|---:|---:|
| GPT-6 Astra | 2.41 | 136.02 | 0.29 |
| GPT-6.1 Sol | 17.80 | 750.69 | 2.97 |
| GPT-6 Luna | 138.45 | 13,978.14 | 43.20 |
| Automated approval | 4.37 | 15.21 | 0.04 |

The parent's input is 813.8 million tokens, 5.41% of the available tree's input;
its output is 2.71 million. Across the tree, 98.92% of input is cached.

The parent made 3,446 outer executor calls, 1,438 `send_message` calls, 304
follow-ups and 1,658 agent waits. Only two wait requests were below one minute;
requested duration does not establish actual waiting time. The index flagged
3,833 tool outputs containing truncation markers and 671 containing patch
failure markers, including 225 and 10 respectively in the parent. These are
candidate-bearing output records, not independently confirmed waste events or
counts of unique underlying defects.

## Relative-cost reassessment

The [rate snapshot](session-audit-01a11702-rates.json) records official prices
retrieved on October 19, 2026. Short-context Standard rates per million tokens
are Astra $10/$1/$50, Sol 6.1 $2/$0.10/$10, and Luna $0.10/$0.01/$0.50 for
fresh input/cached input/output respectively.
[Official pricing](https://developers.openai.com/api/docs/pricing) supplies
the rates; the [Sol](https://developers.openai.com/api/docs/models/gpt-6.1-sol)
and [Luna](https://developers.openai.com/api/docs/models/gpt-6-luna) pages
establish the full-request premium above 272,000 input tokens: input/cache
double and output multiplies by 1.5.

Reproduce the calculation with:

```sh
python3 -B scripts/codex_session_audit.py cost /private/tmp/session-audit-01a11702-20261019-final --rates docs/session-audit-01a11702-rates.json
```

The formula is fresh input × its rate + cached input × its rate + output × its
rate, applying the context tier to each response. Cache writes, if present,
replace that token's fresh-input charge. Reasoning is already part of output.
Mirrored cumulative events and duplicate response IDs are not charged again.

| Model | Standard API-equivalent cost | Share of priced cost |
|---|---:|---:|
| GPT-6 Astra | $174.65 | 28.80% |
| GPT-6.1 Sol | $140.37 | 23.14% |
| GPT-6 Luna | $291.48 | 48.06% |
| Total priced | $606.50 | 100% |

By responsibility, the parent is $290.71, the three implementers $291.48,
and the two reviewers $24.30. The 76 approval-agent sessions are unpriced:
329 responses name `codex-auto-review`, with no rate established here, and one
session has no usable per-response usage. No rate or zero-cost assumption is
assigned to them.

These are current-rate scenarios for available recordings, not historical
invoices or subscription charges. The trace does not establish service tiers.
If only Luna used Fast mode at the documented 2x API rates, its estimate would
be $582.96 and the priced total $897.98; the parent's share would be 32.37%.
If all priced models use the same 2x multiplier, cost shares are unchanged.
Subscription allowance multipliers are not inferred from this API calculation.

The corrected interpretation is:

1. **Cheap delegation is economically supported.** Repricing the exact Luna
   workload at Sol 6.1 rates gives $3,402.82, or 11.67 times its Luna price.
   At an unchanged token mix, Sol would need 91.43% less weighted workload to
   break even. This is a price comparison, not evidence that the models would
   do the same work or need equal supervision. It argues against replacing the
   implementer merely because its raw token or patch-failure counts look large.
2. **Parent involvement deserves disproportionate scrutiny.** About half the
   priced cost comes from a parent responsible for only 5.41% of input.
   Prioritize routine replay, unnecessary coordination, and repeated acceptance
   inspection where episodes establish that they added no information. Keep
   semantic intervention and selective independent checks. Encrypted messages
   prevent classifying every parent round trip as useful or wasteful.
3. **Astra should earn its premium through a bounded decision.** Its 1,137
   responses cost $174.65; repricing their exact usage at Sol 6.1 rates gives
   $21.33. The $153.32 difference is a hypothetical price gap, not demonstrated
   savings. The parent's later use of Sol already follows the cheaper pattern.
   Use stronger-model escalation for a specific unresolved design or diagnosis
   when its expected effect justifies the premium.
4. **Cached context is still a material expense.** Luna has 26,419 of 47,312
   responses above the long-context threshold. Pricing all its usage at short
   rates would produce $175.22, understating the applicable estimate by $116.26.
   Compact renewal at accepted boundaries is worth testing, including the fresh
   input and reorientation it causes. Do not assume that resetting context is
   free or that compaction alone proves a problem.

Numerous local retries can be rational on Luna. Their economic priority rises
when they trigger costly parent work, invalidate accepted evidence, or extend
the delivery's critical path. Command runtime, storage and elapsed time remain
separate resource concerns; token pricing does not make repeated cold builds
free. The earlier ranking of oversized reads and patch failures was too driven
by event counts and is downgraded below parent acceptance and routing concerns.

## Findings and proposed changes

### 1. Acceptance repeated work beyond the changed executable boundary

The clearest episode follows two successful cold reconstructions. The parent
reported that removing an unused facade changed source identity, while compiler,
support, core and image bytes stayed identical. It then started two more fresh
shipping reconstructions after refreshing two manifests
([root L49384](/Users/dimitrivorona/.codex/sessions/2026/10/07/rollout-2026-10-07T17-36-59-01a11702-c2a3-7ab0-a5b9-32901a958ed2.jsonl:49384),
[L49870](/Users/dimitrivorona/.codex/sessions/2026/10/07/rollout-2026-10-07T17-36-59-01a11702-c2a3-7ab0-a5b9-32901a958ed2.jsonl:49870)).
The user subsequently required dependency-specific invalidation, focused parent
acceptance, and deferral of fresh reconstruction until final inputs settled
([L49975](/Users/dimitrivorona/.codex/sessions/2026/10/07/rollout-2026-10-07T17-36-59-01a11702-c2a3-7ab0-a5b9-32901a958ed2.jsonl:49975)).

**Assessment:** high confidence in repeated reconstruction and the need for
workflow correction. Some artifact identity checks remained legitimate; the
avoidable fraction of the broader acceptance sequence has not been measured.
Existing guidance already discourages mirroring successful reads and uninformative
reruns. This is partly an execution failure, with room for a clearer decision
rule rather than more general warnings.

**First proposed change:** in supervised acceptance and complex-work integration,
require the next expensive rerun to name its unresolved question or invalidated
dependency. Distinguish executable, recipe, artifact-identity and prose changes
inside the existing brief; do not add another ledger. Retain final exact-candidate
gates. Forward-test a manifest-only refresh and a real backend change: the former
should exercise its actual admission consumer without replaying unrelated
language/performance workloads; the latter should invalidate affected behavior.

### 2. Command orchestration lost failure information

The user explicitly required child status preservation through pipes and
background execution. A focused probe then preserved exit 37 while `tee`
returned 0. Yet a later generator wrapper still lost Cargo's status after
writing artifacts
([L50344](/Users/dimitrivorona/.codex/sessions/2026/10/07/rollout-2026-10-07T17-36-59-01a11702-c2a3-7ab0-a5b9-32901a958ed2.jsonl:50344),
[L50804](/Users/dimitrivorona/.codex/sessions/2026/10/07/rollout-2026-10-07T17-36-59-01a11702-c2a3-7ab0-a5b9-32901a958ed2.jsonl:50804)).

**Assessment:** high confidence in a tooling failure. The later result was
correctly kept diagnostic, avoiding unsupported acceptance. A probe of one
wrapper did not establish that every path actually used was reliable.

**Second proposed change:** add a focused instruction to the implementer role
and acceptance handoff: before expensive runs through new or changed command
wrapping, inject a small failure through the exact entrypoint being used. Check
the reported stage, actual child status and log path. Use the project's scripts,
without building a general orchestration framework. A forward-test should make
an early stage fail while `tee` and a later command succeed; acceptance must
still fail immediately. Recheck after wrapper changes.

### 3. Broad output and stale patch context caused repeated friction

Sampled worker failures are actual missing-anchor errors in REPL, test and
expansion files, not just matching documentation. A later worker's initial
inspection returned 1,482 lines and was truncated from 15,147 tokens
([worker L959](/Users/dimitrivorona/.codex/sessions/2026/10/09/rollout-2026-10-09T22-19-31-01a12252-26c3-76b3-ba18-968d356153d4.jsonl:959),
[L1412](/Users/dimitrivorona/.codex/sessions/2026/10/09/rollout-2026-10-09T22-19-31-01a12252-26c3-76b3-ba18-968d356153d4.jsonl:1412),
[later worker L122](/Users/dimitrivorona/.codex/sessions/2026/10/15/rollout-2026-10-15T23-56-31-01a14191-1bc8-7121-9391-54b0c29955c5.jsonl:122)).

**Assessment:** high confidence in the sampled failures and a large measured
concentration of leads. Their total cost and the causes of every failed anchor
are unknown; an anchor failure does not prove concurrent writers.

**Lower economic priority:** after a missing-anchor failure, refresh the affected
owner narrowly and revise the patch before another attempt. Apply output
budgets to the combined result of batched reads. Forward-test changed anchors
after a continuation and a multi-file inspection that exceeds the combined
budget. Measure patch failures per patch attempt and clipped outputs per
inspection, not total tokens as a proxy for price.

### 4. Architectural risk and recovery deserve targeted follow-up

Redefining `core/first` changed compiler bookkeeping before the definition request
returned. This was found on October 11, almost four days into the trace
([L13030](/Users/dimitrivorona/.codex/sessions/2026/10/07/rollout-2026-10-07T17-36-59-01a11702-c2a3-7ab0-a5b9-32901a958ed2.jsonl:13030)).
An earlier hostile mutation witness is a plausible improvement when changing
compiler/runtime ownership. It is not evidence that the later private-image
architecture was already required by the original plan. Test that hypothesis
at the next comparable design boundary before making it a universal skill rule.

Repeated continuation recovery and deleted recovery directories also mattered
([L2226](/Users/dimitrivorona/.codex/sessions/2026/10/07/rollout-2026-10-07T17-36-59-01a11702-c2a3-7ab0-a5b9-32901a958ed2.jsonl:2226),
[L23928](/Users/dimitrivorona/.codex/sessions/2026/10/07/rollout-2026-10-07T17-36-59-01a11702-c2a3-7ab0-a5b9-32901a958ed2.jsonl:23928)).
The user confirmed deliberate deletion at L23951. Five build inputs had become
dangling diagnostic symlinks. Consider a narrow continuity rule that required
build inputs and the compact recovery handoff survive disposal of generated
caches. Do not attribute the deletion or provider interruptions to the skills.

## Preserve these practices

Parent inspection caught real problems despite passing focused tests: marker
handling and unexecuted assertions at L6321, discarded results and map layout at
L7491, and allocator failure classification at L48825. Independent review02
closed obsolete-owner findings by inspecting actual emitted artifacts and
carrying forward valid coverage without repeating cold chains. These support
selective independent acceptance rather than eliminating acceptance.

The three major user direction changes must stay distinct from failures:
October 11 selected private images and explicitly required image replacement;
October 17 authorized removal of unsupported compatibility machinery;
October 18 removed in-process replacement and simplified acceptance. Earlier
replacement work was authorized. There is no sound basis to label all later
subtraction as unauthorized scope growth.

Provider usage/capacity errors are recorded at L8573, L15939, L18273 and L18590.
Calendar duration therefore cannot be treated as uninterrupted agent work.

The next useful validation is to test parent acceptance reuse, bounded premium
model escalation and exact-wrapper failure reporting on small realistic
episodes and a subsequent comparable delivery package. Measure accepted
outcomes, priced parent/child workload and latency; price child retries before
prioritizing them. This pilot does not prove an improvement caused by new skill
wording, or actual savings from changing models.

## Applied workflow changes

The authorized follow-up adds dependency-specific acceptance reuse to supervised
implementation and review, with complex-work integration consuming that rule.
Cost-based routing now accounts for parent work, cache/context pricing and
bounded stronger-model escalation. Continuity decisions account for renewal
cost and preserve required inputs outside disposable caches. The implementer
role budgets batched output and probes failure propagation through new or
changed wrappers; handoffs carry the actual child status and probe evidence.
Existing patch-context recovery guidance was retained, and the speculative
hostile-mutation recommendation was not made universal. The Luna max default
and selective independent acceptance remain in place.

Validation covers analyzer accounting and export behavior, skill metadata,
TOML parsing, and package reference closure. These checks do not demonstrate
future agent compliance or realized cost savings; a comparable delivery remains
the behavioral follow-up.

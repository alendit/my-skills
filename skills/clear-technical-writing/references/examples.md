# Examples

Use these examples to choose the needed relationship and detail, not as fixed
templates.

## Make A Compressed Operation Explicit

Compressed: “The router classifies failures and invalidates the request.”

Clearer when the distinction matters: “After the response parser identifies an
authentication failure, the request coordinator marks that attempt unusable and
returns it to the caller without retrying.”

The revision names only the actor, operation, object, condition, and consequence
needed for this reader. It does not imply that every sentence must expose five
fields.

## Scale Down For A Compact Artifact

Source facts: the parser now accepts an empty result object; existing successful
row responses are unchanged; the parser tests pass.

Commit message: “Accept successful empty query results”

Body when needed: “Treat a completed response with no row payload as success.
Row-bearing responses keep the existing path. Parser tests cover both forms.”

The compact artifact has no visible planning ceremony, yet preserves the change,
non-change, and evidence.

## Preserve Exact And Observational Values Differently

- Correctness boundary: “Reject payloads above 16 MiB.” Keep `16 MiB` exact.
- Observation: “Median latency fell from 201.8 ms to 183.6 ms across the same
  workload.” For a status summary, “about 202 ms to 184 ms” may be sufficient if
  the exact values remain available and the comparison still supports the
  decision.

Do not round a value when reproducibility, a limit, or a close comparison depends
on it.

## Explain A Project Term Locally

Assume a selected glossary prefers “leaf owner.” A handoff can still say: “The
leaf owner—the artifact-specific skill that decides its substantive content—runs
the final prose pass once.” The local explanation supplies the reader's missing
prerequisite; the glossary remains the project-wide terminology source, not
proof of the ownership rule.

## Rebuild After A Late Change

Old conclusion: “The candidate is faster and preserves correctness.”

New source fact: the corrected comparison shows equal latency and one unresolved
correctness failure.

Do not append “One failure remains.” Rebuild the evidence paragraph, summary,
and conclusion so the artifact says that performance is unchanged, correctness
is unresolved, and the candidate is not yet accepted.

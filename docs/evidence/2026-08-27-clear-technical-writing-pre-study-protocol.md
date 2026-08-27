# Clear Technical Writing Pre-Study Protocol — 2026-08-27

## Study question

Does `clear-technical-writing` help the same model produce more useful
engineering prose from the same source packet than it produces without the
skill?

This protocol was recorded before trial outputs were generated. The repository
validator checks record structure only; the independent review supplies the
quality judgment.

## Model trial method

Run the four cases in
[`fixtures.json`](../../skills/clear-technical-writing/evals/fixtures.json).
The study ID is `CTW-2026-08-27-01`. Use this exact outer instruction for both
conditions:

> Produce only the requested artifact; use only the supplied packet; preserve
> all unknowns and limits; do not mention the study.

For each case, create a matched pair:

1. The baseline receives the assignment, intended reader, source packet, and
   outer instructions, but not the skill.
2. The skill condition receives the same inputs plus the exact installed
   `clear-technical-writing` skill.
3. Hold the model and runtime identity, outer instructions, exposed generation
   settings, tool availability, context configuration, and source packet
   constant. Record the exact skill revision in both records.
4. Hide condition labels before review. Compute SHA-256 over the UTF-8 string
   `<study-id>:<case-id>`. If the first hexadecimal digit is even, label the
   baseline `A` and the skill output `B`; if it is odd, label the skill output
   `A` and the baseline `B`. Retain this mapping outside the material shown to
   reviewers so the masking is reproducible without adding it to the validator.

The only condition difference is that the skill condition receives the exact
installed skill. Use exactly two independent blinded reviewers. Neither may be
an output generator or an implementation author.

The four cases cover initial technical writing, revision after a new requested
change, selected project-glossary use, and an agent handoff. They are a small
representative study, not an exhaustive enumeration of every CTW or GL clause.

## Independent review

For each unlabeled pair, each reviewer independently answers the case-specific
questions and chooses `A`, `B`, or `tie` on:

- clarity: the intended reader can recover the situation, consequence, and
  requested action;
- factual preservation: supplied facts, limits, unknowns, evidence, and
  authority remain intact;
- terminology consistency: necessary terms are stable, locally understandable,
  and consistent with their semantic sources; and
- unnecessary detail: content that does not help the reader understand,
  verify, decide, or act is absent.

Each reviewer also chooses `A`, `B`, or `tie` for overall usefulness. Every
choice must cite observable text and source-packet fields; reviewers must not
infer private reasoning or consult each other's results before submitting.

## Model-trial decision rule

After unmasking, aggregate the two reviews conservatively:

- a case is skill-preferred only when both reviewers prefer the skill overall;
- a case is baseline-preferred when either reviewer prefers the baseline
  overall;
- every other case is a tie; and
- any factual regression reported by either reviewer counts as a factual
  regression for the study.

Classify the skill as useful for this study only when all of the following hold:

- the skill output has no factual-preservation regression in any case;
- the skill output is preferred overall in at least three of the four cases;
- the baseline is not preferred overall in any case; and
- neither reviewer rates the skill worse on terminology consistency in the
  glossary or handoff case.

Otherwise the study does not distinguish the skill from an ineffective one and
the review reports the failed cases, dimensions, and all reviewer disagreements
without adjudication. This rule applies to this commissioned study; it is not a
universal prose-quality metric.

## V11 human comprehension pilot

Run V11 only if at least four intended-reader evaluators are available. Use a
within-reader paired comparison with condition labels hidden and presentation
order randomized or counterbalanced. Before showing outputs, derive the answer
key from each source packet for five questions: what happened before, what
changes, why the behavior is correct or deliberately different, what evidence
matters, and what action or decision the artifact requests.

The commissioned material-improvement threshold is a mean increase of at least
0.5 correct answers out of five for the skill condition, with no factual-score
regression. Record reader profile, sample size, presentation order, answers,
and scoring. This pilot threshold is specific to this study and does not claim
population-level generalization.

If suitable evaluators are unavailable, do not run V11. Record
`human-comprehension-unconfirmed`; do not substitute model judgment or treat the
missing pilot as a deterministic implementation failure.

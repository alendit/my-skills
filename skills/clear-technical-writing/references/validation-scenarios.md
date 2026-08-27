# Validation Scenarios

The evaluation asks one practical question: does this skill help the same model
produce more useful engineering prose from the same source material?

Use the dated
[pre-study protocol](../../../docs/evidence/2026-08-27-clear-technical-writing-pre-study-protocol.md)
for trial conditions, blinded review, the decision rule, and the optional V11
human study. The validator checks records mechanically; it never decides
whether prose or terminology is good.

## Representative Cases

The compact [case manifest](../evals/fixtures.json) contains four paired cases.
Each supplies an assignment, intended reader, source packet, and observable
review questions.

| Case | What it exercises |
|---|---|
| `initial-technical-writing` | Produce a first reader-facing engineering update from accepted facts and unknowns. |
| `revision-after-change` | Rebuild dependent prose after a requested fact changes the conclusion. |
| `project-glossary-use` | Use a selected project term consistently while keeping semantic authority and local explanation clear. |
| `agent-handoff` | Give another agent a self-contained, source-grounded handoff without redefining terms or inventing mechanisms. |

The independent reviewer compares the baseline and skill outputs on clarity,
factual preservation, terminology consistency, and unnecessary detail. These
questions guide human judgment; they are not exact-string checks.

## Mechanical Commands

Run the thin package validator and its bounded malformed-record checks:

```bash
"$SKILLS_REPO/skills/clear-technical-writing/scripts/validate_evidence.py" \
  --repo-root "$SKILLS_REPO" validate-package

"$SKILLS_REPO/skills/clear-technical-writing/scripts/validate_evidence.py" \
  --repo-root "$SKILLS_REPO" self-test
```

Create one record for each paired condition with the same trial ID, model,
runtime, outer instructions, settings, tool/context configuration, and source
packet. Captures default to the system temporary directory:

```bash
"$SKILLS_REPO/skills/clear-technical-writing/scripts/validate_evidence.py" \
  --repo-root "$SKILLS_REPO" prepare-capture \
  --case initial-technical-writing \
  --trial-id STUDY-RUN-ID \
  --condition baseline \
  --model-id MODEL-ID \
  --runtime-id RUNTIME-ID \
  --outer-instructions "OUTER INSTRUCTIONS"
```

Use `--condition skill` for the matched skill output. A completed record needs
the exact current skill revision and a non-empty output. Validate any record
with `validate-capture PATH`.

## Evidence Boundary

Repository validation proves that the skill and four-case study package are
well formed. It does not prove that a model follows the skill, that the skill
is useful, or that a person understands its output. Actual paired outputs and
their blinded independent review provide model-capability evidence.

V11 remains a separate audience-comprehension pilot. Do not run it or claim
human evidence unless the predeclared intended-reader evaluators are available.
Absence of external evaluators or model access does not invalidate a sensibly
implemented skill or its deterministic repository checks.

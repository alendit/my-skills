# Project Glossary

This glossary records the preferred names for concepts that recur across this
repository's skills and improvement plans. It explains terminology; the linked
skill or accepted plan remains authoritative for behavior and acceptance.

| Term | Meaning in this repository | Semantic source |
|---|---|---|
| **Leaf owner** | The artifact-specific skill or caller that makes the substantive decisions for an artifact and applies any final prose pass once. An outer workflow may verify that the pass occurred but does not repeat it. | [Clear-writing plan, CTW2](improvement-clear-technical-writing.md#authoritative-contract-and-evidence-matrix) |
| **Semantic owner** | The code, accepted contract, architecture authority, or artifact-specific skill that decides and maintains a behavior. Explanatory wording, including this glossary, cannot replace that authority. | [Glossary plan, GL3](improvement-glossary.md#authoritative-contract-and-evidence-matrix) |
| **Tick** | An independent review phase that examines the exact committed result of the preceding change. It reports findings and evidence but does not implement remediation. | [`review-fixpoint`](../skills/review-fixpoint/SKILL.md) |
| **Tock** | A remediation phase that addresses the preceding Tick's findings, validates the changed owners, and commits the result before another independent review. | [`review-fixpoint`](../skills/review-fixpoint/SKILL.md) |
| **Deterministic fixed point** | The state in which a fresh independent Tick finds no P0-P3 defect or required unknown, required deterministic checks pass on the reviewed revision, and no valid external product-contract failure or activated follow-up remains unresolved. It does not by itself confirm an external model or human capability. | [`review-fixpoint`](../skills/review-fixpoint/SKILL.md) |
| **Capability unconfirmed** | A required external model, provider, or human capability lacks valid current evidence. This status is distinct from a product-contract failure and does not invalidate an otherwise passing deterministic gate. | [Fixpoint evidence boundary](../skills/review-fixpoint/references/contract-and-evidence-boundary.md) |
| **Look-aside location** | A user-selected glossary location outside the project. The agent must obtain the exact path and intended scope instead of inventing one. | [Glossary plan, GL2](improvement-glossary.md#authoritative-contract-and-evidence-matrix) |

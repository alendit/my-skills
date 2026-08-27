# Research Rationale

Read this reference only when explaining why the skill uses its current design.
These sources inform design choices; none proves that this exact process improves
the model's output or a reader's comprehension.

| Source group | Supported design input | Unsupported inference |
|---|---|---|
| [Reader-expectation guidance](https://pmc.ncbi.nlm.nih.gov/articles/PMC9391546/) | Put recoverable context before dependent new information and make sentence-to-sentence relationships easier to follow. | A fixed private record after every sentence is necessary or sufficient. |
| [PLANET](https://aclanthology.org/2022.acl-long.163/), [PAIR](https://aclanthology.org/2020.emnlp-main.57/), and [Re3](https://aclanthology.org/2022.emnlp-main.296/) | Planning and revision can improve coherence in the evaluated long-form generation tasks. | The same mechanism or cost benefits short commit messages, comments, or current coding agents. |
| [Discourse-relation analysis](https://aclanthology.org/2020.inlg-1.8/) and [model criticism](https://aclanthology.org/2022.emnlp-main.815/) | Locally fluent text can still have discourse or high-level coherence defects, so final evaluation must inspect relationships beyond sentence grammar. | Either paper validates this drafting workflow. |
| [Verbosity bias](https://arxiv.org/abs/2310.10076) and [verbosity compensation](https://arxiv.org/abs/2411.07858) | Length, confidence, preference, and correctness are different properties. | Shorter prose is automatically more accurate or clearer. |
| [Code review as decision-making](https://link.springer.com/article/10.1007/s10664-025-10791-2) and [effective PR descriptions](https://2026.msrconf.org/details/msr-2026-technical-papers/35/The-Value-of-Effective-Pull-Request-Description) | Reviewers need orientation, rationale, purpose, change explanation, evidence, and sometimes an explicit feedback request; useful content depends on the change and context. | One fixed PR template or universal audience fits every review. |
| [Google active-voice guidance](https://developers.google.com/style/voice) and [Microsoft scannability guidance](https://learn.microsoft.com/en-us/style-guide/scannable-content/) | Explicit actors and structure can improve clarity when they fit the sentence and medium. | Passive voice, long sentences, or unheaded prose are categorical defects. |

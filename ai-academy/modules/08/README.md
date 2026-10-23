# Module 08: RAG & Vector Databases

Quarter 3 · Four weeks · 12–15 hours per week · Pilot learning material

## Learning objectives

Students will explain embeddings and cosine similarity; create a local vector index; compare chunking/retrieval approaches; evaluate retrieval separately from generated answers; enforce document authorization before model context construction; and handle deletion and stale content.

## Certification alignment

S1.2, S2.3–2.4; AWS 2.1, 3.1, 3.4, 5.1. This is supporting application practice for AI-901, not a separately named RAG objective.

These are partial curriculum mappings, not complete exam coverage or endorsement. See the [blueprint](../../docs/curriculum-blueprint.html) for versions and platform gaps.

## Weekly lessons

- [Week 1: Understand retrieval representations](week-1.html)
- [Week 2: Build an index with provenance](week-2.html)
- [Week 3: Separate retrieval from answer quality](week-3.html)
- [Week 4: Enforce permissions before context](week-4.html)

## Proof-of-work project: 08-permission-aware-policy-assistant

Index 20–50 instructor-authored BrewByte policies in local Chroma using a small SentenceTransformers model. Give two mock roles different document permissions. Return cited answers or abstain when evidence is insufficient. Pinecone is an optional comparison, not a required account.

## Acceptance evidence

Use 30 labeled questions covering answerable, unanswerable, stale, and unauthorized requests. Report Recall@k, citation correctness, supported-answer rate, abstention quality, and latency. All seeded unauthorized retrieval cases must return no forbidden content. Test authorization at retrieval and context assembly; authorization data comes from verified server-side identity, not user prompt text.

## Security integration

Retrieved content is untrusted; defend against indirect prompt injection, cross-role leakage, unauthorized ingestion, and embedding/index exposure. Use approved sources, source metadata, role filters, controlled ingestion, and deletion/reindex tests. Similarity scores do not establish permission or answer certainty.

## Lab access

- [Guided notebook](lab.ipynb)
- [Starter Python script](starter.py)
- [Open notebook in Colab](https://colab.research.google.com/github/jdmc-services/brewbyte-risk-management-lab/blob/main/ai-academy/modules/08/lab.ipynb) — available after the reviewed branch is merged
- [Live-model and deployment instructions](../../docs/model-and-deployment-labs.html)
- [Shared synthetic dataset guide](../../data/README.md)
- [Raw sales CSV](../../data/sales.csv) · [Synthetic tickets CSV](../../data/tickets.csv)

Run from the repository root: `python ai-academy/modules/08/starter.py`. Module 4 needs the optional classical-ML environment. The default examples for generative modules are explicitly labeled fixtures/baselines.

## Assessment rubric

| Criterion | Weight | Evidence |
|---|---|---|
| Functional behavior | 35% | Meets the stated task and handles meaningful failures |
| Evaluation | 25% | Held-out cases, denominators, observed errors, limitations |
| Security/privacy | 20% | Appropriate boundaries and tested controls |
| Reproducibility | 10% | Clear setup, versions, provenance, commands |
| Explanation | 10% | Own reasoning and an unseen independent modification |

Target at least 80/100 plus mandatory controls. Repair credential exposures, seeded access bypasses, or fabricated results before progression. This threshold is an instructional rule, not an exam passing score. Public worked examples do not replace independent work.

## Free assigned resources

- [SentenceTransformers semantic search](https://sbert.net/)
- [Chroma local documentation](https://docs.trychroma.com/)
- [OWASP 2026 publication](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/)

[Academy home](../../index.html) · [Course guide](../../docs/start-here.html)

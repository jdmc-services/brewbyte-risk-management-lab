# Module 08 · Week 1: Understand retrieval representations

**BrewByte assignment:** Index 20–50 instructor-authored BrewByte policies in local Chroma using a small SentenceTransformers model. Give two mock roles different document permissions. Return cited answers or abstain when evidence is insufficient. Pinecone is an optional comparison, not a required account.

## Learn the concept

Lexical retrieval matches words; embeddings encode a learned representation that can support semantic similarity. Cosine similarity compares vector direction, not truth, authorization, or confidence. Keep a lexical baseline so an embedding system must demonstrate value rather than merely adding components.

## Worked business example

A query about replacing a spilled drink may match a policy titled service recovery through semantic retrieval. That match still needs permission checks and evidence review.

## Guided practice

Read this week's assigned resource sections about **Vectors, dot product/cosine intuition, embeddings, lexical baseline**. Spend about three hours on reading, small examples, and explaining the vocabulary in your own words. You are not expected to complete every linked course this week.

Open [the guided notebook](lab.ipynb) or [starter script](starter.py). The notebook names the dependency and execution requirements. Run the relevant worked example and inspect its inputs and outputs. For Module 1, begin with a manual prompt comparison; coding is introduced in Module 2.

Run lexical search and hand-inspect three queries. Then use the optional SentenceTransformers route and compare rankings. Label lexical and embedding results accurately.

Change one input or condition, predict the result, then run or observe it. Preserve a failing case before repairing it. Complete the task in your own learning repository rather than modifying the public teaching source.

## Security boundary

Retrieved content is untrusted; defend against indirect prompt injection, cross-role leakage, unauthorized ingestion, and embedding/index exposure. Use approved sources, source metadata, role filters, controlled ingestion, and deletion/reindex tests. Similarity scores do not establish permission or answer certainty.

## Submit evidence

Small semantic-search notebook and baseline comparison. Include commands or procedure, relevant outputs, one failed case, your interpretation, and AI-assistance disclosure. Use synthetic data only. Clearly distinguish personally executed work, observed instructor demonstrations, and pending exercises.

## Check your understanding

- Which assumption in understand retrieval representations could make your BrewByte result misleading?
- What fails if the input is malformed, unauthorized, or missing?
- What evidence would convince a reviewer that your change works on an unseen case?

These public questions are formative. Explain your reasoning; they are not hidden certification questions.

## Free assigned resources

- [SentenceTransformers semantic search](https://sbert.net/)
- [Chroma local documentation](https://docs.trychroma.com/)
- [OWASP 2026 publication](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/)

## Continue

[Module assignment and rubric](index.html) · [Academy home](../../index.html) · [Execution guide](../../docs/model-and-deployment-labs.html)

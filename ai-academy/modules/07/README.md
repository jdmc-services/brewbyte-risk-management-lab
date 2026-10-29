# Module 07: Applied Generative AI & API Integration

Quarter 3 · Four weeks · 12–15 hours per week · Pilot learning material

## Learning objectives

Students will describe HTTP, JSON, REST, SDKs, and status codes; build a small Python model client and FastAPI endpoint; validate structured outputs; handle timeout/retry/rate errors; compare prompting, RAG, and fine-tuning; and measure quality, latency, and estimated cost.

## Certification alignment

S1.1, S2.2–2.3; AWS 2.3, 3.1–3.4, 5.1; AI-901 Foundry SDK/client/deployment skills only when the optional platform bridge is executed.

These are partial curriculum mappings, not complete exam coverage or endorsement. See the [blueprint](../../docs/curriculum-blueprint.html) for versions and platform gaps.

## Weekly lessons

- [Week 1: Understand requests, responses, and adapters](week-1.html)
- [Week 2: Build a small validated API](week-2.html)
- [Week 3: Bound failures and consumption](week-3.html)
- [Week 4: Choose customization from evidence](week-4.html)

## Proof-of-work project: 07-model-gateway

Build a ticket-summary API with a provider-neutral adapter, a deterministic fixture, and one real small-model backend. Add adapters from official OpenAI/Anthropic examples without requiring paid calls. Record any unexecuted adapter as untested.

## Acceptance evidence

Evaluate at least 30 held-out requests; report schema success, factual correctness against inputs, rejection behavior, and latency. Test 429/5xx errors, unavailable backends, timeout, malformed responses, and retry limits. Use a representative small pretrained model for genuine inference; fixture success cannot substitute for model quality.

## Security integration

Environment-based secrets, restricted credentials, authenticated routes, payload/token limits, bounded retries, dependency review, sanitized logs, and explicit output validation. Never execute model-generated code or allow arbitrary outbound URLs. Use an instructor-provided simple authentication scaffold until students understand it.

## Lab access

- [Guided notebook](lab.ipynb)
- [Starter Python script](starter.py)
- [Open notebook in Colab](https://colab.research.google.com/github/jdmc-services/brewbyte-risk-management-lab/blob/main/ai-academy/modules/07/lab.ipynb) — available after the reviewed branch is merged
- [Live-model and deployment instructions](../../docs/model-and-deployment-labs.html)
- [Shared synthetic dataset guide](../../data/README.md)
- [Raw sales CSV](../../data/sales.csv) · [Synthetic tickets CSV](../../data/tickets.csv)

Run from the repository root: `python ai-academy/modules/07/starter.py`. Module 4 needs the optional classical-ML environment. The default examples for generative modules are explicitly labeled fixtures/baselines.

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

- [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/)
- [Hugging Face inference course](https://huggingface.co/learn/llm-course/chapter1/1)
- [OpenAI API documentation; inference may cost money](https://platform.openai.com/docs/overview)
- [Anthropic API documentation; inference may cost money](https://docs.anthropic.com/en/docs/overview)

[Academy home](../../index.html) · [Course guide](../../docs/start-here.html)

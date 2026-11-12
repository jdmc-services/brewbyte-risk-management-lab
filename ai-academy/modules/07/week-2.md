# Module 07 · Week 2: Build a small validated API

**BrewByte assignment:** Build a ticket-summary API with a provider-neutral adapter, a deterministic fixture, and one real small-model backend. Add adapters from official OpenAI/Anthropic examples without requiring paid calls. Record any unexecuted adapter as untested.

## Learn the concept

An API endpoint needs a defined request, response, identity, and error policy. Authentication and validation must execute before expensive model work. Never accept a role from model text as identity. Keep secrets in environment configuration, not browser code, notebooks, or container images.

## Worked business example

A staff member submits a ticket to a summary endpoint. An absent credential fails before generation. An oversized request is rejected rather than sent to a provider.

## Guided practice

Read this week's assigned resource sections about **FastAPI request/response models, validation, authentication scaffold**. Spend about three hours on reading, small examples, and explaining the vocabulary in your own words. You are not expected to complete every linked course this week.

Open [the guided notebook](lab.ipynb) or [starter script](starter.py). The notebook names the dependency and execution requirements. Run the relevant worked example and inspect its inputs and outputs. For Module 1, begin with a manual prompt comparison; coding is introduced in Module 2.

Run the optional FastAPI scaffold locally, supply a test credential through the environment, and verify valid, missing-credential, and oversized requests. Do not expose it on a public interface.

Change one input or condition, predict the result, then run or observe it. Preserve a failing case before repairing it. Complete the task in your own learning repository rather than modifying the public teaching source.

## Security boundary

Environment-based secrets, restricted credentials, authenticated routes, payload/token limits, bounded retries, dependency review, sanitized logs, and explicit output validation. Never execute model-generated code or allow arbitrary outbound URLs. Use an instructor-provided simple authentication scaffold until students understand it.

## Submit evidence

Documented endpoint and integration tests. Include commands or procedure, relevant outputs, one failed case, your interpretation, and AI-assistance disclosure. Use synthetic data only. Clearly distinguish personally executed work, observed instructor demonstrations, and pending exercises.

## Check your understanding

- Which assumption in build a small validated api could make your BrewByte result misleading?
- What fails if the input is malformed, unauthorized, or missing?
- What evidence would convince a reviewer that your change works on an unseen case?

These public questions are formative. Explain your reasoning; they are not hidden certification questions.

## Free assigned resources

- [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/)
- [Hugging Face inference course](https://huggingface.co/learn/llm-course/chapter1/1)
- [OpenAI API documentation; inference may cost money](https://platform.openai.com/docs/overview)
- [Anthropic API documentation; inference may cost money](https://docs.anthropic.com/en/docs/overview)

## Continue

[Module assignment and rubric](index.html) · [Academy home](../../index.html) · [Execution guide](../../docs/model-and-deployment-labs.html)

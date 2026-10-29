# Module 07 · Week 3: Bound failures and consumption

**BrewByte assignment:** Build a ticket-summary API with a provider-neutral adapter, a deterministic fixture, and one real small-model backend. Add adapters from official OpenAI/Anthropic examples without requiring paid calls. Record any unexecuted adapter as untested.

## Learn the concept

Timeouts, retry budgets, token caps, and payload limits control failure amplification. A 429 response differs from malformed input; retries must be limited and respect provider guidance. Validate output schemas and semantic evidence before passing results downstream. Automatic evaluation should preserve failed cases rather than silently retrying until success.

## Worked business example

An unavailable model should return a clear service error after a bounded attempt. It must not trigger an infinite retry loop or return a fabricated successful summary.

## Guided practice

Read this week's assigned resource sections about **Provider adapters, timeouts/backoff, limits, structured-output failures**. Spend about three hours on reading, small examples, and explaining the vocabulary in your own words. You are not expected to complete every linked course this week.

Open [the guided notebook](lab.ipynb) or [starter script](starter.py). The notebook names the dependency and execution requirements. Run the relevant worked example and inspect its inputs and outputs. For Module 1, begin with a manual prompt comparison; coding is introduced in Module 2.

Inject timeouts, missing backends, malformed output, and a rate-limit response. Document expected handling and verify that no unbounded retries or unsafe outputs occur.

Change one input or condition, predict the result, then run or observe it. Preserve a failing case before repairing it. Complete the task in your own learning repository rather than modifying the public teaching source.

## Security boundary

Environment-based secrets, restricted credentials, authenticated routes, payload/token limits, bounded retries, dependency review, sanitized logs, and explicit output validation. Never execute model-generated code or allow arbitrary outbound URLs. Use an instructor-provided simple authentication scaffold until students understand it.

## Submit evidence

Bounded failure handling and execution-status matrix. Include commands or procedure, relevant outputs, one failed case, your interpretation, and AI-assistance disclosure. Use synthetic data only. Clearly distinguish personally executed work, observed instructor demonstrations, and pending exercises.

## Check your understanding

- Which assumption in bound failures and consumption could make your BrewByte result misleading?
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

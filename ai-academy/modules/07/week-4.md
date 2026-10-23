# Module 07 · Week 4: Choose customization from evidence

**BrewByte assignment:** Build a ticket-summary API with a provider-neutral adapter, a deterministic fixture, and one real small-model backend. Add adapters from official OpenAI/Anthropic examples without requiring paid calls. Record any unexecuted adapter as untested.

## Learn the concept

Prompting changes instructions; RAG supplies external evidence; fine-tuning changes model parameters. They solve different problems. Fine-tuning is not the default solution for facts that change frequently. Compare quality, latency, cost, data rights, and maintenance burden using a labeled held-out set.

## Worked business example

BrewByte policies change monthly, favoring retrieval. A stable formatting behavior may be improved with examples or tuning, but first establish a measured prompt baseline.

## Guided practice

Read this week's assigned resource sections about **Model evaluation, customization decision, optional tiny tuning**. Spend about three hours on reading, small examples, and explaining the vocabulary in your own words. You are not expected to complete every linked course this week.

Open [the guided notebook](lab.ipynb) or [starter script](starter.py). The notebook names the dependency and execution requirements. Run the relevant worked example and inspect its inputs and outputs. For Module 1, begin with a manual prompt comparison; coding is introduced in Module 2.

Evaluate thirty held-out requests with one real backend and document schema/factual errors and latency. Write a customization memo. Optional tiny-model tuning needs separate training/validation data and a baseline comparison.

Change one input or condition, predict the result, then run or observe it. Preserve a failing case before repairing it. Complete the task in your own learning repository rather than modifying the public teaching source.

## Security boundary

Environment-based secrets, restricted credentials, authenticated routes, payload/token limits, bounded retries, dependency review, sanitized logs, and explicit output validation. Never execute model-generated code or allow arbitrary outbound URLs. Use an instructor-provided simple authentication scaffold until students understand it.

## Submit evidence

Evaluation report, model gateway, and decision memo. Include commands or procedure, relevant outputs, one failed case, your interpretation, and AI-assistance disclosure. Use synthetic data only. Clearly distinguish personally executed work, observed instructor demonstrations, and pending exercises.

## Check your understanding

- Which assumption in choose customization from evidence could make your BrewByte result misleading?
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

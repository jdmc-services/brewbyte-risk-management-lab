# Module 01 · Week 2: Understand LLM limits

**BrewByte assignment:** Create a synthetic service-request summarization and routing playbook. Supply 20 labeled requests, two prompt versions, a scoring rubric, actual model outputs, and a one-page adoption recommendation. Use a free accessible interface or instructor-led/local model session; hand-record results before automating evaluation later.

## Learn the concept

A language model predicts tokens from context learned during training. Inference generates a response without necessarily updating model weights. Context is finite, and important instructions or evidence may be absent. Generation can produce unsupported details; confident wording does not mean calibrated confidence. Verification must use an independent trusted source.

## Worked business example

Ask a model to summarize an invented BrewByte notice. Compare every factual claim with the notice. Mark a made-up closing time as an unsupported addition even if the wording sounds professional.

## Guided practice

Read this week's assigned resource sections about **Tokens, context, capabilities, uncertainty, basic multimodal examples; verify a fabricated claim**. Spend about three hours on reading, small examples, and explaining the vocabulary in your own words. You are not expected to complete every linked course this week.

Open [the guided notebook](lab.ipynb) or [starter script](starter.py). The notebook names the dependency and execution requirements. Run the relevant worked example and inspect its inputs and outputs. For Module 1, begin with a manual prompt comparison; coding is introduced in Module 2.

Write a 120-word synthetic policy and test a summary, an extraction, and an unanswerable question. Save the prompt and actual output; annotate supported, contradicted, and missing claims.

Change one input or condition, predict the result, then run or observe it. Preserve a failing case before repairing it. Complete the task in your own learning repository rather than modifying the public teaching source.

## Security boundary

Threat: a request contains instructions to reveal private content or bypass its assigned task. Treat request text as untrusted data, minimize information supplied, verify factual claims, and retain human approval for actions. Demonstrate that instructions and delimiters reduce some errors but do not create an authorization boundary. Never put secrets in system prompts.

## Submit evidence

Annotated examples and a limitations checklist. Include commands or procedure, relevant outputs, one failed case, your interpretation, and AI-assistance disclosure. Use synthetic data only. Clearly distinguish personally executed work, observed instructor demonstrations, and pending exercises.

## Check your understanding

- Which assumption in understand llm limits could make your BrewByte result misleading?
- What fails if the input is malformed, unauthorized, or missing?
- What evidence would convince a reviewer that your change works on an unseen case?

These public questions are formative. Explain your reasoning; they are not hidden certification questions.

## Free assigned resources

- [Hugging Face: introductory LLM concepts](https://huggingface.co/learn/llm-course/chapter1/1)
- [Microsoft AI-901 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-901)

## Continue

[Module assignment and rubric](index.html) · [Academy home](../../index.html) · [Execution guide](../../docs/model-and-deployment-labs.html)

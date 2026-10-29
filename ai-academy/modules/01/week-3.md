# Module 01 · Week 3: Build and compare prompts

**BrewByte assignment:** Create a synthetic service-request summarization and routing playbook. Supply 20 labeled requests, two prompt versions, a scoring rubric, actual model outputs, and a one-page adoption recommendation. Use a free accessible interface or instructor-led/local model session; hand-record results before automating evaluation later.

## Learn the concept

A useful prompt states the task, context, allowed evidence, constraints, examples, and response format. Few-shot examples teach the expected pattern; they do not guarantee correctness. Compare changes on the same development cases so differences are attributable. Keep a separate held-out set to detect improvements that only memorize your examples.

## Worked business example

Task: summarize a request using only its text. Format: category, summary, needs_review. Example: an incorrect drink becomes service, not billing. Require unknown when the evidence is insufficient.

## Guided practice

Read this week's assigned resource sections about **Prompt architecture, zero/few-shot examples, output contracts, manual version control**. Spend about three hours on reading, small examples, and explaining the vocabulary in your own words. You are not expected to complete every linked course this week.

Open [the guided notebook](lab.ipynb) or [starter script](starter.py). The notebook names the dependency and execution requirements. Run the relevant worked example and inspect its inputs and outputs. For Module 1, begin with a manual prompt comparison; coding is introduced in Module 2.

Write two prompt versions, run both on ten development requests, and score factual support, category, and format. Change one design choice at a time. Explain which version you would retain and why.

Change one input or condition, predict the result, then run or observe it. Preserve a failing case before repairing it. Complete the task in your own learning repository rather than modifying the public teaching source.

## Security boundary

Threat: a request contains instructions to reveal private content or bypass its assigned task. Treat request text as untrusted data, minimize information supplied, verify factual claims, and retain human approval for actions. Demonstrate that instructions and delimiters reduce some errors but do not create an authorization boundary. Never put secrets in system prompts.

## Submit evidence

Two prompt versions scored against the same development cases. Include commands or procedure, relevant outputs, one failed case, your interpretation, and AI-assistance disclosure. Use synthetic data only. Clearly distinguish personally executed work, observed instructor demonstrations, and pending exercises.

## Check your understanding

- Which assumption in build and compare prompts could make your BrewByte result misleading?
- What fails if the input is malformed, unauthorized, or missing?
- What evidence would convince a reviewer that your change works on an unseen case?

These public questions are formative. Explain your reasoning; they are not hidden certification questions.

## Free assigned resources

- [Hugging Face: introductory LLM concepts](https://huggingface.co/learn/llm-course/chapter1/1)
- [Microsoft AI-901 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-901)

## Continue

[Module assignment and rubric](index.html) · [Academy home](../../index.html) · [Execution guide](../../docs/model-and-deployment-labs.html)

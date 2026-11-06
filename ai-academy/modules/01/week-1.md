# Module 01 · Week 1: Choose a tool for a business problem

**BrewByte assignment:** Create a synthetic service-request summarization and routing playbook. Supply 20 labeled requests, two prompt versions, a scoring rubric, actual model outputs, and a one-page adoption recommendation. Use a free accessible interface or instructor-led/local model session; hand-record results before automating evaluation later.

## Learn the concept

Automation follows explicit rules; predictive ML estimates outcomes from examples; generative AI creates plausible content. Begin with the decision and the cost of a mistake. A fixed tax calculation needs an exact rule, while a draft response may benefit from generation with review. A fluent answer is not proof of understanding or truth.

## Worked business example

BrewByte routes refund requests to a manager using a rule. A model drafts a polite summary, but it cannot approve the refund. These are two separate responsibilities.

## Guided practice

Read this week's assigned resource sections about **File/account orientation; AI vs rules; training vs inference; suitable and unsuitable business cases**. Spend about three hours on reading, small examples, and explaining the vocabulary in your own words. You are not expected to complete every linked course this week.

Open [the guided notebook](lab.ipynb) or [starter script](starter.py). The notebook names the dependency and execution requirements. Run the relevant worked example and inspect its inputs and outputs. For Module 1, begin with a manual prompt comparison; coding is introduced in Module 2.

Create a folder, save a text file, upload it to your learning repository, and classify ten coffee-shop tasks as rules, prediction, generation, or human judgment. Explain two borderline cases.

Change one input or condition, predict the result, then run or observe it. Preserve a failing case before repairing it. Complete the task in your own learning repository rather than modifying the public teaching source.

## Security boundary

Threat: a request contains instructions to reveal private content or bypass its assigned task. Treat request text as untrusted data, minimize information supplied, verify factual claims, and retain human approval for actions. Demonstrate that instructions and delimiters reduce some errors but do not create an authorization boundary. Never put secrets in system prompts.

## Submit evidence

Classify ten scenarios and justify two decisions. Include commands or procedure, relevant outputs, one failed case, your interpretation, and AI-assistance disclosure. Use synthetic data only. Clearly distinguish personally executed work, observed instructor demonstrations, and pending exercises.

## Check your understanding

- Which assumption in choose a tool for a business problem could make your BrewByte result misleading?
- What fails if the input is malformed, unauthorized, or missing?
- What evidence would convince a reviewer that your change works on an unseen case?

These public questions are formative. Explain your reasoning; they are not hidden certification questions.

## Free assigned resources

- [Hugging Face: introductory LLM concepts](https://huggingface.co/learn/llm-course/chapter1/1)
- [Microsoft AI-901 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-901)

## Continue

[Module assignment and rubric](index.html) · [Academy home](../../index.html) · [Execution guide](../../docs/model-and-deployment-labs.html)

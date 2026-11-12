# Module 01: Introduction to AI, Automation & Prompt Engineering

Quarter 1 · Four weeks · 12–15 hours per week · Pilot learning material

## Learning objectives

Students will distinguish deterministic automation, predictive ML, and generative AI using workplace examples; explain tokens, context windows, probabilistic generation, and hallucination in plain language; design a prompt with task, context, constraints, examples, and output format; compare prompt versions against a rubric; and decide when a human or conventional software should perform the task.

## Certification alignment

S1.1, S1.3, S4.2; AWS 1.1–1.2, 2.1–2.2, 3.2; AI-901 model/workload concepts, responsible AI, and prompt design. Coding is not required yet.

These are partial curriculum mappings, not complete exam coverage or endorsement. See the [blueprint](../../docs/curriculum-blueprint.html) for versions and platform gaps.

## Weekly lessons

- [Week 1: Choose a tool for a business problem](week-1.html)
- [Week 2: Understand LLM limits](week-2.html)
- [Week 3: Build and compare prompts](week-3.html)
- [Week 4: Evaluate and govern workplace use](week-4.html)

## Proof-of-work project: 01-prompt-evaluation-playbook

Create a synthetic service-request summarization and routing playbook. Supply 20 labeled requests, two prompt versions, a scoring rubric, actual model outputs, and a one-page adoption recommendation. Use a free accessible interface or instructor-led/local model session; hand-record results before automating evaluation later.

## Acceptance evidence

On a separate set of ten previously unseen requests, achieve at least 8/10 correct routes and schema-conforming outputs; make no unsupported factual additions; document failures and required review. Record the model/date/settings available to the student. Report these as small-sample classroom results, not business performance guarantees.

## Security integration

Threat: a request contains instructions to reveal private content or bypass its assigned task. Treat request text as untrusted data, minimize information supplied, verify factual claims, and retain human approval for actions. Demonstrate that instructions and delimiters reduce some errors but do not create an authorization boundary. Never put secrets in system prompts.

## Lab access

- [Guided notebook](lab.ipynb)
- [Starter Python script](starter.py)
- [Open notebook in Colab](https://colab.research.google.com/github/jdmc-services/brewbyte-risk-management-lab/blob/main/ai-academy/modules/01/lab.ipynb) — available after the reviewed branch is merged
- [Live-model and deployment instructions](../../docs/model-and-deployment-labs.html)
- [Shared synthetic dataset guide](../../data/README.md)
- [Raw sales CSV](../../data/sales.csv) · [Synthetic tickets CSV](../../data/tickets.csv)

Run from the repository root: `python ai-academy/modules/01/starter.py`. Module 4 needs the optional classical-ML environment. The default examples for generative modules are explicitly labeled fixtures/baselines.

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

- [Hugging Face: introductory LLM concepts](https://huggingface.co/learn/llm-course/chapter1/1)
- [Microsoft AI-901 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-901)

[Academy home](../../index.html) · [Course guide](../../docs/start-here.html)

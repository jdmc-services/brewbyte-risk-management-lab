# Module 11 · Week 1: Inventory the use case and owners

**BrewByte assignment:** Produce a short application/system card, an AI inventory entry, data-flow map, RACI, ten-risk register, control/evidence matrix, supplier questionnaire, monitoring/incident plan, and a two-page release memo. Apply the pack to the actual student application, including known weaknesses.

## Learn the concept

Governance starts with knowing which system exists, what it is intended to do, who is accountable, and who may be harmed. A system card should state prohibited uses as well as intended ones. A RACI clarifies decisions but does not transfer accountability to a model or vendor.

## Worked business example

BrewByte operations owns inventory recommendations; a named human role approves ordering changes. The assistant supplier does not become accountable for every business decision.

## Guided practice

Read this week's assigned resource sections about **AI inventory, stakeholders, intended/prohibited uses, accountable owners**. Spend about three hours on reading, small examples, and explaining the vocabulary in your own words. You are not expected to complete every linked course this week.

Open [the guided notebook](lab.ipynb) or [starter script](starter.py). The notebook names the dependency and execution requirements. Run the relevant worked example and inspect its inputs and outputs. For Module 1, begin with a manual prompt comparison; coding is introduced in Module 2.

Create an inventory entry, stakeholder map, RACI, and short system card for your actual application. Include data sources, users, model dependencies, and prohibited uses.

Change one input or condition, predict the result, then run or observe it. Preserve a failing case before repairing it. Complete the task in your own learning repository rather than modifying the public teaching source.

## Security boundary

Integrate privacy, fairness, transparency, data residency, retention, model/supplier change control, shadow AI, and human oversight. Use deterministic policy enforcement as the required low-compute path; optionally compare NeMo Guardrails or a suitable Llama Guard model. Evaluate their model/backend requirements and license. Guardrails are fallible and do not confer legal compliance.

## Submit evidence

Inventory, RACI, system card, and scope statement. Include commands or procedure, relevant outputs, one failed case, your interpretation, and AI-assistance disclosure. Use synthetic data only. Clearly distinguish personally executed work, observed instructor demonstrations, and pending exercises.

## Check your understanding

- Which assumption in inventory the use case and owners could make your BrewByte result misleading?
- What fails if the input is malformed, unauthorized, or missing?
- What evidence would convince a reviewer that your change works on an unseen case?

These public questions are formative. Explain your reasoning; they are not hidden certification questions.

## Free assigned resources

- [NIST AI RMF Playbook](https://airc.nist.gov/airmf-resources/playbook/)
- [OECD AI Principles](https://oecd.ai/en/ai-principles)
- [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails)

## Continue

[Module assignment and rubric](index.html) · [Academy home](../../index.html) · [Execution guide](../../docs/model-and-deployment-labs.html)

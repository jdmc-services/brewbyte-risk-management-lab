# Module 11 · Week 4: Defend a release recommendation

**BrewByte assignment:** Produce a short application/system card, an AI inventory entry, data-flow map, RACI, ten-risk register, control/evidence matrix, supplier questionnaire, monitoring/incident plan, and a two-page release memo. Apply the pack to the actual student application, including known weaknesses.

## Learn the concept

A release decision should state scope, evidence, remaining risks, accountable approver, and conditions for rollback or reassessment. Legal applicability depends on the actual processing and jurisdiction. Distinguish voluntary frameworks from legal duties and avoid claiming compliance from a small classroom demonstration.

## Worked business example

A manager approves a limited staff-only pilot while deferring autonomous actions. The memo records unresolved model errors and a stop condition after any cross-role exposure.

## Guided practice

Read this week's assigned resource sections about **Legal applicability scenario, exceptions, residual risk, governance board simulation**. Spend about three hours on reading, small examples, and explaining the vocabulary in your own words. You are not expected to complete every linked course this week.

Open [the guided notebook](lab.ipynb) or [starter script](starter.py). The notebook names the dependency and execution requirements. Run the relevant worked example and inspect its inputs and outputs. For Module 1, begin with a manual prompt comparison; coding is introduced in Module 2.

Present a two-page approve/defer/reject memo supported by your controls and tests. Include supplier questions, retention, incident handling, exceptions, and evidence gaps.

Change one input or condition, predict the result, then run or observe it. Preserve a failing case before repairing it. Complete the task in your own learning repository rather than modifying the public teaching source.

## Security boundary

Integrate privacy, fairness, transparency, data residency, retention, model/supplier change control, shadow AI, and human oversight. Use deterministic policy enforcement as the required low-compute path; optionally compare NeMo Guardrails or a suitable Llama Guard model. Evaluate their model/backend requirements and license. Guardrails are fallible and do not confer legal compliance.

## Submit evidence

Release memo and defensible approve/defer/reject decision. Include commands or procedure, relevant outputs, one failed case, your interpretation, and AI-assistance disclosure. Use synthetic data only. Clearly distinguish personally executed work, observed instructor demonstrations, and pending exercises.

## Check your understanding

- Which assumption in defend a release recommendation could make your BrewByte result misleading?
- What fails if the input is malformed, unauthorized, or missing?
- What evidence would convince a reviewer that your change works on an unseen case?

These public questions are formative. Explain your reasoning; they are not hidden certification questions.

## Free assigned resources

- [NIST AI RMF Playbook](https://airc.nist.gov/airmf-resources/playbook/)
- [OECD AI Principles](https://oecd.ai/en/ai-principles)
- [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails)

## Continue

[Module assignment and rubric](index.html) · [Academy home](../../index.html) · [Execution guide](../../docs/model-and-deployment-labs.html)

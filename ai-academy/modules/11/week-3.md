# Module 11 · Week 3: Implement and evaluate a policy

**BrewByte assignment:** Produce a short application/system card, an AI inventory entry, data-flow map, RACI, ten-risk register, control/evidence matrix, supplier questionnaire, monitoring/incident plan, and a two-page release memo. Apply the pack to the actual student application, including known weaknesses.

## Learn the concept

A guardrail must enforce an observable policy and be evaluated against permitted and prohibited cases. Deterministic rules can enforce narrow conditions; model-based classifiers offer broader judgments but are fallible. Neither replaces authentication, authorization, or an application-specific release decision.

## Worked business example

A public request for a manager-only document is denied by access rules. A toxicity classifier may be an additional filter, but it cannot decide who is a manager.

## Guided practice

Read this week's assigned resource sections about **Testable policy, deterministic/optional model guardrails, retention and supplier review**. Spend about three hours on reading, small examples, and explaining the vocabulary in your own words. You are not expected to complete every linked course this week.

Open [the guided notebook](lab.ipynb) or [starter script](starter.py). The notebook names the dependency and execution requirements. Run the relevant worked example and inspect its inputs and outputs. For Module 1, begin with a manual prompt comparison; coding is introduced in Module 2.

Implement one policy in code and test twenty permitted and twenty prohibited cases. Report bypasses and false rejections. Optionally compare a supported NeMo or Llama Guard configuration.

Change one input or condition, predict the result, then run or observe it. Preserve a failing case before repairing it. Complete the task in your own learning repository rather than modifying the public teaching source.

## Security boundary

Integrate privacy, fairness, transparency, data residency, retention, model/supplier change control, shadow AI, and human oversight. Use deterministic policy enforcement as the required low-compute path; optionally compare NeMo Guardrails or a suitable Llama Guard model. Evaluate their model/backend requirements and license. Guardrails are fallible and do not confer legal compliance.

## Submit evidence

Implemented guardrail and evaluation report. Include commands or procedure, relevant outputs, one failed case, your interpretation, and AI-assistance disclosure. Use synthetic data only. Clearly distinguish personally executed work, observed instructor demonstrations, and pending exercises.

## Check your understanding

- Which assumption in implement and evaluate a policy could make your BrewByte result misleading?
- What fails if the input is malformed, unauthorized, or missing?
- What evidence would convince a reviewer that your change works on an unseen case?

These public questions are formative. Explain your reasoning; they are not hidden certification questions.

## Free assigned resources

- [NIST AI RMF Playbook](https://airc.nist.gov/airmf-resources/playbook/)
- [OECD AI Principles](https://oecd.ai/en/ai-principles)
- [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails)

## Continue

[Module assignment and rubric](index.html) · [Academy home](../../index.html) · [Execution guide](../../docs/model-and-deployment-labs.html)

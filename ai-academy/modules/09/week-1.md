# Module 09 · Week 1: Build an actionable threat model

**BrewByte assignment:** Harden Module 8 with an OWASP 2026 traceability matrix, a documented attack set, access checks, safe rendering, tool restrictions, request limits, and security regression tests. For model extraction, inversion, and membership inference, perform a bounded conceptual or toy-model demonstration and discuss limits; do not claim to prevent all variants.

## Learn the concept

List assets, attacker goals, entry points, and trust boundaries before selecting defenses. Use OWASP as a risk taxonomy and MITRE ATLAS to examine adversary behavior. A threat model must connect each material risk to a concrete control and test; naming a framework is not itself a defense.

## Worked business example

Assets include customer data, policy documents, credentials, tool permissions, model integrity, and service capacity. Each has a different failure consequence and responsible owner.

## Guided practice

Read this week's assigned resource sections about **Assets, attacker goals, entry points, STRIDE-style boundaries, OWASP/ATLAS mapping**. Spend about three hours on reading, small examples, and explaining the vocabulary in your own words. You are not expected to complete every linked course this week.

Open [the guided notebook](lab.ipynb) or [starter script](starter.py). The notebook names the dependency and execution requirements. Run the relevant worked example and inspect its inputs and outputs. For Module 1, begin with a manual prompt comparison; coding is introduced in Module 2.

Draw the assistant data flow, identify five attacker goals, and map relevant OWASP 2026 categories to controls and measurable tests. Keep identifier editions explicit.

Change one input or condition, predict the result, then run or observe it. Preserve a failing case before repairing it. Complete the task in your own learning repository rather than modifying the public teaching source.

## Security boundary

Apply deny-by-default server-side permissions, read-only/allowlisted tools, human approval for consequential actions, output escaping, safe deserialization, dependency/model provenance, quotas/timeouts, and log minimization. Prompts, safety classifiers, and model refusals supplement these boundaries rather than enforce them alone.

## Submit evidence

Prioritized threat model and attack-case plan. Include commands or procedure, relevant outputs, one failed case, your interpretation, and AI-assistance disclosure. Use synthetic data only. Clearly distinguish personally executed work, observed instructor demonstrations, and pending exercises.

## Check your understanding

- Which assumption in build an actionable threat model could make your BrewByte result misleading?
- What fails if the input is malformed, unauthorized, or missing?
- What evidence would convince a reviewer that your change works on an unseen case?

These public questions are formative. Explain your reasoning; they are not hidden certification questions.

## Free assigned resources

- [OWASP canonical 2026 source](https://github.com/GenAI-Security-Project/GenAI-LLM-Top10)
- [MITRE ATLAS](https://atlas.mitre.org/)
- [garak scanner](https://github.com/NVIDIA/garak)

## Continue

[Module assignment and rubric](index.html) · [Academy home](../../index.html) · [Execution guide](../../docs/model-and-deployment-labs.html)

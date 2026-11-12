# Module 09 · Week 3: Layer controls outside the model

**BrewByte assignment:** Harden Module 8 with an OWASP 2026 traceability matrix, a documented attack set, access checks, safe rendering, tool restrictions, request limits, and security regression tests. For model extraction, inversion, and membership inference, perform a bounded conceptual or toy-model demonstration and discuss limits; do not claim to prevent all variants.

## Learn the concept

Deny-by-default permissions, scoped read-only tools, schema checks, output escaping, quotas, and provenance checks address different risks. A safety classifier may miss an attack or reject a valid request. Separate identity and action approval from generation. Never deserialize an untrusted model artifact or execute arbitrary generated code.

## Worked business example

Even if a model asks to delete a file, the read-only tool registry contains no delete operation. A missing permission fails independently of wording or model confidence.

## Guided practice

Read this week's assigned resource sections about **Layered mitigations, access enforcement, model/supply-chain controls, budgets**. Spend about three hours on reading, small examples, and explaining the vocabulary in your own words. You are not expected to complete every linked course this week.

Open [the guided notebook](lab.ipynb) or [starter script](starter.py). The notebook names the dependency and execution requirements. Run the relevant worked example and inspect its inputs and outputs. For Module 1, begin with a manual prompt comparison; coding is introduced in Module 2.

Implement one control per trust boundary, then rerun attacks and benign cases. Explain which failures the model cannot cause because the capability is absent.

Change one input or condition, predict the result, then run or observe it. Preserve a failing case before repairing it. Complete the task in your own learning repository rather than modifying the public teaching source.

## Security boundary

Apply deny-by-default server-side permissions, read-only/allowlisted tools, human approval for consequential actions, output escaping, safe deserialization, dependency/model provenance, quotas/timeouts, and log minimization. Prompts, safety classifiers, and model refusals supplement these boundaries rather than enforce them alone.

## Submit evidence

Hardened application and control tests. Include commands or procedure, relevant outputs, one failed case, your interpretation, and AI-assistance disclosure. Use synthetic data only. Clearly distinguish personally executed work, observed instructor demonstrations, and pending exercises.

## Check your understanding

- Which assumption in layer controls outside the model could make your BrewByte result misleading?
- What fails if the input is malformed, unauthorized, or missing?
- What evidence would convince a reviewer that your change works on an unseen case?

These public questions are formative. Explain your reasoning; they are not hidden certification questions.

## Free assigned resources

- [OWASP canonical 2026 source](https://github.com/GenAI-Security-Project/GenAI-LLM-Top10)
- [MITRE ATLAS](https://atlas.mitre.org/)
- [garak scanner](https://github.com/NVIDIA/garak)

## Continue

[Module assignment and rubric](index.html) · [Academy home](../../index.html) · [Execution guide](../../docs/model-and-deployment-labs.html)

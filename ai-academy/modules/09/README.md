# Module 09: Securing AI Systems & Adversarial Defense

Quarter 3 · Four weeks · 12–15 hours per week · Pilot learning material

## Learning objectives

Students will build an asset/trust-boundary threat model; connect threats to OWASP and MITRE ATLAS; reproduce safe attacks in their own isolated lab; implement layered controls; and measure attack success and benign-request rejection before and after a change.

## Certification alignment

S2.1–2.6; AWS 3.2, 5.1; AI-901 responsible AI with additional secure-development practice.

These are partial curriculum mappings, not complete exam coverage or endorsement. See the [blueprint](../../docs/curriculum-blueprint.html) for versions and platform gaps.

## Weekly lessons

- [Week 1: Build an actionable threat model](week-1.html)
- [Week 2: Reproduce safe failures](week-2.html)
- [Week 3: Layer controls outside the model](week-3.html)
- [Week 4: Measure residual risk honestly](week-4.html)

## Proof-of-work project: 09-ai-security-assurance-lab

Harden Module 8 with an OWASP 2026 traceability matrix, a documented attack set, access checks, safe rendering, tool restrictions, request limits, and security regression tests. For model extraction, inversion, and membership inference, perform a bounded conceptual or toy-model demonstration and discuss limits; do not claim to prevent all variants.

## Acceptance evidence

At least 40 cases across the relevant threat categories plus 20 benign cases. Give each case an expected result and severity. Demonstrate zero bypasses in seeded authorization/tool-permission tests and no secret exposure in the defined test suite; report residual injection failures honestly. Test results do not prove universal security. A scanner run without reviewed findings is insufficient.

## Security integration

Apply deny-by-default server-side permissions, read-only/allowlisted tools, human approval for consequential actions, output escaping, safe deserialization, dependency/model provenance, quotas/timeouts, and log minimization. Prompts, safety classifiers, and model refusals supplement these boundaries rather than enforce them alone.

## Lab access

- [Guided notebook](lab.ipynb)
- [Starter Python script](starter.py)
- [Open notebook in Colab](https://colab.research.google.com/github/jdmc-services/brewbyte-risk-management-lab/blob/main/ai-academy/modules/09/lab.ipynb) — available after the reviewed branch is merged
- [Live-model and deployment instructions](../../docs/model-and-deployment-labs.html)
- [Shared synthetic dataset guide](../../data/README.md)
- [Raw sales CSV](../../data/sales.csv) · [Synthetic tickets CSV](../../data/tickets.csv)

Run from the repository root: `python ai-academy/modules/09/starter.py`. Module 4 needs the optional classical-ML environment. The default examples for generative modules are explicitly labeled fixtures/baselines.

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

- [OWASP canonical 2026 source](https://github.com/GenAI-Security-Project/GenAI-LLM-Top10)
- [MITRE ATLAS](https://atlas.mitre.org/)
- [garak scanner](https://github.com/NVIDIA/garak)

[Academy home](../../index.html) · [Course guide](../../docs/start-here.html)

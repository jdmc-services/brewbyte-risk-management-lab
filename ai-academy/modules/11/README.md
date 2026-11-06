# Module 11: AI Governance, Risk & Compliance

Quarter 4 · Four weeks · 12–15 hours per week · Pilot learning material

## Learning objectives

Students will inventory an AI use case and assign owners; organize risks using NIST Govern/Map/Measure/Manage; assess impacts and evidence; write proportionate AI-use and data policies; implement a testable guardrail; and communicate a release decision to an executive audience.

## Certification alignment

S4.1–4.3, S2.2, S2.5; AWS 4.1–4.2, 5.2; AI-901 responsible AI principles.

These are partial curriculum mappings, not complete exam coverage or endorsement. See the [blueprint](../../docs/curriculum-blueprint.html) for versions and platform gaps.

## Weekly lessons

- [Week 1: Inventory the use case and owners](week-1.html)
- [Week 2: Connect risk to evidence](week-2.html)
- [Week 3: Implement and evaluate a policy](week-3.html)
- [Week 4: Defend a release recommendation](week-4.html)

## Proof-of-work project: 11-ai-governance-release-pack

Produce a short application/system card, an AI inventory entry, data-flow map, RACI, ten-risk register, control/evidence matrix, supplier questionnaire, monitoring/incident plan, and a two-page release memo. Apply the pack to the actual student application, including known weaknesses.

## Acceptance evidence

Every material risk has an owner, mitigation, evidence pointer, residual rating, and review trigger. Each governance claim must link to a test or clearly identify missing evidence. Test at least 20 prohibited and 20 permitted cases against one implemented policy, reporting bypasses and false rejections. An independent reviewer should reproduce the decision from the supplied record.

## Security integration

Integrate privacy, fairness, transparency, data residency, retention, model/supplier change control, shadow AI, and human oversight. Use deterministic policy enforcement as the required low-compute path; optionally compare NeMo Guardrails or a suitable Llama Guard model. Evaluate their model/backend requirements and license. Guardrails are fallible and do not confer legal compliance.

## Lab access

- [Guided notebook](lab.ipynb)
- [Starter Python script](starter.py)
- [Open notebook in Colab](https://colab.research.google.com/github/jdmc-services/brewbyte-risk-management-lab/blob/main/ai-academy/modules/11/lab.ipynb) — available after the reviewed branch is merged
- [Live-model and deployment instructions](../../docs/model-and-deployment-labs.html)
- [Shared synthetic dataset guide](../../data/README.md)
- [Raw sales CSV](../../data/sales.csv) · [Synthetic tickets CSV](../../data/tickets.csv)

Run from the repository root: `python ai-academy/modules/11/starter.py`. Module 4 needs the optional classical-ML environment. The default examples for generative modules are explicitly labeled fixtures/baselines.

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

- [NIST AI RMF Playbook](https://airc.nist.gov/airmf-resources/playbook/)
- [OECD AI Principles](https://oecd.ai/en/ai-principles)
- [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails)

[Academy home](../../index.html) · [Course guide](../../docs/start-here.html)

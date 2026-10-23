# Module 06: Security in the AI Lifecycle & Data Protection

Quarter 2 · Four weeks · 12–15 hours per week · Pilot learning material

## Learning objectives

Students will map a data/model lifecycle and its trust boundaries; classify data; detect selected PII types; implement minimization and controlled data release; detect seeded integrity problems; and distinguish laws, voluntary frameworks, and organizational policies.

## Certification alignment

S1.2–1.3, S2.4, S4.3; AWS 5.1–5.2; AI-901 privacy/security principles.

These are partial curriculum mappings, not complete exam coverage or endorsement. See the [blueprint](../../docs/curriculum-blueprint.html) for versions and platform gaps.

## Weekly lessons

- [Week 1: Map data and trust boundaries](week-1.html)
- [Week 2: Measure redaction instead of assuming privacy](week-2.html)
- [Week 3: Control ingestion and integrity](week-3.html)
- [Week 4: Separate compliance evidence from claims](week-4.html)

## Proof-of-work project: 06-protected-data-pipeline

Ingest synthetic tickets, validate schema and source manifests, identify and redact supported PII types, quarantine suspicious records, and write a release report. Keep raw files and sanitized outputs separate. Include a deletion/retention demonstration and mock access roles.

## Acceptance evidence

Evaluate at least 100 labeled synthetic PII examples and report entity-level precision/recall by type. Test that known synthetic identifiers do not appear in released logs/exports. Detect a seeded file alteration and record quarantined cases. State which poisoning scenarios remain undetected; hashes cannot identify semantically poisoned but correctly hashed data.

## Security integration

Model unauthorized access, accidental logging, malicious training rows, and excessive retention. Introduce TLS and at-rest encryption concepts, identity-bound permissions, access logs, provenance, and human quarantine review. Redaction is imperfect, pseudonymization is not necessarily anonymization, and sanitized output is not automatically safe for publication.

## Lab access

- [Guided notebook](lab.ipynb)
- [Starter Python script](starter.py)
- [Open notebook in Colab](https://colab.research.google.com/github/jdmc-services/brewbyte-risk-management-lab/blob/main/ai-academy/modules/06/lab.ipynb) — available after the reviewed branch is merged
- [Live-model and deployment instructions](../../docs/model-and-deployment-labs.html)
- [Shared synthetic dataset guide](../../data/README.md)
- [Raw sales CSV](../../data/sales.csv) · [Synthetic tickets CSV](../../data/tickets.csv)

Run from the repository root: `python ai-academy/modules/06/starter.py`. Module 4 needs the optional classical-ML environment. The default examples for generative modules are explicitly labeled fixtures/baselines.

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

- [Presidio recognizers and evaluation](https://presidio.dataprivacystack.org/)
- [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework)
- [Official GDPR text](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng)

[Academy home](../../index.html) · [Course guide](../../docs/start-here.html)

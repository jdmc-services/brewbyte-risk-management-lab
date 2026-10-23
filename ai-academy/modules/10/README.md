# Module 10: AI-Assisted Security & Operations

Quarter 4 · Four weeks · 12–15 hours per week · Pilot learning material

## Learning objectives

Students will parse and normalize synthetic security events; correlate alerts with rules; compare rule-based and ML anomaly detection; generate evidence-linked incident summaries; implement a human-reviewed automation workflow; and identify AI-enabled impersonation or misinformation risks.

## Certification alignment

S2.5, S3.1–3.3; AWS 1.2–1.3, 3.4, 5.1; AI-901 app/agent and text-analysis skills when practiced on the named platform.

These are partial curriculum mappings, not complete exam coverage or endorsement. See the [blueprint](../../docs/curriculum-blueprint.html) for versions and platform gaps.

## Weekly lessons

- [Week 1: Normalize security evidence](week-1.html)
- [Week 2: Compare rules and anomaly detection](week-2.html)
- [Week 3: Draft evidence-linked incident tickets](week-3.html)
- [Week 4: Validate automation and recover from errors](week-4.html)

## Proof-of-work project: 10-security-triage-assistant

Process 1,000 synthetic login/endpoint events containing ten known incident storylines. Correlate events, compare rules with IsolationForest or a similar small baseline, and draft incident tickets with event IDs, severity rationale, uncertainty, and next investigative steps. All response actions are dry-run proposals.

## Acceptance evidence

Report storyline-level precision/recall, duplicate-alert reduction, unsupported-claim rate, and measured review time on a defined sample. Compare against a deterministic baseline. Reject attempts to trigger real account changes, network blocks, or arbitrary tools. Evaluate an incident-summary model separately from event-detection rules.

## Security integration

Treat logs as attacker-controlled text, preserve evidence identifiers/timestamps, redact sensitive data, scope agent tools, and require approval outside the model. Use synthetic impersonation/deepfake scenarios for defensive analysis; no impersonation of real people is needed.

## Lab access

- [Guided notebook](lab.ipynb)
- [Starter Python script](starter.py)
- [Open notebook in Colab](https://colab.research.google.com/github/jdmc-services/brewbyte-risk-management-lab/blob/main/ai-academy/modules/10/lab.ipynb) — available after the reviewed branch is merged
- [Live-model and deployment instructions](../../docs/model-and-deployment-labs.html)
- [Shared synthetic dataset guide](../../data/README.md)
- [Raw sales CSV](../../data/sales.csv) · [Synthetic tickets CSV](../../data/tickets.csv)

Run from the repository root: `python ai-academy/modules/10/starter.py`. Module 4 needs the optional classical-ML environment. The default examples for generative modules are explicitly labeled fixtures/baselines.

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

- [MITRE ATT&CK](https://attack.mitre.org/)
- [scikit-learn anomaly detection](https://scikit-learn.org/stable/modules/outlier_detection.html)
- [NIST incident response](https://csrc.nist.gov/projects/incident-response)

[Academy home](../../index.html) · [Course guide](../../docs/start-here.html)

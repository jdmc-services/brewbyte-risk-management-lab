# Module 05: Model Training, Evaluation & Validation

Quarter 2 · Four weeks · 12–15 hours per week · Pilot learning material

## Learning objectives

Students will design train/validation/test partitions; prevent group/time leakage; use cross-validation within training data; calculate and interpret precision, recall, F1, MAE/RMSE, and confusion matrices; choose a threshold using business costs; and describe drift and uncertainty.

## Certification alignment

S1.3, S2.5; AWS 1.3, 3.4, 4.1–4.2; AI-901 responsible AI/model choice. Foundation-model evaluation is introduced here and applied in Modules 7–9.

These are partial curriculum mappings, not complete exam coverage or endorsement. See the [blueprint](../../docs/curriculum-blueprint.html) for versions and platform gaps.

## Weekly lessons

- [Week 1: Protect the evaluation boundary](week-1.html)
- [Week 2: Choose metrics with consequences](week-2.html)
- [Week 3: Tune within training data](week-3.html)
- [Week 4: Make a release decision from evidence](week-4.html)

## Proof-of-work project: 05-evaluation-and-leakage-audit

Extend Module 4 into an imbalanced escalation classifier. Deliberately add a post-outcome leakage feature, expose misleading performance, remove it, and rebuild the evaluation. Compare rule-based, dummy, and trained approaches.

## Acceptance evidence

Freeze the test partition; select preprocessing, hyperparameters, and thresholds using training/validation only; evaluate the selected approach once on test data. Report class counts, confusion matrix, per-class metrics, and a simple bootstrap interval where appropriate. Document limitations of synthetic labels and small subgroup sizes.

## Security integration

Treat evaluation data and metric reports as integrity assets. Restrict edits, record dataset/model hashes and versions, and distinguish honest mistakes from deliberate metric manipulation. Never equate a language model's stated confidence with calibrated probability.

## Lab access

- [Guided notebook](lab.ipynb)
- [Starter Python script](starter.py)
- [Open notebook in Colab](https://colab.research.google.com/github/jdmc-services/brewbyte-risk-management-lab/blob/main/ai-academy/modules/05/lab.ipynb) — available after the reviewed branch is merged
- [Live-model and deployment instructions](../../docs/model-and-deployment-labs.html)
- [Shared synthetic dataset guide](../../data/README.md)
- [Raw sales CSV](../../data/sales.csv) · [Synthetic tickets CSV](../../data/tickets.csv)

Run from the repository root: `python ai-academy/modules/05/starter.py`. Module 4 needs the optional classical-ML environment. The default examples for generative modules are explicitly labeled fixtures/baselines.

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

- [scikit-learn Common Pitfalls](https://scikit-learn.org/stable/common_pitfalls.html)
- [Cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html)
- [Model evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html)

[Academy home](../../index.html) · [Course guide](../../docs/start-here.html)

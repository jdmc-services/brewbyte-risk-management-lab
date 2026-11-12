# Module 04: Supervised & Unsupervised Machine Learning

Quarter 2 · Four weeks · 12–15 hours per week · Pilot learning material

## Learning objectives

Students will identify features/labels; distinguish regression, classification, and clustering; train linear/logistic regression, decision trees, random forests, and a clustering model with scikit-learn; compare against a simple baseline; and explain predictions without treating clusters as verified categories.

## Certification alignment

S1.1, S1.3; AWS 1.1–1.3; AI-901 workload/model-selection concepts. Model implementation exceeds foundational certification expectations.

These are partial curriculum mappings, not complete exam coverage or endorsement. See the [blueprint](../../docs/curriculum-blueprint.html) for versions and platform gaps.

## Weekly lessons

- [Week 1: Frame a prediction and baseline](week-1.html)
- [Week 2: Fit linear and logistic models](week-2.html)
- [Week 3: Compare trees and forests](week-3.html)
- [Week 4: Explore clusters without inventing labels](week-4.html)

## Proof-of-work project: 04-ml-baseline-comparison

On reproducible synthetic business data, predict a numeric outcome, classify a ticket category, and explore customer/ticket clusters. Provide clear feature availability times, baselines, preprocessing pipelines, model comparisons, and a model card.

## Acceptance evidence

Execute all five model families, use splits fixed before training, and compare primary models with appropriate dummy baselines. Explain an observed error and the business cost of choosing the wrong model. There is no arbitrary universal accuracy threshold.

## Security integration

Identify label leakage, sensitive features, proxy attributes, and untrusted model downloads. Introduce train/test separation immediately; preprocessing learns only from training data. Use locally trained artifacts and explain unsafe deserialization risk.

## Lab access

- [Guided notebook](lab.ipynb)
- [Starter Python script](starter.py)
- [Open notebook in Colab](https://colab.research.google.com/github/jdmc-services/brewbyte-risk-management-lab/blob/main/ai-academy/modules/04/lab.ipynb) — available after the reviewed branch is merged
- [Live-model and deployment instructions](../../docs/model-and-deployment-labs.html)
- [Shared synthetic dataset guide](../../data/README.md)
- [Raw sales CSV](../../data/sales.csv) · [Synthetic tickets CSV](../../data/tickets.csv)

Run from the repository root: `python ai-academy/modules/04/starter.py`. Module 4 needs the optional classical-ML environment. The default examples for generative modules are explicitly labeled fixtures/baselines.

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

- [Inria scikit-learn course: predictive pipelines and models](https://inria.github.io/scikit-learn-mooc/)
- [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)

[Academy home](../../index.html) · [Course guide](../../docs/start-here.html)

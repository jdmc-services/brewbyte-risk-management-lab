# Module 03: Data Processing & Statistics for AI

Quarter 1 · Four weeks · 12–15 hours per week · Pilot learning material

## Learning objectives

Students will clean and join tabular data with pandas; manipulate arrays and shapes with NumPy; interpret mean/median, variance, standard deviation, percentiles, and outliers; explain sampling bias and correlation vs causation; and verify a pandas summary using SQL.

## Certification alignment

S1.2; AWS 1.1, 1.3, 5.1. Data skills support AI-901 without representing a separate named objective.

These are partial curriculum mappings, not complete exam coverage or endorsement. See the [blueprint](../../docs/curriculum-blueprint.html) for versions and platform gaps.

## Weekly lessons

- [Week 1: Represent data and inspect sources](week-1.html)
- [Week 2: Describe distributions honestly](week-2.html)
- [Week 3: Clean data with an audit trail](week-3.html)
- [Week 4: Verify analysis with SQL](week-4.html)

## Proof-of-work project: 03-data-quality-workbench

Process an instructor-provided, seeded dataset of 2,000 fictional tickets with duplicates, missing fields, inconsistent dates, invalid categories, and synthetic identifiers. Produce a reusable cleaning script, data dictionary, lineage record, SQLite queries, and a concise exploratory report.

## Acceptance evidence

Detect all intentionally seeded schema violations; account for every removed/changed row; reconcile pre/post counts; match three SQL summaries to pandas; and explain why a chosen missing-value treatment is appropriate. Statistical plots must include units, sample sizes, and relevant limitations.

## Security integration

Threats include accidental identifier disclosure, silent data corruption, and contaminated sources. Preserve an immutable source copy, validate schema and ranges, document provenance and transformation decisions, and limit exports. A hash establishes consistency relative to a trusted reference, not source trustworthiness or privacy. Explain why identifier removal alone may leave re-identification risk.

## Lab access

- [Guided notebook](lab.ipynb)
- [Starter Python script](starter.py)
- [Open notebook in Colab](https://colab.research.google.com/github/jdmc-services/brewbyte-risk-management-lab/blob/main/ai-academy/modules/03/lab.ipynb) — available after the reviewed branch is merged
- [Live-model and deployment instructions](../../docs/model-and-deployment-labs.html)
- [Shared synthetic dataset guide](../../data/README.md)
- [Raw sales CSV](../../data/sales.csv) · [Synthetic tickets CSV](../../data/tickets.csv)

Run from the repository root: `python ai-academy/modules/03/starter.py`. Module 4 needs the optional classical-ML environment. The default examples for generative modules are explicitly labeled fixtures/baselines.

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

- [pandas: reading, statistics, combining tables](https://pandas.pydata.org/docs/getting_started/intro_tutorials/)
- [NumPy absolute basics](https://numpy.org/doc/stable/user/absolute_beginners.html)
- [OpenStax statistics](https://openstax.org/details/books/introductory-statistics-2e)
- [SQLite language](https://www.sqlite.org/lang.html)

[Academy home](../../index.html) · [Course guide](../../docs/start-here.html)

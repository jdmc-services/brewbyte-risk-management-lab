# Module 02: Python Programming Essentials

Quarter 1 · Four weeks · 12–15 hours per week · Pilot learning material

## Learning objectives

Students will run Python in VS Code and Colab; use types, collections, branches, loops, and functions; read/write CSV and JSON; debug exceptions; write behavioral tests; create a virtual environment; and use a basic Git branch/commit/review workflow.

## Certification alignment

Enables S3.3 and the Python prerequisite for AI-901. Python implementation is an employability extension rather than a direct AIF-C01 objective.

These are partial curriculum mappings, not complete exam coverage or endorsement. See the [blueprint](../../docs/curriculum-blueprint.html) for versions and platform gaps.

## Weekly lessons

- [Week 1: Run Python and inspect values](week-1.html)
- [Week 2: Use control flow and functions](week-2.html)
- [Week 3: Read files and handle failure](week-3.html)
- [Week 4: Test and explain a program](week-4.html)

## Proof-of-work project: 02-ticket-intake-cli

Build a command-line program that reads synthetic requests, validates required fields, assigns a rule-based queue, and writes JSON summaries. Include a deliberately malformed input file and a repair exercise.

## Acceptance evidence

At least ten meaningful tests covering normal, empty, malformed, and oversized input; predictable exit/error behavior; a reproducible setup guide; and a live, unseen function change the student can explain.

## Security integration

Introduce confidentiality/integrity/availability, authentication vs authorization, least privilege, and basic client/server concepts. Validate data rather than executing it; prohibit `eval` on input and unsafe shell interpolation. Store no credentials in notebooks or commits; inspect dependencies and keep generated outputs free of sensitive content.

## Lab access

- [Guided notebook](lab.ipynb)
- [Starter Python script](starter.py)
- [Open notebook in Colab](https://colab.research.google.com/github/jdmc-services/brewbyte-risk-management-lab/blob/main/ai-academy/modules/02/lab.ipynb) — available after the reviewed branch is merged
- [Live-model and deployment instructions](../../docs/model-and-deployment-labs.html)
- [Shared synthetic dataset guide](../../data/README.md)
- [Raw sales CSV](../../data/sales.csv) · [Synthetic tickets CSV](../../data/tickets.csv)

Run from the repository root: `python ai-academy/modules/02/starter.py`. Module 4 needs the optional classical-ML environment. The default examples for generative modules are explicitly labeled fixtures/baselines.

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

- [CS50P: variables, conditions, loops, exceptions, tests, files](https://cs50.harvard.edu/python/)
- [VS Code Python setup](https://code.visualstudio.com/docs/python/python-tutorial)
- [GitHub Learn](https://learn.github.com/)

[Academy home](../../index.html) · [Course guide](../../docs/start-here.html)

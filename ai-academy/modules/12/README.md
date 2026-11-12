# Module 12: Capstone, Deployment & Career Launch

Quarter 4 · Four weeks · 12–15 hours per week · Pilot learning material

## Learning objectives

Students will package a tested AI application with FastAPI and containers; deploy/run it reproducibly; apply basic identity, secret, dependency, and logging controls; demonstrate rollback and failure recovery; document a portfolio honestly; and complete an interview explanation and unseen repair task.

## Certification alignment

S1.3, S2.2–2.5, S3.3; AWS 1.3, 2.3, 3.1, 5.1; AI-901 platform deployment/client skills only for executed Azure exercises. Docker and FastAPI implementation are broader employment skills.

These are partial curriculum mappings, not complete exam coverage or endorsement. See the [blueprint](../../docs/curriculum-blueprint.html) for versions and platform gaps.

## Weekly lessons

- [Week 1: Freeze a reliable vertical slice](week-1.html)
- [Week 2: Operate and recover a release](week-2.html)
- [Week 3: Review the release as a peer](week-3.html)
- [Week 4: Translate evidence into employment](week-4.html)

## Proof-of-work project: 12-secure-ai-operations-capstone

Integrate the protected dataset pipeline, ticket analytics, permission-aware policy assistant, measured model behavior, triage workflow, and governance release record. Narrow scope to a reliable vertical slice instead of integrating every experiment. Required deployment is reproducible local container execution; hosted cloud deployment is optional and clearly labeled.

## Acceptance evidence

A reviewer can follow a clean setup, run tests, start the container, issue an authenticated request, demonstrate a denied request, trigger a controlled failure, and roll back a release. Provide health checks, a monitoring sample, dependency versions, model/data provenance, an architecture diagram, known limitations, and a five-minute demo. Record actual measurements rather than declaring the app production-ready solely because it runs.

## Security integration

Non-root containers where feasible, minimal dependencies, secret injection rather than image-baked secrets, safe artifact loading, request/time limits, sanitized logs, least-privilege deployment, and dependency scans with reviewed findings. Public code can be showcased without exposing an unauthenticated model endpoint.

## Lab access

- [Guided notebook](lab.ipynb)
- [Starter Python script](starter.py)
- [Open notebook in Colab](https://colab.research.google.com/github/jdmc-services/brewbyte-risk-management-lab/blob/main/ai-academy/modules/12/lab.ipynb) — available after the reviewed branch is merged
- [Live-model and deployment instructions](../../docs/model-and-deployment-labs.html)
- [Shared synthetic dataset guide](../../data/README.md)
- [Raw sales CSV](../../data/sales.csv) · [Synthetic tickets CSV](../../data/tickets.csv)

Run from the repository root: `python ai-academy/modules/12/starter.py`. Module 4 needs the optional classical-ML environment. The default examples for generative modules are explicitly labeled fixtures/baselines.

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

- [FastAPI deployment](https://fastapi.tiangolo.com/deployment/)
- [Docker getting started](https://docs.docker.com/get-started/)
- [GitHub Actions](https://docs.github.com/en/actions)

[Academy home](../../index.html) · [Course guide](../../docs/start-here.html)

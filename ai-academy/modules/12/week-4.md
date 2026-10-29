# Module 12 · Week 4: Translate evidence into employment

**BrewByte assignment:** Integrate the protected dataset pipeline, ticket analytics, permission-aware policy assistant, measured model behavior, triage workflow, and governance release record. Narrow scope to a reliable vertical slice instead of integrating every experiment. Required deployment is reproducible local container execution; hosted cloud deployment is optional and clearly labeled.

## Learn the concept

A portfolio is strongest when it explains a business problem, an implementation decision, measured results, and limits. Tailor evidence to a role rather than listing every tool. Interviews often test debugging and tradeoffs; being able to explain and modify your own work matters more than polished generated prose.

## Worked business example

A junior application-support candidate demonstrates timeout handling, SQL checks, and a denied request. A governance-support candidate explains the risk decision and evidence behind the controls.

## Guided practice

Read this week's assigned resource sections about **Portfolio curation, résumé evidence, targeted applications, mock interview**. Spend about three hours on reading, small examples, and explaining the vocabulary in your own words. You are not expected to complete every linked course this week.

Open [the guided notebook](lab.ipynb) or [starter script](starter.py). The notebook names the dependency and execution requirements. Run the relevant worked example and inspect its inputs and outputs. For Module 1, begin with a manual prompt comparison; coding is introduced in Module 2.

Curate three showcase projects, record a five-minute demo, tailor a role-specific resume, and complete an unseen repair task. Identify skill gaps from current job descriptions without inventing employment outcomes.

Change one input or condition, predict the result, then run or observe it. Preserve a failing case before repairing it. Complete the task in your own learning repository rather than modifying the public teaching source.

## Security boundary

Non-root containers where feasible, minimal dependencies, secret injection rather than image-baked secrets, safe artifact loading, request/time limits, sanitized logs, least-privilege deployment, and dependency scans with reviewed findings. Public code can be showcased without exposing an unauthenticated model endpoint.

## Submit evidence

Three curated showcases, demo, role-specific résumé, and unseen repair. Include commands or procedure, relevant outputs, one failed case, your interpretation, and AI-assistance disclosure. Use synthetic data only. Clearly distinguish personally executed work, observed instructor demonstrations, and pending exercises.

## Check your understanding

- Which assumption in translate evidence into employment could make your BrewByte result misleading?
- What fails if the input is malformed, unauthorized, or missing?
- What evidence would convince a reviewer that your change works on an unseen case?

These public questions are formative. Explain your reasoning; they are not hidden certification questions.

## Free assigned resources

- [FastAPI deployment](https://fastapi.tiangolo.com/deployment/)
- [Docker getting started](https://docs.docker.com/get-started/)
- [GitHub Actions](https://docs.github.com/en/actions)

## Continue

[Module assignment and rubric](index.html) · [Academy home](../../index.html) · [Execution guide](../../docs/model-and-deployment-labs.html)

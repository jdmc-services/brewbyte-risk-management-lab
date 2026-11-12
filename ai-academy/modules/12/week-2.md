# Module 12 · Week 2: Operate and recover a release

**BrewByte assignment:** Integrate the protected dataset pipeline, ticket analytics, permission-aware policy assistant, measured model behavior, triage workflow, and governance release record. Narrow scope to a reliable vertical slice instead of integrating every experiment. Required deployment is reproducible local container execution; hosted cloud deployment is optional and clearly labeled.

## Learn the concept

Health checks, structured logs, bounded requests, and rollback make failures diagnosable. A healthy process does not mean the model is correct. Deployment evidence must identify the actual environment: running localhost is local execution, not cloud experience. Public endpoints require additional operational review.

## Worked business example

If a model backend is absent, the health response reports that limitation. A failed request should not expose a stack trace or credential in the response.

## Guided practice

Read this week's assigned resource sections about **CI checks, deployment, health/observability, failure/recovery**. Spend about three hours on reading, small examples, and explaining the vocabulary in your own words. You are not expected to complete every linked course this week.

Open [the guided notebook](lab.ipynb) or [starter script](starter.py). The notebook names the dependency and execution requirements. Run the relevant worked example and inspect its inputs and outputs. For Module 1, begin with a manual prompt comparison; coding is introduced in Module 2.

Run checks from a clean environment, start the API, issue authorized and unauthorized requests, trigger a controlled failure, and demonstrate rollback. Execute the optional cloud bridge only with approved limits.

Change one input or condition, predict the result, then run or observe it. Preserve a failing case before repairing it. Complete the task in your own learning repository rather than modifying the public teaching source.

## Security boundary

Non-root containers where feasible, minimal dependencies, secret injection rather than image-baked secrets, safe artifact loading, request/time limits, sanitized logs, least-privilege deployment, and dependency scans with reviewed findings. Public code can be showcased without exposing an unauthenticated model endpoint.

## Submit evidence

Local release, clean-run evidence, rollback record; optional cloud lab. Include commands or procedure, relevant outputs, one failed case, your interpretation, and AI-assistance disclosure. Use synthetic data only. Clearly distinguish personally executed work, observed instructor demonstrations, and pending exercises.

## Check your understanding

- Which assumption in operate and recover a release could make your BrewByte result misleading?
- What fails if the input is malformed, unauthorized, or missing?
- What evidence would convince a reviewer that your change works on an unseen case?

These public questions are formative. Explain your reasoning; they are not hidden certification questions.

## Free assigned resources

- [FastAPI deployment](https://fastapi.tiangolo.com/deployment/)
- [Docker getting started](https://docs.docker.com/get-started/)
- [GitHub Actions](https://docs.github.com/en/actions)

## Continue

[Module assignment and rubric](index.html) · [Academy home](../../index.html) · [Execution guide](../../docs/model-and-deployment-labs.html)

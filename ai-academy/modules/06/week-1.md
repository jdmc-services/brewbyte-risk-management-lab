# Module 06 · Week 1: Map data and trust boundaries

**BrewByte assignment:** Ingest synthetic tickets, validate schema and source manifests, identify and redact supported PII types, quarantine suspicious records, and write a release report. Keep raw files and sanitized outputs separate. Include a deletion/retention demonstration and mock access roles.

## Learn the concept

Confidentiality limits disclosure, integrity protects correctness, and availability supports timely access. Authentication establishes identity; authorization determines permitted actions. A data-flow diagram identifies sources, processors, storage, and boundary crossings so controls have a specific place to operate. Start by minimizing the data the use case needs.

## Worked business example

A public assistant does not need customer email addresses. A staff policy store requires authenticated access even when the model itself runs locally.

## Guided practice

Read this week's assigned resource sections about **Security primitives review, data classification, lifecycle, trust boundaries, retention**. Spend about three hours on reading, small examples, and explaining the vocabulary in your own words. You are not expected to complete every linked course this week.

Open [the guided notebook](lab.ipynb) or [starter script](starter.py). The notebook names the dependency and execution requirements. Run the relevant worked example and inspect its inputs and outputs. For Module 1, begin with a manual prompt comparison; coding is introduced in Module 2.

Draw the ticket-to-model data flow and classify fields. Assign permitted readers, retention periods, and deletion owners. Explain which boundary must reject an unauthorized request.

Change one input or condition, predict the result, then run or observe it. Preserve a failing case before repairing it. Complete the task in your own learning repository rather than modifying the public teaching source.

## Security boundary

Model unauthorized access, accidental logging, malicious training rows, and excessive retention. Introduce TLS and at-rest encryption concepts, identity-bound permissions, access logs, provenance, and human quarantine review. Redaction is imperfect, pseudonymization is not necessarily anonymization, and sanitized output is not automatically safe for publication.

## Submit evidence

Data-flow/threat diagram and classification policy. Include commands or procedure, relevant outputs, one failed case, your interpretation, and AI-assistance disclosure. Use synthetic data only. Clearly distinguish personally executed work, observed instructor demonstrations, and pending exercises.

## Check your understanding

- Which assumption in map data and trust boundaries could make your BrewByte result misleading?
- What fails if the input is malformed, unauthorized, or missing?
- What evidence would convince a reviewer that your change works on an unseen case?

These public questions are formative. Explain your reasoning; they are not hidden certification questions.

## Free assigned resources

- [Presidio recognizers and evaluation](https://presidio.dataprivacystack.org/)
- [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework)
- [Official GDPR text](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng)

## Continue

[Module assignment and rubric](index.html) · [Academy home](../../index.html) · [Execution guide](../../docs/model-and-deployment-labs.html)

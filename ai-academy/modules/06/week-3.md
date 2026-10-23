# Module 06 · Week 3: Control ingestion and integrity

**BrewByte assignment:** Ingest synthetic tickets, validate schema and source manifests, identify and redact supported PII types, quarantine suspicious records, and write a release report. Keep raw files and sanitized outputs separate. Include a deletion/retention demonstration and mock access roles.

## Learn the concept

A trusted manifest can identify a changed file, but a hash cannot judge whether the original content was malicious. Poisoning may alter labels or examples while retaining valid syntax. Separate intake, quarantine, review, and release. Permissions and provenance complement integrity checks rather than replacing them.

## Worked business example

An attacker changes training labels to route refunds incorrectly. A schema check still passes; label distribution review and provenance investigation may reveal the problem.

## Guided practice

Read this week's assigned resource sections about **Poisoning scenarios, provenance, trusted manifests, quarantine, role permissions**. Spend about three hours on reading, small examples, and explaining the vocabulary in your own words. You are not expected to complete every linked course this week.

Open [the guided notebook](lab.ipynb) or [starter script](starter.py). The notebook names the dependency and execution requirements. Run the relevant worked example and inspect its inputs and outputs. For Module 1, begin with a manual prompt comparison; coding is introduced in Module 2.

Modify a copied fixture and verify a manifest mismatch. Seed a syntactically valid bad label, show why hashing alone cannot reject it, and document a quarantine/review decision.

Change one input or condition, predict the result, then run or observe it. Preserve a failing case before repairing it. Complete the task in your own learning repository rather than modifying the public teaching source.

## Security boundary

Model unauthorized access, accidental logging, malicious training rows, and excessive retention. Introduce TLS and at-rest encryption concepts, identity-bound permissions, access logs, provenance, and human quarantine review. Redaction is imperfect, pseudonymization is not necessarily anonymization, and sanitized output is not automatically safe for publication.

## Submit evidence

Alteration/quarantine demonstrations and access tests. Include commands or procedure, relevant outputs, one failed case, your interpretation, and AI-assistance disclosure. Use synthetic data only. Clearly distinguish personally executed work, observed instructor demonstrations, and pending exercises.

## Check your understanding

- Which assumption in control ingestion and integrity could make your BrewByte result misleading?
- What fails if the input is malformed, unauthorized, or missing?
- What evidence would convince a reviewer that your change works on an unseen case?

These public questions are formative. Explain your reasoning; they are not hidden certification questions.

## Free assigned resources

- [Presidio recognizers and evaluation](https://presidio.dataprivacystack.org/)
- [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework)
- [Official GDPR text](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng)

## Continue

[Module assignment and rubric](index.html) · [Academy home](../../index.html) · [Execution guide](../../docs/model-and-deployment-labs.html)

# Module 06 · Week 2: Measure redaction instead of assuming privacy

**BrewByte assignment:** Ingest synthetic tickets, validate schema and source manifests, identify and redact supported PII types, quarantine suspicious records, and write a release report. Keep raw files and sanitized outputs separate. Include a deletion/retention demonstration and mock access roles.

## Learn the concept

PII detectors make both false positives and false negatives. Regex can recognize some structured patterns, while contextual entities need additional methods. Removing direct identifiers does not guarantee anonymity because combinations of remaining attributes may identify a person. Evaluate by entity type and preserve only the minimum necessary output.

## Worked business example

A regex can replace an example.invalid email but miss a name written in prose. A successful email test says nothing about names, account identifiers, or indirect identifiers.

## Guided practice

Read this week's assigned resource sections about **PII labels, detection, masking/redaction, minimization, test design**. Spend about three hours on reading, small examples, and explaining the vocabulary in your own words. You are not expected to complete every linked course this week.

Open [the guided notebook](lab.ipynb) or [starter script](starter.py). The notebook names the dependency and execution requirements. Run the relevant worked example and inspect its inputs and outputs. For Module 1, begin with a manual prompt comparison; coding is introduced in Module 2.

Run the baseline scrubber, create a labeled synthetic evaluation set, and report precision/recall by supported type. Compare with Presidio in an optional environment. List unsupported types explicitly.

Change one input or condition, predict the result, then run or observe it. Preserve a failing case before repairing it. Complete the task in your own learning repository rather than modifying the public teaching source.

## Security boundary

Model unauthorized access, accidental logging, malicious training rows, and excessive retention. Introduce TLS and at-rest encryption concepts, identity-bound permissions, access logs, provenance, and human quarantine review. Redaction is imperfect, pseudonymization is not necessarily anonymization, and sanitized output is not automatically safe for publication.

## Submit evidence

Redaction pipeline and labeled evaluation cases. Include commands or procedure, relevant outputs, one failed case, your interpretation, and AI-assistance disclosure. Use synthetic data only. Clearly distinguish personally executed work, observed instructor demonstrations, and pending exercises.

## Check your understanding

- Which assumption in measure redaction instead of assuming privacy could make your BrewByte result misleading?
- What fails if the input is malformed, unauthorized, or missing?
- What evidence would convince a reviewer that your change works on an unseen case?

These public questions are formative. Explain your reasoning; they are not hidden certification questions.

## Free assigned resources

- [Presidio recognizers and evaluation](https://presidio.dataprivacystack.org/)
- [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework)
- [Official GDPR text](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng)

## Continue

[Module assignment and rubric](index.html) · [Academy home](../../index.html) · [Execution guide](../../docs/model-and-deployment-labs.html)

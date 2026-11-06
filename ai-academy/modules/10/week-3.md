# Module 10 · Week 3: Draft evidence-linked incident tickets

**BrewByte assignment:** Process 1,000 synthetic login/endpoint events containing ten known incident storylines. Correlate events, compare rules with IsolationForest or a similar small baseline, and draft incident tickets with event IDs, severity rationale, uncertainty, and next investigative steps. All response actions are dry-run proposals.

## Learn the concept

A useful incident summary names evidence, uncertainty, and next investigative steps. Generated content must not invent malware, users, or timestamps. Actions require a separate approval boundary. Read-only tools reduce the consequences of a misleading summary while a human verifies the evidence.

## Worked business example

A draft ticket cites SYN-E0001 through SYN-E0004 and proposes reviewing authentication history. It does not claim a confirmed compromise without supporting evidence or disable the account.

## Guided practice

Read this week's assigned resource sections about **Evidence-linked summaries, read-only agent/tool scaffold, approval queues**. Spend about three hours on reading, small examples, and explaining the vocabulary in your own words. You are not expected to complete every linked course this week.

Open [the guided notebook](lab.ipynb) or [starter script](starter.py). The notebook names the dependency and execution requirements. Run the relevant worked example and inspect its inputs and outputs. For Module 1, begin with a manual prompt comparison; coding is introduced in Module 2.

Create incident drafts with event IDs, severity rationale, uncertainty, and recommended next steps. Test unsupported-claim detection and attempt a prohibited real response action.

Change one input or condition, predict the result, then run or observe it. Preserve a failing case before repairing it. Complete the task in your own learning repository rather than modifying the public teaching source.

## Security boundary

Treat logs as attacker-controlled text, preserve evidence identifiers/timestamps, redact sensitive data, scope agent tools, and require approval outside the model. Use synthetic impersonation/deepfake scenarios for defensive analysis; no impersonation of real people is needed.

## Submit evidence

Dry-run incident ticket workflow. Include commands or procedure, relevant outputs, one failed case, your interpretation, and AI-assistance disclosure. Use synthetic data only. Clearly distinguish personally executed work, observed instructor demonstrations, and pending exercises.

## Check your understanding

- Which assumption in draft evidence-linked incident tickets could make your BrewByte result misleading?
- What fails if the input is malformed, unauthorized, or missing?
- What evidence would convince a reviewer that your change works on an unseen case?

These public questions are formative. Explain your reasoning; they are not hidden certification questions.

## Free assigned resources

- [MITRE ATT&CK](https://attack.mitre.org/)
- [scikit-learn anomaly detection](https://scikit-learn.org/stable/modules/outlier_detection.html)
- [NIST incident response](https://csrc.nist.gov/projects/incident-response)

## Continue

[Module assignment and rubric](index.html) · [Academy home](../../index.html) · [Execution guide](../../docs/model-and-deployment-labs.html)

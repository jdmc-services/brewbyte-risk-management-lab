# Module 10 · Week 1: Normalize security evidence

**BrewByte assignment:** Process 1,000 synthetic login/endpoint events containing ten known incident storylines. Correlate events, compare rules with IsolationForest or a similar small baseline, and draft incident tickets with event IDs, severity rationale, uncertainty, and next investigative steps. All response actions are dry-run proposals.

## Learn the concept

Events need consistent timestamps, identifiers, actors, actions, and outcomes before correlation. Preserve raw evidence separately from derived summaries. An incident is a hypothesis about related events, not merely a severe-looking log line. Establish synthetic ground truth so detection quality can be measured.

## Worked business example

Repeated failed logins followed by a success may deserve investigation. Event IDs let a reviewer inspect the actual sequence instead of trusting a generated narrative.

## Guided practice

Read this week's assigned resource sections about **Incident-response fundamentals, event fields, timestamps, baselines, parsing**. Spend about three hours on reading, small examples, and explaining the vocabulary in your own words. You are not expected to complete every linked course this week.

Open [the guided notebook](lab.ipynb) or [starter script](starter.py). The notebook names the dependency and execution requirements. Run the relevant worked example and inspect its inputs and outputs. For Module 1, begin with a manual prompt comparison; coding is introduced in Module 2.

Load the synthetic events, normalize fields, and reconstruct one known storyline. Separate observation from interpretation and retain the source IDs in every derived record.

Change one input or condition, predict the result, then run or observe it. Preserve a failing case before repairing it. Complete the task in your own learning repository rather than modifying the public teaching source.

## Security boundary

Treat logs as attacker-controlled text, preserve evidence identifiers/timestamps, redact sensitive data, scope agent tools, and require approval outside the model. Use synthetic impersonation/deepfake scenarios for defensive analysis; no impersonation of real people is needed.

## Submit evidence

Normalized synthetic event store and schema tests. Include commands or procedure, relevant outputs, one failed case, your interpretation, and AI-assistance disclosure. Use synthetic data only. Clearly distinguish personally executed work, observed instructor demonstrations, and pending exercises.

## Check your understanding

- Which assumption in normalize security evidence could make your BrewByte result misleading?
- What fails if the input is malformed, unauthorized, or missing?
- What evidence would convince a reviewer that your change works on an unseen case?

These public questions are formative. Explain your reasoning; they are not hidden certification questions.

## Free assigned resources

- [MITRE ATT&CK](https://attack.mitre.org/)
- [scikit-learn anomaly detection](https://scikit-learn.org/stable/modules/outlier_detection.html)
- [NIST incident response](https://csrc.nist.gov/projects/incident-response)

## Continue

[Module assignment and rubric](index.html) · [Academy home](../../index.html) · [Execution guide](../../docs/model-and-deployment-labs.html)

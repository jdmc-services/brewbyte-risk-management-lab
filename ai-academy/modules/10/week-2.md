# Module 10 · Week 2: Compare rules and anomaly detection

**BrewByte assignment:** Process 1,000 synthetic login/endpoint events containing ten known incident storylines. Correlate events, compare rules with IsolationForest or a similar small baseline, and draft incident tickets with event IDs, severity rationale, uncertainty, and next investigative steps. All response actions are dry-run proposals.

## Learn the concept

Rules identify specified patterns; anomaly models identify unusual observations under a learned representation. Unusual does not necessarily mean malicious. Compare with ground truth and evaluate false positives at the incident/storyline level rather than inflating results through duplicate alerts.

## Worked business example

An unusual high-volume sales day may be legitimate. A sequence of failed logins may be more meaningful when joined with account and time-window context.

## Guided practice

Read this week's assigned resource sections about **Correlation rules, anomaly detection, false positives, ground truth**. Spend about three hours on reading, small examples, and explaining the vocabulary in your own words. You are not expected to complete every linked course this week.

Open [the guided notebook](lab.ipynb) or [starter script](starter.py). The notebook names the dependency and execution requirements. Run the relevant worked example and inspect its inputs and outputs. For Module 1, begin with a manual prompt comparison; coding is introduced in Module 2.

Compare the provided correlation rule with a simple anomaly baseline. Report storyline precision/recall and duplicate alerts. Explain one benign anomaly and one missed incident.

Change one input or condition, predict the result, then run or observe it. Preserve a failing case before repairing it. Complete the task in your own learning repository rather than modifying the public teaching source.

## Security boundary

Treat logs as attacker-controlled text, preserve evidence identifiers/timestamps, redact sensitive data, scope agent tools, and require approval outside the model. Use synthetic impersonation/deepfake scenarios for defensive analysis; no impersonation of real people is needed.

## Submit evidence

Comparative detection report. Include commands or procedure, relevant outputs, one failed case, your interpretation, and AI-assistance disclosure. Use synthetic data only. Clearly distinguish personally executed work, observed instructor demonstrations, and pending exercises.

## Check your understanding

- Which assumption in compare rules and anomaly detection could make your BrewByte result misleading?
- What fails if the input is malformed, unauthorized, or missing?
- What evidence would convince a reviewer that your change works on an unseen case?

These public questions are formative. Explain your reasoning; they are not hidden certification questions.

## Free assigned resources

- [MITRE ATT&CK](https://attack.mitre.org/)
- [scikit-learn anomaly detection](https://scikit-learn.org/stable/modules/outlier_detection.html)
- [NIST incident response](https://csrc.nist.gov/projects/incident-response)

## Continue

[Module assignment and rubric](index.html) · [Academy home](../../index.html) · [Execution guide](../../docs/model-and-deployment-labs.html)

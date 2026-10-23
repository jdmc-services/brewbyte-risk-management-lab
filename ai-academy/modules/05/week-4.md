# Module 05 · Week 4: Make a release decision from evidence

**BrewByte assignment:** Extend Module 4 into an imbalanced escalation classifier. Deliberately add a post-outcome leakage feature, expose misleading performance, remove it, and rebuild the evaluation. Compare rule-based, dummy, and trained approaches.

## Learn the concept

Report sample size, class counts, errors, and uncertainty alongside average scores. Small subgroup estimates can be unstable; absence of a measured disparity is not proof of fairness. Drift means the deployment distribution may differ from training. A release recommendation should include monitoring and stop conditions.

## Worked business example

A model trained on normal sales may fail during a festival. Monitor input changes and errors rather than assuming the original evaluation remains valid forever.

## Guided practice

Read this week's assigned resource sections about **Final held-out assessment, subgroup errors, drift scenarios, release criteria**. Spend about three hours on reading, small examples, and explaining the vocabulary in your own words. You are not expected to complete every linked course this week.

Open [the guided notebook](lab.ipynb) or [starter script](starter.py). The notebook names the dependency and execution requirements. Run the relevant worked example and inspect its inputs and outputs. For Module 1, begin with a manual prompt comparison; coding is introduced in Module 2.

Evaluate the selected model once on held-out data. Add a subgroup/error review and drift scenario. Repeat one analysis on an instructor-vetted licensed public dataset and discuss transfer limitations.

Change one input or condition, predict the result, then run or observe it. Preserve a failing case before repairing it. Complete the task in your own learning repository rather than modifying the public teaching source.

## Security boundary

Treat evaluation data and metric reports as integrity assets. Restrict edits, record dataset/model hashes and versions, and distinguish honest mistakes from deliberate metric manipulation. Never equate a language model's stated confidence with calibrated probability.

## Submit evidence

Auditable evaluation card and go/no-go recommendation. Include commands or procedure, relevant outputs, one failed case, your interpretation, and AI-assistance disclosure. Use synthetic data only. Clearly distinguish personally executed work, observed instructor demonstrations, and pending exercises.

## Check your understanding

- Which assumption in make a release decision from evidence could make your BrewByte result misleading?
- What fails if the input is malformed, unauthorized, or missing?
- What evidence would convince a reviewer that your change works on an unseen case?

These public questions are formative. Explain your reasoning; they are not hidden certification questions.

## Free assigned resources

- [scikit-learn Common Pitfalls](https://scikit-learn.org/stable/common_pitfalls.html)
- [Cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html)
- [Model evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html)

## Continue

[Module assignment and rubric](index.html) · [Academy home](../../index.html) · [Execution guide](../../docs/model-and-deployment-labs.html)

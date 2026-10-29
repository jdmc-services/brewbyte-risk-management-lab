# Module 05 · Week 3: Tune within training data

**BrewByte assignment:** Extend Module 4 into an imbalanced escalation classifier. Deliberately add a post-outcome leakage feature, expose misleading performance, remove it, and rebuild the evaluation. Compare rule-based, dummy, and trained approaches.

## Learn the concept

Cross-validation estimates variability across training subsets; a pipeline refits preprocessing within each fold. Select hyperparameters and thresholds using development data only. Repeatedly checking the test set turns it into another validation set. More search is not necessarily better when the dataset is small.

## Worked business example

Choose a review threshold using the cost of missed escalations and extra reviews. Lock the threshold before the final test rather than optimizing it on the final report.

## Guided practice

Read this week's assigned resource sections about **Pipelines, cross-validation, modest tuning, threshold costs, uncertainty**. Spend about three hours on reading, small examples, and explaining the vocabulary in your own words. You are not expected to complete every linked course this week.

Open [the guided notebook](lab.ipynb) or [starter script](starter.py). The notebook names the dependency and execution requirements. Run the relevant worked example and inspect its inputs and outputs. For Module 1, begin with a manual prompt comparison; coding is introduced in Module 2.

Use a small cross-validation search and record the selection rule. Compare two thresholds on validation data, freeze a choice, and explain why it fits the business objective.

Change one input or condition, predict the result, then run or observe it. Preserve a failing case before repairing it. Complete the task in your own learning repository rather than modifying the public teaching source.

## Security boundary

Treat evaluation data and metric reports as integrity assets. Restrict edits, record dataset/model hashes and versions, and distinguish honest mistakes from deliberate metric manipulation. Never equate a language model's stated confidence with calibrated probability.

## Submit evidence

Validation-only selection record. Include commands or procedure, relevant outputs, one failed case, your interpretation, and AI-assistance disclosure. Use synthetic data only. Clearly distinguish personally executed work, observed instructor demonstrations, and pending exercises.

## Check your understanding

- Which assumption in tune within training data could make your BrewByte result misleading?
- What fails if the input is malformed, unauthorized, or missing?
- What evidence would convince a reviewer that your change works on an unseen case?

These public questions are formative. Explain your reasoning; they are not hidden certification questions.

## Free assigned resources

- [scikit-learn Common Pitfalls](https://scikit-learn.org/stable/common_pitfalls.html)
- [Cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html)
- [Model evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html)

## Continue

[Module assignment and rubric](index.html) · [Academy home](../../index.html) · [Execution guide](../../docs/model-and-deployment-labs.html)

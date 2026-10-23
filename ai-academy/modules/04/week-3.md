# Module 04 · Week 3: Compare trees and forests

**BrewByte assignment:** On reproducible synthetic business data, predict a numeric outcome, classify a ticket category, and explore customer/ticket clusters. Provide clear feature availability times, baselines, preprocessing pipelines, model comparisons, and a model card.

## Learn the concept

A decision tree partitions feature space through successive questions. Deep trees can memorize training observations. A random forest combines many trees to reduce some instability, but it is not automatically better for every business problem. Evaluate with the same split and metric before preferring a more complex model.

## Worked business example

A tree learns whether product and weekend indicators change demand. Its perfect training score may disappear on later dates. A forest can improve generalization while increasing model size and explanation effort.

## Guided practice

Read this week's assigned resource sections about **Trees and random forests, complexity, feature effects**. Spend about three hours on reading, small examples, and explaining the vocabulary in your own words. You are not expected to complete every linked course this week.

Open [the guided notebook](lab.ipynb) or [starter script](starter.py). The notebook names the dependency and execution requirements. Run the relevant worked example and inspect its inputs and outputs. For Module 1, begin with a manual prompt comparison; coding is introduced in Module 2.

Compare a shallow tree, deeper tree, and forest. Report training and validation results, inspect errors, and justify the simpler or more accurate choice using business constraints.

Change one input or condition, predict the result, then run or observe it. Preserve a failing case before repairing it. Complete the task in your own learning repository rather than modifying the public teaching source.

## Security boundary

Identify label leakage, sensitive features, proxy attributes, and untrusted model downloads. Introduce train/test separation immediately; preprocessing learns only from training data. Use locally trained artifacts and explain unsafe deserialization risk.

## Submit evidence

Comparative results and an error analysis. Include commands or procedure, relevant outputs, one failed case, your interpretation, and AI-assistance disclosure. Use synthetic data only. Clearly distinguish personally executed work, observed instructor demonstrations, and pending exercises.

## Check your understanding

- Which assumption in compare trees and forests could make your BrewByte result misleading?
- What fails if the input is malformed, unauthorized, or missing?
- What evidence would convince a reviewer that your change works on an unseen case?

These public questions are formative. Explain your reasoning; they are not hidden certification questions.

## Free assigned resources

- [Inria scikit-learn course: predictive pipelines and models](https://inria.github.io/scikit-learn-mooc/)
- [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)

## Continue

[Module assignment and rubric](index.html) · [Academy home](../../index.html) · [Execution guide](../../docs/model-and-deployment-labs.html)

# Module 04 · Week 2: Fit linear and logistic models

**BrewByte assignment:** On reproducible synthetic business data, predict a numeric outcome, classify a ticket category, and explore customer/ticket clusters. Provide clear feature availability times, baselines, preprocessing pipelines, model comparisons, and a model card.

## Learn the concept

Linear regression estimates a numeric outcome from weighted features. Logistic regression estimates class probabilities and applies a decision threshold. Scaling changes numerical ranges; fitting it on the entire dataset leaks test information. Coefficients can support interpretation, but correlated variables and preprocessing affect their meaning.

## Worked business example

A demand model predicts units, while an escalation model estimates whether a ticket needs review. They use different objectives even if both are described as regression models.

## Guided practice

Read this week's assigned resource sections about **Linear and logistic regression, scaling, coefficients, classification vs regression**. Spend about three hours on reading, small examples, and explaining the vocabulary in your own words. You are not expected to complete every linked course this week.

Open [the guided notebook](lab.ipynb) or [starter script](starter.py). The notebook names the dependency and execution requirements. Run the relevant worked example and inspect its inputs and outputs. For Module 1, begin with a manual prompt comparison; coding is introduced in Module 2.

Run the classical-ML demonstration. Inspect one linear prediction and one logistic decision. Explain the features, target, preprocessing, and metric. Compare results with a dummy estimator.

Change one input or condition, predict the result, then run or observe it. Preserve a failing case before repairing it. Complete the task in your own learning repository rather than modifying the public teaching source.

## Security boundary

Identify label leakage, sensitive features, proxy attributes, and untrusted model downloads. Introduce train/test separation immediately; preprocessing learns only from training data. Use locally trained artifacts and explain unsafe deserialization risk.

## Submit evidence

Two fitted pipelines and plain-language interpretation. Include commands or procedure, relevant outputs, one failed case, your interpretation, and AI-assistance disclosure. Use synthetic data only. Clearly distinguish personally executed work, observed instructor demonstrations, and pending exercises.

## Check your understanding

- Which assumption in fit linear and logistic models could make your BrewByte result misleading?
- What fails if the input is malformed, unauthorized, or missing?
- What evidence would convince a reviewer that your change works on an unseen case?

These public questions are formative. Explain your reasoning; they are not hidden certification questions.

## Free assigned resources

- [Inria scikit-learn course: predictive pipelines and models](https://inria.github.io/scikit-learn-mooc/)
- [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)

## Continue

[Module assignment and rubric](index.html) · [Academy home](../../index.html) · [Execution guide](../../docs/model-and-deployment-labs.html)

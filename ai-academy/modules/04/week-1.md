# Module 04 · Week 1: Frame a prediction and baseline

**BrewByte assignment:** On reproducible synthetic business data, predict a numeric outcome, classify a ticket category, and explore customer/ticket clusters. Provide clear feature availability times, baselines, preprocessing pipelines, model comparisons, and a model card.

## Learn the concept

Supervised learning uses known labels; unsupervised learning searches for structure without them. Features must be available at prediction time. A dummy baseline exposes whether a sophisticated model adds useful signal. Split data before fitting transformations. For future demand, chronological separation is more realistic than randomly mixing future and past.

## Worked business example

Forecast next-day coffee demand from calendar and product information. The final revenue for that day is not a valid input because it is only known after the event.

## Guided practice

Read this week's assigned resource sections about **Problem framing, features/targets, vectors and weighted sums, splits, dummy models**. Spend about three hours on reading, small examples, and explaining the vocabulary in your own words. You are not expected to complete every linked course this week.

Open [the guided notebook](lab.ipynb) or [starter script](starter.py). The notebook names the dependency and execution requirements. Run the relevant worked example and inspect its inputs and outputs. For Module 1, begin with a manual prompt comparison; coding is introduced in Module 2.

Define a numeric prediction, a category prediction, and a clustering question. State when each feature becomes available. Run dummy baselines and choose a split appropriate to each task.

Change one input or condition, predict the result, then run or observe it. Preserve a failing case before repairing it. Complete the task in your own learning repository rather than modifying the public teaching source.

## Security boundary

Identify label leakage, sensitive features, proxy attributes, and untrusted model downloads. Introduce train/test separation immediately; preprocessing learns only from training data. Use locally trained artifacts and explain unsafe deserialization risk.

## Submit evidence

Written task/metric choice and baseline notebook. Include commands or procedure, relevant outputs, one failed case, your interpretation, and AI-assistance disclosure. Use synthetic data only. Clearly distinguish personally executed work, observed instructor demonstrations, and pending exercises.

## Check your understanding

- Which assumption in frame a prediction and baseline could make your BrewByte result misleading?
- What fails if the input is malformed, unauthorized, or missing?
- What evidence would convince a reviewer that your change works on an unseen case?

These public questions are formative. Explain your reasoning; they are not hidden certification questions.

## Free assigned resources

- [Inria scikit-learn course: predictive pipelines and models](https://inria.github.io/scikit-learn-mooc/)
- [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)

## Continue

[Module assignment and rubric](index.html) · [Academy home](../../index.html) · [Execution guide](../../docs/model-and-deployment-labs.html)

# Module 04 · Week 4: Explore clusters without inventing labels

**BrewByte assignment:** On reproducible synthetic business data, predict a numeric outcome, classify a ticket category, and explore customer/ticket clusters. Provide clear feature availability times, baselines, preprocessing pipelines, model comparisons, and a model card.

## Learn the concept

Clustering groups observations according to a chosen representation and distance. Scaling can change the groups dramatically. A cluster ID has no inherent business meaning; it is not a verified customer identity or intent. Inspect group characteristics, stability, and whether the analysis is actually actionable.

## Worked business example

K-means may separate transaction patterns by quantity and price, but calling a cluster loyal customers would require independent evidence of loyalty.

## Guided practice

Read this week's assigned resource sections about **K-means, scaling and cluster inspection; limits of unsupervised results**. Spend about three hours on reading, small examples, and explaining the vocabulary in your own words. You are not expected to complete every linked course this week.

Open [the guided notebook](lab.ipynb) or [starter script](starter.py). The notebook names the dependency and execution requirements. Run the relevant worked example and inspect its inputs and outputs. For Module 1, begin with a manual prompt comparison; coding is introduced in Module 2.

Run a scaled clustering experiment with two settings. Describe observed patterns without causal or personal claims. Publish the five-model comparison and a model card with intended use and limitations.

Change one input or condition, predict the result, then run or observe it. Preserve a failing case before repairing it. Complete the task in your own learning repository rather than modifying the public teaching source.

## Security boundary

Identify label leakage, sensitive features, proxy attributes, and untrusted model downloads. Introduce train/test separation immediately; preprocessing learns only from training data. Use locally trained artifacts and explain unsafe deserialization risk.

## Submit evidence

Reproducible comparison package and model card. Include commands or procedure, relevant outputs, one failed case, your interpretation, and AI-assistance disclosure. Use synthetic data only. Clearly distinguish personally executed work, observed instructor demonstrations, and pending exercises.

## Check your understanding

- Which assumption in explore clusters without inventing labels could make your BrewByte result misleading?
- What fails if the input is malformed, unauthorized, or missing?
- What evidence would convince a reviewer that your change works on an unseen case?

These public questions are formative. Explain your reasoning; they are not hidden certification questions.

## Free assigned resources

- [Inria scikit-learn course: predictive pipelines and models](https://inria.github.io/scikit-learn-mooc/)
- [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)

## Continue

[Module assignment and rubric](index.html) · [Academy home](../../index.html) · [Execution guide](../../docs/model-and-deployment-labs.html)

# Module 03 · Week 3: Clean data with an audit trail

**BrewByte assignment:** Process an instructor-provided, seeded dataset of 2,000 fictional tickets with duplicates, missing fields, inconsistent dates, invalid categories, and synthetic identifiers. Produce a reusable cleaning script, data dictionary, lineage record, SQLite queries, and a concise exploratory report.

## Learn the concept

A cleaning pipeline should be repeatable and explicit. Deduplicate using a business key, distinguish invalid values from missing values, and document rejected rows. Joins can multiply records when keys are not unique; validate the relationship rather than trusting a plausible-looking total. Learn preprocessing parameters only from training data when preparing an ML pipeline.

## Worked business example

Two copies of SYN-T0001 should not become two customer requests. A missing amount is not necessarily zero. A many-to-many join can inflate revenue without raising an exception.

## Guided practice

Read this week's assigned resource sections about **Missingness, duplicates, dates, joins, validation, provenance**. Spend about three hours on reading, small examples, and explaining the vocabulary in your own words. You are not expected to complete every linked course this week.

Open [the guided notebook](lab.ipynb) or [starter script](starter.py). The notebook names the dependency and execution requirements. Run the relevant worked example and inspect its inputs and outputs. For Module 1, begin with a manual prompt comparison; coding is introduced in Module 2.

Implement cleaning rules for duplicate IDs, absent descriptions, and invalid amounts. Reconcile accepted plus rejected plus duplicate counts to the original input. Explain each imputation or exclusion.

Change one input or condition, predict the result, then run or observe it. Preserve a failing case before repairing it. Complete the task in your own learning repository rather than modifying the public teaching source.

## Security boundary

Threats include accidental identifier disclosure, silent data corruption, and contaminated sources. Preserve an immutable source copy, validate schema and ranges, document provenance and transformation decisions, and limit exports. A hash establishes consistency relative to a trusted reference, not source trustworthiness or privacy. Explain why identifier removal alone may leave re-identification risk.

## Submit evidence

Deterministic cleaning pipeline and row-level reconciliation. Include commands or procedure, relevant outputs, one failed case, your interpretation, and AI-assistance disclosure. Use synthetic data only. Clearly distinguish personally executed work, observed instructor demonstrations, and pending exercises.

## Check your understanding

- Which assumption in clean data with an audit trail could make your BrewByte result misleading?
- What fails if the input is malformed, unauthorized, or missing?
- What evidence would convince a reviewer that your change works on an unseen case?

These public questions are formative. Explain your reasoning; they are not hidden certification questions.

## Free assigned resources

- [pandas: reading, statistics, combining tables](https://pandas.pydata.org/docs/getting_started/intro_tutorials/)
- [NumPy absolute basics](https://numpy.org/doc/stable/user/absolute_beginners.html)
- [OpenStax statistics](https://openstax.org/details/books/introductory-statistics-2e)
- [SQLite language](https://www.sqlite.org/lang.html)

## Continue

[Module assignment and rubric](index.html) · [Academy home](../../index.html) · [Execution guide](../../docs/model-and-deployment-labs.html)

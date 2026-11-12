# Module 02 · Week 2: Use control flow and functions

**BrewByte assignment:** Build a command-line program that reads synthetic requests, validates required fields, assigns a rule-based queue, and writes JSON summaries. Include a deliberately malformed input file and a repair exercise.

## Learn the concept

Conditions choose a branch; loops repeat a computation; functions give a reusable behavior a clear input/output contract. Keep business decisions in small functions so you can test them without reading files or calling services. Tracing means following values step by step, which is more reliable than repeatedly asking a model to rewrite unclear code.

## Worked business example

A routing function returns billing for a payment issue and service for a drink-quality issue. An empty description should raise a clear validation error rather than inventing a category.

## Guided practice

Read this week's assigned resource sections about **Branches, loops, Boolean conditions, functions, tracing and debugging**. Spend about three hours on reading, small examples, and explaining the vocabulary in your own words. You are not expected to complete every linked course this week.

Open [the guided notebook](lab.ipynb) or [starter script](starter.py). The notebook names the dependency and execution requirements. Run the relevant worked example and inspect its inputs and outputs. For Module 1, begin with a manual prompt comparison; coding is introduced in Module 2.

Implement a priority function for three explicit business rules. Trace five requests by hand, then run them. Add a new category without changing unrelated branches. Explain your precedence rule.

Change one input or condition, predict the result, then run or observe it. Preserve a failing case before repairing it. Complete the task in your own learning repository rather than modifying the public teaching source.

## Security boundary

Introduce confidentiality/integrity/availability, authentication vs authorization, least privilege, and basic client/server concepts. Validate data rather than executing it; prohibit `eval` on input and unsafe shell interpolation. Store no credentials in notebooks or commits; inspect dependencies and keep generated outputs free of sensitive content.

## Submit evidence

Rule-based router and function diagram. Include commands or procedure, relevant outputs, one failed case, your interpretation, and AI-assistance disclosure. Use synthetic data only. Clearly distinguish personally executed work, observed instructor demonstrations, and pending exercises.

## Check your understanding

- Which assumption in use control flow and functions could make your BrewByte result misleading?
- What fails if the input is malformed, unauthorized, or missing?
- What evidence would convince a reviewer that your change works on an unseen case?

These public questions are formative. Explain your reasoning; they are not hidden certification questions.

## Free assigned resources

- [CS50P: variables, conditions, loops, exceptions, tests, files](https://cs50.harvard.edu/python/)
- [VS Code Python setup](https://code.visualstudio.com/docs/python/python-tutorial)
- [GitHub Learn](https://learn.github.com/)

## Continue

[Module assignment and rubric](index.html) · [Academy home](../../index.html) · [Execution guide](../../docs/model-and-deployment-labs.html)

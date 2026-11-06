# Module 02 · Week 4: Test and explain a program

**BrewByte assignment:** Build a command-line program that reads synthetic requests, validates required fields, assigns a rule-based queue, and writes JSON summaries. Include a deliberately malformed input file and a repair exercise.

## Learn the concept

Behavioral tests describe observable results for meaningful inputs. A test that duplicates the implementation can reproduce its bug. Include boundary and failure cases, and use readable errors. Git records changes; a branch lets you review one improvement independently. Never commit credentials, even if you plan to remove them later.

## Worked business example

Test that a blank request is rejected, an oversized request is rejected, and a billing request reaches the expected queue. The expected behavior comes from the business rule, not from copying the function.

## Guided practice

Read this week's assigned resource sections about **Tests, refactoring, Git branches/reviews, safe input handling**. Spend about three hours on reading, small examples, and explaining the vocabulary in your own words. You are not expected to complete every linked course this week.

Open [the guided notebook](lab.ipynb) or [starter script](starter.py). The notebook names the dependency and execution requirements. Run the relevant worked example and inspect its inputs and outputs. For Module 1, begin with a manual prompt comparison; coding is introduced in Module 2.

Complete ten tests for the ticket intake CLI, open a reviewable branch, and demonstrate an unseen routing change. Document setup, invocation, output, and at least one repaired bug.

Change one input or condition, predict the result, then run or observe it. Preserve a failing case before repairing it. Complete the task in your own learning repository rather than modifying the public teaching source.

## Security boundary

Introduce confidentiality/integrity/availability, authentication vs authorization, least privilege, and basic client/server concepts. Validate data rather than executing it; prohibit `eval` on input and unsafe shell interpolation. Store no credentials in notebooks or commits; inspect dependencies and keep generated outputs free of sensitive content.

## Submit evidence

Tested CLI, README, reviewed change, and independent modification. Include commands or procedure, relevant outputs, one failed case, your interpretation, and AI-assistance disclosure. Use synthetic data only. Clearly distinguish personally executed work, observed instructor demonstrations, and pending exercises.

## Check your understanding

- Which assumption in test and explain a program could make your BrewByte result misleading?
- What fails if the input is malformed, unauthorized, or missing?
- What evidence would convince a reviewer that your change works on an unseen case?

These public questions are formative. Explain your reasoning; they are not hidden certification questions.

## Free assigned resources

- [CS50P: variables, conditions, loops, exceptions, tests, files](https://cs50.harvard.edu/python/)
- [VS Code Python setup](https://code.visualstudio.com/docs/python/python-tutorial)
- [GitHub Learn](https://learn.github.com/)

## Continue

[Module assignment and rubric](index.html) · [Academy home](../../index.html) · [Execution guide](../../docs/model-and-deployment-labs.html)

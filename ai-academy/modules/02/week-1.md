# Module 02 · Week 1: Run Python and inspect values

**BrewByte assignment:** Build a command-line program that reads synthetic requests, validates required fields, assigns a rule-based queue, and writes JSON summaries. Include a deliberately malformed input file and a repair exercise.

## Learn the concept

A variable binds a name to a value. Strings represent text, numbers support arithmetic, lists preserve sequences, and dictionaries associate keys with values. Types matter: adding two strings joins them, while adding numbers sums them. Run small statements, predict their output, then inspect what actually happens before writing a large program.

## Worked business example

A coffee order can be represented as a dictionary with product, quantity, and unit_price. A list of orders can be processed one item at a time. Use fictional values only.

## Guided practice

Read this week's assigned resource sections about **Interpreter/notebook/editor, variables, types, strings, lists/dictionaries, terminal basics**. Spend about three hours on reading, small examples, and explaining the vocabulary in your own words. You are not expected to complete every linked course this week.

Open [the guided notebook](lab.ipynb) or [starter script](starter.py). The notebook names the dependency and execution requirements. Run the relevant worked example and inspect its inputs and outputs. For Module 1, begin with a manual prompt comparison; coding is introduced in Module 2.

Run the Module 2 starter. Create three order dictionaries, calculate totals, and deliberately mix a string quantity with a number. Explain the resulting error. Make a local Git commit.

Change one input or condition, predict the result, then run or observe it. Preserve a failing case before repairing it. Complete the task in your own learning repository rather than modifying the public teaching source.

## Security boundary

Introduce confidentiality/integrity/availability, authentication vs authorization, least privilege, and basic client/server concepts. Validate data rather than executing it; prohibit `eval` on input and unsafe shell interpolation. Store no credentials in notebooks or commits; inspect dependencies and keep generated outputs free of sensitive content.

## Submit evidence

Small scripts, working environment, and first Git commits. Include commands or procedure, relevant outputs, one failed case, your interpretation, and AI-assistance disclosure. Use synthetic data only. Clearly distinguish personally executed work, observed instructor demonstrations, and pending exercises.

## Check your understanding

- Which assumption in run python and inspect values could make your BrewByte result misleading?
- What fails if the input is malformed, unauthorized, or missing?
- What evidence would convince a reviewer that your change works on an unseen case?

These public questions are formative. Explain your reasoning; they are not hidden certification questions.

## Free assigned resources

- [CS50P: variables, conditions, loops, exceptions, tests, files](https://cs50.harvard.edu/python/)
- [VS Code Python setup](https://code.visualstudio.com/docs/python/python-tutorial)
- [GitHub Learn](https://learn.github.com/)

## Continue

[Module assignment and rubric](index.html) · [Academy home](../../index.html) · [Execution guide](../../docs/model-and-deployment-labs.html)

# Module 02 · Week 3: Read files and handle failure

**BrewByte assignment:** Build a command-line program that reads synthetic requests, validates required fields, assigns a rule-based queue, and writes JSON summaries. Include a deliberately malformed input file and a repair exercise.

## Learn the concept

CSV stores tabular rows; JSON represents nested objects and arrays. File input is untrusted even when it comes from a familiar source. Validate required keys and types, handle expected exceptions specifically, and preserve the original file. A virtual environment isolates installed packages from other projects; dependency records help another person reproduce your work.

## Worked business example

A ticket file may contain a missing description or malformed amount. Reject that row with a reason while processing valid rows. Avoid catching every exception and returning success.

## Guided practice

Read this week's assigned resource sections about **CSV/JSON, file paths, exceptions, package environments, dependency records**. Spend about three hours on reading, small examples, and explaining the vocabulary in your own words. You are not expected to complete every linked course this week.

Open [the guided notebook](lab.ipynb) or [starter script](starter.py). The notebook names the dependency and execution requirements. Run the relevant worked example and inspect its inputs and outputs. For Module 1, begin with a manual prompt comparison; coding is introduced in Module 2.

Read the synthetic tickets, validate records, and write separate accepted and rejected outputs. Test missing files, empty files, and malformed JSON. Record interpreter and package versions.

Change one input or condition, predict the result, then run or observe it. Preserve a failing case before repairing it. Complete the task in your own learning repository rather than modifying the public teaching source.

## Security boundary

Introduce confidentiality/integrity/availability, authentication vs authorization, least privilege, and basic client/server concepts. Validate data rather than executing it; prohibit `eval` on input and unsafe shell interpolation. Store no credentials in notebooks or commits; inspect dependencies and keep generated outputs free of sensitive content.

## Submit evidence

Working import/export path with readable error messages. Include commands or procedure, relevant outputs, one failed case, your interpretation, and AI-assistance disclosure. Use synthetic data only. Clearly distinguish personally executed work, observed instructor demonstrations, and pending exercises.

## Check your understanding

- Which assumption in read files and handle failure could make your BrewByte result misleading?
- What fails if the input is malformed, unauthorized, or missing?
- What evidence would convince a reviewer that your change works on an unseen case?

These public questions are formative. Explain your reasoning; they are not hidden certification questions.

## Free assigned resources

- [CS50P: variables, conditions, loops, exceptions, tests, files](https://cs50.harvard.edu/python/)
- [VS Code Python setup](https://code.visualstudio.com/docs/python/python-tutorial)
- [GitHub Learn](https://learn.github.com/)

## Continue

[Module assignment and rubric](index.html) · [Academy home](../../index.html) · [Execution guide](../../docs/model-and-deployment-labs.html)

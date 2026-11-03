# BrewByte Cybersecurity Maintenance

Practice keeping a changing business secure. This module is independent of any college course and uses fictional systems and data. No login or live-system testing is required.

## The scenario

BrewByte has a Downtown coffee shop and is opening Eastside. It adds a delivery integration, changes staff, retires a register, and enables temporary vendor support. Your job is to explain how security maintenance should respond.

Start with [the scenario and decision rules](SCENARIO.md) and [the data guide](data/README.md). Baseline files describe **October 20, 2026**. Current files describe **November 3, 2026, at 08:00 Eastern Time**. The later tabletop events are a separate exercise, not proof of a breach in the current-state data.

## Activities

| Activity | What you practice | Suggested time |
|---|---|---|
| [1. What changed?](activities/01-environmental-change.md) | Identify changed assets, relationships, people, and risk | 10 minutes |
| [2. Which warning matters?](activities/02-external-monitoring.md) | Match fictional advisories to inventory and exposure | 10 minutes |
| [3. Compare the approved state](activities/03-internal-monitoring.md) | Detect configuration drift and incomplete changes | 15 minutes |
| [4. Assess partner access](activities/04-risk-assessment.md) | Connect threats, weaknesses, consequences, and controls | 15 minutes |
| [5. Prioritize and verify fixes](activities/05-remediation.md) | Validate findings and plan accountable correction | 15 minutes |
| [6. Plan a controlled change](activities/06-change-management.md) | Define tests, approval, rollback, and monitoring | 15 minutes |
| [7. Rehearse an outage](activities/07-readiness-review.md) | Evaluate recovery readiness and assign improvements | 15 minutes |
| [Capstone: one issue across five domains](activities/08-capstone.md) | Explain the complete maintenance cycle | 15 minutes |

For a shorter session, complete activities **1, 3, and 5** first. Use the others for follow-up practice.

## Working with the files

Read Markdown instructions directly on GitHub. Open CSV files in GitHub's table view or download them for Excel, Google Sheets, or a text editor. Download a response template, save a personal copy, and complete it locally. If your spreadsheet app puts everything in one column, import the CSV using comma as the delimiter and UTF-8 as the encoding.

There is no automatic grading, student account, response collection, or progress tracking. Keep your responses locally. If an instructor assigns the work, submit through their chosen private channel. Do not post student names or work records in public GitHub issues.

## What to explain in every response

State your decision, cite a record ID and relevant evidence, explain the business consequence, and describe how you would verify the result. Different priorities can be defensible when evidence and assumptions support them.

## Terms

- **Asset:** something the business values or depends on.
- **Threat:** a potential cause of harm.
- **Vulnerability:** a weakness a threat might exploit.
- **Baseline:** the documented approved or comparison state.
- **Drift:** a difference between the observed and approved state.
- **Remediation:** action to correct a weakness or reduce its risk, followed by verification.
- **RTO:** target time to restore a service.
- **RPO:** acceptable data-loss window.

Original educational scenarios. Product names, versions, advisories, accounts, and records are invented. No textbook slides, copied diagrams, real credentials, or employer data are included.

# Plan a controlled change

Suggested time: 15 minutes. Work individually or in pairs.

## Learning goal

Use testing, authority, rollback, and monitoring to make a change reviewable and verifiable.

## Evidence to open

- [vendor-advisories.md](../data/vendor-advisories.md)
- [vulnerability-findings.csv](../data/vulnerability-findings.csv)
- [configuration-current.csv](../data/configuration-current.csv)
- [approved-changes.csv](../data/approved-changes.csv)
- [SCENARIO.md](../SCENARIO.md)

## Your work

1. Draft a new change request for GW-01, addressing F-001 and the conditions of CHG-105.
2. State the intended version and required authentication/access settings.
3. Define pre-change tests, affected dependencies, implementation steps, and who approves the change.
4. Set explicit rollback triggers and describe how the last known working state would be restored safely.
5. Define post-change checks for support access, security, business operation, and logs.
6. List the evidence required before closing the change. A package installation message alone is insufficient.

## Deliverable

Complete [the response template](../templates/06-change-request.md). Use record IDs to support each important claim. Keep the response in your own files; there is no automatic upload or grading.

## Discussion

What evidence could change your decision? Which assumption did you make that someone else should verify?

[Back to the module](../README.md)

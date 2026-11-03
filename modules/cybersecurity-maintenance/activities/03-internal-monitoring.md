# Compare the approved state

Suggested time: 15 minutes. Work individually or in pairs.

## Learning goal

Detect drift while distinguishing a difference, an approval record, and proof of correct implementation.

## Evidence to open

- [asset-inventory-baseline.csv](../data/asset-inventory-baseline.csv)
- [asset-inventory-current.csv](../data/asset-inventory-current.csv)
- [configuration-baseline.csv](../data/configuration-baseline.csv)
- [configuration-current.csv](../data/configuration-current.csv)
- [approved-changes.csv](../data/approved-changes.csv)

## Your work

1. Join the two inventories using asset_id. Record new assets and changed fields.
2. Compare settings using the pair (asset_id, setting). Record differences for existing baseline entries separately from current-only entries.
3. Check each difference against the approval log. Read the conditions on CHG-105 carefully.
4. Classify observations as documented approved change, incomplete/conditional implementation, or unexplained change requiring investigation.
5. Choose two items for investigation. Explain what evidence you would collect before deciding whether there was an attack.
6. Identify an ownership gap and explain why it affects maintenance.

## Deliverable

Complete [the response template](../templates/03-baseline-comparison.md). Use record IDs to support each important claim. Keep the response in your own files; there is no automatic upload or grading.

## Discussion

What evidence could change your decision? Which assumption did you make that someone else should verify?

[Back to the module](../README.md)

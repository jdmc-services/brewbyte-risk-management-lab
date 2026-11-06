# Synthetic BrewByte datasets

Generated with seed 42. No actual customer, student, employee, or payment records. sales.csv has date-ordered daily product/location demand; tickets.csv has simplified labels; tickets-dirty.csv adds deliberate missing/malformed fields and duplicate IDs; events.csv contains ten synthetic login storylines and benign events. Labels are public formative ground truth, not private exam keys. policies.json defines public/staff/manager examples. security-cases.json tests deterministic boundaries only.

Do not use post-outcome fields as prediction features. Synthetic patterns do not establish real-world performance. The manifest detects byte changes relative to this trusted snapshot; it cannot establish semantic correctness.

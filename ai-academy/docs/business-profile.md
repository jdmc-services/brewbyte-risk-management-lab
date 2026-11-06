# BrewByte Coffee: shared business profile

BrewByte is a fictional three-location coffee retailer: Central, Riverside, and Market. It sells Espresso, Latte, Tea, and Cold Brew, operates 07:00–19:00, and uses a small support desk, online ordering, and staff policy library.

The curriculum follows an analyst's progression: reliable prompts → Python scripts → clean data → predictive baselines → trustworthy evaluations → protected pipelines → generative APIs → retrieval → security assurance → triage → governance → release.

## Decisions and boundaries

- Forecasting supports stock planning; a manager approves inventory changes.
- Customer-service summaries assist staff; they do not autonomously issue refunds.
- The public role sees published customer guidance. Staff sees staff policies. Managers see manager policies as well as staff/public documents.
- Identity is established by server-side credentials. A prompt claiming to be a manager grants nothing.
- The assistant must cite accessible sources or state that evidence is insufficient. It must not invent prices, employee rules, or security incidents.
- Security automation proposes actions in dry-run mode; it cannot disable users, contact external systems, or alter production settings.

## Synthetic data conventions

All identifiers begin with `SYN-`; addresses use `example.invalid`; no real payment information is present. The generated dirty dataset intentionally contains duplicates, malformed amounts, absent fields, and email-like identifiers. These support cleaning and redaction exercises. A SHA-256 manifest detects byte changes relative to the trusted course snapshot; it does not prove semantic truth or detect all poisoning.

Synthetic patterns are intentionally simplified. A strong score on them does not establish real-world generalization. Module 5 includes a transfer challenge using an instructor-vetted licensed public dataset.

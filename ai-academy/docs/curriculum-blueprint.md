# AI Application Development, Data Literacy & Security: 12-Month Curriculum

**Design baseline: October 22, 2026. Audience: absolute beginners.**

This is a proposed instructional blueprint, with instructor-set assessment targets. It is not an endorsed certification course, a claim of complete exam coverage, or a job-placement guarantee. The primary employment pathway is junior Python/AI application development or technical AI support. AI evaluation, data operations, and junior governance support are alternative portfolio pathways. Independent AI security engineering and advanced ML research require additional experience.

## Program operating model

- **Schedule:** 48 instructional weeks, four weeks per module, plus four flexible weeks distributed after the quarters for remediation, portfolio review, and interviews. Twelve four-week modules alone are not a full 52-week year.
- **Workload:** plan 12–15 hours per week: approximately 3 hours of instruction/readings, 6–8 hours of guided and independent lab work, 2 hours of assessment/debugging, and 1–2 hours of documentation and career practice. Adjust after the first cohort; this is a planning assumption.
- **Entry support:** begin Module 1 with file/folder navigation, browser safety, account setup, plain-text editing, and a numeracy diagnostic. Provide worked examples, captions/transcripts, starter files, and an optional slower remediation track.
- **Teaching sequence:** retrieve prior knowledge; demonstrate a worked example; complete a guided variation; attempt an independent change; explain the result; revisit it in the next module. Fade scaffolding across each quarter.
- **Common business case:** BrewByte, a fictional small business, needs trustworthy ticket analytics, a policy assistant, and a secure operations dashboard. Use synthetic records and instructor-authored policies throughout. No employer, student, customer, patient, or live security data belongs in these labs.
- **Portfolio:** use one repository with module folders while learning; curate three or four standalone showcase projects by graduation. Students should explain business value, evidence, security decisions, limitations, and their own contribution.
- **AI-use policy:** AI assistance is allowed with disclosure. Students must explain submitted code, trace a failing case, and complete a small unseen modification without generated answers. A polished artifact alone does not establish mastery.

## Cost and access design

The required route has **no required software subscription or paid model API**. Existing hardware and internet access are assumed. Use Python, VS Code, Git, SQLite, pandas, NumPy, scikit-learn, small local models, local Chroma, FastAPI, and Docker Engine where suitable. Select compatible stable package versions, test a cohort environment, and record a lockfile; do not automatically choose every newest release.

Keep tabular datasets small (roughly 1,000–10,000 rows) and RAG corpora small (20–50 short documents). Aim for CPU execution on an ordinary laptop; an 8 GB machine can handle the tabular labs, while generative-model suitability must be checked against the selected model. Offer interactive Colab notebooks when local setup fails. Free Colab resources are variable and not guaranteed; do not use Colab as persistent API hosting or bypass resource restrictions.

For model-based assignments, distinguish three evidence levels:

1. **Deterministic fixture:** tests application plumbing, timeouts, policy checks, and output schemas at zero inference cost. It does not establish generative behavior or attack resistance.
2. **Small local or interactive notebook model:** required for genuine generation and model-behavior evaluation; record model identifier, revision, license, inference settings, hardware, and observed limitations.
3. **Optional hosted API/cloud:** strengthens vendor-specific experience but is not required for core completion. OpenAI, Anthropic, managed vector stores, and Azure/AWS services are not assumed free. Publish an instructor-approved spending cap, limited privileges, cleanup instructions, and use a hard service quota where supported. Budget alerts alone do not stop charges.

If a student cannot run a live model, provide a supervised shared session using synthetic content. Recorded results may support analysis, but the student must label that limitation and cannot claim they personally executed a model evaluation. Certification exams, paid certificates, and permanent public hosting are outside the zero-cost promise.

## Certification alignment and scope

These are curriculum-design mappings to specific official objectives, not claims made by the exam providers. AWS tasks below use **AIF-C01**. Microsoft mappings use **AI-901**, skills measured April 15, 2026; AI-900 retired June 30, 2026. SecAI+ mappings use the **CompTIA-authored CY0-001 V1 objectives, document version 2.0**, accessible through an ONLC-hosted copy. That PDF includes some unfinished administrative fields, so validate the objectives against CompTIA's current download before advertising exam preparation. Its recommended experience is substantially above a beginner's starting point.

### Objective key: paraphrased labels

| Key | Objective or skill addressed |
|---|---|
| S1.1 | AI approaches and techniques |
| S1.2 | Data security and processing |
| S1.3 | Security across the lifecycle |
| S2.1 | Threat-modeling resources |
| S2.2 | AI security controls |
| S2.3 | Access controls |
| S2.4 | Data protection controls |
| S2.5 | Monitoring and audits |
| S2.6 | Attack evidence and mitigations |
| S3.1 | AI-enabled security tooling |
| S3.2 | AI-enhanced attack vectors |
| S3.3 | Security task automation |
| S4.1 | Governance structures and roles |
| S4.2 | AI risks |
| S4.3 | Compliance implications |

| Module | SecAI+ objectives | AWS AIF-C01 tasks | AI-901 skills; platform gaps are explicit |
|---|---|---|---|
| 1 | S1.1, S1.3, S4.2 | 1.1–1.2, 2.1–2.2, 3.2 | AI model concepts, workloads, responsible AI; prompt design within the Foundry apps/agents skill |
| 2 | Enabling skill for S3.3; no standalone Python objective | Enabling only; coding is beyond this foundational exam's target tasks | Python prerequisite; client-building skills practiced later |
| 3 | S1.2 | 1.1, 1.3, 5.1 | Data preparation is supporting knowledge, not a separately numbered skill |
| 4 | S1.1, S1.3 | 1.1–1.3 | AI workload/model selection concepts; classical model coding is enrichment |
| 5 | S1.3, S2.5 | 1.3, 3.4, 4.1–4.2 | Responsible AI and model selection; evaluation implementation goes beyond baseline |
| 6 | S1.2–1.3, S2.4, S4.3 | 5.1–5.2 | Privacy/security within responsible AI |
| 7 | S1.1, S2.2–2.3 | 2.3, 3.1–3.4, 5.1 | Foundry model deployment and SDK chat client; single-agent/client work in optional Azure bridge |
| 8 | S1.2, S2.3–2.4 | 2.1, 3.1, 3.4, 5.1 | Supporting application knowledge; RAG is not a standalone named skill in the retrieved blueprint |
| 9 | S2.1–2.6 | 3.2, 5.1 | Responsible AI; security testing enriches app/agent implementation |
| 10 | S2.5, S3.1–3.3 | 1.2–1.3, 3.4, 5.1 | App/agent and text-analysis skills; local work is not evidence of Foundry use |
| 11 | S4.1–4.3, S2.2, S2.5 | 4.1–4.2, 5.2 | Responsible AI principles |
| 12 | S1.3, S2.2–2.5, S3.3 | 1.3, 2.3, 3.1, 5.1 | Model deployment and SDK client skills only when Azure bridge is executed |

**Exam-coverage boundary:** this program builds more coding skill than AIF-C01 requires, but local applications do not teach every AWS service-selection question or prove cloud experience. Add a vendor bridge for service capabilities, identity, shared responsibility, pricing, managed model services, and governance tools. AI-901 also requires platform-specific text/speech, vision/image generation, information extraction, and single-agent implementation; these need dedicated Azure exercises and may require provisioned services. Do not label this course complete AI-901 exam preparation without them. Similarly, the SecAI+ mappings do not replace the broader security background its blueprint recommends.

## Quarter 1 — Foundations & Data Literacy

### Module 1 — Introduction to AI, Automation & Prompt Engineering

**Learning objectives.** Students will distinguish deterministic automation, predictive ML, and generative AI using workplace examples; explain tokens, context windows, probabilistic generation, and hallucination in plain language; design a prompt with task, context, constraints, examples, and output format; compare prompt versions against a rubric; and decide when a human or conventional software should perform the task.

**Alignment.** S1.1, S1.3, S4.2; AWS 1.1–1.2, 2.1–2.2, 3.2; AI-901 model/workload concepts, responsible AI, and prompt design. Coding is not required yet.

**Proof of work: `01-prompt-evaluation-playbook`.** Create a synthetic service-request summarization and routing playbook. Supply 20 labeled requests, two prompt versions, a scoring rubric, actual model outputs, and a one-page adoption recommendation. Use a free accessible interface or instructor-led/local model session; hand-record results before automating evaluation later.

**Acceptance evidence.** On a separate set of ten previously unseen requests, achieve at least 8/10 correct routes and schema-conforming outputs; make no unsupported factual additions; document failures and required review. Record the model/date/settings available to the student. Report these as small-sample classroom results, not business performance guarantees.

**Security integration.** Threat: a request contains instructions to reveal private content or bypass its assigned task. Treat request text as untrusted data, minimize information supplied, verify factual claims, and retain human approval for actions. Demonstrate that instructions and delimiters reduce some errors but do not create an authorization boundary. Never put secrets in system prompts.

**Assigned free resources.** Hugging Face LLM Course, introductory concepts only; Microsoft AI-901 study guide and its linked introductory learning paths; OWASP 2026 prompt-injection and information-disclosure entries. Use the Python-heavy Hugging Face sections later.

| Week | Lessons and practice | Checkable output |
|---|---|---|
| 1 | File/account orientation; AI vs rules; training vs inference; suitable and unsuitable business cases | Classify ten scenarios and justify two decisions |
| 2 | Tokens, context, capabilities, uncertainty, basic multimodal examples; verify a fabricated claim | Annotated examples and a limitations checklist |
| 3 | Prompt architecture, zero/few-shot examples, output contracts, manual version control | Two prompt versions scored against the same development cases |
| 4 | Synthetic malicious requests, data classification, human review; blinded evaluation and demonstration | GitHub web-uploaded playbook, held-out scores, and three-minute explanation |

### Module 2 — Python Programming Essentials

**Learning objectives.** Students will run Python in VS Code and Colab; use types, collections, branches, loops, and functions; read/write CSV and JSON; debug exceptions; write behavioral tests; create a virtual environment; and use a basic Git branch/commit/review workflow.

**Alignment.** Enables S3.3 and the Python prerequisite for AI-901. Python implementation is an employability extension rather than a direct AIF-C01 objective.

**Proof of work: `02-ticket-intake-cli`.** Build a command-line program that reads synthetic requests, validates required fields, assigns a rule-based queue, and writes JSON summaries. Include a deliberately malformed input file and a repair exercise.

**Acceptance evidence.** At least ten meaningful tests covering normal, empty, malformed, and oversized input; predictable exit/error behavior; a reproducible setup guide; and a live, unseen function change the student can explain.

**Security integration.** Introduce confidentiality/integrity/availability, authentication vs authorization, least privilege, and basic client/server concepts. Validate data rather than executing it; prohibit `eval` on input and unsafe shell interpolation. Store no credentials in notebooks or commits; inspect dependencies and keep generated outputs free of sensitive content.

**Assigned free resources.** CS50P selections: variables/functions, conditionals, loops, exceptions, unit tests, and file I/O; VS Code Python tutorial; Python tutorial as a reference; GitHub Learn introductory Git/GitHub exercises. Completing the entire CS50P course is optional.

| Week | Lessons and practice | Checkable output |
|---|---|---|
| 1 | Interpreter/notebook/editor, variables, types, strings, lists/dictionaries, terminal basics | Small scripts, working environment, and first Git commits |
| 2 | Branches, loops, Boolean conditions, functions, tracing and debugging | Rule-based router and function diagram |
| 3 | CSV/JSON, file paths, exceptions, package environments, dependency records | Working import/export path with readable error messages |
| 4 | Tests, refactoring, Git branches/reviews, safe input handling | Tested CLI, README, reviewed change, and independent modification |

### Module 3 — Data Processing & Statistics for AI

**Learning objectives.** Students will clean and join tabular data with pandas; manipulate arrays and shapes with NumPy; interpret mean/median, variance, standard deviation, percentiles, and outliers; explain sampling bias and correlation vs causation; and verify a pandas summary using SQL.

**Alignment.** S1.2; AWS 1.1, 1.3, 5.1. Data skills support AI-901 without representing a separate named objective.

**Proof of work: `03-data-quality-workbench`.** Process an instructor-provided, seeded dataset of 2,000 fictional tickets with duplicates, missing fields, inconsistent dates, invalid categories, and synthetic identifiers. Produce a reusable cleaning script, data dictionary, lineage record, SQLite queries, and a concise exploratory report.

**Acceptance evidence.** Detect all intentionally seeded schema violations; account for every removed/changed row; reconcile pre/post counts; match three SQL summaries to pandas; and explain why a chosen missing-value treatment is appropriate. Statistical plots must include units, sample sizes, and relevant limitations.

**Security integration.** Threats include accidental identifier disclosure, silent data corruption, and contaminated sources. Preserve an immutable source copy, validate schema and ranges, document provenance and transformation decisions, and limit exports. A hash establishes consistency relative to a trusted reference, not source trustworthiness or privacy. Explain why identifier removal alone may leave re-identification risk.

**Assigned free resources.** pandas Getting Started tutorials on reading, filtering, derived columns, statistics, and joins; NumPy Absolute Basics; selected OpenStax Introductory Statistics 2e sections; SQLite SELECT, JOIN, and aggregate documentation.

| Week | Lessons and practice | Checkable output |
|---|---|---|
| 1 | Percentages, elementary algebra, arrays/shapes, vectors, basic tables; load CSV/JSON | Data dictionary and source profile |
| 2 | Distributions, summary statistics, sampling, conditional probability intuition, correlation | Annotated exploratory notebook with defensible conclusions |
| 3 | Missingness, duplicates, dates, joins, validation, provenance | Deterministic cleaning pipeline and row-level reconciliation |
| 4 | SQLite SELECT/WHERE/GROUP BY/JOIN; parameterized queries; reporting | SQL/pandas checks, data-quality report, and reproducibility instructions |

**Quarter 1 gate:** a student can run and explain a script, clean unseen data, distinguish AI from automation, and identify inappropriate data sharing. Remediate these skills before advancing.

## Quarter 2 — Core Machine Learning & Model Security

### Module 4 — Supervised & Unsupervised Machine Learning

**Learning objectives.** Students will identify features/labels; distinguish regression, classification, and clustering; train linear/logistic regression, decision trees, random forests, and a clustering model with scikit-learn; compare against a simple baseline; and explain predictions without treating clusters as verified categories.

**Alignment.** S1.1, S1.3; AWS 1.1–1.3; AI-901 workload/model-selection concepts. Model implementation exceeds foundational certification expectations.

**Proof of work: `04-ml-baseline-comparison`.** On reproducible synthetic business data, predict a numeric outcome, classify a ticket category, and explore customer/ticket clusters. Provide clear feature availability times, baselines, preprocessing pipelines, model comparisons, and a model card.

**Acceptance evidence.** Execute all five model families, use splits fixed before training, and compare primary models with appropriate dummy baselines. Explain an observed error and the business cost of choosing the wrong model. There is no arbitrary universal accuracy threshold.

**Security integration.** Identify label leakage, sensitive features, proxy attributes, and untrusted model downloads. Introduce train/test separation immediately; preprocessing learns only from training data. Use locally trained artifacts and explain unsafe deserialization risk.

**Assigned free resources.** Inria scikit-learn MOOC, predictive modeling and linear/tree selections; scikit-learn User Guide for linear models, trees, ensembles, and clustering.

| Week | Lessons and practice | Checkable output |
|---|---|---|
| 1 | Problem framing, features/targets, vectors and weighted sums, splits, dummy models | Written task/metric choice and baseline notebook |
| 2 | Linear and logistic regression, scaling, coefficients, classification vs regression | Two fitted pipelines and plain-language interpretation |
| 3 | Trees and random forests, complexity, feature effects | Comparative results and an error analysis |
| 4 | K-means, scaling and cluster inspection; limits of unsupervised results | Reproducible comparison package and model card |

### Module 5 — Model Training, Evaluation & Validation

**Learning objectives.** Students will design train/validation/test partitions; prevent group/time leakage; use cross-validation within training data; calculate and interpret precision, recall, F1, MAE/RMSE, and confusion matrices; choose a threshold using business costs; and describe drift and uncertainty.

**Alignment.** S1.3, S2.5; AWS 1.3, 3.4, 4.1–4.2; AI-901 responsible AI/model choice. Foundation-model evaluation is introduced here and applied in Modules 7–9.

**Proof of work: `05-evaluation-and-leakage-audit`.** Extend Module 4 into an imbalanced escalation classifier. Deliberately add a post-outcome leakage feature, expose misleading performance, remove it, and rebuild the evaluation. Compare rule-based, dummy, and trained approaches.

**Acceptance evidence.** Freeze the test partition; select preprocessing, hyperparameters, and thresholds using training/validation only; evaluate the selected approach once on test data. Report class counts, confusion matrix, per-class metrics, and a simple bootstrap interval where appropriate. Document limitations of synthetic labels and small subgroup sizes.

**Security integration.** Treat evaluation data and metric reports as integrity assets. Restrict edits, record dataset/model hashes and versions, and distinguish honest mistakes from deliberate metric manipulation. Never equate a language model's stated confidence with calibrated probability.

**Assigned free resources.** Inria MOOC on validation/learning curves; scikit-learn Common Pitfalls, cross-validation, and model-evaluation documentation.

| Week | Lessons and practice | Checkable output |
|---|---|---|
| 1 | Under/overfitting; random, stratified, grouped, and time-based splitting | Partition plan and an intentionally leaky counterexample |
| 2 | Confusion matrices, precision/recall/F1, PR tradeoffs, MAE/RMSE | Hand-verified metric examples and automated report |
| 3 | Pipelines, cross-validation, modest tuning, threshold costs, uncertainty | Validation-only selection record |
| 4 | Final held-out assessment, subgroup errors, drift scenarios, release criteria | Auditable evaluation card and go/no-go recommendation |

### Module 6 — Security in the AI Lifecycle & Data Protection

**Learning objectives.** Students will map a data/model lifecycle and its trust boundaries; classify data; detect selected PII types; implement minimization and controlled data release; detect seeded integrity problems; and distinguish laws, voluntary frameworks, and organizational policies.

**Alignment.** S1.2–1.3, S2.4, S4.3; AWS 5.1–5.2; AI-901 privacy/security principles.

**Proof of work: `06-protected-data-pipeline`.** Ingest synthetic tickets, validate schema and source manifests, identify and redact supported PII types, quarantine suspicious records, and write a release report. Keep raw files and sanitized outputs separate. Include a deletion/retention demonstration and mock access roles.

**Acceptance evidence.** Evaluate at least 100 labeled synthetic PII examples and report entity-level precision/recall by type. Test that known synthetic identifiers do not appear in released logs/exports. Detect a seeded file alteration and record quarantined cases. State which poisoning scenarios remain undetected; hashes cannot identify semantically poisoned but correctly hashed data.

**Security integration.** Model unauthorized access, accidental logging, malicious training rows, and excessive retention. Introduce TLS and at-rest encryption concepts, identity-bound permissions, access logs, provenance, and human quarantine review. Redaction is imperfect, pseudonymization is not necessarily anonymization, and sanitized output is not automatically safe for publication.

**Compliance scope.** Teach GDPR applicability, lawful basis, purpose limitation, minimization, retention, and rights as an introductory scenario analysis. Separate these from the voluntary NIST AI RMF. The lab demonstrates selected controls; it does not certify GDPR compliance.

**Assigned free resources.** Presidio quickstart/recognizers/evaluation guidance; NIST AI RMF and Generative AI Profile; official GDPR text and European Commission explanatory guidance. Use official sources for legal concepts and recheck applicability for each cohort.

| Week | Lessons and practice | Checkable output |
|---|---|---|
| 1 | Security primitives review, data classification, lifecycle, trust boundaries, retention | Data-flow/threat diagram and classification policy |
| 2 | PII labels, detection, masking/redaction, minimization, test design | Redaction pipeline and labeled evaluation cases |
| 3 | Poisoning scenarios, provenance, trusted manifests, quarantine, role permissions | Alteration/quarantine demonstrations and access tests |
| 4 | GDPR scenario, NIST distinction, deletion/retention evidence, control review | Release report, limitations, and privacy/security briefing |

**Quarter 2 gate:** justify an evaluation without leakage; reproduce a pipeline; identify data release risks; and defend a limited model recommendation using evidence. For a transfer challenge, repeat one cleaning/evaluation task on an instructor-vetted public dataset with documented license and provenance. This exposes students to naturally occurring messiness and reduces dependence on synthetic patterns.

## Quarter 3 — Generative AI, Systems & Threat Defense

### Module 7 — Applied Generative AI & API Integration

**Learning objectives.** Students will describe HTTP, JSON, REST, SDKs, and status codes; build a small Python model client and FastAPI endpoint; validate structured outputs; handle timeout/retry/rate errors; compare prompting, RAG, and fine-tuning; and measure quality, latency, and estimated cost.

**Alignment.** S1.1, S2.2–2.3; AWS 2.3, 3.1–3.4, 5.1; AI-901 Foundry SDK/client/deployment skills only when the optional platform bridge is executed.

**Proof of work: `07-model-gateway`.** Build a ticket-summary API with a provider-neutral adapter, a deterministic fixture, and one real small-model backend. Add adapters from official OpenAI/Anthropic examples without requiring paid calls. Record any unexecuted adapter as untested.

**Acceptance evidence.** Evaluate at least 30 held-out requests; report schema success, factual correctness against inputs, rejection behavior, and latency. Test 429/5xx errors, unavailable backends, timeout, malformed responses, and retry limits. Use a representative small pretrained model for genuine inference; fixture success cannot substitute for model quality.

**Security integration.** Environment-based secrets, restricted credentials, authenticated routes, payload/token limits, bounded retries, dependency review, sanitized logs, and explicit output validation. Never execute model-generated code or allow arbitrary outbound URLs. Use an instructor-provided simple authentication scaffold until students understand it.

**Fine-tuning scope.** Required: a decision memo and a small curated train/validation example set. Optional: tune a tiny model in an approved notebook session and compare it with a baseline. Full LLM fine-tuning is not a beginner hardware requirement.

**Assigned free resources.** Hugging Face LLM Course inference/Transformers sections; FastAPI tutorial; official OpenAI and Anthropic API documentation. Documentation is free; hosted inference is not promised free.

| Week | Lessons and practice | Checkable output |
|---|---|---|
| 1 | HTTP/JSON, REST/SDKs, environment configuration, fixture and first inference | Working client with request/response explanation |
| 2 | FastAPI request/response models, validation, authentication scaffold | Documented endpoint and integration tests |
| 3 | Provider adapters, timeouts/backoff, limits, structured-output failures | Bounded failure handling and execution-status matrix |
| 4 | Model evaluation, customization decision, optional tiny tuning | Evaluation report, model gateway, and decision memo |

### Module 8 — RAG & Vector Databases

**Learning objectives.** Students will explain embeddings and cosine similarity; create a local vector index; compare chunking/retrieval approaches; evaluate retrieval separately from generated answers; enforce document authorization before model context construction; and handle deletion and stale content.

**Alignment.** S1.2, S2.3–2.4; AWS 2.1, 3.1, 3.4, 5.1. This is supporting application practice for AI-901, not a separately named RAG objective.

**Proof of work: `08-permission-aware-policy-assistant`.** Index 20–50 instructor-authored BrewByte policies in local Chroma using a small SentenceTransformers model. Give two mock roles different document permissions. Return cited answers or abstain when evidence is insufficient. Pinecone is an optional comparison, not a required account.

**Acceptance evidence.** Use 30 labeled questions covering answerable, unanswerable, stale, and unauthorized requests. Report Recall@k, citation correctness, supported-answer rate, abstention quality, and latency. All seeded unauthorized retrieval cases must return no forbidden content. Test authorization at retrieval and context assembly; authorization data comes from verified server-side identity, not user prompt text.

**Security integration.** Retrieved content is untrusted; defend against indirect prompt injection, cross-role leakage, unauthorized ingestion, and embedding/index exposure. Use approved sources, source metadata, role filters, controlled ingestion, and deletion/reindex tests. Similarity scores do not establish permission or answer certainty.

**Assigned free resources.** SentenceTransformers semantic-search documentation; Chroma local/getting-started documentation; OWASP 2026 vector/embedding and injection entries; Hugging Face embedding examples.

| Week | Lessons and practice | Checkable output |
|---|---|---|
| 1 | Vectors, dot product/cosine intuition, embeddings, lexical baseline | Small semantic-search notebook and baseline comparison |
| 2 | Chunk size/overlap, metadata, local storage, document versions | Repeatable ingestion/index build |
| 3 | Retrieval, context assembly, citations, unknown-answer handling | Assistant and labeled retrieval/answer test set |
| 4 | Role enforcement, malicious documents, stale data, deletion | Security tests, evaluation report, and data-flow diagram |

### Module 9 — Securing AI Systems & Adversarial Defense

**Learning objectives.** Students will build an asset/trust-boundary threat model; connect threats to OWASP and MITRE ATLAS; reproduce safe attacks in their own isolated lab; implement layered controls; and measure attack success and benign-request rejection before and after a change.

**Alignment.** S2.1–2.6; AWS 3.2, 5.1; AI-901 responsible AI with additional secure-development practice.

**Proof of work: `09-ai-security-assurance-lab`.** Harden Module 8 with an OWASP 2026 traceability matrix, a documented attack set, access checks, safe rendering, tool restrictions, request limits, and security regression tests. For model extraction, inversion, and membership inference, perform a bounded conceptual or toy-model demonstration and discuss limits; do not claim to prevent all variants.

**Acceptance evidence.** At least 40 cases across the relevant threat categories plus 20 benign cases. Give each case an expected result and severity. Demonstrate zero bypasses in seeded authorization/tool-permission tests and no secret exposure in the defined test suite; report residual injection failures honestly. Test results do not prove universal security. A scanner run without reviewed findings is insufficient.

**Security integration.** Apply deny-by-default server-side permissions, read-only/allowlisted tools, human approval for consequential actions, output escaping, safe deserialization, dependency/model provenance, quotas/timeouts, and log minimization. Prompts, safety classifiers, and model refusals supplement these boundaries rather than enforce them alone.

**Assigned free resources.** OWASP 2026 canonical publication/source; MITRE ATLAS; NVIDIA garak; OWASP prompt-injection prevention guidance. Run attack exercises only against student-owned or explicitly authorized targets.

| Week | Lessons and practice | Checkable output |
|---|---|---|
| 1 | Assets, attacker goals, entry points, STRIDE-style boundaries, OWASP/ATLAS mapping | Prioritized threat model and attack-case plan |
| 2 | Direct/indirect injection, information exposure, unsafe output, tool abuse | Reproducible isolated attack results |
| 3 | Layered mitigations, access enforcement, model/supply-chain controls, budgets | Hardened application and control tests |
| 4 | Regression, limited garak probes, benign-case tradeoffs, evidence review | Before/after report and residual-risk register |

### OWASP 2026 threat-to-control reference

The 2026 publication is the baseline. Some older OWASP landing pages still display 2025 identifiers; always attach the edition to an identifier rather than mixing years.

| 2026 identifier | Risk | Required curriculum control or exercise |
|---|---|---|
| LLM01 | Prompt Injection | Untrusted-content handling, tool isolation, adversarial regression |
| LLM02 | Sensitive Information Disclosure | Data minimization, access checks, redaction evaluation |
| LLM03 | Excessive Agency | Read-only scoped tools, action approval, allowlists |
| LLM04 | Supply Chain | Trusted sources, reviewed versions, dependency/model provenance |
| LLM05 | Data and Model Poisoning | Controlled ingestion, lineage, quarantine, integrity checks |
| LLM06 | Unbounded Consumption | Payload/token caps, bounded retries, rate/time limits |
| LLM07 | Misinformation | Evidence-based answers, citations, abstention, human review |
| LLM08 | Hidden Context Exposure | No secrets in hidden context, isolate access-controlled content |
| LLM09 | Vector and Embedding Weaknesses | Permission-aware retrieval, protected indexes, deletion tests |
| LLM10 | Improper Output Handling | Schema checks, escaping, no arbitrary execution |

**Quarter 3 gate:** demonstrate one real generative application, a measured retrieval pipeline, and working server-side authorization. Students must explain at least one successful attack and its mitigation.

## Quarter 4 — AI-Assisted Operations, Governance & Career Launch

### Module 10 — AI-Assisted Security & Operations

**Learning objectives.** Students will parse and normalize synthetic security events; correlate alerts with rules; compare rule-based and ML anomaly detection; generate evidence-linked incident summaries; implement a human-reviewed automation workflow; and identify AI-enabled impersonation or misinformation risks.

**Alignment.** S2.5, S3.1–3.3; AWS 1.2–1.3, 3.4, 5.1; AI-901 app/agent and text-analysis skills when practiced on the named platform.

**Proof of work: `10-security-triage-assistant`.** Process 1,000 synthetic login/endpoint events containing ten known incident storylines. Correlate events, compare rules with IsolationForest or a similar small baseline, and draft incident tickets with event IDs, severity rationale, uncertainty, and next investigative steps. All response actions are dry-run proposals.

**Acceptance evidence.** Report storyline-level precision/recall, duplicate-alert reduction, unsupported-claim rate, and measured review time on a defined sample. Compare against a deterministic baseline. Reject attempts to trigger real account changes, network blocks, or arbitrary tools. Evaluate an incident-summary model separately from event-detection rules.

**Security integration.** Treat logs as attacker-controlled text, preserve evidence identifiers/timestamps, redact sensitive data, scope agent tools, and require approval outside the model. Use synthetic impersonation/deepfake scenarios for defensive analysis; no impersonation of real people is needed.

**Assigned free resources.** MITRE ATT&CK/ATLAS; scikit-learn anomaly-detection guide; Python logging documentation; official CI/testing guidance; NIST incident-response resources. A full SIEM installation is optional, not a prerequisite.

| Week | Lessons and practice | Checkable output |
|---|---|---|
| 1 | Incident-response fundamentals, event fields, timestamps, baselines, parsing | Normalized synthetic event store and schema tests |
| 2 | Correlation rules, anomaly detection, false positives, ground truth | Comparative detection report |
| 3 | Evidence-linked summaries, read-only agent/tool scaffold, approval queues | Dry-run incident ticket workflow |
| 4 | Adversarial log text, impersonation tabletop, automation failure/recovery | Triage evaluation, runbook, and five-minute demonstration |

### Module 11 — AI Governance, Risk & Compliance

**Learning objectives.** Students will inventory an AI use case and assign owners; organize risks using NIST Govern/Map/Measure/Manage; assess impacts and evidence; write proportionate AI-use and data policies; implement a testable guardrail; and communicate a release decision to an executive audience.

**Alignment.** S4.1–4.3, S2.2, S2.5; AWS 4.1–4.2, 5.2; AI-901 responsible AI principles.

**Proof of work: `11-ai-governance-release-pack`.** Produce a short application/system card, an AI inventory entry, data-flow map, RACI, ten-risk register, control/evidence matrix, supplier questionnaire, monitoring/incident plan, and a two-page release memo. Apply the pack to the actual student application, including known weaknesses.

**Acceptance evidence.** Every material risk has an owner, mitigation, evidence pointer, residual rating, and review trigger. Each governance claim must link to a test or clearly identify missing evidence. Test at least 20 prohibited and 20 permitted cases against one implemented policy, reporting bypasses and false rejections. An independent reviewer should reproduce the decision from the supplied record.

**Security integration.** Integrate privacy, fairness, transparency, data residency, retention, model/supplier change control, shadow AI, and human oversight. Use deterministic policy enforcement as the required low-compute path; optionally compare NeMo Guardrails or a suitable Llama Guard model. Evaluate their model/backend requirements and license. Guardrails are fallible and do not confer legal compliance.

**Assigned free resources.** NIST AI RMF Playbook and Generative AI Profile; OECD AI Principles; official European Commission/EUR-Lex AI Act guidance; NeMo Guardrails documentation. Discuss ISO AI management/risk standards at a high level using official summaries; paid standards texts are not required course purchases.

| Week | Lessons and practice | Checkable output |
|---|---|---|
| 1 | AI inventory, stakeholders, intended/prohibited uses, accountable owners | Inventory, RACI, system card, and scope statement |
| 2 | NIST functions, impact assessment, threat/business risk, fairness limitations | Ten-risk register with evidence gaps |
| 3 | Testable policy, deterministic/optional model guardrails, retention and supplier review | Implemented guardrail and evaluation report |
| 4 | Legal applicability scenario, exceptions, residual risk, governance board simulation | Release memo and defensible approve/defer/reject decision |

### Module 12 — Capstone, Deployment & Career Launch

**Learning objectives.** Students will package a tested AI application with FastAPI and containers; deploy/run it reproducibly; apply basic identity, secret, dependency, and logging controls; demonstrate rollback and failure recovery; document a portfolio honestly; and complete an interview explanation and unseen repair task.

**Alignment.** S1.3, S2.2–2.5, S3.3; AWS 1.3, 2.3, 3.1, 5.1; AI-901 platform deployment/client skills only for executed Azure exercises. Docker and FastAPI implementation are broader employment skills.

**Proof of work: `12-secure-ai-operations-capstone`.** Integrate the protected dataset pipeline, ticket analytics, permission-aware policy assistant, measured model behavior, triage workflow, and governance release record. Narrow scope to a reliable vertical slice instead of integrating every experiment. Required deployment is reproducible local container execution; hosted cloud deployment is optional and clearly labeled.

**Acceptance evidence.** A reviewer can follow a clean setup, run tests, start the container, issue an authenticated request, demonstrate a denied request, trigger a controlled failure, and roll back a release. Provide health checks, a monitoring sample, dependency versions, model/data provenance, an architecture diagram, known limitations, and a five-minute demo. Record actual measurements rather than declaring the app production-ready solely because it runs.

**Security integration.** Non-root containers where feasible, minimal dependencies, secret injection rather than image-baked secrets, safe artifact loading, request/time limits, sanitized logs, least-privilege deployment, and dependency scans with reviewed findings. Public code can be showcased without exposing an unauthenticated model endpoint.

**Assigned free resources.** FastAPI tutorial/deployment guidance; Docker getting-started and build guidance; GitHub Learn/Actions documentation; free Microsoft Learn/AWS documentation for the chosen optional bridge. Verify current hosting allowances before any cloud exercise.

| Week | Lessons and practice | Checkable output |
|---|---|---|
| 1 | Scope freeze, API review, container image/build, environments | Reproducible container and integrated test plan |
| 2 | CI checks, deployment, health/observability, failure/recovery | Local release, clean-run evidence, rollback record; optional cloud lab |
| 3 | Final evaluation, security review, peer acceptance, documentation | Release candidate, security report, and system/governance cards |
| 4 | Portfolio curation, résumé evidence, targeted applications, mock interview | Three curated showcases, demo, role-specific résumé, and unseen repair |

## Assessment, progression & employment evidence

Use the same rubric each month: **35% functional behavior, 25% evidence/evaluation, 20% security/privacy, 10% reproducibility/documentation, 10% explanation and independent modification**. Proposed progression threshold: at least 80/100 plus all mandatory controls. This threshold is an instructional rule, unrelated to vendor exam scoring.

An unresolved credential exposure, seeded authorization bypass, fabricated result, or inability to explain the central code requires correction and reassessment. Keep other feedback proportionate and specific. Offer a new but equivalent task after remediation; repeat-until-pass with the identical answers does not demonstrate transfer.

Every module submission includes a README, source/notebooks as appropriate, a small synthetic fixture or licensed source reference, environment/dependency record, results with denominators, threat/control notes, limitations, and AI-assistance disclosure. Add behavioral tests as soon as code begins. Do not publish private originals merely to prove a redaction pipeline.

**Career work starts before Month 12.** In Quarter 1, read job descriptions and practice explaining scripts. In Quarter 2, create a skills-to-evidence matrix and describe a data/model decision. In Quarter 3, practice demos, code review, and informational interviews using synthetic work. In Quarter 4, tailor applications to current requirements and rehearse debugging/technical explanations.

| Portfolio emphasis | Roles to investigate, subject to local requirements | Evidence a hiring reviewer can inspect |
|---|---|---|
| Python + data + deployment | Junior Python developer, AI application support, technical AI implementation | Tested code, API handling, SQL, clean deployment and troubleshooting |
| Data + evaluations | Junior data operations or AI evaluation/support roles | Data-quality pipeline, labels, evaluation design and error analysis |
| Governance + technical literacy | AI governance coordinator or junior technology-risk support | Risk register, evidence-linked controls, data map and release memo |
| Security operations + AI | Entry security operations/support roles with additional security preparation | Event correlation, triage validation, access controls and incident runbook |

These are pathway examples, not verified vacancies or a promise that a particular job accepts beginners. Students pursuing AI/ML engineering should add software design, stronger mathematics, databases, cloud operations, and real collaborative experience after this foundation.

## Official sources and assigned-resource directory

Certification and framework claims were checked against the sources below. Links and free-service conditions can change; revalidate the blueprint and cohort environment before launch. Named exam providers do not endorse this curriculum.

### Certification sources

- [CompTIA-authored SecAI+ CY0-001 objectives, document v2.0, hosted by ONLC](https://www.onlc.com/graphics/Publications/CompTIA/comptia-secai-cy0-001-exam-objectives.pdf). Mapping source, not a promise that this mirrored file is the latest revision.
- [AWS AIF-C01 official exam guide](https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01.html).
- [AWS domain 1 tasks](https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain1.html), [domain 2](https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain2.html), [domain 3](https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain3.html), [domain 4](https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain4.html), [domain 5](https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain5.html).
- [AI-901 official study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-901).
- [AI-900 retirement notice](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-900).

### Quarter 1 resources

- M1: [Hugging Face LLM Course introduction](https://huggingface.co/learn/llm-course/chapter1/1); [AI-901 learning links](https://learn.microsoft.com/en-us/credentials/certifications/exams/ai-901/); [OWASP 2026 source](https://github.com/GenAI-Security-Project/GenAI-LLM-Top10).
- M2: [CS50P OpenCourseWare](https://cs50.harvard.edu/python/); [VS Code Python tutorial](https://code.visualstudio.com/docs/python/python-tutorial); [Python tutorial](https://docs.python.org/3/tutorial/); [GitHub Learn](https://learn.github.com/); [Colab FAQ and limits](https://research.google.com/colaboratory/faq.html).
- M3: [pandas introductory tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/); [NumPy absolute basics](https://numpy.org/doc/stable/user/absolute_beginners.html); [OpenStax statistics](https://openstax.org/details/books/introductory-statistics-2e); [SQLite language reference](https://www.sqlite.org/lang.html).

### Quarter 2 resources

- M4: [Inria scikit-learn MOOC](https://inria.github.io/scikit-learn-mooc/); [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html).
- M5: [Common Pitfalls](https://scikit-learn.org/stable/common_pitfalls.html); [cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html); [model evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html).
- M6: [Presidio](https://presidio.dataprivacystack.org/); [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework); [NIST Generative AI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf); [GDPR official text](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng); [European Commission data protection](https://commission.europa.eu/law/law-topic/data-protection_en).

### Quarter 3 resources

- M7: [Hugging Face course](https://huggingface.co/learn/llm-course/chapter1/1); [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/); [OpenAI API documentation](https://platform.openai.com/docs/overview); [Anthropic API documentation](https://docs.anthropic.com/en/docs/overview).
- M8: [SentenceTransformers](https://sbert.net/); [Chroma documentation](https://docs.trychroma.com/); [OWASP 2026 publication](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/).
- M9: [OWASP canonical repository](https://github.com/GenAI-Security-Project/GenAI-LLM-Top10); [MITRE ATLAS](https://atlas.mitre.org/); [NVIDIA garak](https://github.com/NVIDIA/garak); [OWASP prompt-injection prevention cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html).

### Quarter 4 resources

- M10: [MITRE ATT&CK](https://attack.mitre.org/); [scikit-learn outlier detection](https://scikit-learn.org/stable/modules/outlier_detection.html); [Python logging](https://docs.python.org/3/library/logging.html); [NIST incident response](https://csrc.nist.gov/projects/incident-response).
- M11: [NIST AI RMF Playbook](https://airc.nist.gov/airmf-resources/playbook/); [OECD AI Principles](https://oecd.ai/en/ai-principles); [European Commission AI Act information](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai); [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails).
- M12: [FastAPI deployment](https://fastapi.tiangolo.com/deployment/); [Docker getting started](https://docs.docker.com/get-started/); [GitHub Actions documentation](https://docs.github.com/en/actions); the selected vendor's official deployment/identity documentation.

## Optional vendor bridge: evidence required before claiming cloud skills

Schedule these within flexible weeks or as clearly labeled additional study; completing both vendor tracks may require more time. Free documentation can be studied without provisioning services. Real platform execution depends on current access, quotas, region, and funding; it is not included in the zero-cost completion requirement.

| Track | Concrete exercise | Evidence and boundary |
|---|---|---|
| AWS baseline | Map the application to S3, IAM, Bedrock/SageMaker AI, CloudTrail, and appropriate encryption/network controls; compare two service choices and estimate a small workload | Architecture, shared-responsibility matrix, cost assumptions, and service-selection explanations support AIF-C01 study but do not establish deployment experience |
| AWS execution, optional | In an approved sandbox, provision the minimum permitted model access, make an authenticated synthetic-data request, inspect available audit evidence, revoke access, and remove provisioned resources | Sanitized configuration/execution/cleanup evidence; record any logging coverage gaps and actual spend |
| Azure concepts and client | Study AI-901's current two skill areas; in an approved subscription, deploy an allowed model and build a minimal Foundry SDK chat client | Executed deployment and client demonstration; a local compatible endpoint is not a replacement for this evidence |
| Azure agent | Create/test a single agent and a lightweight client using a narrowly scoped read-only tool | Agent transcript, access restrictions, failure case, and cleanup record |
| Azure modalities and extraction | Complete distinct lightweight exercises for text analysis, speech, vision/image generation, and Content Understanding information extraction using the official learning path | Explicit objective checklist and executed outputs for each skill; document unsupported/region-restricted features and remaining gaps |

## Instructor launch checklist

Before enrollment, supply synthetic data generators/fixtures and labels; model license/revision and CPU benchmark; starter code that gradually removes scaffolding; role/authorization fixtures; held-out evaluations; scoring exemplars and remediation tasks; a tested package lockfile; optional cloud budgets/cleanup; accessibility alternatives; and an updated certification crosswalk. This document specifies the course and projects; those runnable lab assets and lesson scripts still need authoring and pilot testing.

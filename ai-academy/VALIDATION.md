# Initial pilot validation

Date: October 22, 2026. These are repository execution checks, not a course-completion record or security certification.

- Deterministic generator: 12 module assignments, 48 weekly lessons, 12 notebooks and starter scripts, shared datasets, and rendered HTML. Freshness checked with `build_course.py --check`.
- Offline validator: required module fields, lesson content, local HTML paths/anchors, notebook/Python syntax, empty notebook outputs, and selected credential patterns. External URLs were not exhaustively network-tested.
- Core/classical-ML suite: 17 tests passed with ML enabled, including execution of all 12 worked notebooks, chronological model comparisons, row accounting, SQLite checks, incident evidence, permission-aware retrieval and read-only tools. Tested on Python 3.12 with the declared NumPy 2.2.6, pandas 2.2.3 and scikit-learn 1.6.1 and SciPy 1.15.3 direct pins.
- HTTP scaffold: 5 tests passed for health labeling, missing/invalid credentials, server-bound roles, extra role-field rejection, blank/oversized input, and fixture output labeling/redaction.
- Public security corpus: 60 toy boundary cases passed. These inspect deterministic code boundaries, not an LLM's resistance to prompt injection.
- Existing lab files: byte-for-byte unchanged; only portal navigation/copy and README are edited outside the new Academy/workflow paths.

## Not established by these checks

### Windows portability correction — October 23, 2026

The initial publisher relied on locale-default text decoding. A simulated Windows CP1252 default reproduced the reported 122 generated-file mismatches. Course source, generated-text comparisons, validation and lab reads now specify UTF-8 explicitly; generated writes use UTF-8 and LF line endings. A regression test verifies generation with simulated legacy Windows defaults. The updated core/ML suite passes 18 tests. This regression does not require a PowerShell session setting. The review-package publisher additionally sets UTF-8 for child Python processes and checks workflow permission before cloning. The actual authenticated Windows publishing path still needs execution on the user's computer.

- Real local LLM/embedding execution, provider SDK behavior, RAG answer quality, fine-tuning results, and cloud deployment remain separate learner/instructor exercises.
- Docker execution was not performed in the authoring environment. The local API was exercised through HTTP test clients.
- Full browser rendering and mobile visual review were not completed: a browser binary download failed. Semantic HTML, stylesheet references and local navigation were checked programmatically. Include desktop/mobile review before publishing.
- GitHub-hosted workflow results are separate from these local results. A new workflow may require repository-owner approval before running. Python 3.11 is configured in CI but local execution used 3.12.

Pilot the lessons with a beginner, verify model/hardware access, review external resources, and create private summative assessments before advertising a finished instructional release.

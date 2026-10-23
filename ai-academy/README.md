# BrewByte AI Academy

A 12-module, 48-week learning pathway using a fictional coffee business. Start at [the Academy](index.html), or read the [course guide](docs/start-here.md).

## Build and check

From the repository root, using Python 3.11 or 3.12:

```sh
python ai-academy/tools/build_course.py
python ai-academy/tools/validate_course.py
python -m unittest discover -s ai-academy/tests -v
```

The core demonstrations and checks use the Python standard library. Install `ai-academy/requirements-ml.txt` in a virtual environment for pandas/scikit-learn demonstrations. Model/API dependencies are separate and optional for repository checks, but real-model execution is required before claiming generative-AI mastery.

Preview the entire portal locally with `python -m http.server 8000` from the repository root, then open `http://localhost:8000/ai-academy/`. GitHub Pages serves the committed HTML; it does not execute Python or host the lab API. Existing publishing settings remain unchanged. If Pages currently publishes `main` at the repository root, merging the reviewed PR includes this pathway in its next publication.

## Authoring workflow

Edit `source/course.json`, lesson content in that file, or the clearly labeled guided lab code. Run the builder and checks. Generated `modules/`, `index.html`, datasets, and starter notebooks must be committed with the source. `build_course.py --check` detects stale generated output without rewriting it. The builder writes only known Academy-generated paths and never deletes portal files or custom files. It never calls a model provider, asks for credentials, or pushes commits.

The GitHub Actions check runs on relevant PRs and pushes. It tests deterministic code and optional classical-ML demos. It does **not** claim to evaluate real LLM quality, cloud deployment, or external link availability. Course authors review those separately.

## Course status

This initial review release contains all 48 lessons, module assignments/rubrics, 12 guided lab notebooks and starter scripts, shared synthetic data, and executable baseline checks. Model exercises include an explicit live-model route and execution limitations. It requires instructor pilot review; it is not a vendor-endorsed certification product or a placement guarantee. No student assessment answer keys are included. Worked examples are deliberately public instructional material.

Do not commit instructor keys, student submissions, credentials, or real business records. Keep instructor assessments in a separate private repository. No learner telemetry or external tracking is included.

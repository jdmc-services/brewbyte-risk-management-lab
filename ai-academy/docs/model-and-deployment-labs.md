# Live models and deployment: execution boundaries

Core fixtures are deterministic. They are not substitutes for actual model, embedding, container, or cloud evidence. Use synthetic input only and never execute model output. The adapters in this release support local Transformers generation and local embeddings/Chroma. Hosted OpenAI/Anthropic adapters remain student extensions; no successful provider integration is claimed.

## Prepare a local-model environment

Use a separate virtual environment and install `ai-academy/requirements-model.txt`. The ranges in this experimental file are not a tested lockfile. Freeze your working environment after the instructor validates it. Use an approved small model that fits available RAM, review its model card/license, and record a commit revision. A small model can demonstrate inference while failing the instructional-quality rubric. Hardware/GPU access in free notebooks varies.

```sh
python ai-academy/labs/live_model.py --model APPROVED_MODEL_ID --revision REVIEWED_COMMIT --text "Summarize: BrewByte opens at seven."
```

Replace the uppercase arguments with an actual instructor-approved model and reviewed revision. This downloads model weights on first execution. Do not enable remote code execution to make an unknown model work. Report the returned text, runtime, model/revision, software versions, and failures. The script does not upload input to an inference provider.

## Real embedding/RAG exercise

```sh
python ai-academy/labs/embedding_rag.py --embed-model APPROVED_EMBEDDING_ID --embed-revision REVIEWED_COMMIT --gen-model APPROVED_GENERATOR_ID --gen-revision REVIEWED_COMMIT --role public --query "What is the refund policy?"
```

The CLI role simulates an already authenticated caller for isolated testing; it is not a network authentication system. The API scaffold establishes identity separately. The example builds an ephemeral role-filtered index before retrieval. Students extend chunking, deletion/version tests, citation validation, and abstention. Score retrieval and generation separately; do not infer truth from vector similarity. No model-weight download or live RAG quality test is performed by core CI.

## Local API and container

Install the optional API dependencies, set distinct randomly generated staff and manager tokens in environment variables, then run:

```sh
python -m uvicorn api:app --app-dir ai-academy/labs --host 127.0.0.1 --port 8000
```

Request `/health`, then POST JSON `{"text":"What is the refund policy?"}` to `/policy` with a Bearer credential. Verify that missing/invalid credentials fail. The API uses a fixture/lexical backend and simple teaching credentials; a public service needs managed identity, TLS, rate limits, rotation, monitoring, and review.

Build from the repository root:

```sh
docker build -f ai-academy/Dockerfile -t brewbyte-academy:pilot .
docker run --rm -p 127.0.0.1:8000:8000 --env BREWBYTE_STAFF_TOKEN --env BREWBYTE_MANAGER_TOKEN brewbyte-academy:pilot
```

Tokens come from the host environment, not the image. Inspect health, test authorization, stop the container, and relaunch the previously reviewed image tag to demonstrate rollback. A container run is local evidence; cloud execution is optional and must be recorded separately.

## Optional cloud bridge

Use an approved AWS/Azure sandbox. Record identity permissions, service/model selection, cost assumptions, deployment, one authenticated synthetic request, audit evidence, failure handling, and cleanup. Use hard quotas where supported; budget alerts alone do not cap costs. AI-901 also requires dedicated platform agent, text/speech, vision/image generation, and information-extraction exercises. Local examples do not establish those skills. See the curriculum blueprint for the detailed boundary.

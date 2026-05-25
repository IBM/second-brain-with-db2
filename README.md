# second-brain-with-db2

A FastAPI app for building a personal knowledge base — fetches URLs via [docling](https://github.com/DS4SD/docling), extracts the article content, and stores it in IBM Db2 for later retrieval.

Built incrementally — each stage under [stages/](stages/) is a self-contained, runnable snapshot showing how the app evolves from a minimal save endpoint toward more sophisticated processing.

## Stages

| Stage | Description |
|-------|-------------|
| [01-basic](stages/01-basic/) | Minimal save endpoint: paste URL → docling → markdown file on disk |
| [02-db2](stages/02-db2/) | Replace filesystem write with INSERT into a Db2 `DOCUMENTS(CLOB)` table |

## Setup (RHEL)

One shared venv at the project root, reused across stages:

```bash
python3.12 -m venv .venv
```

That's the only manual setup step. Each stage's `run.sh` activates the venv and installs that stage's requirements on launch.

## Run a stage

```bash
./stages/01-basic/run.sh
```

Then open http://127.0.0.1:8000.

## Note

The first run downloads docling's models (~1 GB), so the VM needs outbound internet access on first launch. Models are cached under `~/.cache/huggingface/` and shared across stages.

# url-vault

A small FastAPI app that fetches URLs via [docling](https://github.com/DS4SD/docling) and saves the extracted articles as markdown files in `~/url-vault/`.

Built incrementally — each stage under [stages/](stages/) is a self-contained, runnable snapshot showing how the app evolves from a minimal save endpoint toward more sophisticated processing.

## Stages

| Stage | Description |
|-------|-------------|
| [01-basic](stages/01-basic/) | Minimal save endpoint: paste URL → docling → markdown file on disk |

## Setup (RHEL)

One shared venv at the project root, reused across stages:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r stages/01-basic/requirements.txt
```

When a later stage adds dependencies, install its `requirements.txt` the same way — pip is idempotent for already-installed packages.

## Run a stage

```bash
source .venv/bin/activate
cd stages/01-basic
python app.py
```

Then open http://127.0.0.1:8000.

## Note

The first run downloads docling's models (~1 GB), so the VM needs outbound internet access on first launch. Models are cached under `~/.cache/huggingface/` and shared across stages.

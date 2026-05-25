#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

if [ ! -d "$REPO_ROOT/.venv" ]; then
  echo "Error: .venv not found at $REPO_ROOT/.venv" >&2
  echo "Create it first: python3.12 -m venv .venv" >&2
  exit 1
fi

source "$REPO_ROOT/.venv/bin/activate"
pip install -q -r "$SCRIPT_DIR/requirements.txt"
cd "$SCRIPT_DIR"
exec python app.py

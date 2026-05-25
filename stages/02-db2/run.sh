#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
VENV_DIR="$REPO_ROOT/.venv"

if [ ! -d "$VENV_DIR" ]; then
  echo "Error: .venv not found at $VENV_DIR" >&2
  echo "Create it first: python3.12 -m venv .venv" >&2
  exit 1
fi

# Call the venv's binaries by absolute path — works even if another
# venv is already active in the parent shell.
"$VENV_DIR/bin/python" -m pip install -q -r "$SCRIPT_DIR/requirements.txt"

# Bootstrap the Db2 schema (CREATE TABLE IF NOT EXISTS — safe to re-run).
source ~/sqllib/db2profile
db2 connect to "${DB2_DATABASE:-SAMPLE}" > /dev/null
db2 -tf "$SCRIPT_DIR/schema.sql"
db2 terminate > /dev/null

cd "$SCRIPT_DIR"
exec "$VENV_DIR/bin/python" app.py

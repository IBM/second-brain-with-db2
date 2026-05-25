# Stage 2: store documents in Db2

Replaces the filesystem write from stage 1 with an INSERT into a Db2 `DOCUMENTS` table. Each save creates a new row with the URL, a timestamp, and the markdown as a `CLOB`.

## What's new vs stage 1

- **Schema** ([schema.sql](schema.sql)): `DOCUMENTS(ID, URL, SAVED_AT, CONTENT CLOB(10M))` with an identity PK. **The table is dropped and recreated on every launch** (`DROP TABLE IF EXISTS` → `CREATE TABLE`) — saved documents do not survive a re-run.
- **Driver:** adds `ibm_db` (official IBM Db2 Python driver) to requirements.
- **Connection:** one long-lived `ibm_db.connect(...)` at module load, same pattern as `DocumentConverter`.
- **Save flow:** `converter.convert(url).document.export_to_markdown()` → `INSERT INTO DOCUMENTS` → return the new identity column value as `id`.
- **No filesystem writes.** Existing markdown files from stage 1 in `~/second-brain/` are left untouched.

## Configuration

Defaults assume you're running as the Db2 instance owner (`db2inst1`) against a locally cataloged `SAMPLE` database. Override via env vars if needed:

| Variable | Default | Notes |
|---|---|---|
| `DB2_DATABASE` | `SAMPLE` | Database alias to connect to |
| `DB2_USER` | `""` | Empty → implicit OS auth (works for local instance owner) |
| `DB2_PASSWORD` | `""` | Required if `DB2_USER` is set |

## Run

From the project root (with `.venv` created):

```bash
./stages/02-db2/run.sh
```

The script installs deps, runs `schema.sql` against the target database (**this wipes the `DOCUMENTS` table**), then launches the app on http://127.0.0.1:8000.

## Inspect saved documents

```bash
db2 connect to sample
db2 "SELECT ID, URL, SAVED_AT, LENGTH(CONTENT) AS BYTES FROM DOCUMENTS ORDER BY ID DESC"
db2 "SELECT SUBSTR(CONTENT, 1, 500) FROM DOCUMENTS WHERE ID = 1"
db2 terminate
```

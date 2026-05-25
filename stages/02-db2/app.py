import os

import ibm_db
import uvicorn
from docling.document_converter import DocumentConverter
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

DB2_DATABASE = os.environ.get("DB2_DATABASE", "SAMPLE")
DB2_USER = os.environ.get("DB2_USER", "")
DB2_PASSWORD = os.environ.get("DB2_PASSWORD", "")

converter = DocumentConverter()
conn = ibm_db.connect(DB2_DATABASE, DB2_USER, DB2_PASSWORD)
app = FastAPI()


class SaveRequest(BaseModel):
    url: str


PAGE = """<!doctype html>
<title>second-brain-with-db2</title>
<h1>second-brain-with-db2</h1>
<input id="u" size="60" placeholder="https://...">
<button onclick="save()">Save</button>
<p id="s"></p>
<script>
async function save() {
  const url = document.getElementById('u').value;
  const s = document.getElementById('s');
  s.textContent = 'Saving...';
  const r = await fetch('/save', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({url})
  });
  const j = await r.json();
  s.textContent = r.ok ? 'Saved: row id ' + j.id : 'Error: ' + JSON.stringify(j);
}
</script>
"""


@app.get("/", response_class=HTMLResponse)
def index():
    return PAGE


@app.post("/save")
def save(req: SaveRequest):
    markdown = converter.convert(req.url).document.export_to_markdown()
    stmt = ibm_db.prepare(conn, "INSERT INTO DOCUMENTS (URL, CONTENT) VALUES (?, ?)")
    ibm_db.bind_param(stmt, 1, req.url)
    ibm_db.bind_param(stmt, 2, markdown)
    ibm_db.execute(stmt)
    result = ibm_db.exec_immediate(conn, "VALUES IDENTITY_VAL_LOCAL()")
    row = ibm_db.fetch_tuple(result)
    return {"id": int(row[0]), "url": req.url}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

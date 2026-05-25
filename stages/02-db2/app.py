import ibm_db
import uvicorn
from docling.document_converter import DocumentConverter
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

converter = DocumentConverter()
conn = ibm_db.connect("SAMPLE", "", "")
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
    ibm_db.execute(stmt, (req.url, markdown))
    row = ibm_db.fetch_tuple(ibm_db.exec_immediate(conn, "VALUES IDENTITY_VAL_LOCAL()"))
    return {"id": int(row[0])}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

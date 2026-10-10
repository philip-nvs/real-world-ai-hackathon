import mimetypes
from datetime import UTC, datetime
from pathlib import PurePosixPath

from fastapi import FastAPI, Form, HTTPException, UploadFile
from fastapi.responses import Response

from src.repository import get_db

app = FastAPI()

# ponytail: whole case in one document, so capped under Mongo's 16 MB; move file bodies to GridFS if cases outgrow it
MAX_CASE_BYTES = 15 * 1024 * 1024


@app.get("/health")
def health():
    return {"status": "ok"}


def clean_path(name):
    """Upload filename -> safe relative POSIX path. Browsers send `001/attachments/x.pdf` for a folder upload."""
    p = PurePosixPath((name or "").replace("\\", "/"))
    if not p.parts or p.is_absolute() or any(part in ("", ".", "..") for part in p.parts):
        raise HTTPException(422, f"bad file path: {name!r}")
    return p


@app.post("/cases", status_code=201)
async def upload_case(files: list[UploadFile], case_id: str | None = Form(None)):
    """Upload a case folder (or loose files) as multipart `files`; each filename is its path in the case.

    If every file sits under one top folder, that folder is the case id (unless `case_id` is given) and is
    stripped, so paths match the on-disk layout: `index.md`, `history.md`, `attachments/...`.
    Re-uploading a case id replaces it.
    """
    paths = [clean_path(f.filename) for f in files]
    tops = {p.parts[0] for p in paths}
    if len(tops) == 1 and all(len(p.parts) > 1 for p in paths):
        case_id = case_id or tops.pop()
        paths = [PurePosixPath(*p.parts[1:]) for p in paths]
    if not case_id:
        raise HTTPException(422, "case_id required when files aren't inside one folder")
    if len({str(p) for p in paths}) != len(paths):
        raise HTTPException(422, "duplicate file paths")

    docs, total = [], 0
    for f, p in zip(files, paths):
        data = await f.read()
        total += len(data)
        if total > MAX_CASE_BYTES:
            raise HTTPException(413, f"case larger than {MAX_CASE_BYTES} bytes")
        docs.append({"path": str(p), "size": len(data), "data": data,
                     "content_type": f.content_type or mimetypes.guess_type(p.name)[0] or "application/octet-stream"})

    await get_db().cases.replace_one(
        {"_id": case_id}, {"files": docs, "uploaded_at": datetime.now(UTC)}, upsert=True)
    return {"id": case_id, "files": [d["path"] for d in docs]}


@app.get("/cases")
async def list_cases():
    return [{"id": c["_id"], "uploaded_at": c["uploaded_at"]}
            async for c in get_db().cases.find({}, {"uploaded_at": 1}).sort("_id")]


@app.get("/cases/{case_id}")
async def get_case(case_id: str):
    c = await get_db().cases.find_one({"_id": case_id}, {"files.data": 0})
    if not c:
        raise HTTPException(404, "case not found")
    return {"id": c["_id"], "uploaded_at": c["uploaded_at"], "files": c["files"]}


@app.get("/cases/{case_id}/files/{path:path}")
async def get_case_file(case_id: str, path: str):
    c = await get_db().cases.find_one({"_id": case_id}, {"files": {"$elemMatch": {"path": path}}})
    if not c or not c.get("files"):
        raise HTTPException(404, "file not found")
    f = c["files"][0]
    return Response(f["data"], media_type=f["content_type"])


@app.delete("/cases/{case_id}", status_code=204)
async def delete_case(case_id: str):
    if not (await get_db().cases.delete_one({"_id": case_id})).deleted_count:
        raise HTTPException(404, "case not found")

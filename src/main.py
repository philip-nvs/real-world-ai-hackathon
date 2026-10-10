import io
import mimetypes
import zipfile
from contextlib import asynccontextmanager
from datetime import UTC, datetime
from pathlib import PurePosixPath
from uuid import uuid4

from fastapi import FastAPI, Form, HTTPException, Query, UploadFile
from fastapi.responses import Response

from src.agent.sessions import start_session
from src.repository import close, get_db


@asynccontextmanager
async def lifespan(app):
    db = get_db()
    await db.session_events.create_index([("session_id", 1), ("seq", 1)], unique=True)
    await db.sessions.create_index([("case_id", 1), ("created_at", -1)])
    # ponytail: assumes one API process; with several, this would fail another process's live runs
    await db.sessions.update_many({"status": {"$in": ["queued", "running"]}},
                                  {"$set": {"status": "failed", "error": "interrupted: the server stopped mid-run"}})
    yield
    await close()


app = FastAPI(lifespan=lifespan)

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


# ---------- agent sessions ----------

def session_out(s):
    return {"id": s.pop("_id"), **s}


@app.post("/cases/{case_id}/sessions", status_code=202)
async def create_session(case_id: str):
    """Start a one-shot agent run on a stored case. Poll GET /sessions/{id} and its /events."""
    case = await get_db().cases.find_one({"_id": case_id})
    if not case:
        raise HTTPException(404, "case not found")
    session = {"_id": uuid4().hex, "case_id": case_id, "status": "queued", "created_at": datetime.now(UTC)}
    await get_db().sessions.insert_one(session)
    start_session(session["_id"], case_id, case["files"])
    return session_out(session)


@app.get("/cases/{case_id}/sessions")
async def list_sessions(case_id: str):
    fields = {"case_id": 1, "status": 1, "created_at": 1, "finished_at": 1, "decision.decision": 1, "crashed": 1}
    return [session_out(s) async for s in get_db().sessions.find({"case_id": case_id}, fields).sort("created_at", -1)]


@app.get("/sessions/{session_id}")
async def get_session(session_id: str):
    s = await get_db().sessions.find_one({"_id": session_id})
    if not s:
        raise HTTPException(404, "session not found")
    return session_out(s)


@app.get("/sessions/{session_id}/events")
async def get_session_events(session_id: str, after: int = -1):
    """Trace lines with seq > after, in order: pass the last seq you have to get only new ones."""
    if not await get_db().sessions.count_documents({"_id": session_id}, limit=1):
        raise HTTPException(404, "session not found")
    cursor = get_db().session_events.find({"session_id": session_id, "seq": {"$gt": after}}, {"_id": 0, "session_id": 0})
    return [e async for e in cursor.sort("seq")]


@app.get("/export")
async def export_answers(case_id: list[str] = Query()):
    """Zip of <case>/ANSWER.md and REASONING.md from each case's newest done session, like run.py's ANSWERS/."""
    buf, found = io.BytesIO(), 0
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        for cid in dict.fromkeys(case_id):
            s = await get_db().sessions.find_one({"case_id": cid, "status": "done"}, sort=[("created_at", -1)])
            if not s:
                continue
            found += 1
            name = cid.replace("/", "_").replace("\\", "_").lstrip(".") or "case"  # keep entries inside the zip
            z.writestr(f"{name}/ANSWER.md", s["answer_md"])
            z.writestr(f"{name}/REASONING.md", s["reasoning_md"])
    if not found:
        raise HTTPException(404, "none of these cases has a finished session")
    return Response(buf.getvalue(), media_type="application/zip",
                    headers={"Content-Disposition": 'attachment; filename="ANSWERS.zip"'})

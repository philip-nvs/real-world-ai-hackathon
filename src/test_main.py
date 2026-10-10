import os
import re
from pathlib import Path

import yaml

os.environ["MONGODB_DB"] = "banking_case_agent_test"

from fastapi.testclient import TestClient

from src.main import app


def test_health():
    assert TestClient(app).get("/health").json() == {"status": "ok"}


def test_openapi_yaml_matches_routes():
    """src/openapi.yaml is hand-written; every route must be in it and nothing else."""
    spec = yaml.safe_load((Path(__file__).parent / "openapi.yaml").read_text())
    documented = {(p, m.upper()) for p, ops in spec["paths"].items() for m in ops if m != "parameters"}
    served = {(re.sub(r":\w+}", "}", r.path), m) for r in app.routes if r.include_in_schema for m in r.methods}
    assert documented == served


def test_case_upload_roundtrip():
    """Needs MongoDB running (see README)."""
    folder = [("files", ("t-001/index.md", b"# Case")), ("files", ("t-001/history.md", b"events")),
              ("files", ("t-001/attachments/a.pdf", b"%PDF-1", "application/pdf"))]
    with TestClient(app) as c:
        r = c.post("/cases", files=folder)
        assert r.status_code == 201, r.text
        assert r.json() == {"id": "t-001", "files": ["index.md", "history.md", "attachments/a.pdf"]}
        try:
            meta = c.get("/cases/t-001").json()
            assert [(f["path"], f["size"]) for f in meta["files"]] == [
                ("index.md", 6), ("history.md", 6), ("attachments/a.pdf", 6)]
            assert "data" not in meta["files"][0]
            f = c.get("/cases/t-001/files/attachments/a.pdf")
            assert f.content == b"%PDF-1" and f.headers["content-type"] == "application/pdf"
            assert "t-001" in [x["id"] for x in c.get("/cases").json()]

            # loose files need an explicit id; re-upload replaces
            assert c.post("/cases", files=[("files", ("index.md", b"x"))]).status_code == 422
            r = c.post("/cases", files=[("files", ("index.md", b"x"))], data={"case_id": "t-001"})
            assert r.json()["files"] == ["index.md"]
            assert c.get("/cases/t-001/files/history.md").status_code == 404

            assert c.post("/cases", files=[("files", ("../etc/passwd", b"x"))],
                          data={"case_id": "t-002"}).status_code == 422
        finally:
            assert c.delete("/cases/t-001").status_code == 204
        assert c.get("/cases/t-001").status_code == 404


def test_agent_session():
    """A session runs the agent (a scripted fake Claude here) on an uploaded case with its bank_env fixture
    and stores the trace and answer. Needs MongoDB running."""
    import time
    from types import SimpleNamespace as NS

    from src.agent import sessions

    replies = iter([
        [NS(type="tool_use", id="tu_1", name="check_record",
            input={"system": "transfer journal", "query": "£420 to Alder & Reed"})],
        [NS(type="tool_use", id="tu_2", name="submit_decision", input=dict(
            decision="act", next_action="Check the transfer journal for the £420 payment.", evidence=[], conflicts=[],
            customer_message="", handover="", rejected_options=[], final_result="Journal checked."))],
    ])
    create = lambda **kw: NS(content=next(replies), stop_reason="tool_use", usage=NS(input_tokens=10, output_tokens=5))
    sessions.get_client = lambda: NS(beta=NS(messages=NS(create=create)))

    case = Path(__file__).parents[1] / "cases" / "full" / "001"
    files = [("files", (f"001/{p.relative_to(case)}", p.read_bytes())) for p in sorted(case.rglob("*")) if p.is_file()]
    with TestClient(app) as c:
        assert c.post("/cases", files=files).status_code == 201
        try:
            assert c.post("/cases/nope/sessions").status_code == 404
            r = c.post("/cases/001/sessions")
            assert r.status_code == 202 and r.json()["status"] == "queued", r.text
            sid = r.json()["id"]
            for _ in range(100):
                s = c.get(f"/sessions/{sid}").json()
                if s["status"] in ("done", "failed"):
                    break
                time.sleep(0.05)
            assert s["status"] == "done" and not s["crashed"], s
            assert s["decision"]["decision"] == "act" and s["bank"] == "fixture" and s["bank_log"]
            assert s["answer_md"].startswith("# Case 001: ACT") and "REASONING" not in s["answer_md"]

            events = c.get(f"/sessions/{sid}/events").json()
            assert [e["seq"] for e in events] == list(range(len(events)))
            assert [e["kind"] for e in events][0] == "loaded" and events[-1]["kind"] == "decision"
            assert "tool_result" in [e["kind"] for e in events]
            assert c.get(f"/sessions/{sid}/events", params={"after": events[-2]["seq"]}).json() == events[-1:]
            assert [x["id"] for x in c.get("/cases/001/sessions").json()][0] == sid
            assert c.get("/sessions/nope").status_code == 404

            import io, zipfile
            r = c.get("/export", params={"case_id": ["001", "nope"]})
            assert r.status_code == 200 and r.headers["content-type"] == "application/zip", r.text
            z = zipfile.ZipFile(io.BytesIO(r.content))
            assert z.namelist() == ["001/ANSWER.md", "001/REASONING.md"]
            assert z.read("001/ANSWER.md").decode() == s["answer_md"]
            assert c.get("/export", params={"case_id": "nope"}).status_code == 404
        finally:
            c.delete("/cases/001")
            sessions.sync_db().sessions.delete_many({"case_id": {"$in": ["001", "nope"]}})
            sessions.sync_db().session_events.delete_many({"session_id": sid})

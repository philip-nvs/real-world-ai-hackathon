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

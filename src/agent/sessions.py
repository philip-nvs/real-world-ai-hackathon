"""Agent sessions: one run of the case agent on an uploaded case, in the background, kept in MongoDB.

    sessions        one document per run: status, decision, ANSWER/REASONING markdown, bank log, tokens
    session_events  one document per trace line ({session_id, seq, t, kind, ...}), read back with seq > after

A session goes queued -> running -> done (an agent crash still ends done, with the Escalate fallback and
crashed: true) or failed (the run itself broke, or the server stopped mid-run).
"""

import os
import re
import tempfile
from concurrent.futures import ThreadPoolExecutor
from datetime import UTC, datetime
from functools import cache
from itertools import count
from pathlib import Path

import anthropic
from pymongo import MongoClient

from src.bank_env.fixture_adapter import FixtureAdapter
from src.bank_env.world import FIXTURES, load_scenario
from src.agent.core import load_case, load_env, run_case
from src.agent.tools import TOOLS

# ponytail: in-process pool, runs die with the server (marked failed on restart); a job queue if we run several API processes
EXECUTOR = ThreadPoolExecutor(int(os.environ.get("AGENT_WORKERS", "4")))


@cache
def get_client():
    load_env()
    return anthropic.Anthropic(timeout=600, max_retries=3)


@cache
def sync_db():
    """Runs happen in worker threads, so they write with the sync client; the API uses src.repository's async one."""
    return MongoClient(os.environ.get("MONGODB_URI", "mongodb://localhost:27017"), tz_aware=True)[
        os.environ.get("MONGODB_DB", "banking_case_agent")]


def bank_for(case_id, case_dir):
    """The case's bank_env fixture ("017-event-004" -> fixtures/017.json), seeing only the events in its history.
    None when there's no fixture: the agent then uses tools.py, which records actions without executing them."""
    fixture = case_id.split("-")[0]
    if not (FIXTURES / f"{fixture}.json").is_file():
        return None
    return FixtureAdapter(load_scenario(fixture), visible_events={e["id"] for e in load_case(case_dir)["events"]})


def run_session(session_id, case_id, files, client=None):
    """Write the case's files to a temp folder, run the agent there, store its trace and answer."""
    db, now = sync_db(), lambda: datetime.now(UTC)
    db.sessions.update_one({"_id": session_id}, {"$set": {"status": "running", "started_at": now()}})
    seq = count()
    on_trace = lambda line: db.session_events.insert_one({"session_id": session_id, "seq": next(seq), **line})
    try:
        with tempfile.TemporaryDirectory() as tmp:
            case_dir = Path(tmp) / "cases" / (re.sub(r"[^\w-]", "_", case_id) or "case")  # folder name is the case id the agent sees
            for f in files:  # paths were cleaned at upload
                (case_dir / f["path"]).parent.mkdir(parents=True, exist_ok=True)
                (case_dir / f["path"]).write_bytes(f["data"])
            out = Path(tmp) / "out"
            bank = bank_for(case_id, case_dir)
            r = run_case(case_dir, out, client or get_client(), bank.tools() if bank else TOOLS, on_trace)
            result = {"status": "done", "decision": r["output"], "crashed": r["crashed"], "blocked": r["blocked"],
                      "tokens": r["tokens"], "bank": "fixture" if bank else "mock", "bank_log": bank.log if bank else [],
                      "answer_md": (out / "ANSWER.md").read_text(), "reasoning_md": (out / "REASONING.md").read_text()}
    except Exception as e:
        result = {"status": "failed", "error": f"{type(e).__name__}: {e}"}
    db.sessions.update_one({"_id": session_id}, {"$set": {**result, "finished_at": now()}})


def start_session(session_id, case_id, files):
    EXECUTOR.submit(run_session, session_id, case_id, files)

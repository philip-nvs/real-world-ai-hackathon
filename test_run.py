"""Offline self-check: loader, policy guard, and the agent loop driven by a scripted fake Claude.
    python test_run.py
"""

import json
import tempfile
from pathlib import Path
from types import SimpleNamespace as NS

from evaluate import FULL_CASES, TEST_CASES, case_id, parse_gold, stage_case
from make_cutoffs import CUTOFFS, build_cut, decision_points
from run import guard_tool, load_case, red_flags, run_case

CASE = FULL_CASES / "017"


def tool_use(i, name, **args):
    return NS(type="tool_use", id=f"tu_{i}", name=name, input=args)


def fake_client(script):
    replies = iter(script)
    create = lambda **kw: NS(content=next(replies), stop_reason="tool_use", usage=NS(input_tokens=10, output_tokens=5))
    return NS(beta=NS(messages=NS(create=create)))


DECISION = dict(decision="act", next_action="Check the standing-order journal for the specific run.",
                evidence=[{"event_id": "event-002", "fact": "Customer asked about the run"}], conflicts=[],
                customer_message="", handover="", rejected_options=[], final_result="Journal check requested.")

if __name__ == "__main__":
    case = load_case(CASE)
    assert [e["channel"] for e in case["events"]][:2] == ["External message", "Secure chat"], case["events"]
    assert case["events"][4]["id"] == "event-005"

    assert red_flags("Your refund will be issued tomorrow.") == ["promises a refund"]
    assert red_flags("We cannot promise a refund.") == []
    assert red_flags("Please never share your PIN.") == []
    assert red_flags("Receipt confirmed: batch-041.csv was received by H&V.") == []
    assert red_flags("The payment will arrive on Friday.") == ["promises delivery or receipt"]
    assert guard_tool("submit_instruction", {"system": "SO", "instruction": "Cancel order", "authorised_by_event": "event-001"}, case)
    assert not guard_tool("submit_instruction", {"system": "SO", "instruction": "Cancel order", "authorised_by_event": "event-002"}, case)
    assert guard_tool("submit_instruction", {"system": "PAY", "instruction": "Re-send the payment", "authorised_by_event": "event-002"}, case)

    with tempfile.TemporaryDirectory() as tmp:
        # the dev loop's gold answer is parsed, and never staged where the agent can read it
        gold = parse_gold(TEST_CASES / "017" / "ANSWER.md")
        assert gold["action"] == "act" and gold["cut_off"].startswith("event-") and "standing" in gold["description"].lower()
        (Path(tmp) / "staged/stale.txt").parent.mkdir(parents=True)
        (Path(tmp) / "staged/stale.txt").write_text("left over from an earlier run")
        stage_case(TEST_CASES / "017", Path(tmp) / "staged")
        assert sorted(f.name for f in (Path(tmp) / "staged").iterdir()) == ["history.md", "index.md"]
        assert all(parse_gold(a)["action"] in ("act", "ask", "wait", "escalate") for a in TEST_CASES.glob("*/ANSWER.md"))

        # the cut-off builder reproduces every curated test case from the full one
        for curated in sorted(TEST_CASES.iterdir()):
            k = int(parse_gold(curated / "ANSWER.md")["cut_off"].split("-")[1])
            build_cut(curated.name, k, Path(tmp) / "rebuilt" / curated.name)
            for f in ("index.md", "history.md"):
                assert (Path(tmp) / "rebuilt" / curated.name / f).read_text().rstrip() == (curated / f).read_text().rstrip(), (curated.name, f)
            assert k not in decision_points(curated.name, k)

        # every generated cut-off: history ends at its cut, gold parses, only attachments the agent could know of
        for cut in sorted(p for p in CUTOFFS.iterdir() if p.is_dir()):
            gold = parse_gold(cut / "ANSWER.md")
            k = int(cut.name.split("-e")[1])
            events = load_case(cut)["events"]
            assert gold["cut_off"] == f"event-{k:03d}" and gold["action"] in ("act", "ask", "wait", "escalate"), cut.name
            assert [e["id"] for e in events] == [f"event-{i:03d}" for i in range(1, k + 1)], cut.name
            assert f"Total events: {k}" in (cut / "history.md").read_text(), cut.name
            visible_text = (cut / "history.md").read_text() + (cut / "index.md").read_text()
            assert all(a.name in visible_text for a in (cut / "attachments").glob("*")), cut.name
            assert (FULL_CASES / case_id(cut)).is_dir(), cut.name

        # first a red-flag message (blocked), then a clean check + decision
        client = fake_client([
            [tool_use(1, "send_secure_message", recipient="Mara", message="Your refund will be issued tomorrow.")],
            [tool_use(2, "check_record", system="standing-order journal", query="HV-017 run status"),
             tool_use(3, "submit_decision", **DECISION)],
        ])
        r = run_case(CASE, Path(tmp) / "out", client)
        assert (r["decision"], r["blocked"], r["crashed"]) == ("act", 1, False), r
        answer = (Path(tmp) / "out/ANSWER.md").read_text()
        assert "**ACT**" in answer and "standing-order journal" in answer and "promises a refund" in answer
        kinds = [json.loads(l)["kind"] for l in (Path(tmp) / "out/trace.jsonl").read_text().splitlines()]
        assert "guard_block" in kinds and kinds[-1] == "decision"

        # a crashing client still yields an Escalate answer
        r = run_case(CASE, Path(tmp) / "crash", fake_client([]))
        assert r["crashed"] and r["decision"] == "escalate"
        assert "could not finish" in (Path(tmp) / "crash/ANSWER.md").read_text()
    print("ok")

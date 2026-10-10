"""Offline self-check: loader, policy guard, and the agent loop driven by a scripted fake Claude.
    python test_run.py
"""

import json
import tempfile
from pathlib import Path
from types import SimpleNamespace as NS

from evaluate import FULL_CASES, TEST_CASES, case_id, gold_file, parse_gold, stage_case
from run import guard_decision, guard_tool, load_case, red_flags, run_case

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
    unsent = dict(DECISION, customer_message="Your standing order run was not executed.")
    assert any("no message was sent" in p for p in guard_decision(unsent))
    assert not guard_decision(unsent, [{"tool": "send_secure_message"}])

    with tempfile.TemporaryDirectory() as tmp:
        # the dev loop's gold answer is parsed, and the answer/ folder is never staged where the agent can read it
        sample = TEST_CASES / "017-event-002"
        gold = parse_gold(gold_file(sample))
        assert gold["action"] == "act" and gold["cut_off"] == "event-002" and "standing" in gold["description"].lower()
        (Path(tmp) / "staged/stale.txt").parent.mkdir(parents=True)
        (Path(tmp) / "staged/stale.txt").write_text("left over from an earlier run")
        stage_case(TEST_CASES / "031-event-004", Path(tmp) / "staged")
        assert sorted(f.name for f in (Path(tmp) / "staged").iterdir()) == ["attachments", "history.md", "index.md"]

        # every test cut-off: gold parses and matches its folder, history ends at the cut-off, and only
        # attachments the visible history or request names
        cuts = sorted(p for p in TEST_CASES.iterdir() if p.is_dir())
        uncovered = {p.name for p in FULL_CASES.iterdir() if p.is_dir()} - {case_id(c) for c in cuts}
        assert not uncovered, f"public cases without a test cut-off: {sorted(uncovered)}"
        for cut in cuts:
            gold = parse_gold(gold_file(cut))
            k = int(cut.name.split("-event-")[1])
            assert gold["cut_off"] == f"event-{k:03d}" and gold["action"] in ("act", "ask", "wait", "escalate"), cut.name
            assert [e["id"] for e in load_case(cut)["events"]] == [f"event-{i:03d}" for i in range(1, k + 1)], cut.name
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
        # with no live bank the check is recorded, not executed, and nothing invents a result or reference
        assert "(recorded, not executed)" in answer and "were not executed; no results came back" in answer, answer
        assert "MOCK" not in answer and "queued" not in answer and "delivered" not in answer
        kinds = [json.loads(l)["kind"] for l in (Path(tmp) / "out/trace.jsonl").read_text().splitlines()]
        assert "guard_block" in kinds and kinds[-1] == "decision"

        # a crashing client still yields an Escalate answer
        r = run_case(CASE, Path(tmp) / "crash", fake_client([]))
        assert r["crashed"] and r["decision"] == "escalate"
        assert "could not finish" in (Path(tmp) / "crash/ANSWER.md").read_text()
    print("ok")

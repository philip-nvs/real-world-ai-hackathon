"""Offline self-check: loader, policy guard, and the agent loop driven by a scripted fake Claude.
    python test_run.py
"""

import json
import tempfile
from pathlib import Path
from types import SimpleNamespace as NS

from evaluate import PUBLIC, cut_case
from run import guard_tool, load_case, red_flags, run_case

CASE = PUBLIC / "017"


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
        gold, _, cut = cut_case(CASE, Path(tmp) / "cut")
        assert cut == 2 and "event 003" not in (Path(tmp) / "cut/history.md").read_text()
        assert "insufficient" not in (Path(tmp) / "cut/index.md").read_text() and "journal entry" in gold

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

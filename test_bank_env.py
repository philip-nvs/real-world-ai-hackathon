"""Offline self-check for the simulated bank: fixtures, alias resolution, the fixture adapter, overlays.
    uv run test_bank_env.py
"""

import re
from pathlib import Path

from bank_env.fixture_adapter import FixtureAdapter
from bank_env.ports import PortError
from bank_env.schema import check_world
from bank_env.systems import resolve_process, resolve_system, resolve_team
from bank_env.world import FIXTURES, load_scenario
from run import EVENT_RE, load_case
from tools import TOOLS

CASES = Path(__file__).parent / "cases" / "full"


def raises(code, fn, *args):
    try:
        fn(*args)
    except PortError as e:
        assert e.code == code, e
        return
    raise AssertionError(f"expected PortError {code}")


if __name__ == "__main__":
    assert resolve_system("H&V transfer journal") == "payment_journal"
    assert resolve_system("H&V account transaction journal") == "incoming_payments"
    assert resolve_system("H&V standing-order journal") == "instruction_register"
    assert resolve_team("H&V archive group") == "statements_service"
    assert resolve_process("H&V Direct Debit service") == "instruction_process"

    # every committed fixture is consistent with its case, and answers the lookups the case's own agent made:
    # found (018 lists both instructions), or ambiguous where 006 holds two look-alike instructions to compare
    replayed = 0
    for path in sorted(FIXTURES.glob("*.json")):
        case = load_case(CASES / path.stem)
        world = load_scenario(path.stem).world
        assert not check_world(world, [e["id"] for e in case["events"]]), path.stem
        bank = FixtureAdapter(load_scenario(path.stem))
        marks = list(EVENT_RE.finditer(case["history"]))
        for i, e in enumerate(case["events"]):
            if (e["channel"].lower() != "internal note" or "agent" not in e["from"].lower() or not resolve_system(e["to"])
                    or not re.search(r"journal|register|log|records", e["to"], re.I)):
                continue
            body = case["history"][marks[i].end(): marks[i + 1].start() if i + 1 < len(marks) else None]
            r = bank.lookup(e["to"], re.sub(r"^\s*- \*\*.*$", "", body, flags=re.M))
            assert r["status"] == ("ambiguous" if path.stem == "006" else "found"), (path.stem, e["id"], r)
            replayed += 1
    assert replayed >= 20, replayed

    # 001: the specific transfer is found, with limits on what H&V may share
    bank = FixtureAdapter(load_scenario("001"))
    r = bank.lookup("H&V transfer journal", "Mara Ellison's one-off £420 transfer to Alder & Reed Workshop")
    assert r["status"] == "found" and r["facts"]["status"] == "SENT", r
    assert "permitted_customer_wording" in r or r.get("disclosure_rules"), r
    assert bank.lookup("incoming payments", "£420 from Alder & Reed")["status"] == "not_found"
    raises("unknown_system", bank.lookup, "crystal ball", "anything")

    # the same lookup in the conflicting-transfer variant is ambiguous
    bank = FixtureAdapter(load_scenario(overlay="001-conflicting-transfer"))
    r = bank.lookup("payment journal", "£420 transfer to Alder & Reed Workshop")
    assert r["status"] == "ambiguous" and len(r["candidates"]) == 2, r

    # 006: two separate instructions share every identifier; each candidate opens by its record_ref
    bank = FixtureAdapter(load_scenario("006"))
    r = bank.lookup("payment instruction journal", "Mira Ellison £84.20 to North Quay Utilities")
    assert r["status"] == "ambiguous", r
    statuses = {bank.lookup("payment journal", f"open {c['record_ref']}")["facts"]["status"] for c in r["candidates"]}
    assert statuses == {"Completed", "Pending"}, statuses

    # 012: a chat request is not a confirmation; the portal confirmation only counts once it has happened
    instruction = ("instruction process", "Amend the Westmere Garden Cooperative standing order from £42.00 to £68.00")
    bank = FixtureAdapter(load_scenario("012"), visible_events={"event-001", "event-002"})
    assert bank.submit_instruction(*instruction, "event-002")["status"] == "rejected"
    assert bank.submit_instruction(*instruction, "event-005")["status"] == "rejected"
    bank = FixtureAdapter(load_scenario("012"))
    assert bank.submit_instruction(*instruction, "event-5")["status"] == "applied"
    assert bank.lookup("standing-order journal", "Westmere Garden Cooperative standing order")["facts"]["amount_gbp"] == "68.00"

    # 024: disclosure limits travel with the record
    r = FixtureAdapter(load_scenario("024")).lookup("card journal", "Rowan Ellery card restriction")
    assert r["status"] == "found" and r["disclosure_rules"], r

    # 042: the import service returns the validation report; an unscripted request just queues
    bank = FixtureAdapter(load_scenario("042"))
    r = bank.submit_request("H&V import service", "Validation report for batch HV-042, Fenwick Workshop")
    assert r["status"] == "completed" and r["document"] == "validation-042.txt", r
    assert bank.submit_request("card team", "Unrelated card question")["status"] == "queued"

    # 045: nobody approved the access, so granting it is rejected
    bank = FixtureAdapter(load_scenario("045"))
    r = bank.submit_instruction("admin process", "Grant secure-portal access to the new colleague at Merefield Design Studio Ltd", "event-002")
    assert r["status"] == "rejected", r

    # 045: the access request only exists once the agent sends it, not from the start
    bank = FixtureAdapter(load_scenario("045"), visible_events={"event-001", "event-002"})
    query = ("business mandate", "New-user access request for the new colleague at Merefield Design Studio Ltd")
    before = bank.lookup(*query)
    assert "Awaiting" not in str(before), before
    sent = bank.submit_request("business support", "Send the new-user secure-portal access request for the new "
                                                   "colleague to the company administrator for approval")
    assert sent["status"] != "queued", sent
    assert "Awaiting" in str(bank.lookup(*query))

    # 036: wording written after the address change stays hidden until the change is applied
    bank = FixtureAdapter(load_scenario("036"))
    query = ("customer profile", "Mara Ellison correspondence address")
    assert "permitted_customer_wording" not in bank.lookup(*query)
    process = next(x for x in bank.world.processes if x.action == "change_address")
    bank.submit_instruction("profile change", " ".join(process.match_terms), process.confirmed_by[0])
    assert "permitted_customer_wording" in bank.lookup(*query)

    # faults: an unavailable system fails the call and is logged
    bank = FixtureAdapter(load_scenario(overlay={"base": "001", "faults": [
        {"port": "records", "target": "payment_journal", "mode": "unavailable", "message": "journal offline"}]}))
    raises("unavailable", bank.lookup, "transfer journal", "£420 Alder & Reed")
    assert bank.log[-1]["fault"] == "unavailable"

    # the adapter offers exactly the agent's tool surface
    assert set(bank.tools()) == set(TOOLS)
    print("ok")

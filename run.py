#!/usr/bin/env python3
"""Batch case agent for the Banking track.

    python run.py CASES_DIR --out ANSWERS/

Every case folder (one holding index.md) under CASES_DIR gets ANSWERS/<case>/ with
ANSWER.md, REASONING.md and trace.jsonl. A case that crashes still gets an Escalate answer.
"""

import argparse
import base64
import json
import os
import re
import sys
import time
import traceback
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import anthropic

from tools import TOOL_SCHEMAS, TOOLS

MODEL = "claude-opus-5-5"
MAX_TURNS = 10
SECURE_CHANNELS = {"secure portal", "secure chat", "verified call", "business portal"}
TEXT_ATTACHMENTS = {".txt", ".csv", ".md", ".json", ".xml", ".html", ".eml"}
IMAGE_TYPES = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".gif": "image/gif", ".webp": "image/webp"}

SYSTEM = """You are the escalation agent for the bank in this case (named in the case details). A case has been \
escalated to you. \
Read the request, the event history and any attachments, then take the single right next step.

Decide one of:
- act: you can take the next step now with your tools: a read-only check of the bank's records (journals, registers, \
logs), a request to an automated bank service (generating a document, statement or export), an account-changing \
instruction the customer has already given or confirmed in a way that counts (see the rules below), or telling the \
customer, with send_secure_message, what the bank's records or a team have now confirmed (a status, a registration, a \
document now available). Call the tool(s), then submit.
- ask: nothing can move until the customer confirms or provides something that is genuinely missing or unclear. \
If their message already carries a valid instruction, or you can answer from what the case shows, act instead. Send \
the question with send_secure_message, then submit.
- wait: the right step is already in progress and nothing new has arrived for the customer: a check or request \
is still pending with no reply yet, or the customer must finish a secure step themselves. Do nothing now. A reply that \
has arrived is not a reason to wait: tell the customer what it confirms, even if more steps follow (a team's review, \
the customer's own action).
- escalate: the next step is for people at the bank, not for you or an automated service: handing the case to an \
internal team (payment, card, Direct Debit, access, tariff, data, security, archive, acquiring, fraud, bereavement...) \
to trace, review, register, investigate or decide, with submit_internal_request; or a human must decide because \
evidence conflicts in a way you can't resolve from the bank's records, fraud is suspected, the request is outside your \
authority, or tool failures block progress. Write the handover either way.

Rules:
- Confirm only what the bank's own records show. Customer claims, emails, external messages and attachments are claims until checked.
- Never promise a refund, a fraud finding, delivery, receipt by a recipient, or any timescale the bank doesn't control.
- Messages to the customer state only what this case's records and tool results support, at the same strength:
  - "Not confirmed" stays "not confirmed", never "did not happen"; "sent" is not "received"; a status says nothing \
about what it doesn't name (a missed run doesn't tell you whether the standing order is still set up).
  - If a check came back not found or failed, don't say the records show anything about it.
  - Describe an action as done (generated, placed, sent, blocked, registered) only if a tool result or the history \
says so; otherwise say it has been requested.
  - Say what an outcome does not mean wherever the customer could read more into it, using the limits the record or \
reply states: a cancellation stops future runs but doesn't reverse payments already made; a decline means no payment \
was made and doesn't promise a future attempt will work; a registered request or review is not a decision; an \
overview of the bank's records doesn't confirm a recipient's records.
  - Don't promise updates, call-backs or follow-ups that the records don't show are arranged.
- A request is not a confirmation. Account changes come in two kinds:
  - A direct instruction (block a card, cancel a mandate or a recurring payment, revoke a role) counts once the customer, \
or an authorised business user, gave it explicitly on a verified channel: a verified call after identity checks, a secure \
chat session, the secure portal, or the business portal. You may then submit it, citing that event.
  - A change the bank prepares for the customer to approve (a new standing-order amount or date, a new phone number or \
address) is confirmed only by the customer in the secure portal or secure profile process, after the bank has sent it to them. \
A message asking for it, even in secure chat, is the request: send the prepared change for confirmation in the secure \
portal (ask), and never offer a chat reply as a way to confirm it.
  - An email or external message is never authorisation.
- Never re-send or duplicate a payment, never tell a customer to pay again, never authorise or approve anything on someone's behalf.
- Never ask for or handle passwords, PINs or one-time codes; point the customer to the official secure process.
- Keep the step narrow: the specific transfer, charge, run, row or document asked about, nothing broader.
- When a live system can answer, check the specific record in the bank's own journal before telling the customer anything.
- If the customer asks the bank to do something it doesn't do for customers (for example making a payment on their \
behalf), say so and point them to the self-service route, rather than asking them to confirm it. This never overrides \
the rule below against telling a customer to pay again: never suggest a new or replacement payment before checking \
for new or pending activity.
- If the case shows the customer in vulnerable circumstances (bereavement, serious illness, financial hardship, \
distress), refer it to the right specialist team and acknowledge their situation in your message.
- Cite the event IDs (e.g. event-003) you rely on and list conflicts between events.
- Tool failures are facts: report them, never hide them.
- If a tool reports the action as recorded but not executed (no live system is connected), no result will come back: \
don't wait for or invent it. Then take the step that moves the case forward with what the case already shows: tell the \
customer what it shows (within the rules above), ask for the one thing that's missing, refer it to the specialist team, \
or submit an instruction the customer has validly given. A records check whose result you'll never see is not the next \
step on its own, and next_action is that forward step, not the check.
- Messages to customers go through the secure portal only.

Finish by calling submit_decision exactly once. Its next_action is the step the bank takes at this point in the case: the \
action you just took with your tools, not what should happen after it. If the policy guard rejects a call, fix the \
problem and try again."""

DECISION_TOOL = {
    "name": "submit_decision",
    "description": "Submit the final decision for this case. Call exactly once, last.",
    "strict": True,
    "input_schema": {
        "type": "object",
        "additionalProperties": False,
        "required": ["decision", "next_action", "evidence", "conflicts", "customer_message",
                     "handover", "rejected_options", "final_result"],
        "properties": {
            "decision": {"type": "string", "enum": ["act", "ask", "wait", "escalate"]},
            "next_action": {"type": "string", "description": "The step the bank takes at this point in the case, one "
                            "sentence starting with the action, e.g. 'Check the bank's payment journal for ...'. For act or "
                            "ask: the step you just took with your tools, not what happens after it. For wait: what "
                            "is pending. For escalate: the hand-off."},
            "evidence": {"type": "array", "items": {
                "type": "object", "additionalProperties": False, "required": ["event_id", "fact"],
                "properties": {"event_id": {"type": "string"}, "fact": {"type": "string"}}}},
            "conflicts": {"type": "array", "items": {"type": "string"}},
            "customer_message": {"type": "string", "description": "The message you sent with send_secure_message in "
                                 "this step, verbatim, or empty if you sent none. Filling this in sends nothing."},
            "handover": {"type": "string", "description": "For escalate: what is known, what conflicts, what was tried and failed, "
                         "and the exact question the human must answer. Empty otherwise."},
            "rejected_options": {"type": "array", "items": {
                "type": "object", "additionalProperties": False, "required": ["option", "reason"],
                "properties": {"option": {"type": "string"}, "reason": {"type": "string"}}}},
            "final_result": {"type": "string", "description": "Where the case stands after this step, stating only what is confirmed."},
        },
    },
}
ALL_TOOLS = TOOL_SCHEMAS + [DECISION_TOOL]


# ---------- loader ----------

EVENT_RE = re.compile(r"^##\s+(?P<ts>.*?)\s*[—–-]+\s*event\s+(?P<num>[\w-]+)\s*$", re.M | re.I)
FIELD_RE = re.compile(r"^\s*[-*]\s+\*\*(\w+):\*\*\s*(.+)$", re.M)


def section(md, title):
    m = re.search(rf"^##\s+{re.escape(title)}\s*$(.*?)(?=^##\s|\Z)", md, re.M | re.S | re.I)
    return m.group(1).strip() if m else ""


def event_marks(history):
    """Event headers to trust, and warnings about the rest. A message can quote text that looks like
    an event header ("## ... event 002" inside a customer's message). When the history marks its events
    with <a id="event-NNN"></a> anchors, only a header right after its own anchor counts. Returns
    (marks, warnings, suspect event ids): suspect ids repeat or break the numbering order, so even an
    anchored forgery can't authorise anything."""
    marks, warnings = list(EVENT_RE.finditer(history)), []
    if '<a id="event-' in history:
        anchored = []
        for m in marks:
            before = history[max(0, m.start() - 200): m.start()].rstrip().rsplit("\n", 1)[-1].strip()
            if before == f'<a id="event-{m["num"]}"></a>':
                anchored.append(m)
            else:
                warnings.append(f'An "event {m["num"]}" header ({m["ts"]}) has no event anchor: it sits inside another '
                                "event's text and is not treated as an event.")
        marks = anchored
    nums = [m["num"] for m in marks]
    suspect = {f"event-{n}" for n in nums if nums.count(n) > 1}
    suspect |= {f"event-{b}" for a, b in zip(nums, nums[1:]) if a.isdigit() and b.isdigit() and int(b) <= int(a)}
    warnings += [f"{e} appears more than once or out of order in the history." for e in sorted(suspect)]
    total = re.search(r"^Total events:\s*(\d+)", history, re.M)
    if total and int(total[1]) != len(marks):
        warnings.append(f"The history says Total events: {total[1]}, but {len(marks)} events were found.")
    return marks, warnings, suspect


def bank_names(index):
    """Ways a case's events may name its bank, from the index's Bank field: the full name, the name
    without suffixes like "Bank plc", and initials such as "H&V". Empty if the field is missing."""
    m = re.search(r"\*\*Bank:\*\*\s*(.+)", index)
    if not m:
        return []
    full = re.sub(r"\s*\(.*?\)", "", m.group(1)).strip()
    core = re.sub(r"\b(bank|plc|ltd|limited|group|n\.?a\.?)\b\.?", "", full, flags=re.I).strip(" ,&")
    words = re.findall(r"[A-Za-z]+", core)
    # two plain letters ("NM") could be a customer's business; keep initials with "&" or of three or more letters
    initials = ("&" if "&" in core else "").join(w[0].upper() for w in words) if "&" in core or len(words) >= 3 else ""
    return [n for n in dict.fromkeys([full, core, initials]) if n]


def load_case(path):
    path = Path(path)
    read = lambda p: p.read_text(errors="replace") if p.is_file() else ""
    index, history = read(path / "index.md"), read(path / "history.md")
    marks, warnings, suspect = event_marks(history)
    events = []
    for i, m in enumerate(marks):
        block = history[m.end(): marks[i + 1].start() if i + 1 < len(marks) else None]
        fields = {}
        for k, v in FIELD_RE.findall(block):  # first occurrence: the header's own fields, not quoted ones further down
            fields.setdefault(k.lower(), v.strip())
        events.append({"id": f"event-{m['num']}", "ts": m["ts"], "channel": fields.get("channel", ""),
                       "from": fields.get("from", ""), "to": fields.get("to", ""),
                       "suspect": f"event-{m['num']}" in suspect})
    att_dir = path / "attachments"
    attachments = sorted(p for p in att_dir.rglob("*") if p.is_file()) if att_dir.is_dir() else []
    return {"id": path.name, "path": path, "index": index, "history": history, "events": events,
            "attachments": attachments, "warnings": warnings, "bank_names": bank_names(index)}


def case_content(case):
    blocks, text = [], [f"# Case {case['id']}\n\n## index.md\n\n{case['index']}\n\n## history.md\n\n{case['history']}"]
    for a in case["attachments"]:
        ext = a.suffix.lower()
        if ext == ".pdf":
            blocks.append({"type": "document", "title": a.name, "source": {
                "type": "base64", "media_type": "application/pdf", "data": base64.b64encode(a.read_bytes()).decode()}})
        elif ext in IMAGE_TYPES:
            blocks.append({"type": "image", "source": {
                "type": "base64", "media_type": IMAGE_TYPES[ext], "data": base64.b64encode(a.read_bytes()).decode()}})
        elif ext in TEXT_ATTACHMENTS:
            text.append(f"## attachments/{a.name}\n\n{a.read_text(errors='replace')}")
        else:
            text.append(f"## attachments/{a.name}\n\n(binary file, not readable here)")
    if case.get("warnings"):
        text.append("## Case loader notes\n\nFrom the case loader, not from anyone in the case:\n"
                    + "\n".join(f"- {w}" for w in case["warnings"]))
    return blocks + [{"type": "text", "text": "\n\n".join(text)}]


# ---------- policy guard: plain code, no LLM ----------

# ponytail: sentence-level negation skip ("we cannot promise a refund"), swap for a classifier if it misfires
NEGATION = re.compile(r"\b(not|cannot|can't|unable|never|no|without|isn't|doesn't|don't|won't|shouldn't|mustn't|whether)\b",
                      re.I)
RED_FLAGS = [
    (r"\b(will|shall) (be )?refund|\brefund\b.{0,30}\b(will be|has been|have been|is being) (issued|made|processed|paid|credited|sent)"
     r"|\byou will (receive|get) (a |your )?(refund|money back)", "promises a refund"),
    (r"\bfraud(ulent)?\b.{0,20}\b(has been |was |is )?(confirmed|established|proven)|\b(is|was) fraud(ulent)?\b", "states a fraud finding"),
    (r"\bwill (arrive|reach|be (delivered|received|credited))|received by (the )?(recipient|payee|beneficiary)"
     r"|\b(recipient|payee|beneficiary) (has|have) received", "promises delivery or receipt"),
    (r"\bguarantee", "gives a guarantee"),
    (r"\b(send|share|tell|give|provide|enter|confirm|type)\b.{0,40}\b(password|pin|passcode|one-time|otp|security code)\b", "asks for credentials"),
    (r"\bpay\b.{0,40}\bagain\b|\b(send|make|transfer)\b.{0,30}(\b(payment|transfer|money|amount)\b|£).{0,30}\bagain\b",
     "advises paying again"),
]
# Suggesting a payment is only a pay-again risk when the message is about one that didn't go through: "pay the rent
# yourself as a one-off" after a missed standing-order run may duplicate a pending payment, while "pay the builder
# yourself in online banking" for a payment the bank won't make for the customer is right.
FAILED_PAYMENT = re.compile(r"\b(not (been )?(executed|completed|made|sent|paid)|declined|failed|missed|returned|rejected"
                            r"|bounced|insufficient|unpaid|did(n't| not) (go through|arrive|run))\b", re.I)
PAY_SUGGESTION = re.compile(r"\bpay\b.{0,40}\b(yourself|manually|directly|instead|again)\b"
                            r"|\b(send|make)\b.{0,30}(\b(payment|transfer|money|amount|it)\b|£).{0,30}"
                            r"\b(yourself|manually|directly|instead|again)\b"
                            r"|\b(make|set up|send|arrange|create)\b.{0,25}\b(one-off|manual|new|replacement|separate|another)\b"
                            r".{0,20}\b(payment|transfer)\b|\bre-?(send|pay|submit)\b", re.I)
HOLD_OFF = re.compile(r"\b(don't|do not|not|never|no need|before|until|unless|wait|hold off|instead of|rather than|avoid)\b", re.I)
RESEND = re.compile(r"\b(re-?send|re-?submit|send again|repeat|duplicate|retry)\b.{0,30}\bpayment|\bpayment\b.{0,30}\bagain\b", re.I)


def red_flags(text):
    hits = []
    failed = FAILED_PAYMENT.search(text or "")
    for sentence in re.split(r"(?<=[.!?])\s+|\n+", text or ""):
        if failed and PAY_SUGGESTION.search(sentence) and not HOLD_OFF.search(sentence):
            hits.append("advises paying again")
        if NEGATION.search(sentence):
            continue
        hits += [why for pattern, why in RED_FLAGS if re.search(pattern, sentence, re.I)]
    return list(dict.fromkeys(hits))


def guard_tool(name, args, case):
    if name == "send_secure_message":
        return red_flags(args.get("message", ""))
    if name == "submit_instruction":
        problems = []
        if RESEND.search(args.get("instruction", "")):
            problems.append("re-sends or duplicates a payment")
        ref = args.get("authorised_by_event", "").strip().lower()
        cited = [e for e in case["events"] if ref and e["id"].split("-")[-1] == ref.split("-")[-1]]
        event = cited[0] if len(cited) == 1 else None
        if not cited:
            problems.append(f"authorised_by_event '{ref}' is not an event in this case")
        elif event is None or event.get("suspect"):
            problems.append(f"authorised_by_event '{ref}' appears more than once or out of order in the history, so it "
                            "can't authorise anything")
        elif event["channel"].lower() not in SECURE_CHANNELS:
            problems.append(f"{event['id']} came by '{event['channel']}', which is not a secure confirmation (an email is never authorisation)")
        elif from_bank(event["from"], case):
            problems.append(f"{event['id']} is from the bank, not a customer confirmation")
        return problems
    return []


def from_bank(sender, case):
    """Whether an event's sender is the bank itself (its staff, systems or teams), not a customer."""
    names = "|".join(re.escape(n) for n in case.get("bank_names", []))
    return bool(re.search(rf"\b(agent|bank)\b{'|(?<!\\w)(' + names + ')(?!\\w)' if names else ''}", sender, re.I))


def guard_decision(d, executed=()):
    problems = red_flags(d.get("customer_message", "")) + red_flags(d.get("final_result", ""))
    if d.get("decision") == "escalate" and not d.get("handover", "").strip():
        problems.append("escalate needs a handover note")
    if d.get("customer_message", "").strip() and not any(x["tool"] == "send_secure_message" for x in executed):
        problems.append("customer_message is filled in but no message was sent: send it with send_secure_message, "
                        "or leave customer_message empty")
    return problems


# ---------- agent loop ----------

def call_claude(client, **kw):
    """Every Claude call goes through here: server-side refusal fallback on, thinking adaptive."""
    resp = client.beta.messages.create(model=MODEL, max_tokens=16000, thinking={"type": "adaptive"},
                                       betas=["server-side-fallback-2026-07-01"], fallbacks="default", **kw)
    if resp.stop_reason == "refusal":
        raise RuntimeError("model refused the request")
    return resp


def run_agent(case, client, trace, tools=TOOLS):
    messages = [{"role": "user", "content": case_content(case)}]
    state = {"executed": [], "blocked": [], "failures": [], "tokens": [0, 0]}
    for _ in range(MAX_TURNS):
        resp = call_claude(client, system=SYSTEM, tools=ALL_TOOLS, messages=messages, output_config={"effort": "high"})
        state["tokens"][0] += resp.usage.input_tokens
        state["tokens"][1] += resp.usage.output_tokens
        trace("model", stop_reason=resp.stop_reason, text=[b.text for b in resp.content if b.type == "text"],
              usage=[resp.usage.input_tokens, resp.usage.output_tokens])
        messages.append({"role": "assistant", "content": resp.content})
        uses = [b for b in resp.content if b.type == "tool_use"]
        if not uses:
            messages.append({"role": "user", "content": "Finish by calling submit_decision."})
            continue
        results, decision = [], None
        for u in uses:
            out, is_error = execute(u.name, u.input, case, state, trace, tools)
            if u.name == "submit_decision" and not is_error:
                decision = u.input
            results.append({"type": "tool_result", "tool_use_id": u.id, "content": json.dumps(out), "is_error": is_error})
        messages.append({"role": "user", "content": results})
        if decision:
            return decision, state
    raise RuntimeError(f"no accepted decision after {MAX_TURNS} turns")


def execute(name, args, case, state, trace, tools=TOOLS):
    trace("tool_call", tool=name, input=args)
    if name == "submit_decision":
        problems = guard_decision(args, state["executed"])
    elif name in tools:
        problems = guard_tool(name, args, case)
    else:
        problems = [f"unknown tool {name}"]
    if problems:
        state["blocked"].append({"tool": name, "problems": problems})
        trace("guard_block", tool=name, problems=problems)
        return {"blocked_by_policy_guard": problems, "hint": "Revise and try again."}, True
    if name == "submit_decision":
        return {"status": "accepted"}, False
    try:
        out = tools[name](**args)
        state["executed"].append({"tool": name, "input": args, "output": out})
        trace("tool_result", tool=name, output=out)
        return out, False
    except Exception as e:  # tool failures go back to the agent, not hidden
        state["failures"].append(f"{name} failed: {e}")
        trace("tool_error", tool=name, error=str(e))
        return {"error": str(e)}, True


def fallback_decision(error):
    return {
        "decision": "escalate", "evidence": [], "conflicts": [], "rejected_options": [], "customer_message": "",
        "next_action": "A human case handler reviews this case from the start.",
        "handover": f"The automated agent could not finish this case ({error}). Nothing was changed and the customer "
                    "was not contacted. Question for the handler: what is the right next step for this case?",
        "final_result": "Escalated to a human handler. No action taken.",
    }


def run_case(case_dir, out_dir, client, tools=TOOLS):
    """tools: name -> function, same signatures as tools.TOOLS (e.g. a bank_env adapter's .tools())."""
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    trace_file = (out_dir / "trace.jsonl").open("w")

    def trace(kind, **data):
        trace_file.write(json.dumps({"t": round(time.time(), 3), "kind": kind, **data}, default=str) + "\n")
        trace_file.flush()

    case, error = None, None
    state = {"executed": [], "blocked": [], "failures": [], "tokens": [0, 0]}
    try:
        case = load_case(case_dir)
        trace("loaded", case=case["id"], events=len(case["events"]), attachments=[a.name for a in case["attachments"]])
        decision, state = run_agent(case, client, trace, tools)
    except Exception as e:
        error = f"{type(e).__name__}: {e}"
        trace("crash", error=error, traceback=traceback.format_exc())
        decision = fallback_decision(error)
        state["failures"].append(f"Agent crashed: {error}")
    trace("decision", **decision)
    trace_file.close()
    write_answer(out_dir, case or {"id": Path(case_dir).name, "index": "", "events": [], "attachments": []},
                 decision, state)
    return {"case": Path(case_dir).name, "decision": decision["decision"], "crashed": error is not None,
            "blocked": len(state["blocked"]), "tokens": state["tokens"], "next_action": decision["next_action"]}


# ---------- writer ----------

def bullets(items, empty):
    return "\n".join(f"- {i}" for i in items) if items else empty


def write_answer(out_dir, case, d, state):
    request = section(case["index"], "Initial request") or "(no initial request section found)"
    did = [f"`{x['tool']}` → {x['input'].get('system') or x['input'].get('team') or x['input'].get('recipient')}: "
           f"{x['input'].get('query') or x['input'].get('request') or x['input'].get('instruction') or x['input'].get('message')} "
           f"({x['output'].get('status')}{', ' + x['output']['reference'] if 'reference' in x['output'] else ''}"
           f"{', not executed' if x['output'].get('executed') is False else ''})"
           for x in state["executed"]]
    not_executed = [x for x in state["executed"] if x["output"].get("executed") is False]
    if not_executed:
        did.append("No live bank system is connected, so these actions are recorded as the system's next steps and "
                   "were not executed; no results came back.")
    failed = state["failures"] + [f"Policy guard blocked `{b['tool']}`: {'; '.join(b['problems'])}" for b in state["blocked"]]
    received = (f"{request}\n\n{len(case['events'])} events; attachments: "
                f"{', '.join(a.name for a in case['attachments']) or 'none'}.")
    if case.get("warnings"):
        received += "\n\nCase loader notes:\n" + bullets(case["warnings"], "")
    answer = f"""# Case {case['id']}: {d['decision'].upper()}

## What the system received

{received}

## What the system did

{bullets(did, 'No tool actions were taken.')}

## Decision

**{d['decision'].upper()}**: {d['next_action']}

## What was escalated

{d['handover'] or 'Nothing was escalated.'}

## What failed

{bullets(failed, 'Nothing failed.')}

## Final result

{d['final_result']}
"""
    if d["customer_message"]:
        unsent = any(x["tool"] == "send_secure_message" for x in not_executed)
        answer += f"\nMessage to the customer (secure portal{', recorded, not sent' if unsent else ''}):\n\n> {d['customer_message']}\n"
    reasoning = f"""# Case {case['id']}: reasoning

## Evidence relied on

{bullets([f"{e['event_id']}: {e['fact']}" for e in d['evidence']], 'No evidence cited.')}

## Conflicts between events

{bullets(d['conflicts'], 'No conflicts found.')}

## Options rejected

{bullets([f"{o['option']}: {o['reason']}" for o in d['rejected_options']], 'None recorded.')}

## Policy guard

{bullets([f"Blocked `{b['tool']}`: {'; '.join(b['problems'])}" for b in state['blocked']], 'No calls were blocked.')}
"""
    (out_dir / "ANSWER.md").write_text(answer)
    (out_dir / "REASONING.md").write_text(reasoning)


# ---------- batch ----------

def load_env():
    env = Path(__file__).parent / ".env"
    for line in env.read_text().splitlines() if env.is_file() else []:
        key, _, value = line.partition("=")
        if key.strip() and not key.lstrip().startswith("#"):
            os.environ.setdefault(key.strip(), value.strip().strip('"'))


def find_cases(root):
    root = Path(root)
    if (root / "index.md").is_file():
        return [(root, Path(root.name))]
    return sorted((p.parent, p.parent.relative_to(root)) for p in root.rglob("index.md"))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cases", help="folder of case folders (or a single case folder)")
    ap.add_argument("--out", default="ANSWERS", help="output folder (default ANSWERS/)")
    ap.add_argument("--workers", type=int, default=4, help="cases run in parallel (default 4)")
    args = ap.parse_args()

    load_env()
    cases = find_cases(args.cases)
    if not cases:
        sys.exit(f"No case folders (with index.md) under {args.cases}")
    client = anthropic.Anthropic(timeout=600, max_retries=3)
    print(f"Running {len(cases)} cases with {MODEL} -> {args.out}/", file=sys.stderr)

    def one(item):
        src, rel = item
        r = run_case(src, Path(args.out) / rel, client)
        print(f"  {rel}: {r['decision']}{' (CRASHED → fallback)' if r['crashed'] else ''}", file=sys.stderr)
        return r

    with ThreadPoolExecutor(args.workers) as pool:
        results = list(pool.map(one, cases))
    counts = {k: sum(r["decision"] == k for r in results) for k in ("act", "ask", "wait", "escalate")}
    crashed = sum(r["crashed"] for r in results)
    print(f"Done: {len(results)} cases · " + " · ".join(f"{k} {v}" for k, v in counts.items())
          + f" · crashed {crashed} · guard blocks {sum(r['blocked'] for r in results)}", file=sys.stderr)
    if crashed == len(results):
        print("Every case crashed. Check credentials (ANTHROPIC_API_KEY) and a trace.jsonl.", file=sys.stderr)


if __name__ == "__main__":
    main()

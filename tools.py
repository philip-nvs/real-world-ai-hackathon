"""Bank tool adapter. Mock implementations today; swap the bodies of TOOLS for the
organisers' real tools at 16:30. Schemas stay the same, so the agent doesn't change."""

import itertools

_ref = itertools.count(1)


def _queued(kind, target, text):
    return {
        "status": "queued",
        "reference": f"MOCK-{next(_ref):04d}",
        "detail": f"{kind} sent to {target}. Mock adapter: no live data; the reply will arrive as a new case event.",
        "echo": text,
    }


def check_record(system, query):
    return _queued("Read-only check", system, query)


def submit_internal_request(team, request):
    return _queued("Internal request", team, request)


def submit_instruction(system, instruction, authorised_by_event):
    return _queued("Account-changing instruction", system, instruction)


def send_secure_message(recipient, message):
    return {"status": "delivered", "channel": "Secure portal", "recipient": recipient}


TOOLS = {
    "check_record": check_record,
    "submit_internal_request": submit_internal_request,
    "submit_instruction": submit_instruction,
    "send_secure_message": send_secure_message,
}


def _schema(props):
    return {
        "type": "object",
        "properties": {k: {"type": "string", "description": v} for k, v in props.items()},
        "required": list(props),
        "additionalProperties": False,
    }


TOOL_SCHEMAS = [
    {
        "name": "check_record",
        "description": "Read-only lookup in an H&V system (payment journal, card journal, standing-order journal, "
        "mandate register, access log, import journal, limit register, tariff, incoming-payment records...). "
        "Changes nothing. Use this to establish facts from H&V's own records.",
        "input_schema": _schema({"system": "Which H&V system to check", "query": "Exactly what to look up, with case reference and identifiers"}),
    },
    {
        "name": "submit_internal_request",
        "description": "Ask an internal H&V team or service (payment team, card team, statements service, document "
        "service, security team, tariff team...) to check, prepare or register something. Changes nothing on the customer's account by itself.",
        "input_schema": _schema({"team": "Internal team or service", "request": "The specific request, with case reference"}),
    },
    {
        "name": "submit_instruction",
        "description": "Execute an account-changing instruction (block a card, cancel a mandate or standing order, revoke a role, "
        "change a limit...). Only for an instruction the customer confirmed through a secure, verified channel. "
        "authorised_by_event must be the event ID (e.g. 'event-004') holding that confirmation.",
        "input_schema": _schema({
            "system": "H&V system that executes the instruction",
            "instruction": "The exact instruction",
            "authorised_by_event": "Event ID of the customer's secure confirmation",
        }),
    },
    {
        "name": "send_secure_message",
        "description": "Send a message to the customer through their H&V secure portal. Never by email.",
        "input_schema": _schema({"recipient": "Customer or business user name", "message": "The message text"}),
    },
]
for _t in TOOL_SCHEMAS:
    _t["strict"] = True

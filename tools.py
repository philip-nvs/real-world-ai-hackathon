"""Bank tool adapter for cases with no live H&V systems (the unseen Reality Test cases).

Each tool records the action as the system's next step and executes nothing: no data comes
back, no reference is invented, no message is delivered. Swap the bodies of TOOLS for the
organisers' real tools if they supply any; schemas stay the same, so the agent doesn't change.
The dev loop uses bank_env's fixture adapter instead, which does answer."""

NOT_EXECUTED = "Recorded as H&V's next step; not executed. No live H&V system is connected in this environment, " \
               "so no result will come back. Treat the step as taken; don't wait for or assume its result."


def _recorded(kind, target):
    return {"status": "recorded", "executed": False, "action": kind, "target": target, "detail": NOT_EXECUTED}


def check_record(system, query):
    return _recorded("read-only check", system)


def submit_internal_request(team, request):
    return _recorded("internal request", team)


def submit_instruction(system, instruction, authorised_by_event):
    return _recorded("account-changing instruction", system)


def send_secure_message(recipient, message):
    return _recorded("secure-portal message", recipient)


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

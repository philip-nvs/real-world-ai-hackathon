"""Canonical H&V systems, teams and processes, and resolution of the free-text names the
cases (and the agent) use for them: "H&V transfer journal", "Card journal", "Tariff Team"..."""

import re

RECORD_SYSTEMS = {
    "payment_journal": "Outgoing payments and transfers H&V executed or attempted: status, amount, purpose, decline code, trace, batch rows.",
    "instruction_register": "Payment instructions: saved or pending one-off instructions, standing orders (schedule, runs), Direct Debit mandates.",
    "incoming_payments": "Credits received into an account, including refunds.",
    "card_journal": "Cards: status, restrictions, replacement and dispatch, authorisation attempts and decline reasons.",
    "access_log": "Profile sign-in sessions, devices and their linking state, recovery state.",
    "customer_profile": "Profile data: name, address, phone number.",
    "import_journal": "Business file uploads: receipt and validation results.",
    "signing_queue": "Business payment packages and the consents recorded against them.",
    "business_mandate": "Company users, roles, permissions and administrators.",
    "limit_register": "Payment limits on a profile.",
    "tariff": "Fee tariff entries and the fees charged against transactions.",
}

# Where else a lookup searches when the named system has no match: the boundaries above are ours,
# not the bank's. incoming_payments stays strict, so "no credit found" never turns into an outgoing payment.
RELATED_SYSTEMS = {
    "payment_journal": ["instruction_register", "tariff"],
    "instruction_register": ["payment_journal"],
    "tariff": ["payment_journal"],
    "limit_register": ["business_mandate"],
    "signing_queue": ["business_mandate"],
    "business_mandate": ["limit_register", "signing_queue"],
}

TEAMS = {
    "payment_team": "Payment traces, return requests, payment-stage checks.",
    "card_team": "Card cases, e.g. an unrecognised purchase.",
    "direct_debit_team": "Direct Debit charge reviews.",
    "tariff_team": "Fee and tariff reviews.",
    "data_team": "Profile data corrections.",
    "data_service": "Transaction exports.",
    "statements_service": "Current and archived statements.",
    "document_service": "Account confirmations and payment records.",
    "security_team": "Permitted session extracts and security reviews.",
    "acquiring_service": "Merchant acquiring reports.",
    "access_team": "PIN and access procedures.",
    "import_service": "Batch validation reports.",
    "business_support": "Business access requests sent for administrator approval.",
}

PROCESSES = {
    "card_system": "Block or unblock a card.",
    "instruction_process": "Change or cancel a standing order, recurring instruction or Direct Debit mandate.",
    "profile_change": "Change profile data such as phone number or address.",
    "admin_process": "Grant or revoke business users' roles and access.",
}

# First match wins, so the more specific patterns come first.
_RECORD_RULES = [
    (r"business mandate|company (admin|user|role)|\broles?\b|permission|admin log|access.request", "business_mandate"),
    (r"limit", "limit_register"),
    (r"access log|session|device|sign-in|recovery", "access_log"),
    (r"signing|signator|consent|package", "signing_queue"),
    (r"import|batch|upload", "import_journal"),
    (r"card", "card_journal"),
    (r"incoming|credit|refund|account transaction|account activity", "incoming_payments"),
    (r"standing|mandate|direct debit|instruction|recurring|schedul", "instruction_register"),
    (r"transfer|transaction|payment", "payment_journal"),
    (r"tariff|fee", "tariff"),
    (r"profile|address|phone|name", "customer_profile"),
]
_TEAM_RULES = [
    (r"direct debit", "direct_debit_team"),
    (r"card", "card_team"),
    (r"tariff|fee", "tariff_team"),
    (r"acquiring|merchant", "acquiring_service"),
    (r"import|validation", "import_service"),
    (r"security|session", "security_team"),
    (r"statement|archive", "statements_service"),
    (r"document", "document_service"),
    (r"data service|export", "data_service"),
    (r"data", "data_team"),
    (r"access|\bpin\b", "access_team"),
    (r"business|admin", "business_support"),
    (r"payment", "payment_team"),
]
_PROCESS_RULES = [
    (r"card", "card_system"),
    (r"profile|address|phone", "profile_change"),
    (r"admin|role|access", "admin_process"),
    (r"standing|mandate|direct debit|instruction|recurring", "instruction_process"),
]


def _resolve(name, canonical, rules):
    key = re.sub(r"\b(h&v|harrow (&|and) vale( bank)?( plc)?)\b", "", (name or "").lower()).strip()
    if key.replace(" ", "_") in canonical:
        return key.replace(" ", "_")
    return next((target for pattern, target in rules if re.search(pattern, key)), None)


def resolve_system(name):
    return _resolve(name, RECORD_SYSTEMS, _RECORD_RULES)


def resolve_team(name):
    return _resolve(name, TEAMS, _TEAM_RULES)


def resolve_process(name):
    return _resolve(name, PROCESSES, _PROCESS_RULES)

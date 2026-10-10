"""World model for one case: what H&V's systems, teams and processes hold.

Every fact carries the event it was extracted from. Unknown values stay null; extraction
never invents them. The same model is the JSON schema Claude fills in during extraction."""

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

from bank_env.systems import PROCESSES, RECORD_SYSTEMS, TEAMS

SystemName = Literal[tuple(RECORD_SYSTEMS)]
TeamName = Literal[tuple(TEAMS)]
ProcessName = Literal[tuple(PROCESSES)]


class Strict(BaseModel):
    model_config = ConfigDict(extra="forbid")


class Attr(Strict):
    key: str = Field(description="snake_case fact name, e.g. status, amount_gbp, next_run_date, decline_reason")
    value: str


class Party(Strict):
    id: str = Field(description="Short id, e.g. p1")
    name: str
    kind: Literal["person", "business"]
    roles: list[str] = Field(description="e.g. account_holder, cardholder, authorised_uploader, report_viewer, "
                                         "first_signatory, company_administrator, payout_viewer")
    acts_for: str | None = Field(description="Business party id this person acts for, else null")


class ChannelEvent(Strict):
    id: str = Field(description="event-NNN")
    channel: str
    party: str | None = Field(description="Party id of the sender, null if the sender is H&V or an outsider")
    bank_originated: bool = Field(description="Sent by an H&V system, team or agent")
    verified: bool = Field(description="Customer identity verified on this channel for this event "
                                       "(secure portal or chat session, verified call, business portal). Emails/external messages: false")


class Record(Strict):
    id: str = Field(description="Short id, e.g. r1")
    system: SystemName
    kind: str = Field(description="e.g. outgoing_transfer, standing_order, direct_debit_mandate, card, "
                                  "card_authorisation, device, payroll_file, payment_package, company_limit, fee")
    party: str | None = Field(description="Owning party id")
    match_terms: list[str] = Field(description="Identifiers a lookup would use: payee, amount, date, case ref, file "
                                               "name, row id, card or device description")
    attributes: list[Attr] = Field(description="Facts the system shows the agent, as stated in the case")
    customer_facing: str | None = Field(description="Wording H&V is permitted to share with the customer, if the case "
                                                    "states such a restriction; else null")
    disclosure_rules: list[str] = Field(description="Explicit limits on what may be shared, e.g. 'exact basis not shown'")
    exists_before_agent: bool = Field(description="True if the object existed before the bank agent's first action (the "
                                                  "transfer or card the customer asks about). False if it only comes into "
                                                  "being during the case: a request registered or sent, a document issued")
    created_by: str | None = Field(description="If exists_before_agent is false: id of the team_response or process "
                                               "whose action creates it, else null")
    source_event: str


class TeamResponse(Strict):
    id: str = Field(description="Short id, e.g. t1")
    team: TeamName
    topic_terms: list[str] = Field(description="Terms a request about this would contain")
    status: Literal["registered", "completed", "pending", "rejected"]
    reference: str | None
    response: str = Field(description="What the team replies, close to the case wording")
    document: str | None = Field(description="Attachment file name the team produces, else null")
    source_event: str


class Process(Strict):
    id: str = Field(description="Short id, e.g. x1")
    process: ProcessName
    action: str = Field(description="e.g. block_card, amend_standing_order, cancel_mandate, revoke_role, change_phone")
    match_terms: list[str]
    target_record: str | None = Field(description="Record id the change applies to, else null")
    confirmed_by: list[str] = Field(description="Event ids holding a valid customer (or administrator) confirmation "
                                                "of exactly this change. A request is not a confirmation.")
    effect: list[Attr] = Field(description="Attribute values on the target record once applied")
    result: str = Field(description="What the process reports once applied")
    applied_event: str | None = Field(description="Event in which the case records the change as applied "
                                                  "(e.g. the system confirming it), else null")
    source_event: str


class World(Strict):
    case_id: str
    case_ref: str | None = Field(description="e.g. HV-017, if the case names one")
    parties: list[Party]
    events: list[ChannelEvent]
    records: list[Record]
    team_responses: list[TeamResponse]
    processes: list[Process]


def check_world(world, event_ids):
    """Referential checks the JSON schema can't express. Returns a list of problems."""
    parties = {p.id for p in world.parties}
    records = {r.id for r in world.records}
    events = set(event_ids)
    problems = [f"event {e.id} not in case" for e in world.events if e.id not in events]
    problems += [f"{e.id}: unknown party {e.party}" for e in world.events if e.party and e.party not in parties]
    for item in world.records + world.team_responses + world.processes:
        if item.source_event not in events:
            problems.append(f"{item.id}: source_event {item.source_event} not in case")
    problems += [f"{r.id}: unknown party {r.party}" for r in world.records if r.party and r.party not in parties]
    creators = {t.id for t in world.team_responses} | {x.id for x in world.processes}
    for r in world.records:
        if r.created_by and r.created_by not in creators:
            problems.append(f"{r.id}: created_by {r.created_by} is not a team_response or process")
        if r.created_by and r.exists_before_agent:
            problems.append(f"{r.id}: created_by set but exists_before_agent is true")
    for x in world.processes:
        if x.target_record and x.target_record not in records:
            problems.append(f"{x.id}: unknown target_record {x.target_record}")
        problems += [f"{x.id}: confirmed_by {e} not in case" for e in x.confirmed_by if e not in events]
        if x.applied_event and x.applied_event not in events:
            problems.append(f"{x.id}: applied_event {x.applied_event} not in case")
    ids = [i.id for i in world.parties + world.records + world.team_responses + world.processes]
    problems += [f"duplicate id {i}" for i in {i for i in ids if ids.count(i) > 1}]
    return problems

"""FixtureAdapter: answers the four ports from a case's world model, deterministically, no LLM.

    adapter = FixtureAdapter(load_scenario("001"), visible_events={"event-001", "event-002"})
    adapter.tools()["check_record"](system="H&V transfer journal", query="£420 to Alder & Reed")

Lookups match the query against each record's match_terms: one best match is returned, a tie
comes back as "ambiguous" with the candidates, nothing matching is "not_found". A record created
during the case (a request sent, a document issued) stays hidden until its source event is visible
or the agent fires the team request or process that creates it. Every call and its outcome goes
into adapter.log, for scoring."""

import re

from bank_env.ports import PortError
from bank_env.schema import Attr
from bank_env.systems import PROCESSES, RECORD_SYSTEMS, RELATED_SYSTEMS, TEAMS, resolve_process, resolve_system, resolve_team

STOPWORDS = {"the", "a", "an", "of", "for", "and", "to", "in", "on", "my", "her", "his", "their", "h", "v", "s",
             "check", "status", "record", "please", "is", "was", "with", "from", "by", "this", "that", "specific"}


def tokens(text):
    text = (text or "").lower().replace("£", " ").replace(",", "")
    out = set()
    for t in re.findall(r"\d+(?:\.\d+)?|[a-z]+", text):
        out.add(f"{float(t):.2f}" if t[0].isdigit() else t)
    return out - STOPWORDS


def score(terms, query):
    """Sum over terms of the share of their words in the query, counting terms at least half present."""
    q = tokens(query)
    total = 0.0
    for term in terms:
        words = tokens(term)
        share = len(words & q) / len(words) if words else 0
        if share >= 0.5:
            total += share
    return total


def best(items, terms_of, query):
    scored = [(score(terms_of(i), query), i) for i in items]
    top = max((s for s, _ in scored), default=0)
    return [i for s, i in scored if s == top and s > 0]


LIST_INTENT = re.compile(r"\b(all|list|every|each|both|which|active)\b[^.]*\b(instructions?|entry|entries|records?|payments?|orders?|mandates?|sessions?|users?|roles?)\b", re.I)


def event_id(ref):
    m = re.search(r"\d+", ref or "")
    return f"event-{int(m.group()):03d}" if m else ""


class FixtureAdapter:
    def __init__(self, scenario, visible_events=None):
        """visible_events: the event ids the agent has seen. Confirmations outside it haven't
        happened yet. None means all events are visible."""
        self.world, self.faults = scenario.world, scenario.faults
        self.visible = set(visible_events) if visible_events is not None else {e.id for e in self.world.events}
        self.parties = {p.id: p.name for p in self.world.parties}
        self.log, self._ref, self.fired = [], 0, set()
        for x in self.world.processes:  # changes the visible history already records as done
            if x.applied_event in self.visible:
                self._apply(x)

    # ---------- plumbing ----------

    def _fault(self, port, target, call):
        for f in self.faults:
            if f["port"] == port and f.get("target") in (None, target):
                self.log.append({"port": port, **call, "fault": f["mode"]})
                raise PortError(f["mode"], f.get("message") or f"{target or port} is {f['mode']}")

    def _record(self, port, call, out):
        self.log.append({"port": port, **call, "output": out})
        return out

    def _next_ref(self, prefix):
        self._ref += 1
        return f"{prefix}-{self._ref:04d}"

    def _exists(self, record):
        return record.exists_before_agent or record.source_event in self.visible or record.created_by in self.fired

    def _terms(self, record):
        return record.match_terms + [self.parties.get(record.party, ""), record.kind.replace("_", " ")]

    # ---------- RecordsPort ----------

    def lookup(self, system, query):
        call = {"call": "lookup", "system": system, "query": query}
        canonical = resolve_system(system)
        if canonical is None:
            raise PortError("unknown_system", f"no H&V record system called '{system}'. Known: {', '.join(RECORD_SYSTEMS)}")
        self._fault("records", canonical, call)
        existing = [r for r in self.world.records if self._exists(r)]
        by_ref = [r for r in existing if re.search(rf"\b{re.escape(r.system)}:{re.escape(r.id)}\b", query or "")]
        matches = by_ref
        for related in [canonical] + RELATED_SYSTEMS.get(canonical, []):
            matches = matches or best([r for r in existing if r.system == related], self._terms, query)
        if not matches and LIST_INTENT.search(query or ""):
            listed = [r for r in existing if r.system == canonical]
            if listed:
                return self._record("records", call, {"status": "found", "system": canonical,
                                                      "records": [self._view(r) for r in listed]})
        if not matches:
            return self._record("records", call, {"status": "not_found", "system": canonical,
                                                  "detail": f"No record in {canonical} matches the query."})
        if len(matches) > 1:
            return self._record("records", call, {
                "status": "ambiguous", "system": matches[0].system,
                "detail": "More than one record matches. Identify which one before relying on either; "
                          "look one up by putting its record_ref in the query.",
                "candidates": [{"record_ref": f"{r.system}:{r.id}", "kind": r.kind, "identifiers": r.match_terms}
                               for r in matches]})
        return self._record("records", call, {"status": "found", "system": matches[0].system, **self._view(matches[0])})

    def _holds(self, record, attr):
        """A fact holds once its since_event is visible; the facts a created record is born with (since its own
        source_event) hold as soon as the agent fires the request or process that creates it."""
        return (attr.since_event is None or attr.since_event in self.visible
                or (record.created_by in self.fired and attr.since_event == record.source_event))

    def _event_no(self, event):
        return int(event.split("-")[1]) if event else 0

    def _view(self, r):
        # a fact can change during the case (027: access "declined", then "restored" after the customer's own
        # recovery); show each key's latest value whose since_event the agent has seen
        visible = sorted((a for a in r.attributes if self._holds(r, a)), key=lambda a: self._event_no(a.since_event))
        out = {"record_ref": f"{r.system}:{r.id}", "kind": r.kind, "facts": {a.key: a.value for a in visible}}
        # wording on a record that still changes is often written after the change (036: "new address is marked
        # as current"), so it only shows once the record has reached its final state
        pending = any(x.target_record == r.id and x.id not in self.fired for x in self.world.processes) or \
            not all(self._holds(r, a) for a in r.attributes)
        if r.customer_facing and not pending:
            out["permitted_customer_wording"] = r.customer_facing
        if r.disclosure_rules:
            out["disclosure_rules"] = r.disclosure_rules
        return out

    # ---------- RequestsPort ----------

    def submit_request(self, team, request):
        call = {"call": "submit_request", "team": team, "request": request}
        canonical = resolve_team(team)
        if canonical is None:
            raise PortError("unknown_team", f"no H&V team called '{team}'. Known: {', '.join(TEAMS)}")
        self._fault("requests", canonical, call)
        matches = best([t for t in self.world.team_responses if t.team == canonical], lambda t: t.topic_terms, request)
        if len(matches) != 1:  # no scripted reply (or no way to tell which): the request just sits in the queue
            return self._record("requests", call, {"status": "queued", "team": canonical,
                                                   "reference": self._next_ref("REQ"),
                                                   "detail": f"Request logged with {canonical}; no reply yet."})
        t = matches[0]
        self.fired.add(t.id)
        out = {"status": t.status, "team": canonical, "reference": t.reference or self._next_ref("REQ"), "reply": t.response}
        if t.document:
            out["document"] = t.document
        return self._record("requests", call, out)

    # ---------- InstructionsPort ----------

    def submit_instruction(self, process, instruction, authorised_by_event):
        call = {"call": "submit_instruction", "process": process, "instruction": instruction,
                "authorised_by_event": authorised_by_event}
        canonical = resolve_process(process)
        if canonical is None:
            raise PortError("unknown_process", f"no H&V process called '{process}'. Known: {', '.join(PROCESSES)}")
        self._fault("instructions", canonical, call)
        matches = best([x for x in self.world.processes if x.process == canonical], lambda x: x.match_terms, instruction)
        if len(matches) != 1:
            return self._record("instructions", call, {
                "status": "rejected", "process": canonical,
                "detail": "No single matching change is available for this customer in this process."})
        x, event = matches[0], event_id(authorised_by_event)
        if event not in x.confirmed_by or event not in self.visible:
            return self._record("instructions", call, {
                "status": "rejected", "process": canonical,
                "detail": f"'{authorised_by_event}' is not a confirmation of this change on record. "
                          "Nothing was changed."})
        self._apply(x)
        return self._record("instructions", call, {"status": "applied", "process": canonical,
                                                   "reference": self._next_ref("INS"), "result": x.result})

    def _apply(self, x):
        self.fired.add(x.id)
        target = next((r for r in self.world.records if r.id == x.target_record), None)
        if target:
            new = {a.key: a.value for a in x.effect}
            target.attributes = [a for a in target.attributes if a.key not in new] + [Attr(key=k, value=v) for k, v in new.items()]

    # ---------- MessagingPort ----------

    def send(self, recipient, message):
        call = {"call": "send", "recipient": recipient, "message": message}
        self._fault("messaging", None, call)
        return self._record("messaging", call, {"status": "delivered", "channel": "Secure portal", "recipient": recipient})

    # ---------- tool surface ----------

    def tools(self):
        """Same names and arguments as tools.TOOLS, so the agent can run against this adapter unchanged."""
        return {
            "check_record": lambda system, query: self.lookup(system, query),
            "submit_internal_request": lambda team, request: self.submit_request(team, request),
            "submit_instruction": lambda system, instruction, authorised_by_event:
                self.submit_instruction(system, instruction, authorised_by_event),
            "send_secure_message": lambda recipient, message: self.send(recipient, message),
        }

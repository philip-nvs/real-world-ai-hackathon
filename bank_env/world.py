"""Load a case's world fixture, optionally with an overlay that adds conflicts or faults.

Overlay file (bank_env/overlays/<name>.json):
    {"base": "001", "description": "...",
     "add_records": [Record...], "patch_records": [{"id": "r1", "attributes": [{"key": ..., "value": ...}]}],
     "clone_records": [{"from": "r1", "id": "r9", "attributes": [...], <any other Record field to override>}],
     "add_team_responses": [TeamResponse...],
     "faults": [{"port": "records|requests|instructions|messaging", "target": "<canonical name or null>",
                 "mode": "unavailable|timeout|permission_denied", "message": "..."}]}
"""

import json
from dataclasses import dataclass, field
from pathlib import Path

from bank_env.schema import Attr, Record, TeamResponse, World, check_world

HERE = Path(__file__).parent
FIXTURES, OVERLAYS = HERE / "fixtures", HERE / "overlays"


@dataclass
class Scenario:
    world: World
    faults: list = field(default_factory=list)
    description: str = ""


def load_scenario(case_id=None, overlay=None):
    """load_scenario("001") for the plain fixture, load_scenario(overlay="001-conflicting-transfer")
    for a variant. overlay may also be a dict."""
    spec = overlay if isinstance(overlay, dict) else json.loads((OVERLAYS / f"{overlay}.json").read_text()) if overlay else {}
    case_id = case_id or spec["base"]
    world = World.model_validate_json((FIXTURES / f"{case_id}.json").read_text())
    world.records += [Record.model_validate(r) for r in spec.get("add_records", [])]
    for clone in spec.get("clone_records", []):  # a look-alike of a base record: same identifiers, survives re-extraction
        base = next(r for r in world.records if r.id == clone["from"])
        new = {a["key"]: a["value"] for a in clone.get("attributes", [])}
        fields = {k: v for k, v in clone.items() if k not in ("from", "attributes")}
        attributes = [a for a in base.attributes if a.key not in new] + [Attr(key=k, value=v) for k, v in new.items()]
        world.records.append(base.model_copy(update={**fields, "attributes": attributes}))
    world.team_responses += [TeamResponse.model_validate(t) for t in spec.get("add_team_responses", [])]
    for patch in spec.get("patch_records", []):
        record = next(r for r in world.records if r.id == patch["id"])
        new = {a["key"]: a["value"] for a in patch["attributes"]}
        record.attributes = [a for a in record.attributes if a.key not in new] + [Attr(key=k, value=v) for k, v in new.items()]
    problems = check_world(world, [e.id for e in world.events])
    if problems:
        raise ValueError(f"overlay breaks the world: {problems}")
    return Scenario(world, spec.get("faults", []), spec.get("description", ""))

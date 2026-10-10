"""Ports the agent's tools talk to. Adapters implement them: fixtures today, the organisers'
real tools later. Replies are plain dicts; a PortError is a failed call the agent must handle."""

from typing import Protocol


class PortError(Exception):
    def __init__(self, code, message):
        super().__init__(f"{code}: {message}")
        self.code = code


class RecordsPort(Protocol):
    def lookup(self, system: str, query: str) -> dict: ...


class RequestsPort(Protocol):
    def submit_request(self, team: str, request: str) -> dict: ...


class InstructionsPort(Protocol):
    def submit_instruction(self, process: str, instruction: str, authorised_by_event: str) -> dict: ...


class MessagingPort(Protocol):
    def send(self, recipient: str, message: str) -> dict: ...

from dataclasses import dataclass


@dataclass(frozen=True)
class SendDataStatus:
    status: bool
    message: str

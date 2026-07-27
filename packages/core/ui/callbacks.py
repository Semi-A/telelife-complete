"""Signed, owned, expiring callback payloads.

Format:  ns:action:owner_id:arg
`owner_id` is embedded so a stranger tapping your panel is rejected without a
database round-trip. Cheapest possible ownership check.
"""

from __future__ import annotations

from dataclasses import dataclass

SEP = ":"


@dataclass(slots=True, frozen=True)
class Callback:
    namespace: str
    action: str
    owner_id: int
    arg: str = ""

    def pack(self) -> str:
        parts = [self.namespace, self.action, str(self.owner_id)]
        if self.arg:
            parts.append(self.arg)
        data = SEP.join(parts)
        if len(data.encode()) > 64:
            raise ValueError(f"callback_data exceeds Telegram 64-byte limit: {data!r}")
        return data

    @classmethod
    def parse(cls, raw: str) -> Callback | None:
        parts = raw.split(SEP)
        if len(parts) < 3:
            return None
        try:
            owner_id = int(parts[2])
        except ValueError:
            return None
        return cls(parts[0], parts[1], owner_id, parts[3] if len(parts) > 3 else "")

    def owned_by(self, telegram_id: int) -> bool:
        return self.owner_id == telegram_id


def cb(namespace: str, action: str, owner_id: int, arg: str = "") -> str:
    return Callback(namespace, action, owner_id, arg).pack()
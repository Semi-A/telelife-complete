"""Process-local runtime health registry shared with the admin panel."""
from __future__ import annotations

import time
from dataclasses import asdict, dataclass
from typing import Any


@dataclass(slots=True)
class ServiceState:
    name: str
    status: str = "starting"
    restarts: int = 0
    last_error: str | None = None
    last_started_monotonic: float | None = None
    last_healthy_monotonic: float | None = None
    consecutive_health_failures: int = 0

    def public(self) -> dict[str, Any]:
        data = asdict(self)
        now = time.monotonic()
        started = data.pop("last_started_monotonic")
        healthy = data.pop("last_healthy_monotonic")
        data["uptime_seconds"] = round(max(0.0, now - started), 1) if started else 0.0
        data["healthy_ago_seconds"] = round(max(0.0, now - healthy), 1) if healthy else None
        # The process-local registry is authoritative for lifecycle state. A
        # service in its startup grace period is not a failed bot.
        raw_status = str(data["status"])
        if raw_status == "healthy":
            display_status, severity = "online", "ok"
        elif raw_status == "starting":
            display_status, severity = "starting", "info"
        elif raw_status == "restarting":
            display_status, severity = "recovering", "warning"
        elif raw_status == "stopped":
            display_status, severity = "offline", "critical"
        else:
            display_status, severity = raw_status, "warning"
        data["display_status"] = display_status
        data["severity"] = severity
        return data


_states: dict[str, ServiceState] = {}


def state(name: str) -> ServiceState:
    return _states.setdefault(name, ServiceState(name=name))


def snapshot() -> dict[str, dict[str, Any]]:
    return {name: item.public() for name, item in sorted(_states.items())}
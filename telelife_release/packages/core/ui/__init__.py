"""Telegram UI primitives, loaded lazily to keep submodules independent."""

from __future__ import annotations

from typing import Any

__all__ = [
    "Callback",
    "Keyboard",
    "Style",
    "button",
    "cb",
    "schedule_cleanup",
    "timeout_for",
]


def __getattr__(name: str) -> Any:
    if name in {"Callback", "cb"}:
        from packages.core.ui import callbacks

        return getattr(callbacks, name)
    if name in {"Keyboard", "Style", "button"}:
        from packages.core.ui import buttons

        return getattr(buttons, name)
    if name in {"schedule_cleanup", "timeout_for"}:
        from packages.core.ui import panels

        return getattr(panels, name)
    raise AttributeError(name)
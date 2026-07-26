"""Offline-safe stubs so pure game logic is testable without a database."""

from __future__ import annotations

import sys
import types


def _stub(name: str, **attrs: object) -> None:
    if name in sys.modules:
        return
    module = types.ModuleType(name)
    for key, value in attrs.items():
        setattr(module, key, value)
    sys.modules[name] = module


try:  # pragma: no cover
    import asyncpg  # noqa: F401
except ImportError:  # pragma: no cover
    _stub("asyncpg", Connection=object, Record=object, Pool=object, create_pool=None)
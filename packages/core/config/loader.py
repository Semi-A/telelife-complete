"""YAML game-config loader. Zero hardcoded game numbers anywhere else."""

from __future__ import annotations

import logging
from functools import lru_cache
from pathlib import Path
from typing import Any

_MISSING = object()

import yaml

logger = logging.getLogger(__name__)

CONFIG_DIR = Path(__file__).resolve().parent / "data"


class ConfigError(RuntimeError):
    """Raised when game configuration is missing or invalid."""


class GameConfig:
    """Read-only dotted access over merged YAML files."""

    __slots__ = ("_data",)

    def __init__(self, data: dict[str, Any]) -> None:
        self._data = data

    def get(self, path: str, default: Any = _MISSING) -> Any:
        node: Any = self._data
        for part in path.split("."):
            if not isinstance(node, dict):
                if default is _MISSING:
                    raise ConfigError(f"Missing config key: {path}")
                return default
            key: str | int = part
            if key not in node and part.lstrip("-").isdigit():
                key = int(part)
            if key not in node:
                if default is _MISSING:
                    raise ConfigError(f"Missing config key: {path}")
                return default
            node = node[key]
        return node

    def has(self, path: str) -> bool:
        """Return whether a dotted path exists."""
        try:
            self.get(path)
        except ConfigError:
            return False
        return True

    def int_(self, path: str, default: int | object = _MISSING) -> int:
        value = self.get(path, default)
        if isinstance(value, bool):
            raise ConfigError(f"Config key '{path}' must be an integer")
        try:
            return int(value)
        except (TypeError, ValueError) as exc:
            raise ConfigError(f"Config key '{path}' must be an integer") from exc

    def float_(self, path: str, default: float | object = _MISSING) -> float:
        value = self.get(path, default)
        if isinstance(value, bool):
            raise ConfigError(f"Config key '{path}' must be numeric")
        try:
            return float(value)
        except (TypeError, ValueError) as exc:
            raise ConfigError(f"Config key '{path}' must be numeric") from exc

    def bool_(self, path: str, default: bool | object = _MISSING) -> bool:
        value = self.get(path, default)
        if not isinstance(value, bool):
            raise ConfigError(f"Config key '{path}' must be a boolean")
        return value

    def section(self, path: str) -> dict[str, Any]:
        value = self.get(path)
        if not isinstance(value, dict):
            raise ConfigError(f"Config key '{path}' is not a section")
        return value

    def as_dict(self) -> dict[str, Any]:
        return self._data


@lru_cache(maxsize=1)
def get_config() -> GameConfig:
    merged: dict[str, Any] = {}
    if not CONFIG_DIR.exists():
        raise ConfigError(f"Config directory not found: {CONFIG_DIR}")
    paths = sorted(CONFIG_DIR.glob("*.yaml"))
    if not paths:
        raise ConfigError(f"No YAML config files found in: {CONFIG_DIR}")
    for path in paths:
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        except (OSError, yaml.YAMLError) as exc:
            raise ConfigError(f"Unable to load config file '{path.name}': {exc}") from exc
        if not isinstance(data, dict):
            raise ConfigError(f"Config file '{path.name}' must contain a mapping")
        merged[path.stem] = data
    logger.info("loaded game config sections: %s", ", ".join(sorted(merged)))
    return GameConfig(merged)


def reload_config() -> GameConfig:
    get_config.cache_clear()
    return get_config()

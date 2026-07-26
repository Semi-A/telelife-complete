"""YAML game-config loader. Zero hardcoded game numbers anywhere else."""

from __future__ import annotations

import logging
from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml

logger = logging.getLogger(__name__)

CONFIG_DIR = Path(__file__).resolve().parent / "data"


class ConfigError(RuntimeError):
    pass


class GameConfig:
    """Read-only dotted access over merged YAML files."""

    __slots__ = ("_data",)

    def __init__(self, data: dict[str, Any]) -> None:
        self._data = data

    def get(self, path: str, default: Any = None) -> Any:
        node: Any = self._data
        for part in path.split("."):
            if not isinstance(node, dict) or part not in node:
                if default is None:
                    raise ConfigError(f"Missing config key: {path}")
                return default
            node = node[part]
        return node

    def int_(self, path: str, default: int | None = None) -> int:
        return int(self.get(path, default))

    def float_(self, path: str, default: float | None = None) -> float:
        return float(self.get(path, default))

    def bool_(self, path: str, default: bool | None = None) -> bool:
        return bool(self.get(path, default))

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
    for path in sorted(CONFIG_DIR.glob("*.yaml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        if not isinstance(data, dict):
            raise ConfigError(f"Config file '{path.name}' must contain a mapping")
        merged[path.stem] = data
    logger.info("loaded game config sections: %s", ", ".join(sorted(merged)))
    return GameConfig(merged)


def reload_config() -> GameConfig:
    get_config.cache_clear()
    return get_config()
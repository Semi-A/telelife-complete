from __future__ import annotations
import pytest
from pydantic import ValidationError
from packages.core.settings import Settings

BASE = {
    "DATABASE_URL": "postgresql://test_user:test_password@127.0.0.1/test_db",
    "ADMIN_USERNAME": "admin",
    "ADMIN_PASSWORD": "a-strong-password",
    "RUN_MODE": "polling",
}

def test_two_pollers_cannot_share_one_token(monkeypatch: pytest.MonkeyPatch) -> None:
    for key, value in BASE.items():
        monkeypatch.setenv(key, value)
    monkeypatch.setenv("TELELIFE_BOT_TOKEN", "123:shared")
    monkeypatch.setenv("TELEWORLD_BOT_TOKEN", "123:shared")
    with pytest.raises(ValidationError, match="two different bots"):
        Settings()

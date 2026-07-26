"""Environment-driven settings. Secrets live here; game numbers live in config/*.yaml."""

from __future__ import annotations

from enum import StrEnum
from functools import lru_cache

from pydantic import Field, PostgresDsn, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class RunMode(StrEnum):
    POLLING = "polling"
    WEBHOOK = "webhook"


class Service(StrEnum):
    TELELIFE = "telelife"
    TELEWORLD = "teleworld"
    SCHEDULER = "scheduler"
    ADMIN = "admin"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore", case_sensitive=False
    )

    service: Service = Service.TELELIFE
    environment: str = "development"
    debug: bool = False
    log_level: str = "INFO"

    # --- database ---
    database_url: PostgresDsn
    db_pool_min: int = Field(default=2, ge=1)
    db_pool_max: int = Field(default=10, ge=1)
    db_command_timeout: float = 15.0
    # Supabase transaction pooler is incompatible with prepared statements.
    db_statement_cache_size: int = 0

    # --- bots ---
    telelife_bot_token: str = ""
    teleworld_bot_token: str = ""
    global_news_chat_id: int | None = None

    # --- run mode ---
    run_mode: RunMode = RunMode.POLLING
    webhook_base_url: str = ""
    webhook_secret: str = ""
    port: int = 8000
    host: str = "0.0.0.0"  # noqa: S104

    # --- admin ---
    admin_session_secret: str = "change-me"
    admin_username: str = "admin"
    admin_password: str = "change-me"

    @field_validator("db_pool_max")
    @classmethod
    def _check_pool(cls, v: int, info) -> int:  # type: ignore[no-untyped-def]
        mn = info.data.get("db_pool_min", 1)
        if v < mn:
            raise ValueError("db_pool_max must be >= db_pool_min")
        return v

    def token_for(self, service: Service) -> str:
        token = {
            Service.TELELIFE: self.telelife_bot_token,
            Service.TELEWORLD: self.teleworld_bot_token,
        }.get(service, "")
        if not token:
            raise RuntimeError(f"Missing bot token for service '{service}'")
        return token

    def webhook_url(self, service: Service) -> str:
        base = self.webhook_base_url.rstrip("/")
        if not base:
            raise RuntimeError("WEBHOOK_BASE_URL is required in webhook mode")
        return f"{base}/telegram/{service}"


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()  # type: ignore[call-arg]
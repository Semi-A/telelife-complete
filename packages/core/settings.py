"""Validated, environment-driven runtime settings."""

from __future__ import annotations

from enum import StrEnum
from functools import lru_cache

from pydantic import Field, PostgresDsn, ValidationInfo, field_validator, model_validator
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
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )

    service: Service = Service.ADMIN
    environment: str = "development"
    debug: bool = False
    log_level: str = "INFO"

    database_url: PostgresDsn
    db_pool_min: int = Field(default=1, ge=1, le=50)
    db_pool_max: int = Field(default=5, ge=1, le=50)
    db_command_timeout: float = Field(default=15.0, gt=0, le=300)
    db_statement_cache_size: int = Field(default=0, ge=0)
    db_max_inactive_seconds: float = Field(default=60.0, ge=10, le=3600)
    memory_warning_mb: int = Field(default=450, ge=64, le=4096)

    telelife_bot_token: str = ""
    teleworld_bot_token: str = ""
    global_news_chat_id: int | None = None

    run_mode: RunMode = RunMode.POLLING
    webhook_base_url: str = ""
    webhook_secret: str = ""
    port: int = Field(default=8000, ge=1, le=65535)
    host: str = "0.0.0.0"  # noqa: S104

    admin_username: str = ""
    admin_password: str = ""

    @field_validator("log_level")
    @classmethod
    def validate_log_level(cls, value: str) -> str:
        normalized = value.upper()
        if normalized not in {"CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"}:
            raise ValueError("LOG_LEVEL must be a standard Python logging level")
        return normalized

    @field_validator("db_pool_max")
    @classmethod
    def validate_pool_bounds(cls, value: int, info: ValidationInfo) -> int:
        if value < int(info.data.get("db_pool_min", 1)):
            raise ValueError("DB_POOL_MAX must be greater than or equal to DB_POOL_MIN")
        return value

    @model_validator(mode="after")
    def validate_process_requirements(self) -> Settings:
        # A single supervised process always starts both bots and the admin panel.
        telelife_token = self.token_for(Service.TELELIFE)
        teleworld_token = self.token_for(Service.TELEWORLD)
        if telelife_token == teleworld_token:
            raise ValueError(
                "TELELIFE_BOT_TOKEN and TELEWORLD_BOT_TOKEN must belong to two different bots"
            )
        if not self.admin_username or not self.admin_password:
            raise ValueError("ADMIN_USERNAME and ADMIN_PASSWORD are required")
        if len(self.admin_password) < 12:
            raise ValueError("ADMIN_PASSWORD must contain at least 12 characters")
        if self.run_mode is not RunMode.POLLING:
            raise ValueError("The single-service deployment requires RUN_MODE=polling")
        return self

    def token_for(self, service: Service) -> str:
        token = {
            Service.TELELIFE: self.telelife_bot_token,
            Service.TELEWORLD: self.teleworld_bot_token,
        }.get(service, "").strip()
        if not token:
            raise RuntimeError(f"Missing bot token for service '{service.value}'")
        return token

    def webhook_url(self, service: Service) -> str:
        base = self.webhook_base_url.rstrip("/")
        if not base:
            raise RuntimeError("WEBHOOK_BASE_URL is required in webhook mode")
        return f"{base}/telegram/{service.value}"


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()  # type: ignore[call-arg]

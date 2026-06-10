"""
Application settings loaded from environment variables / .env file.

Uses pydantic-settings so every value is validated at startup.  Missing
required values produce a clear error rather than a silent failure at runtime.
"""

from __future__ import annotations

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """M-AIDA runtime configuration.

    All values can be overridden by environment variables or a .env file
    located in the working directory when uvicorn is launched.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    anthropic_api_key: str = ""
    # Claude model used for extraction; override via ANTHROPIC_MODEL env var.
    anthropic_model: str = "claude-sonnet-4-6"
    notion_token: str = ""
    notion_database_id: str = ""
    maida_port: int = 8765

    # Allowed CORS origins (comma-separated in env; pydantic-settings handles list)
    cors_origins: list[str] = ["http://localhost:3000", "http://127.0.0.1:3000"]


_settings: Settings | None = None


def get_settings() -> Settings:
    """Return the singleton Settings instance, creating it on first call."""
    global _settings  # noqa: PLW0603
    if _settings is None:
        _settings = Settings()
    return _settings

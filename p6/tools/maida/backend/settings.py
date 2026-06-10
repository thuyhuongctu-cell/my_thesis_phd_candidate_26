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
    # Model resolution chain (project-wide convention):
    #   ANTHROPIC_MODEL (explicit override)
    #   -> ANTHROPIC_DEFAULT_FABLE_MODEL (project default tier)
    #   -> "claude-fable-5"
    anthropic_model: str = ""
    anthropic_default_fable_model: str = "claude-fable-5"
    notion_token: str = ""
    notion_database_id: str = ""
    maida_port: int = 8765

    # Allowed CORS origins (comma-separated in env; pydantic-settings handles list)
    cors_origins: list[str] = ["http://localhost:3000", "http://127.0.0.1:3000"]

    @property
    def resolved_model(self) -> str:
        """Claude model for extraction, per the project resolution chain."""
        return self.anthropic_model or self.anthropic_default_fable_model


_settings: Settings | None = None


def get_settings() -> Settings:
    """Return the singleton Settings instance, creating it on first call."""
    global _settings  # noqa: PLW0603
    if _settings is None:
        _settings = Settings()
    return _settings

__all__ = ("BASE_DIR", "get_settings", "get_settings")

from functools import lru_cache
from pathlib import Path

from pydantic import BaseModel, Field, PostgresDsn
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"


class PostgresSettings(BaseModel):
    host: str
    port: int
    user: str
    password: str
    dsn: PostgresDsn


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=ENV_PATH,
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        case_sensitive=False,
    )

    base_dir: Path = BASE_DIR
    debug: bool
    service_name: str
    environment: str = Field(alias="env")
    postgres: PostgresSettings


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()

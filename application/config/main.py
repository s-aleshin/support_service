__all__ = ("BASE_DIR", "Settings", "get_settings")
from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

from .database import DatabaseSettings


BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=ENV_PATH,
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
    )

    project_name: str
    database: DatabaseSettings


@lru_cache
def get_settings() -> Settings:
    return Settings()

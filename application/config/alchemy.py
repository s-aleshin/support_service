__all__ = ("sql_alchemy_plugin",)

from advanced_alchemy.config import AsyncSessionConfig
from litestar.plugins.sqlalchemy import SQLAlchemyAsyncConfig, SQLAlchemyInitPlugin

from .config import get_settings


settings = get_settings()


session_config = AsyncSessionConfig(expire_on_commit=False)
config = SQLAlchemyAsyncConfig(
    connection_string=str(settings.postgres.dsn),
    session_config=session_config,
    before_send_handler="autocommit",
)
sql_alchemy_plugin = SQLAlchemyInitPlugin(config=config)

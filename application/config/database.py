from pydantic import BaseModel, PostgresDsn


class PostgresSettings(BaseModel):
    dsn: PostgresDsn


class DatabaseSettings(BaseModel):
    pg: PostgresSettings

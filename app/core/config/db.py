from pydantic_settings import BaseSettings
from app.core.config.paths import path_settings

class DatabaseSettings(BaseSettings):
    DATABASE_URL: str = f"sqlite:///{path_settings.DATABASE_PATH.as_posix()}"

db_settings = DatabaseSettings()
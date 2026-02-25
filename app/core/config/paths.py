from pydantic_settings import BaseSettings
from pathlib import Path

class PathSettings(BaseSettings):
    APP_PATH: Path = Path.home() / '.polyou'
    DATABASE_PATH: Path = APP_PATH / 'polyou.db'

path_settings = PathSettings()
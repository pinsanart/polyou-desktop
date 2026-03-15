from pydantic_settings import BaseSettings
from PySide6.QtCore import QStandardPaths
from pathlib import Path

from app.core.config.app import app_settings

class PathSettings(BaseSettings):
    APP_PATH:Path = Path(
        QStandardPaths.writableLocation(
            QStandardPaths.AppDataLocation
        )
    ) / app_settings.APP_NAME
    
    DATABASE_PATH: Path = APP_PATH / 'database'
    STATES_PATH: Path = APP_PATH / 'states'
    MEDIA_PATH: Path = APP_PATH / 'media'

    DATABASE_FILE_PATH: Path = DATABASE_PATH / 'polyou.db'

    def ensure_dirs(self):
        self.DATABASE_PATH.mkdir(parents=True, exist_ok=True)
        self.STATES_PATH.mkdir(parents=True, exist_ok=True)
        self.MEDIA_PATH.mkdir(parents=True, exist_ok=True)
        
path_settings = PathSettings()
path_settings.ensure_dirs()
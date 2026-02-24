from pydantic_settings import BaseSettings
import platform
from pathlib import Path

class AppSettings(BaseSettings):
    APP_NAME: str = "Polyou-Desktop"
    BASE_URL: str = "http://127.0.0.1:8000/"
    
    APP_PATH: Path = Path.home() / '.polyou'
    DATABASE_PATH: Path = APP_PATH / 'polyou.db'
    DATABASE_URL: str = f"sqlite:///{DATABASE_PATH.as_posix()}"

    USERNAME: str = platform.node()
    OS: str = platform.system()
    DESKTOP_NAME: str = platform.node()
    DEVICE_NAME: str = f"{APP_NAME} on {OS} ({DESKTOP_NAME})" 

    DEFAULT_TIMEOUT_SECONDS: float = 5.0

settings = AppSettings()
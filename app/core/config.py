from pydantic_settings import BaseSettings
from pydantic import HttpUrl
import platform

class AppSettings(BaseSettings):
    APP_NAME: str = "Polyou Desktop"
    BASE_URL: HttpUrl = "http://127.0.0.1:8000/"
    
    USER_NAME: str = platform.node()
    
    OS: str = platform.system()
    DESKTOP_NAME: str = platform.node()
    DEVICE_NAME: str = f"{APP_NAME} on {OS} ({DESKTOP_NAME})" 

    DEFAULT_TIMEOUT_SECONDS: float = 5.0

settings = AppSettings()
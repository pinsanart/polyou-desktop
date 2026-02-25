from pydantic_settings import BaseSettings
import platform

from .app import app_settings

class DesktopSettings(BaseSettings):
    USERNAME: str = platform.node()
    OS: str = platform.system()
    DESKTOP_NAME: str = platform.node()
    DEVICE_NAME: str = f"{app_settings.APP_NAME} on {OS} ({DESKTOP_NAME})"

desktop_settings = DesktopSettings()
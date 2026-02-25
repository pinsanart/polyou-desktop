from pydantic_settings import BaseSettings

class AppSettings(BaseSettings):
    APP_NAME: str = "Polyou-Desktop"
    DEBUG: bool = True
    
app_settings = AppSettings()
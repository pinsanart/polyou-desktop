from pydantic_settings import BaseSettings

class HTTPSettings(BaseSettings):
    BASE_URL: str = "http://127.0.0.1:8000/"
    DEFAULT_TIMEOUT_SECONDS: float = 5.0

http_settings = HTTPSettings()
from pathlib import Path

class Settings:
    POLYOU_URL = "http://127.0.0.1:8000"
    APP_DIR = Path.home() / ".polyou"
    DB_PATH = APP_DIR / 'polyou.db'
    
    def __init__(self):
        self.APP_DIR.mkdir(exist_ok=True)

settings = Settings()
from pathlib import Path

class Settings:
    APP_DIR = Path.home() / ".polyou"
    DB_PATH = APP_DIR / 'polyou.db'
    
    def __init__(self):
        self.APP_DIR.mkdir(exist_ok=True)

settings = Settings()
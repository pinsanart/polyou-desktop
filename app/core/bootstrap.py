from pathlib import Path
import sqlite3

class Bootstrap:
    def __init__(self, app_path: Path, db_path: Path):
       self.app_path = app_path
       self.db_path = db_path

    def inicialize_app_foulder(self):
        self.app_path.mkdir(parents=True, exist_ok=True)

    def inicialize_local_database(self):
        conn = sqlite3.connect(self.db_path)
        conn.close()

    def run(self):
        self.inicialize_app_foulder()
        self.inicialize_local_database()
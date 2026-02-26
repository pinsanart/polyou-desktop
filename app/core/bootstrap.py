from pathlib import Path
import sqlite3

from app.infrastructure.db.migrations import create_all
from app.infrastructure.db.connections import DBConnection

class Bootstrap:
    def __init__(self, db_connection: DBConnection, app_path: Path, db_path: Path):
        self._app_path = app_path
        self._db_path = db_path
        self._db_connection = db_connection

    def _inicialize_app_foulder(self):
        self._app_path.mkdir(parents=True, exist_ok=True)

    def _inicialize_local_db_file(self):
        conn = sqlite3.connect(self._db_path)
        conn.close()

    def create_db_tables(self):
        create_all(self._db_connection.engine)

    def run(self):
        self._inicialize_app_foulder()
        self._inicialize_local_db_file()
        self.create_db_tables()
from sqlalchemy import event
from sqlalchemy.engine import Engine

from app.infrastructure.db.connections import DBConnection

class DBConnectionFactory:
    @staticmethod
    def create(DATABASE_URL: str, DEBUG: bool = False) -> DBConnection:
        db_connection = DBConnection(
            DATABASE_URL=DATABASE_URL,
            DEBUG=DEBUG
        )
        
        if DATABASE_URL.startswith("sqlite"):
            DBConnectionFactory._configure_sqlite(db_connection.engine)
        
        return db_connection
    
    @staticmethod
    def _configure_sqlite(engine: Engine):
        @event.listens_for(engine, "connect")
        def set_foreign_keys(dbapi_connection, connection_record):
            cursor = dbapi_connection.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")
            cursor.close()
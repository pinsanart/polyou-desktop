from sqlalchemy import create_engine, event
from app.dependencies.config.config import settings
from sqlalchemy.engine import Engine

engine = create_engine(
    f"sqlite:///{settings.DB_PATH}",
    future = True, 
    echo = False
)

@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
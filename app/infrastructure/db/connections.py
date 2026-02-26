from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnection:
    def __init__(self, DATABASE_URL: str, DEBUG:bool = False):
        self.engine = create_engine(DATABASE_URL, echo=DEBUG)
                
        self.session_local = sessionmaker(
            bind=self.engine,
            autocommit=False,
            autoflush=False,
            future=True
        )   
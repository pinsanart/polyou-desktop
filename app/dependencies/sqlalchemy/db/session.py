from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

@contextmanager
def get_db(session_local: sessionmaker):
    db = session_local()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
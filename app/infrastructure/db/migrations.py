from app.infrastructure.db.engine import engine
from app.infrastructure.db.models import PolyouDB

def create_all():
    PolyouDB.metadata.create_all(engine)

def drop_all():
    PolyouDB.metadata.drop_all(engine)
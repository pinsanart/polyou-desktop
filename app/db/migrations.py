from app.db.engine import engine
from app.db.models import PolyouDB

def create_all():
    PolyouDB.metadata.create_all(engine)
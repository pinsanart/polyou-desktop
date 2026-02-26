from .models import PolyouDB
from sqlalchemy import Engine

def create_all(engine: Engine):
    PolyouDB.metadata.create_all(engine)

def drop_all(engine: Engine):
    PolyouDB.metadata.drop_all(engine)
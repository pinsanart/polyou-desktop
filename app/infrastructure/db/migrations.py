from .models import PolyouDB
from .connections import engine

def create_all():
    PolyouDB.metadata.create_all(engine)

def drop_all():
    PolyouDB.metadata.drop_all(engine)
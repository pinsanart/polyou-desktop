from sqlalchemy.orm import sessionmaker
from app.infrastructure.db.engine import engine

SessionLocal = sessionmaker(
    bind = engine,
)
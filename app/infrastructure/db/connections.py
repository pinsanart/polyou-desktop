from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ...core.config.db import db_settings
from ...core.config.app import app_settings

engine = create_engine(db_settings.DATABASE_URL, echo=app_settings.DEBUG)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=True,
    future=True
)
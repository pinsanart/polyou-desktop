from sqlalchemy import create_engine
from app.dependencies.config.config import settings

engine = create_engine(
    f"sqlite:///{settings.DB_PATH}",
    future = True, 
    echo = False
)
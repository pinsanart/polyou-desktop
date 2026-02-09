from ...core.repositories.languages import LanguagesRepository
from ...infrastructure.db.models import LanguageModel

from sqlalchemy.orm import sessionmaker
from sqlalchemy import select

class LanguageRepositorySQLAlchemy(LanguagesRepository):
    def __init__(self, sessionmaker: sessionmaker):
        self.sessionmaker = sessionmaker

    def list_ids(self) -> list[int]:
        with self.sessionmaker() as session:
            stmt = select(LanguageModel.language_id)
            return list(session.execute(stmt).scalars().all())
    
    def get_by_id(self, id: int):
        with self.sessionmaker() as session:
            stmt = select(LanguageModel).where(LanguageModel.language_id == id)
            return session.scalar(stmt)
    
    def get_by_iso_639_1(self, iso_639_1:str):
        with self.sessionmaker() as session:
            stmt = select(LanguageModel).where(LanguageModel.iso_639_1 == iso_639_1)
            return session.scalar(stmt)
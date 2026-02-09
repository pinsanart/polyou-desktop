from sqlalchemy.orm import sessionmaker
from sqlalchemy import select

from ...core.repositories.flashcard_types import FlashcardTypesRepository
from ..db.models import FlashcardTypeModel

class FlashcardTypesRepositorySQLAlchemy(FlashcardTypesRepository):
    def __init__(self, sessionmaker: sessionmaker):
        self.sessionmaker = sessionmaker

    def get_by_id(self, id):
        with self.sessionmaker() as session:
            stmt = select(FlashcardTypeModel).where(FlashcardTypeModel.flashcard_type_id == id)
            return session.scalar(stmt)

    def get_by_name(self, name: str):
        with self.sessionmaker() as session:
            stmt = select(FlashcardTypeModel).where(FlashcardTypeModel.name == name)
            return session.scalar(stmt)
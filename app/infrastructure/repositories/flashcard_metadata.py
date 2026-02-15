from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, update

from ...core.repositories.flashcard_metadata import FlashcardMetadataRepository

from ..db.models import FlashcardMetadataModel

class FlashcardMetadataRepositorySQLAlchemy(FlashcardMetadataRepository):
    def __init__(self, sessionmaker: sessionmaker):
        self.sessionmaker = sessionmaker

    def get(self, id: int):
        with self.sessionmaker() as session:
            stmt = select(FlashcardMetadataModel).where(FlashcardMetadataModel.flashcard_id == id)
            return session.scalar(stmt)

    def touch_has_been_synced(self, ids: list[int]):
        with self.sessionmaker() as session:
            try:
                stmt = (
                    update(FlashcardMetadataModel)
                    .where(FlashcardMetadataModel.flashcard_id.in_(ids))
                    .values(has_been_synced=True)
                )
                session.execute(stmt)
                session.commit()
            except Exception:
                session.rollback()
                raise

    
    def get_ids_not_synced(self) -> list[int]:
        with self.sessionmaker() as session:
            stmt = select(FlashcardMetadataModel.flashcard_id).where(FlashcardMetadataModel.has_been_synced == False)
            return session.execute(stmt).scalars().all()
    
    def get_ids_has_been_synced(self) -> list[int]:
        with self.sessionmaker() as session:
            stmt = select(FlashcardMetadataModel.flashcard_id).where(FlashcardMetadataModel.has_been_synced == True)
            return session.execute(stmt).scalars().all()
    
    def get_ids_locally_deleted(self) -> list[int]:
        with self.sessionmaker() as session:
            stmt = select(FlashcardMetadataModel.flashcard_id).where(FlashcardMetadataModel.locally_deleted == True)
            return session.execute(stmt).scalars().all()
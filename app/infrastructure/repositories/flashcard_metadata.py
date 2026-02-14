from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, update

from ...core.repositories.flashcard_metadata import FlashcardMetadataRepository

from ..db.models import FlashcardMetadataModel

class FlashcardMetadataRepositorySQLAlchemy(FlashcardMetadataRepository):
    def __init__(self, sessionmaker: sessionmaker):
        self.sessionmaker = sessionmaker

    def set_has_been_synced(self, id: int, has_been_synced: bool):
        with self.sessionmaker() as session:
            try:
                stmt = update(FlashcardMetadataModel).where(FlashcardMetadataModel.flashcard_id == id).values(has_been_synced = has_been_synced)
                session.execute(stmt)
                session.commit()
            except Exception:
                session.rollback()
                raise        
    
    def set_locally_deleted(self, id: int, locally_deleted: bool):
        with self.sessionmaker() as session:
            try:
                stmt = update(FlashcardMetadataModel).where(FlashcardMetadataModel.flashcard_id == id).values(locally_deleted = locally_deleted)
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
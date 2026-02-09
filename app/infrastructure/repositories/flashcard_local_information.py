from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, update

from ...core.repositories.flashcard_local_information import FlashcardLocalInformationRepository

from ..db.models import FlashcardLocalInformationModel

class FlashcardLocalInformationRepositorySQLAlchemy(FlashcardLocalInformationRepository):
    def __init__(self, sessionmaker: sessionmaker):
        self.sessionmaker = sessionmaker

    def set_has_been_synced(self, id: int, has_been_synced: bool):
        with self.sessionmaker() as session:
            try:
                stmt = update(FlashcardLocalInformationModel).where(FlashcardLocalInformationModel.flashcard_id == id).values(has_been_synced = has_been_synced)
                session.execute(stmt)
                session.commit()
            except Exception:
                session.rollback()
                raise        
    
    def set_locally_deleted(self, id: int, locally_deleted: bool):
        with self.sessionmaker() as session:
            try:
                stmt = update(FlashcardLocalInformationModel).where(FlashcardLocalInformationModel.flashcard_id == id).values(locally_deleted = locally_deleted)
                session.execute(stmt)
                session.commit()
            except Exception:
                session.rollback()
                raise        
    
    def set_locally_reviewed(self, id: int, locally_reviewed: bool):
        with self.sessionmaker() as session:
            try:
                stmt = update(FlashcardLocalInformationModel).where(FlashcardLocalInformationModel.flashcard_id == id).values(locally_reviewed = locally_reviewed)
                session.execute(stmt)
                session.commit()
            except Exception:
                session.rollback()
                raise        
    
    def set_locally_updated(self, id: int, locally_updated: bool):
        with self.sessionmaker() as session:
            try:
                stmt = update(FlashcardLocalInformationModel).where(FlashcardLocalInformationModel.flashcard_id == id).values(locally_updated = locally_updated)
                session.execute(stmt)
                session.commit()
            except Exception:
                session.rollback()
                raise        
    
    def get_ids_has_been_synced(self) -> bool:
        with self.sessionmaker() as session:
            stmt = select(FlashcardLocalInformationModel.flashcard_id).where(FlashcardLocalInformationModel.has_been_synced == True)
            return session.execute(stmt).scalars().all()
    
    def get_ids_locally_deleted(self) -> bool:
        with self.sessionmaker() as session:
            stmt = select(FlashcardLocalInformationModel.flashcard_id).where(FlashcardLocalInformationModel.locally_deleted == True)
            return session.execute(stmt).scalars().all()
    
    def get_ids_locally_reviewed(self) -> bool:
        with self.sessionmaker() as session:
            stmt = select(FlashcardLocalInformationModel.flashcard_id).where(FlashcardLocalInformationModel.locally_reviewed == True)
            return session.execute(stmt).scalars().all()
    
    def get_ids_locally_updated(self) -> bool:
        with self.sessionmaker() as session:
            stmt = select(FlashcardLocalInformationModel.flashcard_id).where(FlashcardLocalInformationModel.locally_updated == True)
            return session.execute(stmt).scalars().all()
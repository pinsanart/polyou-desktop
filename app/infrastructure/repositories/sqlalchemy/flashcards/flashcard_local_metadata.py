from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List

from app.core.repositories.flashcards.flashcard_local_metadata import FlashcardLocalMetadataRepository
from app.infrastructure.db.models import FlashcardLocalMetadataModel

class FlashcardLocalMetadataRepositorySQLAlchemy(FlashcardLocalMetadataRepository):
    def __init__(self, db_session: Session):
        self.db_session = db_session
    
    def get(self, flashcard_id: int) -> FlashcardLocalMetadataModel | None:
        return self.db_session.get(FlashcardLocalMetadataModel, flashcard_id)
    
    def get_has_been_synced_ids(self) -> List[int]:
        stmt = (
            select(FlashcardLocalMetadataModel.flashcard_id)
            .where(FlashcardLocalMetadataModel.has_been_synced == True)
        )
        return self.db_session.scalars(stmt).all()
    
    def get_locally_deleted_ids(self) -> List[int]:
        stmt = (
            select(FlashcardLocalMetadataModel.flashcard_id)
            .where(FlashcardLocalMetadataModel.locally_deleted == True)
        )
        return self.db_session.scalars(stmt).all()
    
    def get_locally_deleted_and_has_been_synced_ids(self) -> List[int]:
        stmt = (
            select(FlashcardLocalMetadataModel.flashcard_id)
            .where(FlashcardLocalMetadataModel.locally_deleted == True, FlashcardLocalMetadataModel.has_been_synced == True)
        )
        return self.db_session.scalars(stmt).all()
    
    def get_locally_deleted_and_not_synced_ids(self) -> List[int]:
        stmt = (
            select(FlashcardLocalMetadataModel.flashcard_id)
            .where(FlashcardLocalMetadataModel.locally_deleted == True, FlashcardLocalMetadataModel.has_been_synced == False)
        )
        return self.db_session.scalars(stmt).all()

    def update(self, flashcard_id: int, data: dict) -> None:
        model = self.db_session.get(FlashcardLocalMetadataModel, flashcard_id)

        if not model:
            raise ValueError(f"Flashcard Local Metadata with id={flashcard_id} not found.")

        for key, value in data.items():
            if hasattr(model, key):
                setattr(model, key, value)
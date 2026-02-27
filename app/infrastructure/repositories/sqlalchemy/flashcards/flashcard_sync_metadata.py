from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List

from app.core.repositories.flashcards.flashcard_sync_metadata import FlashcardSyncMetadataRepository
from app.infrastructure.db.models import FlashcardSyncMetadataModel

class FlashcardSyncMetadataRepositorySQLAlchemy(FlashcardSyncMetadataRepository):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_one(self, id: int) -> FlashcardSyncMetadataModel | None:
        return self.db_session.get(FlashcardSyncMetadataModel, id)

    def get_all(self) -> List[FlashcardSyncMetadataModel]:
        stmt = select(FlashcardSyncMetadataModel)
        return self.db_session.scalars(stmt).all()

    def update(self, id, data: dict) -> None:
        flashcard_metadata_model = self.db_session.get(FlashcardSyncMetadataModel, id)

        if not flashcard_metadata_model:
            raise ValueError(f"Flashcard Sync Metadata with id={id} not found.")

        for key, value in data.items():
            if hasattr(flashcard_metadata_model, key):
                setattr(flashcard_metadata_model, key, value)
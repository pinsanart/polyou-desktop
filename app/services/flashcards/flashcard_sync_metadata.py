from typing import List

from app.core.services.flashcards.flashcard_sync_metadata import FlashcardSyncMetadataService
from app.infrastructure.repositories.sqlalchemy.flashcards.flashcard_sync_metadata import FlashcardSyncMetadataRepositorySQLAlchemy

from app.core.schemas.flashcards.models import FlashcardSyncMetadata
from app.core.schemas.flashcards.bases import FlashcardSyncMetadataBase

class FlashcardSyncMetadataServiceSQLAlchemy(FlashcardSyncMetadataService):
    def __init__(self, flashcard_sync_metadata_repository: FlashcardSyncMetadataRepositorySQLAlchemy):
        self.flashcard_sync_metadata_repository = flashcard_sync_metadata_repository

    def info_one(self, flashcard_id: int) -> FlashcardSyncMetadata:
        model = self.flashcard_sync_metadata_repository.get_one(flashcard_id)

        if not model:
            raise ValueError(f"Flashcard Sync Metadata id={flashcard_id} not found.")
        
        return FlashcardSyncMetadata.model_validate(model)
    
    def info_all(self) -> List[FlashcardSyncMetadata]:
        models = self.flashcard_sync_metadata_repository.get_all()
        return [FlashcardSyncMetadata.model_validate(model) for model in models]    
    
    def change(self, flashcard_id: int, new_sync_metadata: FlashcardSyncMetadataBase) -> None:
        self.flashcard_sync_metadata_repository.update(flashcard_id, **new_sync_metadata.model_dump())
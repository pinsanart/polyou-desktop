from typing import List

from app.core.services.flashcards.flashcard_local_metadata import FlaschardLocalMetadataService
from app.infrastructure.repositories.sqlalchemy.flashcards.flashcard_local_metadata import FlashcardLocalMetadataRepositorySQLAlchemy

class FlashcardLocalMetadataServiceSQLAlchemy(FlaschardLocalMetadataService):
    def __init__(self, flashcard_local_metadata_repository: FlashcardLocalMetadataRepositorySQLAlchemy):
        self.flashcard_local_metadata_repository = flashcard_local_metadata_repository
    
    def list_locally_deleted_and_has_been_synced_ids(self) -> List[int]:
        return self.flashcard_local_metadata_repository.get_locally_deleted_and_has_been_synced_ids()
    
    def list_locally_deleted_and_not_synced_ids(self) -> List[int]:
        return self.flashcard_local_metadata_repository.get_locally_deleted_and_not_synced_ids()
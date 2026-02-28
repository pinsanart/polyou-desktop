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
    
    def list_locally_deleted_ids(self) -> List[int]:
        return self.flashcard_local_metadata_repository.get_locally_deleted_ids()
    
    def list_has_been_synced_ids(self) -> List[int]:
        return self.flashcard_local_metadata_repository.get_has_been_synced_ids()
    
    def list_not_synced_ids(self) -> List[int]:
        return self.flashcard_local_metadata_repository.get_not_synced_ids()
    
    def touch_has_been_synced(self, flashcard_id: int) -> None:
        self.flashcard_local_metadata_repository.update(flashcard_id, {'has_been_synced': True})

    def touch_locally_deleted(self, flashcard_id: int) -> None:
        self.flashcard_local_metadata_repository.update(flashcard_id, {'locally_deleted': True})
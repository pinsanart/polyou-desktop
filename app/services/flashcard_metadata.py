from ..core.services.flashcard_metadata import FlashcardMetadataService
from ..infrastructure.repositories.flashcard_metadata import FlashcardMetadataRepositorySQLAlchemy

from uuid import UUID

class FlashcardMetadataServiceSQLAlchemy(FlashcardMetadataService):
    def __init__(self, flashcard_metadata_repository:FlashcardMetadataRepositorySQLAlchemy):
        self.flashcard_metadata_repository = flashcard_metadata_repository

    def info(self, public_id: UUID):
        pass

    def get_ids_locally_deleted_and_not_synced(self) -> list[int]:
        locally_deleted = set(self.flashcard_metadata_repository.get_ids_locally_deleted())
        synced = set(self.flashcard_metadata_repository.get_ids_has_been_synced())
        return list(locally_deleted - synced)
    
    def get_ids_locally_deleted_and_synced(self) -> list[int]:
        locally_deleted = set(self.flashcard_metadata_repository.get_ids_locally_deleted())
        synced = set(self.flashcard_metadata_repository.get_ids_has_been_synced())
        return list(locally_deleted.intersection(synced))
    
    def get_new_locally_created_flashcards_ids(self):
        new_locally_created_ids = self.flashcard_metadata_repository.get_ids_not_synced()
        return new_locally_created_ids

    def touch_has_been_synced(self, ids: list[int]):
        self.flashcard_metadata_repository.touch_has_been_synced(ids)
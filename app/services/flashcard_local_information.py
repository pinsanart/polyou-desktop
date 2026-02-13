from ..core.services.flashcard_local_information import FlashcardLocalInformationService
from ..infrastructure.repositories.flashcard_local_information import FlashcardLocalInformationRepositorySQLAlchemy

class FlashcardLocalInformationServiceSQLAlchemy(FlashcardLocalInformationService):
    def __init__(self, flashcard_local_information_repository:FlashcardLocalInformationRepositorySQLAlchemy):
        self.flashcard_local_information_repository = flashcard_local_information_repository

    def get_ids_locally_deleted_and_not_synced(self) -> list[int]:
        locally_deleted = set(self.flashcard_local_information_repository.get_ids_locally_deleted())
        synced = set(self.flashcard_local_information_repository.get_ids_has_been_synced())
        return list(locally_deleted - synced)
    
    def get_ids_locally_deleted_and_synced(self) -> list[int]:
        locally_deleted = set(self.flashcard_local_information_repository.get_ids_locally_deleted())
        synced = set(self.flashcard_local_information_repository.get_ids_has_been_synced())
        return list(locally_deleted.intersection(synced))
    
    def get_new_locally_created_flashcards_ids(self):
        new_locally_created_ids = self.flashcard_local_information_repository.get_ids_not_synced()
        return new_locally_created_ids
    
    def mark_as_sync_by_ids(self, ids: list[int]):
        for id in ids:
            self.flashcard_local_information_repository.set_has_been_synced(id, True)

    def touch_has_been_sync(self, ids: list[int]):
        for id in ids:
            self.flashcard_local_information_repository.set_has_been_synced(id, True)
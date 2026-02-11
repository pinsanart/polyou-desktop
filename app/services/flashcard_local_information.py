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
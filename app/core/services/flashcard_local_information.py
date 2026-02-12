from abc import ABC, abstractmethod

class FlashcardLocalInformationService(ABC):
    @abstractmethod
    def get_ids_locally_deleted_and_not_synced(self):
        pass

    @abstractmethod
    def get_ids_locally_deleted_and_synced(self):
        pass

    @abstractmethod
    def get_new_locally_created_flashcards_ids(self):
        pass
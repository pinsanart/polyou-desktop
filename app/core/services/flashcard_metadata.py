from abc import ABC, abstractmethod

class FlashcardMetadataService(ABC):
    @abstractmethod
    def info(self, public_id):
        pass

    def get_ids_locally_deleted_and_not_synced(self):
        pass

    @abstractmethod
    def get_ids_locally_deleted_and_synced(self):
        pass

    @abstractmethod
    def get_new_locally_created_flashcards_ids(self):
        pass

    @abstractmethod
    def touch_has_been_synced(self, ids):
        pass
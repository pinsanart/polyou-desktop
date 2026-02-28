from abc import ABC, abstractmethod

class FlashcardLocalMetadataRepository(ABC):
    @abstractmethod
    def get(self, flashcard_id):
        pass
    
    @abstractmethod
    def get_has_been_synced_ids(self):
        pass

    @abstractmethod
    def get_not_synced_ids(self):
        pass

    @abstractmethod
    def get_locally_deleted_ids(self):
        pass

    @abstractmethod
    def get_locally_deleted_and_has_been_synced_ids(self):
        pass

    @abstractmethod
    def get_locally_deleted_and_not_synced_ids(self):
        pass

    @abstractmethod
    def update(self, flashcard_id, data):
        pass
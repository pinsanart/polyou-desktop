from abc import ABC, abstractmethod

class FlashcardMetadataRepository(ABC):
    @abstractmethod
    def get(self, id):
        pass

    @abstractmethod
    def touch_has_been_synced(self, ids):
        pass

    @abstractmethod
    def get_ids_not_synced(self):
        pass

    @abstractmethod
    def get_ids_has_been_synced(self):
        pass

    @abstractmethod
    def get_ids_locally_deleted(self):
        pass
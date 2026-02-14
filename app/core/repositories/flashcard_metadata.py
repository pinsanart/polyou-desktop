from abc import ABC, abstractmethod

class FlashcardMetadataRepository(ABC):
    @abstractmethod
    def set_has_been_synced(self, id, has_been_synced: bool):
        pass

    @abstractmethod
    def set_locally_deleted(self, id, locally_deleted: bool):
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
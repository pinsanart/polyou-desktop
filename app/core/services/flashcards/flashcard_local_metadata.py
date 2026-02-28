from abc import ABC, abstractmethod

class FlaschardLocalMetadataService(ABC):
    @abstractmethod
    def list_locally_deleted_and_not_synced_ids(self):
        pass

    @abstractmethod
    def list_locally_deleted_and_has_been_synced_ids(self):
        pass

    @abstractmethod
    def list_locally_deleted_ids(self):
        pass

    @abstractmethod
    def list_has_been_synced_ids(self):
        pass

    @abstractmethod
    def list_not_synced_ids(self):
        pass

    @abstractmethod
    def touch_has_been_synced(self, flashcard_id):
        pass

    @abstractmethod
    def touch_locally_deleted(self, flashcard_id):
        pass
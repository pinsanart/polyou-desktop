from abc import ABC, abstractmethod

class FlaschardLocalMetadataService(ABC):
    @abstractmethod
    def list_locally_deleted_and_not_synced_ids(self):
        pass

    @abstractmethod
    def list_locally_deleted_and_has_been_synced_ids(self):
        pass
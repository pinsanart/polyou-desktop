from abc import ABC, abstractmethod

class FlashcardLocalInformationRepository(ABC):
    @abstractmethod
    def set_has_been_synced(self, id, has_been_synced: bool):
        pass

    @abstractmethod
    def set_locally_deleted(self, id, locally_deleted: bool):
        pass

    @abstractmethod
    def set_locally_updated(self, id, locally_updated: bool):
        pass

    @abstractmethod
    def set_locally_reviewed(self, id, locally_reviewed: bool):
        pass
    
    @abstractmethod
    def get_ids_has_been_synced(self):
        pass

    @abstractmethod
    def get_ids_locally_deleted(self):
        pass

    @abstractmethod
    def get_ids_locally_updated(self):
        pass

    @abstractmethod
    def get_ids_locally_reviewed(self):
        pass
from abc import ABC, abstractmethod

class FlashcardSyncMetadataRepository(ABC):
    @abstractmethod
    def get_one(self, id):
        pass
    
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def update(self, id, data):
        pass
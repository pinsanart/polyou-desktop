from abc import ABC, abstractmethod

class FlashcardSyncMetadataService(ABC):
    @abstractmethod
    def info_one(self, flashcard_id):
        pass

    @abstractmethod
    def info_all(self, flashcard_ids):
        pass

    @abstractmethod
    def change(self, flashcard_id, new_sync_metadata):
        pass
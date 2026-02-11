from abc import ABC, abstractmethod

class FlashcardSyncService(ABC):
    @abstractmethod
    def sync(self):
        pass
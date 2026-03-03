from abc import ABC, abstractmethod
from typing import List

from app.core.schemas.flashcards.models import FlashcardSyncMetadata

class FlashcardSyncMetadataService(ABC):
    @abstractmethod
    def info_one(self, flashcard_id) -> FlashcardSyncMetadata:
        pass

    @abstractmethod
    def info_all(self) -> List[FlashcardSyncMetadata]:
        pass

    @abstractmethod
    def change(self, flashcard_id, new_sync_metadata) -> None:
        pass
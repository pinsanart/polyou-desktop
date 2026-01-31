from abc import ABC, abstractmethod
from ..schemas.flashcards import FlashcardInfo
from typing import List

class FlashcardGateway(ABC):
    @abstractmethod
    def list_ids(self) -> List[int]:
        pass

    @abstractmethod
    def get_info(self, flashcards_ids: List[int]) -> List[FlashcardInfo]:
        pass
from abc import ABC, abstractmethod
from ...schemas.flashcards import FlashcardServerCreateInfo, FlashcardServerInfo
from typing import List

class FlashcardGateway(ABC):
    @abstractmethod
    def list_public_ids(self) -> List[int]:
        pass

    @abstractmethod
    def get_info(self, public_ids: List[int]) -> List[FlashcardServerInfo]:
        pass

    @abstractmethod
    def create_flashcards(self, flashcards: list[FlashcardServerCreateInfo]) -> List[int]:
        pass

    @abstractmethod
    def delete_flashcards(self, public_ids: List[int]):
        pass
from abc import ABC, abstractmethod
from uuid import UUID
from typing import List

from ....core.schemas.flashcards.bases import FlashcardBase
from ....core.schemas.flashcards.models import Flashcard

class FlashcardService(ABC):
    @abstractmethod
    def get_id_by_public_id_or_fail(self, public_id: UUID) -> int:
        pass

    @abstractmethod
    def get_ids_by_public_ids_or_fail(self, public_ids:List[UUID]) -> List[int]:
        pass

    @abstractmethod
    def get_public_id_by_id_or_fail(self, flashcard_id:int) -> UUID:
        pass

    @abstractmethod
    def get_public_ids_by_ids_or_fail(self,flashcards_ids:List[int]) -> List[UUID]:
        pass

    @abstractmethod
    def list_public_ids(self) -> List[UUID]:
        pass
    
    @abstractmethod
    def list_ids(self) -> List[int]:
        pass

    @abstractmethod
    def create_one(self, flashcard_info: FlashcardBase) -> None:
        pass

    @abstractmethod
    def create_many(self, flashcards_info: List[FlashcardBase]) -> None:
        pass
    
    @abstractmethod
    def delete_one(self, flashcard_id: int) -> None:
        pass

    @abstractmethod
    def delete_many(self, flashcards_ids: List[int]) -> None:
        pass

    @abstractmethod
    def info_one(self, flashcard_id: int) -> Flashcard:
        pass

    @abstractmethod
    def info_many(self, flashcards_ids: List[int]) -> List[Flashcard]:
        pass
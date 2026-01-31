# core/gateways/flashcard_repository.py

from abc import ABC, abstractmethod
from typing import List, Optional

from ..schemas.flashcards import (
    FlashcardInfo,
    FlashcardFSRS,
    FlashcardUpdate,
    FlashcardImage,
    FlashcardAudio,
    FlashcardContent,
    FlashcardReview,
)

class FlashcardRepository(ABC):
    @abstractmethod
    def list_ids(self) -> List[int]:
        pass

    @abstractmethod
    def get_info(self, flashcard_id: int) -> Optional[FlashcardInfo]:
        pass

    @abstractmethod
    def get_updated_at(self, flashcard_id: int) -> Optional[FlashcardUpdate]:
        pass

    @abstractmethod
    def insert(self, flashcard: FlashcardInfo):
        pass

    @abstractmethod
    def update_fsrs(self, flashcard_id: int, fsrs: FlashcardFSRS) -> None:
        pass

    @abstractmethod
    def replace_images(self, flashcard_id: int, images: List[FlashcardImage]) -> bool:
        pass

    @abstractmethod
    def replace_audios(self, flashcard_id: int, audios: List[FlashcardAudio]) -> bool:
        pass

    @abstractmethod
    def update_content(self, flashcard_id: int, content: FlashcardContent) -> bool:
        pass

    @abstractmethod
    def replace_reviews(self, flashcard_id: int, reviews: List[FlashcardReview]) -> bool:
        pass

    @abstractmethod
    def change_language(self, flashcard_id: int, language_id: int) -> bool:
        pass

    @abstractmethod
    def change_type(self, flashcard_id: int, flashcard_type_id: int) -> bool:
        pass

    @abstractmethod
    def touch(self, flashcard_id: int) -> bool:
        pass
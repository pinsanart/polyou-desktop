from abc import ABC, abstractmethod
from .flashcards_gateway import FlashcardGateway
from .flashcard_repository import FlashcardRepository

class FlashcardsSync(ABC):
    def __init__(self, flashcard_gateway: FlashcardGateway, flashcard_repository: FlashcardRepository):
        self.flashcard_gateway = flashcard_gateway
        self.flashcard_repository = flashcard_repository

    @abstractmethod
    def sync_db(self):
        pass
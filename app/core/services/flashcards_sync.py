from abc import ABC, abstractmethod

from ..http.gateways.flashcards import FlashcardGateway
from ..services.flashcard import FlashcardService

class FlashcardSyncService(ABC):
    def __init__(self, flashcard_service: FlashcardService, flashcard_gateway: FlashcardGateway):
        self.flashcard_service = flashcard_service
        self.flashcard_gateway = flashcard_gateway

    @abstractmethod
    def sync_db(self):
        pass
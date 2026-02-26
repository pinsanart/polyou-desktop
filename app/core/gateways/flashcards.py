from abc import ABC, abstractmethod
from typing import List

from app.core.schemas.flashcards.responses import (
    UserFlashcardsPublicIdsResponse,
    FlashcardCreateResponse,
    FlashcardCreateBatchResponse
)

from app.core.schemas.flashcards.requests import (
    FlashcardCreateRequest,
)

class FlashcardGateway(ABC):
    @abstractmethod
    def list_public_ids(self) -> UserFlashcardsPublicIdsResponse:
        pass

    @abstractmethod
    def create_one(self, request: FlashcardCreateRequest) -> FlashcardCreateResponse:
        pass
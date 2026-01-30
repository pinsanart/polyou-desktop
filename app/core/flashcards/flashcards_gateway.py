from abc import ABC, abstractmethod
from ..shemas.flashcards import FlashcardInfo
from typing import List

class FlashcardGateway(ABC):
    @abstractmethod
    def get_flashcards_ids(self) ->List[FlashcardInfo]:
        pass
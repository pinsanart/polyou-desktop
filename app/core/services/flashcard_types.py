from abc import ABC, abstractmethod
from ..repositories.flashcard_types import FlashcardTypesRepository

class FlashcardTypesService(ABC):
    def __init__(self, flashcard_type_repository: FlashcardTypesRepository):
        self.flashcard_type_repository = flashcard_type_repository
    
    @abstractmethod
    def get_id_by_name_or_fail(self, name):
        pass
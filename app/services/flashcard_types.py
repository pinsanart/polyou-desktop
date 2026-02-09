from ..core.services.flashcard_types import FlashcardTypesService
from ..infrastructure.repositories.flashcard_types_sqlalchemy import FlashcardTypesRepositorySQLAlchemy

class FlashcardTypesServiceSQLAlchemy(FlashcardTypesService):
    def __init__(self, flashcard_types_repository: FlashcardTypesRepositorySQLAlchemy):
        self.flashcard_type_repository = flashcard_types_repository

    def get_id_by_name_or_fail(self, name:str) -> int:
        flashcard_type = self.flashcard_type_repository.get_by_name(name)

        if not flashcard_type:
            raise f"The flashcard type {name} is not available in the database."
        
        return flashcard_type.name

        
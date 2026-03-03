from app.core.services.flashcards.flashcard_content import FlashcardContentService
from app.core.schemas.flashcards.models import FlashcardContent
from app.core.schemas.flashcards.bases import FlashcardContentBase

from app.infrastructure.repositories.sqlalchemy.flashcards.flashcard_content import FlashcardContentRepositorySQLAlchemy

class FlashcardContentServiceSQLAlchemy(FlashcardContentService):
    def __init__(self, flashcard_content_repository: FlashcardContentRepositorySQLAlchemy):
        self.flashcard_content_repository = flashcard_content_repository
    
    def info(self, flashcard_id: int) -> FlashcardContent:
        model = self.flashcard_content_repository.get(flashcard_id)

        if not model:
            raise ValueError(f"Flashcard Content id={flashcard_id} not found.")
        
        return FlashcardContent.model_validate(model)

    def change(self, flashcard_id: int, new_content: FlashcardContentBase) -> None:
        self.flashcard_content_repository.update(flashcard_id, new_content.model_dump())
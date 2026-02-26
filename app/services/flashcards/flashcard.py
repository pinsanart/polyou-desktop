from typing import List

from ...core.services.flashcards.flashcard import FlashcardService 
from ...core.schemas.flashcards.creates import FlashcardCreateInfo
from ...core.schemas.flashcards.models import Flashcard

from ...infrastructure.repositories.sqlalchemy.flashcards.flashcard import FlashcardRepositorySQLAlchemy
from ...mappers.flashcard_sqlalchemy import FlashcardSQLAlchemyMapper

class FlashcardServiceSQLAlchemy(FlashcardService):
    def __init__(self, flashcard_repository: FlashcardRepositorySQLAlchemy, flashcard_sqlalchemy_mapper: FlashcardSQLAlchemyMapper):
        self.flashcard_repository = flashcard_repository
        self.flashcard_sqlalchemy_mapper = flashcard_sqlalchemy_mapper 
    
    def get_id_by_public_id_or_fail(self, public_id: str) -> int:
        model = self.flashcard_repository.get_by_public_id(public_id)

        if not model:
            raise ValueError(f"Public ID '{public_id}' not found.")
        
        return model.flashcard_id

    def get_ids_by_public_ids_or_fail(self, public_ids:List[str]) -> List[int]:
        models = self.flashcard_repository.get_by_public_ids(public_ids)
        
        if len(models) != len(set(public_ids)):
            raise ValueError("One or more flashcards public ids were not found.")
        
        return [model.flashcard_id for model in models]
        
    def get_public_id_by_id_or_fail(self, flashcard_id:int) -> str:
        model = self.flashcard_repository.get_by_id(flashcard_id)

        if not model:
            raise ValueError(f"ID '{flashcard_id}' not found.")

        return model.public_id

    def get_public_ids_by_ids_or_fail(self,flashcards_ids:List[int]) -> List[str]:
        models = self.flashcard_repository.get_by_ids(flashcards_ids)
        
        if len(models) != len(set(flashcards_ids)):
            raise ValueError("One or more flashcards ids were not found.")

        return [model.public_id for model in models]
        
    def list_public_ids(self) -> List[str]:
        return self.flashcard_repository.list_public_ids()
    
    def list_ids(self) -> List[int]:
        return self.flashcard_repository.list_ids()

    def create_one(self, flashcard_info: FlashcardCreateInfo) -> None:
        model = self.flashcard_sqlalchemy_mapper.create_info_to_model(flashcard_info)
        self.flashcard_repository.create_one(model)

    def create_many(self, flashcards_info: List[FlashcardCreateInfo]) -> None:
        models = [self.flashcard_sqlalchemy_mapper.create_info_to_model(info) for info in flashcards_info]
        self.flashcard_repository.create_many(models)
        
    def delete_one(self, flashcard_id: int) -> None:
        self.flashcard_repository.delete_one(flashcard_id)

    def delete_many(self, flashcards_ids: List[int]) -> None:
        self.flashcard_repository.delete_many(flashcards_ids)

    def info_one(self, flashcard_id: int) -> Flashcard:
        model = self.flashcard_repository.get_by_id(flashcard_id)

        if not model:
            raise ValueError(f"Flashcard ID '{flashcard_id}' not found.")
        
        return Flashcard.model_validate(model)

    def info_many(self, flashcards_ids: List[int]) -> List[Flashcard]:
        models = self.flashcard_repository.get_by_ids(flashcards_ids)

        if len(models) != len(set(flashcards_ids)):
            raise ValueError("One or more flashcards ids were not found.")

        return [Flashcard.model_validate(model) for model in models]
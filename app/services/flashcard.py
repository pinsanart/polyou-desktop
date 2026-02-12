from typing import List
from uuid import UUID

from ..core.services.flashcard import FlashcardService
from ..core.schemas.flashcards import FlashcardLocalCreateInfo
from .language import LanguageServiceSQLAlchemy
from .flashcard_types import FlashcardTypesServiceSQLAlchemy
from ..infrastructure.repositories.flashcards_sqlalchemy import FlashcardRepositorySQLAlchemy

from ..infrastructure.db.models import (
    FlashcardModel,
    FlashcardLocalInformationModel,
    FlashcardContentModel,
    FlashcardFSRSModel,
    FlashcardImageModel,
    FlashcardAudioModel
)

class FlashcardServiceSQLAlchemy(FlashcardService):
    def __init__(self, flashcard_repository: FlashcardRepositorySQLAlchemy, language_service: LanguageServiceSQLAlchemy, flashcard_type_service:FlashcardTypesServiceSQLAlchemy):
        self.language_service = language_service
        self.flashcard_type_service = flashcard_type_service
        self.flashcard_repository = flashcard_repository

    def create_one(self, flashcard_create_info: FlashcardLocalCreateInfo) -> int:
        language_id = self.language_service.get_id_by_iso_639_1_or_fail(flashcard_create_info.language_iso_639_1)
        flashcard_type_id = self.flashcard_type_service.get_id_by_name_or_fail(flashcard_create_info.flashcard_type_name)
        
        local_information = FlashcardLocalInformationModel() 
        fsrs = FlashcardFSRSModel()

        content = FlashcardContentModel(
            front_field_content = flashcard_create_info.content.front_field,
            back_field_content= flashcard_create_info.content.back_field,
        )

        images = [
            FlashcardImageModel(
                field = image.field,
                image_url= image.image_url
            )
            for image in flashcard_create_info.images
        ]

        audios = [
            FlashcardAudioModel(
                field = audio.field,
                audio_url = audio.audio_url
            )
            for audio in flashcard_create_info.audios
        ] 

        flashcard_model = FlashcardModel(
            language_id = language_id,
            flashcard_type_id = flashcard_type_id,
            local_information = local_information,
            content = content,
            fsrs = fsrs,
            images = images,
            audios = audios
        )

        flashcard_id = self.flashcard_repository.create_one(flashcard_model)

        return flashcard_id

    def create_many(self, flashcards_create_info:List[FlashcardLocalCreateInfo]) -> List[int]:
        flashcard_models = []
        for flashcard_create_info in flashcards_create_info:
            language_id = self.language_service.get_id_by_iso_639_1_or_fail(flashcard_create_info.language_iso_639_1)
            flashcard_type_id = self.flashcard_type_service.get_id_by_name_or_fail(flashcard_create_info.flashcard_type_name)
            
            local_information = FlashcardLocalInformationModel() 
            fsrs = FlashcardFSRSModel()

            content = FlashcardContentModel(
                front_field_content = flashcard_create_info.content.front_field,
                back_field_content= flashcard_create_info.content.back_field,
            )

            images = [
                FlashcardImageModel(
                    field = image.field,
                    image_url= image.image_url
                )
                for image in flashcard_create_info.images
            ]

            audios = [
                FlashcardAudioModel(
                    field = audio.field,
                    audio_url = audio.audio_url
                )
                for audio in flashcard_create_info.audios
            ] 

            flashcard_model = FlashcardModel(
                language_id = language_id,
                flashcard_type_id = flashcard_type_id,
                local_information = local_information,
                content = content,
                fsrs = fsrs,
                images = images,
                audios = audios
            )
            
            flashcard_models.append(flashcard_model)
        
        flashcard_ids = self.flashcard_repository.create_many(flashcard_models)
        return flashcard_ids

    def delete_one(self, id):
        self.flashcard_repository.delete_one(id)

    def delete_many(self, ids):
        self.flashcard_repository.delete_many(ids)
    
    def get_public_id_by_id(self, id: int):
        flashcard = self.flashcard_repository.get_by_id(id)
        return flashcard.public_id
    
    def get_public_ids_by_ids(self, ids: List[int]) -> List[UUID]:
        public_ids = []
        for id in ids:
            flashcard = self.flashcard_repository.get_by_id(id)
            public_ids.append(flashcard.public_id)
        return public_ids
        
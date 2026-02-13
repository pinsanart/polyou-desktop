from typing import List
from uuid import UUID

from ..core.services.flashcard import FlashcardService
from ..core.schemas.flashcards import (
    FlashcardLocalCreateInfo,
    FlashcardInfo,
    FlashcardLocalInformation,
    FlashcardFSRS,
    FlashcardContent,
    FlashcardReview,
    FlashcardImage,
    FlashcardAudio,
    FlashcardInsertInfo
)
from .language import LanguageServiceSQLAlchemy
from .flashcard_types import FlashcardTypesServiceSQLAlchemy
from ..infrastructure.repositories.flashcards_sqlalchemy import FlashcardRepositorySQLAlchemy

from ..infrastructure.db.models import (
    FlashcardModel,
    FlashcardLocalInformationModel,
    FlashcardContentModel,
    FlashcardFSRSModel,
    FlashcardImageModel,
    FlashcardAudioModel,
    FlashcardReviewModel
)

class FlashcardServiceSQLAlchemy(FlashcardService):
    def __init__(self, flashcard_repository: FlashcardRepositorySQLAlchemy, language_service: LanguageServiceSQLAlchemy, flashcard_type_service:FlashcardTypesServiceSQLAlchemy):
        self.language_service = language_service
        self.flashcard_type_service = flashcard_type_service
        self.flashcard_repository = flashcard_repository

    def _create_info_to_flashcard_model(self, flashcard_create_info: FlashcardLocalCreateInfo) -> FlashcardModel:
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

        return flashcard_model

    def _flashcard_model_to_flashcard_info(self, flashcard_model:FlashcardModel) -> FlashcardInfo:
        language_iso_639_1 = self.language_service.get_iso_639_1_by_id_or_fail(flashcard_model.language_id)
        flashcard_type_name = self.flashcard_type_service.get_name_by_id_or_fail(flashcard_model.flashcard_type_id)

        content = FlashcardContent(
            front_field = flashcard_model.content.front_field_content,
            back_field  = flashcard_model.content.back_field_content
        )

        local_information = FlashcardLocalInformation(
            has_been_synced  = flashcard_model.local_information.has_been_synced,
            locally_deleted  = flashcard_model.local_information.locally_deleted,
            locally_updated  = flashcard_model.local_information.locally_updated,
            locally_reviewed = flashcard_model.local_information.locally_reviewed
        )

        fsrs = FlashcardFSRS(
            stability   =   flashcard_model.fsrs.stability,
            difficulty  =   flashcard_model.fsrs.difficulty,
            due         =   flashcard_model.fsrs.due,
            last_review =   flashcard_model.fsrs.last_review,
            state       =   flashcard_model.fsrs.state,
        )

        reviews = [
            FlashcardReview(
                reviewed_at         = review.reviewed_at,
                rating              = review.rating,
                response_time_ms    = review.response_time_ms,
                scheduled_days      = review.scheduled_days,
                actual_days         = review.actual_days,
                prev_stability      = review.prev_stability,
                prev_difficulty     = review.prev_difficulty,
                new_stability       = review.new_stability,
                new_difficulty      = review.new_difficulty,
                state_before        = review.state_before,
                state_after         = review.state_after
            )
            for review in flashcard_model.reviews
        ]

        images = [
            FlashcardImage(
                field       = image.field,
                image_url   = image.image_url
            )
            for image in flashcard_model.images
        ]

        audios = [
            FlashcardAudio(
                field= audio.field,
                audio_url= audio.audio_url
            )
            for audio in flashcard_model.audios
        ]

        flashcard_info = FlashcardInfo(
            flashcard_id = flashcard_model.flashcard_id,
            public_id = flashcard_model.public_id,

            language_iso_639_1= language_iso_639_1,
            flashcard_type_name= flashcard_type_name,

            created_at= flashcard_model.created_at,
            updated_at= flashcard_model.updated_at,

            local_information= local_information,
            fsrs= fsrs,
            content= content,
            reviews= reviews,
            images= images,
            audios= audios
        )

        return flashcard_info

    def _flashcard_insert_info_to_flashcard_model(self, flashcard_insert_info: FlashcardInsertInfo) -> FlashcardModel:
        language_id = self.language_service.get_id_by_iso_639_1_or_fail(flashcard_insert_info.language_iso_639_1)
        flashcard_type_id = self.flashcard_type_service.get_id_by_name_or_fail(flashcard_insert_info.flashcard_type_name)

        local_information = FlashcardLocalInformationModel()

        fsrs = FlashcardFSRSModel(
            stability = flashcard_insert_info.fsrs.stability,
            difficulty = flashcard_insert_info.fsrs.difficulty,
            due = flashcard_insert_info.fsrs.due,
            last_review = flashcard_insert_info.fsrs.last_review,
            state = flashcard_insert_info.fsrs.state
        )

        content = FlashcardContentModel(
            front_field_content = flashcard_insert_info.content.front_field,
            back_field_content= flashcard_insert_info.content.back_field,
        )

        images = [
            FlashcardImageModel(
                field = image.field,
                image_url= image.image_url
            )
            for image in flashcard_insert_info.images
        ]

        audios = [
            FlashcardAudioModel(
                field = audio.field,
                audio_url = audio.audio_url
            )
            for audio in flashcard_insert_info.audios
        ] 

        reviews = [
            FlashcardReviewModel(
                reviewed_at = review.reviewed_at,
                rating = review.rating,
                response_time_ms = review.response_time_ms,
                scheduled_days = review.scheduled_days,
                actual_days = review.scheduled_days,
                prev_stability = review.prev_stability,
                prev_difficulty = review.prev_difficulty,
                new_stability = review.new_stability,
                new_difficulty = review.new_difficulty,
                state_before = review.state_before,
                state_after = review.state_after
            )
            for review in flashcard_insert_info.reviews
        ]

        flashcard_model = FlashcardModel(
            public_id = flashcard_insert_info.public_id,
            
            language_id = language_id,
            flashcard_type_id = flashcard_type_id,
            
            created_at = flashcard_insert_info.created_at, 
            updated_at = flashcard_insert_info.updated_at,

            local_information = local_information,

            content = content,
            fsrs = fsrs,
            images = images,
            audios = audios,
            reviews=reviews
        )

        return flashcard_model

    def create_one(self, flashcard_create_info: FlashcardLocalCreateInfo) -> int:
        flashcard_model = self._create_info_to_flashcard_model(flashcard_create_info)
        flashcard_id = self.flashcard_repository.create_one(flashcard_model)

        return flashcard_id

    def create_many(self, flashcards_create_info:List[FlashcardLocalCreateInfo]) -> List[int]:
        flashcard_models = []
        for flashcard_create_info in flashcards_create_info:
            flashcard_model = self._create_info_to_flashcard_model(flashcard_create_info)
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
    
    def get_info_one(self, id: int) -> FlashcardInfo:
        flashcard_model = self.flashcard_repository.get_by_id(id)
        flashcard_info = self._to_flashcard_info(flashcard_model)
        return flashcard_info

    def get_info_many(self, ids: List[int]) -> List[FlashcardInfo]:
        flashcards_info = []
        for id in ids:
            flashcard_model = self.flashcard_repository.get_by_id(id)
            flashcard_info = self._to_flashcard_info(flashcard_model)
            flashcards_info.append(flashcard_info)
        return flashcards_info
    
    def list_public_ids(self) -> List[UUID]:
        ids = self.flashcard_repository.list_ids()
        
        public_ids = []
        for id in ids:
            flashcard = self.flashcard_repository.get_by_id(id)
            public_ids.append(flashcard.public_id)
        
        return public_ids
    
    def insert_one(self, flashcard_insert_info: FlashcardInsertInfo):
        flashcard_model = self._flashcard_insert_info_to_flashcard_model(flashcard_insert_info)
        self.flashcard_repository.create_one(flashcard_model)

    def insert_many(self, flashcards_insert_info: List[FlashcardInsertInfo]):
        flashcards_models = []

        for flashcard_insert_info in flashcards_insert_info:
            flashcard_model = self._flashcard_insert_info_to_flashcard_model(flashcard_insert_info)
            flashcards_models.append(flashcard_model)
        
        self.flashcard_repository.create_many(flashcards_models)

    def get_id_by_public_id(self, public_id: UUID):
        flashcard_model = self.flashcard_repository.get_by_public_id(public_id)
        return flashcard_model.flashcard_id
    
    def get_ids_by_public_ids(self, public_ids: list[UUID]):
        ids = []

        for public_id in public_ids:
            flashcard_model = self.flashcard_repository.get_by_public_id(public_id)
            ids.append(flashcard_model.flashcard_id)
        
        return ids
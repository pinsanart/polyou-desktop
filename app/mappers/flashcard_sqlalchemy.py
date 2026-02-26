from app.core.schemas.flashcards.creates import FlashcardCreateInfo

from app.infrastructure.db.models import (
    FlashcardModel,
    FlashcardSyncMetadataModel,
    FlashcardContentModel,
    FlashcardFSRSModel,
    FlashcardAudioModel,
    FlashcardImageModel,
    FlashcardReviewModel
)

from app.services.flashcards.flashcard_type import FlashcardTypeServiceSQLAlchemy
from app.services.languages.language import LanguageServiceSQLAlchemy

class FlashcardSQLAlchemyMapper:
    def __init__(self, flashcard_type_service: FlashcardTypeServiceSQLAlchemy, language_service: LanguageServiceSQLAlchemy):
        self.flashcard_type_service = flashcard_type_service
        self.language_service = language_service

    def create_info_to_model(self, create_info: FlashcardCreateInfo) -> FlashcardModel:
        model = FlashcardModel(
            public_id = create_info.public_id,
            created_at = create_info.created_at,

            flashcard_type_id = self.flashcard_type_service.get_id_by_name_or_fail(create_info.flashcard_type_name),
            language_id = self.language_service.get_id_by_iso_639_1_or_fail(create_info.language_iso_639_1)
        )

        model.sync_metadata = FlashcardSyncMetadataModel(
            **create_info.sync_metadata.model_dump()
        )

        model.content = FlashcardContentModel(
            **create_info.content.model_dump()
        )

        model.fsrs = FlashcardFSRSModel(
            **create_info.fsrs.model_dump()
        )

        if create_info.reviews:
            model.reviews = [
                FlashcardReviewModel(**review.model_dump())
                for review in create_info.reviews
            ]

        if create_info.images:
            model.images = [
                FlashcardImageModel(**image.model_dump())
                for image in create_info.images
            ]

        if create_info.audios:
            model.audios = [
                FlashcardAudioModel(**audio.model_dump())
                for audio in create_info.audios
            ]
        
        return model
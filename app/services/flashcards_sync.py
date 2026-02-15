from ..core.services.flashcards_sync import FlashcardSyncService
from ..services.flashcard import FlashcardServiceSQLAlchemy
from ..dependencies.gateways.flashcard_http import FlashcardsHTTPGateway 
from .flashcard_metadata import FlashcardMetadataServiceSQLAlchemy

from ..core.schemas.flashcards import (
    FlashcardInfo,
    FlashcardServerCreateInfo,
    FlashcardInsertInfo,
    FlashcardFSRS,
    FlashcardAudio,
    FlashcardImage,
    FlashcardReview,
    FlashcardServerInfo,
    FlashcardContent,
    FlashcardLocalMetadata,
    FlashcardServerMetadata
)

class FlashcardSyncServiceSQLAlchemyHTTP(FlashcardSyncService):
    def __init__(self, flashcard_service: FlashcardServiceSQLAlchemy, flashcard_metadata_service: FlashcardMetadataServiceSQLAlchemy, flashcard_gateway: FlashcardsHTTPGateway):
        self.flashcard_service = flashcard_service
        self.flashcard_metadata_service = flashcard_metadata_service
        self.flashcard_gateway = flashcard_gateway

    def _to_flashcard_server_create_info(self, flashcard_info: FlashcardInfo) -> FlashcardServerCreateInfo:
        create_info = FlashcardServerCreateInfo(
            public_id= flashcard_info.public_id,
            language_iso_639_1= flashcard_info.language_iso_639_1,
            flashcard_type_name= flashcard_info.flashcard_type_name,
            
            metadata = FlashcardServerMetadata(
                created_at=                 flashcard_info.metadata.created_at,
                last_review_at=             flashcard_info.metadata.last_review_at,
                last_content_updated_at=    flashcard_info.metadata.last_content_updated_at,
                last_image_updated_at=      flashcard_info.metadata.last_image_updated_at,
                last_audio_updated_at=      flashcard_info.metadata.last_audio_updated_at
            ),

            content= flashcard_info.content,
            fsrs= flashcard_info.fsrs,
            reviews= flashcard_info.reviews,
            images= flashcard_info.images,
            audios= flashcard_info.audios,
        )

        return create_info

    def delete_locally_deleted_and_not_synced_marked(self):
        locally_deleted_and_not_synced_ids = self.flashcard_metadata_service.get_ids_locally_deleted_and_not_synced()
        if len(locally_deleted_and_not_synced_ids) > 0:
            self.flashcard_service.delete_many(locally_deleted_and_not_synced_ids)
    
    def delete_locally_deleted_and_synced_marked(self):
        locally_deleted_and_synced = self.flashcard_metadata_service.get_ids_locally_deleted_and_synced()
                
        if len(locally_deleted_and_synced) > 0:
            public_ids = self.flashcard_service.get_public_ids_by_ids(locally_deleted_and_synced)
            self.flashcard_gateway.delete_many_flashcards(public_ids)

            self.flashcard_service.delete_many(locally_deleted_and_synced)

    def send_new_flashcards_to_server(self):
        new_locally_created_ids = self.flashcard_metadata_service.get_new_locally_created_flashcards_ids()

        if len(new_locally_created_ids) > 0:
            flashcards_info = self.flashcard_service.get_info_many(new_locally_created_ids)

            flashcard_server_create_info = [
                self._to_flashcard_server_create_info(flashcard_info)
                for flashcard_info in flashcards_info
            ]

            self.flashcard_gateway.create_many_flashcards(flashcard_server_create_info)
            self.flashcard_metadata_service.touch_has_been_synced(new_locally_created_ids)
    
    def _flashcard_server_info_to_flashcard_insert_info(self, flashcards_server_info: FlashcardServerInfo) -> FlashcardInsertInfo:
        return FlashcardInsertInfo (
            public_id= flashcards_server_info.public_id,
            
            language_iso_639_1= flashcards_server_info.language_iso_639_1,
            flashcard_type_name= flashcards_server_info.flashcard_type_name,
            
            metadata= FlashcardLocalMetadata(
                created_at= flashcards_server_info.metadata.created_at,
                locally_deleted= False,
                has_been_synced= True, 
                last_review_at= flashcards_server_info.metadata.last_review_at,
                last_image_updated_at= flashcards_server_info.metadata.last_image_updated_at,
                last_audio_updated_at= flashcards_server_info.metadata.last_audio_updated_at,
                last_content_updated_at= flashcards_server_info.metadata.last_content_updated_at
            ),
            
            fsrs= FlashcardFSRS(
                stability= flashcards_server_info.fsrs.stability,
                difficulty= flashcards_server_info.fsrs.difficulty,
                due= flashcards_server_info.fsrs.due,
                last_review= flashcards_server_info.fsrs.last_review,
                state= flashcards_server_info.fsrs.state
            ),
            
            content= FlashcardContent(
                front_field= flashcards_server_info.content.front_field,
                back_field= flashcards_server_info.content.back_field
            ),

            reviews= [
                FlashcardReview(
                    reviewed_at = review.reviewed_at,
                    rating = review.rating,
                    response_time_ms = review.response_time_ms,
                    scheduled_days = review.scheduled_days,
                    actual_days=  review.actual_days,
                    prev_stability = review.prev_stability,
                    prev_difficulty = review.prev_difficulty,
                    new_stability = review.new_stability,
                    new_difficulty = review.new_difficulty,
                    state_before = review.state_before,
                    state_after = review.state_after
                ) 
                for review in flashcards_server_info.reviews
            ],
            
            images= [
                FlashcardImage(
                    field=image.field,
                    image_url=image.image_url
                ) 
                for image in flashcards_server_info.images
            ],
            
            audios= [
                FlashcardAudio(
                    field=audio.field,
                    audio_url=audio.audio_url
                ) 
                for audio in flashcards_server_info.audios
            ]
        )
    
    def bring_missing_server_flashcards(self):
        local_public_ids = set(self.flashcard_service.list_public_ids())
        server_public_ids = set(self.flashcard_gateway.list_public_ids())

        missing_public_ids = list(server_public_ids - local_public_ids)

        if len(missing_public_ids) > 0:
            flashcards_info = self.flashcard_gateway.get_info(missing_public_ids)
            
            insert_infos = []
            for flashcard_info in flashcards_info:
                insert_info = self._flashcard_server_info_to_flashcard_insert_info(flashcard_info)
                insert_infos.append(insert_info)
            
            self.flashcard_service.insert_many(insert_infos)

            missing_ids = self.flashcard_service.get_ids_by_public_ids(missing_public_ids)
            self.flashcard_metadata_service.touch_has_been_synced(missing_ids)

    def update_server_flashcards_content(self):
        public_ids = [metadata.public_id for metadata in self.flashcards_metadata]

        for public_id in public_ids:
            pass
    
    def sync(self):
        self.delete_locally_deleted_and_not_synced_marked()
        self.delete_locally_deleted_and_synced_marked()

        self.send_new_flashcards_to_server()
        self.bring_missing_server_flashcards()

        self.flashcards_metadata = self.flashcard_gateway.get_all_metadata()
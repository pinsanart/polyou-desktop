from ..core.services.flashcards_sync import FlashcardSyncService
from ..services.flashcard import FlashcardServiceSQLAlchemy
from ..dependencies.gateways.flashcard_http import FlashcardsHTTPGateway 
from ..services.flashcard_local_information import FlashcardLocalInformationServiceSQLAlchemy

from ..core.schemas.flashcards import (
    FlashcardInfo,
    FlashcardServerCreateInfo
)

class FlashcardSyncServiceSQLAlchemyHTTP(FlashcardSyncService):
    def __init__(self, flashcard_service: FlashcardServiceSQLAlchemy, flashcard_local_information_service: FlashcardLocalInformationServiceSQLAlchemy, flashcard_gateway: FlashcardsHTTPGateway):
        self.flashcard_service = flashcard_service
        self.flashcard_local_information_service = flashcard_local_information_service
        self.flashcard_gateway = flashcard_gateway

    def _to_flashcard_server_create_info(self, flashcard_info: FlashcardInfo) -> FlashcardServerCreateInfo:
        create_info = FlashcardServerCreateInfo(
            public_id= flashcard_info.public_id,
            language_iso_639_1= flashcard_info.language_iso_639_1,
            flashcard_type_name= flashcard_info.flashcard_type_name,
            created_at= flashcard_info.created_at,
            updated_at= flashcard_info.updated_at,
            content= flashcard_info.content,
            fsrs= flashcard_info.fsrs,
            reviews= flashcard_info.reviews,
            images= flashcard_info.images,
            audios= flashcard_info.audios,
        )

        return create_info

    def delete_locally_deleted_and_not_synced_marked(self):
        locally_deleted_and_not_synced_ids = self.flashcard_local_information_service.get_ids_locally_deleted_and_not_synced()
        
        if len(locally_deleted_and_not_synced_ids) > 0:
            self.flashcard_service.delete_many(locally_deleted_and_not_synced_ids)
    
    def delete_locally_deleted_and_synced_marked(self):
        locally_deleted_and_synced = self.flashcard_local_information_service.get_ids_locally_deleted_and_synced()
        
        if len(locally_deleted_and_synced) > 0:
            public_ids = self.flashcard_service.get_public_ids_by_ids(locally_deleted_and_synced)
            self.flashcard_gateway.delete_many_flashcards(public_ids)

            self.flashcard_service.delete_many(locally_deleted_and_synced)

    def create_new_servers_flashcards(self):
        new_locally_created_ids = self.flashcard_local_information_service.get_new_locally_created_flashcards_ids()
        
        if len(new_locally_created_ids) > 0:
            flashcards_info = self.flashcard_service.get_info_many(new_locally_created_ids)

            flashcard_server_create_info = [
                self._to_flashcard_server_create_info(flashcard_info)
                for flashcard_info in flashcards_info
            ]

            self.flashcard_gateway.create_many_flashcards(flashcard_server_create_info)
            self.flashcard_local_information_service.mark_as_sync_by_ids(new_locally_created_ids)
        
    def sync(self):
        self.delete_locally_deleted_and_not_synced_marked()
        self.delete_locally_deleted_and_synced_marked()

        self.create_new_servers_flashcards()
from app.core.gateways.flashcard import FlashcardGateway
from app.core.services.flashcards.flashcard import FlashcardService
from app.core.services.flashcards.flashcard_local_metadata import FlaschardLocalMetadataService
from app.core.services.flashcards.flashcard_sync_metadata import FlashcardSyncMetadataService

from app.mappers.flashcard_request import FlashcardRequestMapper

from app.core.schemas.flashcards.requests import FlashcardDeleteBatchRequest, FlashcardPostBatchRequest, FlashcardGetInfosRequest
from app.core.schemas.flashcards.creates import FlashcardCreateInfo

class FlashcardSyncManager:
    def __init__(
        self, 
        flashcard_gateway:FlashcardGateway, 
        flashcard_service:FlashcardService,
        flashcard_local_metadata_service:FlaschardLocalMetadataService,
        flashcard_sync_metadata_service:FlashcardSyncMetadataService,
        flashcard_request_mapper:FlashcardRequestMapper,
    ):
        self.flashcard_gateway = flashcard_gateway
        self.flashcard_service = flashcard_service
        self.flashcard_local_metadata_service = flashcard_local_metadata_service
        self.flashcard_sync_metadata_service = flashcard_sync_metadata_service
        self.flashcard_request_mapper = flashcard_request_mapper
        
    def _delete_locally_deleted_and_not_sync(self):
        flashcards_ids = self.flashcard_local_metadata_service.list_locally_deleted_and_not_synced_ids()
        self.flashcard_service.delete_many(flashcards_ids)

    def _delete_locally_seleted_and_has_been_sync(self):
        flashcards_ids = self.flashcard_local_metadata_service.list_locally_deleted_and_has_been_synced_ids()
        
        if len(flashcards_ids) > 0:
            public_ids = self.flashcard_service.get_public_ids_by_ids_or_fail(flashcards_ids)

            self.flashcard_gateway.delete_many(
                FlashcardDeleteBatchRequest(
                    public_ids=public_ids
                )
            )

            self.flashcard_service.delete_many(flashcards_ids)

    def _delete_remote_deleted(self):
        response = self.flashcard_gateway.list_public_ids()
        
        server_public_ids = set(response.public_ids)

        local_sync_flashcard_ids = self.flashcard_local_metadata_service.list_has_been_synced_ids()
        local_sync_public_ids = set(self.flashcard_service.get_public_ids_by_ids_or_fail(local_sync_flashcard_ids))
        
        remote_deleted_public_ids = list(local_sync_public_ids - server_public_ids)
        
        flashcards_ids = self.flashcard_service.get_ids_by_public_ids_or_fail(remote_deleted_public_ids)
        self.flashcard_service.delete_many(flashcards_ids)

    def _send_new_to_server(self):
        not_synced_ids = self.flashcard_local_metadata_service.list_not_synced_ids()
                
        if len(not_synced_ids) > 0:
            self.flashcard_gateway.create_many(
                FlashcardPostBatchRequest(
                    flashcards= [
                        self.flashcard_request_mapper.model_to_request(info)
                        for info in self.flashcard_service.info_many(not_synced_ids)
                    ]
                )
            )

        for flashcard_id in not_synced_ids:
            self.flashcard_local_metadata_service.touch_has_been_synced(flashcard_id)

    def _bring_server_flashcards(self):
        response = self.flashcard_gateway.list_public_ids()
        
        server_public_ids = set(response.public_ids)
        local_public_ids = set(self.flashcard_service.list_public_ids())

        local_lack_public_ids = list(server_public_ids - local_public_ids)
        
        if len(local_lack_public_ids) > 0:
            response = self.flashcard_gateway.infos(
                FlashcardGetInfosRequest(
                    public_ids=local_lack_public_ids
                )
            )
            
            local_create_infos = [FlashcardCreateInfo.model_validate(info) for info in response.infos]
            self.flashcard_service.create_many(local_create_infos)

            flashcards_ids = self.flashcard_service.get_ids_by_public_ids_or_fail(local_lack_public_ids)
            self.flashcard_local_metadata_service.touch_has_been_synced(flashcards_ids)
        
    def sync(self):
        self._delete_locally_deleted_and_not_sync()
        self._delete_locally_seleted_and_has_been_sync()
        self._delete_remote_deleted()
        
        self._send_new_to_server()
        self._bring_server_flashcards()
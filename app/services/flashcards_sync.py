from ..core.services.flashcards_sync import FlashcardSyncService
from ..services.flashcard import FlashcardServiceSQLAlchemy
from ..dependencies.gateways.flashcard_http import FlashcardsHTTPGateway 
from ..services.flashcard_local_information import FlashcardLocalInformationServiceSQLAlchemy

class FlashcardSyncServiceSQLAlchemyHTTP(FlashcardSyncService):
    def __init__(self, flashcard_service: FlashcardServiceSQLAlchemy, flashcard_local_information_service: FlashcardLocalInformationServiceSQLAlchemy, flashcard_gateway: FlashcardsHTTPGateway):
        self.flashcard_service = flashcard_service
        self.flashcard_local_information_service = flashcard_local_information_service
        self.flashcard_gateway = flashcard_gateway

    def delete_locally_deleted_and_not_synced_marked(self):
        locally_deleted_and_not_synced_ids = self.flashcard_local_information_service.get_ids_locally_deleted_and_not_synced()
        
        if len(locally_deleted_and_not_synced_ids) > 0:
            self.flashcard_service.delete_many(locally_deleted_and_not_synced_ids)
    
    def delete_locally_deleted_and_synced_marked(self):
        locally_deleted_and_synced = self.flashcard_local_information_service.get_ids_locally_deleted_and_synced()
        public_ids = self.flashcard_service.get_public_ids_by_ids(locally_deleted_and_synced)
        
        if len(public_ids) > 0:
            self.flashcard_gateway.delete_many_flashcards(public_ids)
        
    def sync(self):
        self.delete_locally_deleted_and_not_synced_marked()
        self.delete_locally_deleted_and_synced_marked()
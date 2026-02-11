from ..core.services.flashcards_sync import FlashcardSyncService
from ..services.flashcard import FlashcardServiceSQLAlchemy
from ..dependencies.gateways.flashcard_http import FlashcardsHTTPGateway 
from ..services.flashcard_local_information import FlashcardLocalInformationServiceSQLAlchemy

class FlashcardSyncServiceSQLAlchemyHTTP(FlashcardSyncService):
    def __init__(self, flashcard_service: FlashcardServiceSQLAlchemy, flashcard_local_information_service: FlashcardLocalInformationServiceSQLAlchemy, flashcards_gateway: FlashcardsHTTPGateway):
        self.flashcard_service = flashcard_service
        self.flashcard_local_information_service = flashcard_local_information_service
        self.flashcards_gateway = flashcards_gateway

    def delete_locally_deleted_and_not_synced_marked(self):
        locally_deleted_and_not_synced_ids = self.flashcard_local_information_service.get_ids_locally_deleted_and_not_synced()
        self.flashcard_service.delete_many(locally_deleted_and_not_synced_ids)
    
    def delete_locally_deleted_and_synced_marked(self):
        locally_deleted_and_synced = self.flashcard_local_information_service.get_ids_locally_deleted_and_synced()
        
    def sync(self):
        self.delete_locally_deleted_and_not_sync_marked()
        pass
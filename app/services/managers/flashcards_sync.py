from app.core.gateways.flashcard import FlashcardGateway
from app.core.services.flashcards.flashcard import FlashcardService
from app.core.services.flashcards.flashcard_local_metadata import FlaschardLocalMetadataService

class FlashcardSyncManager:
    def __init__(
        self, 
        flashcard_gateway:FlashcardGateway, 
        flashcard_service:FlashcardService,
        flashcard_local_metadata_service: FlaschardLocalMetadataService
    ):
        self.flashcard_gateway = flashcard_gateway
        self.flashcard_service = flashcard_service
        self.flashcard_local_metadata_service = flashcard_local_metadata_service
        
    def sync(self):
        pass
    
    #DELETE LOCALY DELETED AND NOT SYNC
    #DELETE LOCALY DELETED AND SYNC
    
    #DELETE SYNCED AND NOT IN THE SERVER

    #SEND LOCAL FLASHCARDS TO SERVER
    #BRING SERVER FLASHCARDS TO LOCAL
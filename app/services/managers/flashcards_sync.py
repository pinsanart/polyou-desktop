from app.core.gateways.flashcard import FlashcardGateway
from app.core.services.flashcards.flashcard import FlashcardService

class FlashcardSyncManager:
    def __init__(self, flashcard_gateway:FlashcardGateway, flashcard_service:FlashcardService):
        self.flashcard_gateway = flashcard_gateway
        self.flashcard_service = flashcard_service

    def sync(self):
        pass
    
    #DELETE LOCALY DELETED AND NOT SYNC
    #DELETE LOCALY DELETED AND SYNC
    
    #DELETE SYNCED AND NOT IN THE SERVER

    #SEND LOCAL FLASHCARDS TO SERVER
    #BRING SERVER FLASHCARDS TO LOCAL
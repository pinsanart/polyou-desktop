from ..core.services.flashcards_sync import FlashcardSyncService
from ..services.flashcard import FlashcardServiceSQLAlchemy
from ..dependencies.gateways.flashcard_http import FlashcardsHTTPGateway 

class FlashcardSyncServiceSQLAlchemyHTTP(FlashcardSyncService):
    def __init__(self, flashcard_service: FlashcardServiceSQLAlchemy, flashcards_gateway: FlashcardsHTTPGateway):
        super().__init__(flashcard_service, flashcards_gateway)

    def sync(self):
        #DELETE MARKED FLASHCARDS LOCAL & SYNC
        #SYNC FLASHCARDS LOCAL & SERVER
        #UPDATE CONTENT, IMAGES, AUDIO
        #UPDATE REVIEWS
        pass
from ...core.flashcards.flashcards_sync import FlashcardsSync
from ...core.flashcards.flashcard_repository import FlashcardRepository
from .flashcard_http_gateway import FlashcardsHTTPGateway

class FlashcardHTTPSync(FlashcardsSync):
    def __init__(self, flashcard_gateway: FlashcardsHTTPGateway, flashcard_repository: FlashcardRepository):
        super().__init__(flashcard_gateway, flashcard_repository)
    
    def sync_db(self):
        print("Sync DB...")
        return
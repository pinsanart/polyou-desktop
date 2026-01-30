from ..config.config import settings
from ..http.requests_client import RequestsHTTPClient
from ...core.flashcards.flashcards_gateway import FlashcardGateway

class FlashcardsHTTPGateway(FlashcardGateway):
    def __init__(self, http_client: RequestsHTTPClient):
        self.http_client = http_client

    def get_flashcards_ids(self):
        return self.http_client.get('/flashcards/find')
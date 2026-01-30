from typing import List

from ..http.requests_client import RequestsHTTPClient
from ...core.flashcards.flashcards_gateway import FlashcardGateway

class FlashcardsHTTPGateway(FlashcardGateway):
    def __init__(self, http_client: RequestsHTTPClient):
        self.http_client = http_client

    def get_flashcards_ids(self):
        return self.http_client.get('/flashcards/find')
    
    def get_flashcard_info(self, flashcards_ids: List[int]):
        return self.http_client.get(
            '/flashcards/info', 
            query={"flashcards_ids": flashcards_ids}
        )
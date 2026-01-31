from typing import List

from ..http.requests_client import RequestsHTTPClient
from ...core.flashcards.flashcards_gateway import FlashcardGateway
from ...core.schemas.flashcards import FlashcardInfo

class FlashcardsHTTPGateway(FlashcardGateway):
    def __init__(self, http_client: RequestsHTTPClient):
        self.http_client = http_client

    def list_ids(self):
        return self.http_client.get('/flashcards/find')
    
    def get_info(self, flashcards_ids: List[int]) -> List[FlashcardInfo]:
        return self.http_client.get(
            '/flashcards/info', 
            query={"flashcards_ids": flashcards_ids}
        )
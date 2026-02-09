from typing import List
from uuid import UUID

from ..http.requests_client import RequestsHTTPClient
from ...core.http.gateways.flashcards import FlashcardGateway
from ...core.schemas.flashcards import FlashcardServerInfo, FlashcardServerCreateInfo

class FlashcardsHTTPGateway(FlashcardGateway):
    def __init__(self, http_client: RequestsHTTPClient):
        self.http_client = http_client

    def list_public_ids(self):
        return self.http_client.get('/flashcards/')
    
    def get_info(self, public_ids: List[UUID]) -> List[FlashcardServerInfo]:
        return self.http_client.get(
            '/flashcards/info', 
            query={"public_ids": public_ids}
        )
    
    def create_flashcards(self, flashcards: List[FlashcardServerCreateInfo]) -> list[int]:
        return self.http_client.post(
            '/flashcards/batch',
            json=[flashcard.model_dump() for flashcard in flashcards]
        )
    
    def delete_flashcards(self, public_ids: list[UUID]):
        return self.http_client.delete(
            '/flashcards/batch',
            query={"public_ids": public_ids}
        )
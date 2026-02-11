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
    
    def create_one_flashcard(self, flashcard: FlashcardServerCreateInfo):
        return self.http_client.post(
            '/flashcards/',
            json=flashcard.model_dump()
        )
    
    def create_many_flashcards(self, flashcards: List[FlashcardServerCreateInfo]):
        return self.http_client.post(
            '/flashcards/batch',
            json=[flashcard.model_dump() for flashcard in flashcards]
        )

    def delete_one_flashcard(self, public_id:UUID):
        return self.http_client.delete(
            '/flashcards/',
            query={"public_id": public_id}
        )
    
    def delete_many_flashcards(self, public_ids:List[UUID]):
        return self.http_client.delete(
            '/flashcards/batch',
            query={"public_ids": public_ids}
        )
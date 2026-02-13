from typing import List
from uuid import UUID

from ..http.requests_client import RequestsHTTPClient
from ...core.http.gateways.flashcards import FlashcardGateway
from ...core.schemas.flashcards import FlashcardServerInfo, FlashcardServerCreateInfo

class FlashcardsHTTPGateway(FlashcardGateway):
    def __init__(self, http_client: RequestsHTTPClient):
        self.http_client = http_client

    def list_public_ids(self):
        return self.http_client.get('/flashcards/')['public_ids']
    
    def get_info(self, public_ids: List[UUID]) -> List[FlashcardServerInfo]:
        return self.http_client.get(
            '/flashcards/info', 
            query={"public_ids": public_ids}
        )
    
    def get_create_one_flashcard_payload(self, flashcard: FlashcardServerCreateInfo) -> dict:
        payload = {
            "public_id": flashcard.public_id,
            "language_iso_639_1": flashcard.language_iso_639_1,
            "flashcard_type_name": flashcard.flashcard_type_name,

            "created_at": flashcard.created_at.isoformat(),
            "updated_at": flashcard.updated_at.isoformat(),

            "content": flashcard.content.model_dump(mode='json'),
            "fsrs": flashcard.fsrs.model_dump(mode='json'),
            "reviews": [review.model_dump(mode='json') for review in flashcard.reviews],
            "images": [image.model_dump(mode = 'json') for image in flashcard.images],
            "audios": [audio.model_dump(mode = 'json') for audio in flashcard.audios]
        }

        return payload

    def create_one_flashcard(self, flashcard: FlashcardServerCreateInfo):
        payload = self.get_create_one_flashcard_payload(flashcard)

        return self.http_client.post(
            '/flashcards/',
            json=payload
        )
    
    def create_many_flashcards(self, flashcards: List[FlashcardServerCreateInfo]):
        return self.http_client.post(
            '/flashcards/batch',
            json=[self.get_create_one_flashcard_payload(flashcard) for flashcard in flashcards]
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
from typing import List
from uuid import UUID

from ..http.requests_client import RequestsHTTPClient
from ...core.http.gateways.flashcards import FlashcardGateway
from ...core.schemas.flashcards import (
    FlashcardServerInfo, 
    FlashcardServerCreateInfo,
    FlashcardCreateResponse,
    FlashcardMetadataResponse,
    FlashcardDeleteResponse,
    FlashcardDeleteBatchResponse
)

class FlashcardsHTTPGateway(FlashcardGateway):
    def __init__(self, http_client: RequestsHTTPClient):
        self.http_client = http_client

    def _get_create_one_flashcard_payload(self, flashcard: FlashcardServerCreateInfo) -> dict:
        payload = {
            "public_id": flashcard.public_id,
            "language_iso_639_1": flashcard.language_iso_639_1,
            "flashcard_type_name": flashcard.flashcard_type_name,

            "metadata": {
                "created_at": flashcard.metadata.created_at.isoformat(),
                "last_review_at": (flashcard.metadata.last_review_at.isoformat() if flashcard.metadata.last_review_at else None),
                "last_content_updated_at": (flashcard.metadata.last_content_updated_at.isoformat() if flashcard.metadata.last_content_updated_at else None)
            },

            "content": flashcard.content.model_dump(mode='json'),
            "fsrs": flashcard.fsrs.model_dump(mode='json'),
            "reviews": [review.model_dump(mode='json') for review in flashcard.reviews],
            "images": [image.model_dump(mode = 'json') for image in flashcard.images],
            "audios": [audio.model_dump(mode = 'json') for audio in flashcard.audios]
        }

        return payload

    def list_public_ids(self) -> list[UUID]:
        return self.http_client.get('/flashcards/')['public_ids']
    
    def get_info(self, public_ids: List[UUID]) -> List[FlashcardServerInfo]:
        response = self.http_client.get(
            '/flashcards/info', 
            query={"public_ids": public_ids}
        )
        return [FlashcardServerInfo(**r) for r in response]
    
    def create_one_flashcard(self, flashcard: FlashcardServerCreateInfo) -> FlashcardCreateResponse:
        payload = self._get_create_one_flashcard_payload(flashcard)

        response = self.http_client.post(
            '/flashcards/',
            json=payload
        )

        return FlashcardCreateResponse(public_id=response['public_id'])
    
    def create_many_flashcards(self, flashcards: List[FlashcardServerCreateInfo]) -> List[FlashcardCreateResponse]:
        response = self.http_client.post(
            '/flashcards/batch',
            json=[self.get_create_one_flashcard_payload(flashcard) for flashcard in flashcards]
        )

        return [FlashcardCreateResponse(public_id=r.public_id) for r in response]

    def delete_one_flashcard(self, public_id:UUID) -> FlashcardDeleteResponse:
        response = self.http_client.delete(
            '/flashcards/',
            query={"public_id": public_id}
        )

        return FlashcardDeleteResponse(deleted_public_id=response['deleted_public_id'])
    
    def delete_many_flashcards(self, public_ids:List[UUID]) -> FlashcardDeleteBatchResponse:
        response = self.http_client.delete(
            '/flashcards/batch',
            query={"public_ids": public_ids}
        )

        return FlashcardDeleteBatchResponse(deleted_public_ids=response['deleted_public_ids'])
    
    def get_all_metadata(self) -> List[FlashcardMetadataResponse]:
        response = self.http_client.get(
            '/flashcards/all_metadata'
        )
        return [
            FlashcardMetadataResponse(
                public_id=r['public_id'],
                created_at=r['created_at'],
                last_review_at=r['last_review_at'],
                last_content_updated_at= r['last_content_updated_at']
            )
            for r in response
        ]
    
    def get_one_metadata(self, public_id: UUID):
        response = self.http_client.get(
            '/flashcards/metadata',
            query={"public_id": public_id}
        )

        return FlashcardMetadataResponse(
            public_id= response['public_id'],
            created_at= response['created_at'],
            last_review_at= response['last_review_at'],
            last_content_updated_at= response['last_content_updated_at']
        )
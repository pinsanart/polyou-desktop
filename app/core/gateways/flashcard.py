from abc import ABC, abstractmethod

from app.core.schemas.flashcards.requests import (
    FlashcardPostRequest,
    FlashcardPostBatchRequest,
    FlashcardDeleteRequest,
    FlashcardDeleteBatchRequest,
    FlashcardGetInfosRequest,
    FlashcardGetSyncMetadataRequest,
    FlashcardPatchSyncMetadataRequest,
    FlashcardPatchContentRequest,
    FlashcardPatchFSRSRequest,
    FlashcardPatchImagesRequest,
    FlashcardPatchReviewsRequest,
    FlashcardPatchAudiosRequest
)

from app.core.schemas.flashcards.responses import (
    FlashcardGetResponse,
    FlashcardPostResponse,
    FlashcardPostBatchResponse,
    FlashcardDeleteResponse,
    FlashcardDeleteBatchResponse,
    FlashcardGetInfosResponse,
    FlashcardGetSyncMetadataResponse,
    FlashcardPatchSyncMetadataResponse,
    FlashcardGetAllSyncMetadataResponse,
    FlashcardPatchContentResponse,
    FlashcardPatchFSRSResponse,
    FlashcardPatchImagesResponse,
    FlashcardPatchReviewsResponse,
    FlashcardPatchAudiosResponse
)

class FlashcardGateway(ABC):
    @abstractmethod
    def list_public_ids(self) -> FlashcardGetResponse:
        pass

    @abstractmethod
    def infos(self, request: FlashcardGetInfosRequest) -> FlashcardGetInfosResponse:
        pass
    
    @abstractmethod
    def get_sync_metadata(self, request: FlashcardGetSyncMetadataRequest) -> FlashcardGetSyncMetadataResponse:
        pass

    @abstractmethod
    def get_all_sync_metadata(self) -> FlashcardGetAllSyncMetadataResponse:
        pass
    
    @abstractmethod
    def create_one(self, request: FlashcardPostRequest) -> FlashcardPostResponse:
        pass

    @abstractmethod
    def create_many(self, request: FlashcardPostBatchRequest) -> FlashcardPostBatchResponse:
        pass
    
    @abstractmethod
    def change_content(self, request: FlashcardPatchContentRequest) -> FlashcardPatchContentResponse:
        pass

    @abstractmethod
    def change_fsrs(self, request: FlashcardPatchFSRSRequest) -> FlashcardPatchFSRSResponse:
        pass

    @abstractmethod
    def change_images(self, request: FlashcardPatchImagesRequest) -> FlashcardPatchImagesResponse:
        pass

    @abstractmethod
    def change_reviews(self, request: FlashcardPatchReviewsRequest) -> FlashcardPatchReviewsResponse:
        pass

    @abstractmethod
    def change_audios(self, request: FlashcardPatchAudiosRequest) -> FlashcardPatchAudiosResponse:
        pass

    @abstractmethod
    def change_sync_metadata(self, request: FlashcardPatchSyncMetadataRequest) -> FlashcardPatchSyncMetadataResponse:
        pass

    @abstractmethod
    def delete_one(self, request: FlashcardDeleteRequest) -> FlashcardDeleteResponse:
        pass

    @abstractmethod
    def delete_many(self, request: FlashcardDeleteBatchRequest) -> FlashcardDeleteBatchResponse:
        pass
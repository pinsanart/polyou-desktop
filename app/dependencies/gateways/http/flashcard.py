from typing import Type
from contextlib import contextmanager

from app.core.gateways.flashcard import FlashcardGateway
from app.core.http.http_client import HTTPClient

from app.core.exceptions.http.requests import (
    HTTPStatusError,
    RequestTimeoutError,
    ServiceUnavailableError,
)

from app.core.exceptions.gateways.flashcard import (
    FlashcardErrorCode,
    FlashcardGatewayError,
    FlashcardServiceError,
    FlashcardNotFoundError,
    FlashcardInvalidRequestError,
    FlashcardConflictError
)

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


class FlashcardGatewayHTTP(FlashcardGateway):
    def __init__(self, http_client: HTTPClient):
        self._http = http_client

    # =============================
    # HELPERS
    # =============================

    @contextmanager
    def _handle_errors(
        self,
        error_map: dict[int, tuple[Type[FlashcardGatewayError], FlashcardErrorCode]],
        default_error: Type[FlashcardGatewayError],
        default_code: FlashcardErrorCode,
    ):
        try:
            yield
        except HTTPStatusError as error:
            exception_class, error_code = error_map.get(
                error.status_code, 
                (default_error, default_code)
            )
            raise exception_class(
                message="Flashcard request failed.",
                status_code=error.status_code,
                error_code=error_code,
                details=error.detail,
            ) from error
        except (RequestTimeoutError, ServiceUnavailableError) as error:
            raise FlashcardServiceError(
                message="Flashcard service unavailable.",
                error_code=FlashcardErrorCode.SERVICE_ERROR,
        ) from error

    # ===================
    # METHODS
    # ===================

    def list_public_ids(self) -> FlashcardGetResponse:
        with self._handle_errors(
            error_map={},
            default_error=FlashcardServiceError,
            default_code=FlashcardErrorCode.SERVICE_ERROR
        ):
            response = self._http.get(
                url= '/flashcards/'
            )
            return FlashcardGetResponse(**response)
        
    def infos(self, request: FlashcardGetInfosRequest) -> FlashcardGetInfosResponse:
        with self._handle_errors(
            error_map= {
                404: (FlashcardNotFoundError, FlashcardErrorCode.NOT_FOUND), 
                422: (FlashcardInvalidRequestError, FlashcardErrorCode.INVALID_REQUEST)
            },
            default_error= FlashcardServiceError,
            default_code= FlashcardErrorCode.SERVICE_ERROR
        ):
            response = self._http.get(
                url='/flashcards/infos',
                query=request.model_dump()
            )
            return response
    
    def get_sync_metadata(self, request: FlashcardGetSyncMetadataRequest) -> FlashcardGetSyncMetadataResponse:
        with self._handle_errors(
            error_map= {
                404: (FlashcardNotFoundError, FlashcardErrorCode.NOT_FOUND), 
                422: (FlashcardInvalidRequestError, FlashcardErrorCode.INVALID_REQUEST)
            },
            default_error= FlashcardServiceError,
            default_code= FlashcardErrorCode.SERVICE_ERROR
        ):
            response = self._http.get(
                url='/flashcards/sync_metadata',
                query= request.model_dump()
            )
            return response

    def get_all_sync_metadata(self) -> FlashcardGetAllSyncMetadataResponse:
        with self._handle_errors(
            error_map= {
                404: (FlashcardNotFoundError, FlashcardErrorCode.NOT_FOUND)
            },
            default_error= FlashcardServiceError,
            default_code= FlashcardErrorCode.SERVICE_ERROR
        ):
            response = self._http.get(
                url='/flashcards/all_sync_metadata'
            )
            return response
        
    def create_one(self, request: FlashcardPostRequest) -> FlashcardPostResponse:
        with self._handle_errors(
            error_map= {
                409: (FlashcardConflictError, FlashcardErrorCode.CONFLICT),
                422: (FlashcardInvalidRequestError, FlashcardErrorCode.INVALID_REQUEST)
            },
            default_error= FlashcardServiceError,
            default_code= FlashcardErrorCode.SERVICE_ERROR
        ):
            response = self._http.post(
                url='/flashcards/',
                body=request.model_dump()
            )
            return response

    def create_many(self, request: FlashcardPostBatchRequest) -> FlashcardPostBatchResponse:
        with self._handle_errors(
            error_map= {
                409: (FlashcardConflictError, FlashcardErrorCode.CONFLICT),
                422: (FlashcardInvalidRequestError, FlashcardErrorCode.INVALID_REQUEST)
            },
            default_error= FlashcardServiceError,
            default_code= FlashcardErrorCode.SERVICE_ERROR
        ):
            response = self._http.post(
                url='/flashcards/batch',
                body=request.model_dump()
            )
            return response
        
    def change_content(self, request: FlashcardPatchContentRequest) -> FlashcardPatchContentResponse:
        with self._handle_errors(
            error_map= {
                404: (FlashcardNotFoundError, FlashcardErrorCode.NOT_FOUND),
                422: (FlashcardInvalidRequestError, FlashcardErrorCode.INVALID_REQUEST)
            },
            default_error= FlashcardServiceError,
            default_code= FlashcardErrorCode.SERVICE_ERROR
        ):
            response = self._http.patch(
                url='/flashcards/content',
                body=request.model_dump()
            )
            return response
    
    def change_fsrs(self, request: FlashcardPatchFSRSRequest) -> FlashcardPatchFSRSResponse:
        with self._handle_errors(
            error_map= {
                404: (FlashcardNotFoundError, FlashcardErrorCode.NOT_FOUND),
                422: (FlashcardInvalidRequestError, FlashcardErrorCode.INVALID_REQUEST)
            },
            default_error= FlashcardServiceError,
            default_code= FlashcardErrorCode.SERVICE_ERROR
        ):
            response = self._http.patch(
                url='/flashcards/fsrs',
                body=request.model_dump()
            )
            return response
    
    def change_images(self, request: FlashcardPatchImagesRequest) -> FlashcardPatchImagesResponse:
        with self._handle_errors(
            error_map= {
                404: (FlashcardNotFoundError, FlashcardErrorCode.NOT_FOUND),
                422: (FlashcardInvalidRequestError, FlashcardErrorCode.INVALID_REQUEST)
            },
            default_error= FlashcardServiceError,
            default_code= FlashcardErrorCode.SERVICE_ERROR
        ):
            response = self._http.patch(
                url='/flashcards/images',
                body=request.model_dump()
            )
            return response
    
    def change_reviews(self, request: FlashcardPatchReviewsRequest) -> FlashcardPatchReviewsResponse:
        with self._handle_errors(
            error_map= {
                404: (FlashcardNotFoundError, FlashcardErrorCode.NOT_FOUND),
                422: (FlashcardInvalidRequestError, FlashcardErrorCode.INVALID_REQUEST)
            },
            default_error= FlashcardServiceError,
            default_code= FlashcardErrorCode.SERVICE_ERROR
        ):
            response = self._http.patch(
                url='/flashcards/reviews',
                body=request.model_dump()
            )
            return response
    
    def change_audios(self, request: FlashcardPatchAudiosRequest) -> FlashcardPatchAudiosResponse:
        with self._handle_errors(
            error_map= {
                404: (FlashcardNotFoundError, FlashcardErrorCode.NOT_FOUND),
                422: (FlashcardInvalidRequestError, FlashcardErrorCode.INVALID_REQUEST)
            },
            default_error= FlashcardServiceError,
            default_code= FlashcardErrorCode.SERVICE_ERROR
        ):
            response = self._http.patch(
                url='/flashcards/audios',
                body=request.model_dump()
            )
            return response
    
    def change_sync_metadata(self, request: FlashcardPatchSyncMetadataRequest) -> FlashcardPatchSyncMetadataResponse:
        with self._handle_errors(
            error_map= {
                404: (FlashcardNotFoundError, FlashcardErrorCode.NOT_FOUND),
                422: (FlashcardInvalidRequestError, FlashcardErrorCode.INVALID_REQUEST)
            },
            default_error= FlashcardServiceError,
            default_code= FlashcardErrorCode.SERVICE_ERROR
        ):
            response = self._http.patch(
                url='/flashcards/sync_metadata',
                body=request.model_dump()
            )
            return response
    
    def delete_one(self, request: FlashcardDeleteRequest) -> FlashcardDeleteResponse:
        with self._handle_errors(
            error_map= {
                404: (FlashcardNotFoundError, FlashcardErrorCode.NOT_FOUND)
            },
            default_error= FlashcardServiceError,
            default_code= FlashcardErrorCode.SERVICE_ERROR
        ):
            response = self._http.delete(
                url='/flashcards/',
                query=request.model_dump()
            )
            return response

    def delete_many(self, request: FlashcardDeleteBatchRequest) -> FlashcardDeleteBatchResponse:
        with self._handle_errors(
            error_map= {
                404: (FlashcardNotFoundError, FlashcardErrorCode.NOT_FOUND)
            },
            default_error= FlashcardServiceError,
            default_code= FlashcardErrorCode.SERVICE_ERROR
        ):
            response = self._http.delete(
                url='/flashcards/batch',
                query=request.model_dump()
            )
            return response
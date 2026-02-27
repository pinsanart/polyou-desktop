from enum import StrEnum

class FlashcardErrorCode(StrEnum):
    NOT_FOUND = "FLASHCARD_01"
    INVALID_REQUEST = "FLASHCARD_02"
    CONFLICT = "FLASHCARD_03"
    SERVICE_ERROR = "FLASHCARD_999"


class FlashcardGatewayError(Exception):
    def __init__(
        self,
        message: str = "Flashcard service error",
        *,
        status_code: int | None = None,
        error_code: str | None = None,
        details: dict | None = None
    ):
        super().__init__(message)
        self.status_code = status_code
        self.error_code = error_code
        self.details = details or {}

class FlashcardInvalidRequestError(FlashcardGatewayError):
    pass

class FlashcardNotFoundError(FlashcardGatewayError):
    pass

class FlashcardConflictError(FlashcardGatewayError):
    pass

class FlashcardServiceError(FlashcardGatewayError):
    pass
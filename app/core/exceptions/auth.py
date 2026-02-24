from enum import Enum

class AuthErrorCode(str, Enum):
    INVALID_CREDENTIALS = "AUTH_001"
    REFRESH_FAILED = "AUTH_002"
    LOGOUT_FAILED = "AUTH_003"
    SERVICE_ERROR = "AUTH_999"


class AuthGatewayError(Exception):
    def __init__(
        self,
        message: str = "Authentication service error",
        *,
        status_code: int | None = None,
        error_code: str | None = None,
        details: dict | None = None
    ):
        super().__init__(message)
        self.status_code = status_code
        self.error_code = error_code
        self.details = details or {}
        

class InvalidCredentialsError(AuthGatewayError):
    pass

class RefreshTokenError(AuthGatewayError):
    pass

class LogoutError(AuthGatewayError):
    pass

class AuthenticationServiceError(AuthGatewayError):
    pass
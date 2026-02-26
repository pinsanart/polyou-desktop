from typing import Type

from app.core.gateways.auth import AuthGateway
from app.core.schemas.auth.requests import (
    TokenRequest,
    RefreshRequest,
    LogoutRequest,
)
from app.core.schemas.auth.response import (
    TokenResponse,
    RefreshResponse,
    LogoutResponse,
)

from app.core.exceptions.gateways.auth import (
    AuthErrorCode,
    AuthGatewayError,
    AuthenticationServiceError,
    InvalidCredentialsError,
    RefreshTokenError,
    LogoutError,
)

from app.core.exceptions.http.requests import (
    HTTPStatusError,
    RequestTimeoutError,
    ServiceUnavailableError,
)

from app.dependencies.http.authenticated_client import AuthenticatedHTTPClient

class AuthGatewayHTTP(AuthGateway):
    def __init__(self, authenticated_http_client: AuthenticatedHTTPClient):
        self._http = authenticated_http_client

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _map_http_error(
        self,
        error: HTTPStatusError,
        error_map: dict[int, Type[AuthGatewayError]],
        default_error: Type[AuthGatewayError],
        default_code: AuthErrorCode,
    ) -> None:

        exception_class = error_map.get(error.status_code, default_error)

        raise exception_class(
            message="Authentication request failed.",
            status_code=error.status_code,
            error_code=default_code,
            details=error.detail,
        ) from error

    # ------------------------------------------------------------------
    # Public methods
    # ------------------------------------------------------------------

    def token(self, request: TokenRequest) -> TokenResponse:
        try:
            response = self._http.post(
                url="/auth/token",
                body=request.model_dump(),
                form=True,
            )
            return TokenResponse(**response)

        except HTTPStatusError as error:
            self._map_http_error(
                error=error,
                error_map={
                    401: InvalidCredentialsError,
                },
                default_error=AuthenticationServiceError,
                default_code=AuthErrorCode.INVALID_CREDENTIALS,
            )

        except (RequestTimeoutError, ServiceUnavailableError) as error:
            raise AuthenticationServiceError(
                message="Authentication service unavailable.",
                error_code=AuthErrorCode.SERVICE_ERROR,
            ) from error

    # ------------------------------------------------------------------

    def refresh(self, request: RefreshRequest) -> RefreshResponse:
        try:
            response = self._http.post(
                url="/auth/refresh",
                body=request.model_dump(),
            )
            return RefreshResponse(**response)

        except HTTPStatusError as error:
            self._map_http_error(
                error=error,
                error_map={
                    401: RefreshTokenError,
                },
                default_error=AuthenticationServiceError,
                default_code=AuthErrorCode.INVALID_REFRESH_TOKEN,
            )

        except (RequestTimeoutError, ServiceUnavailableError) as error:
            raise AuthenticationServiceError(
                message="Authentication refresh service unavailable.",
                error_code=AuthErrorCode.SERVICE_ERROR,
            ) from error

    # ------------------------------------------------------------------

    def logout(self, request: LogoutRequest) -> LogoutResponse:
        try:
            response = self._http.post(
                url="/auth/logout",
                body=request.model_dump(),
            )
            return LogoutResponse(**response)

        except HTTPStatusError as error:
            self._map_http_error(
                error=error,
                error_map={},
                default_error=LogoutError,
                default_code=AuthErrorCode.LOGOUT_FAILED,
            )

        except (RequestTimeoutError, ServiceUnavailableError) as error:
            raise LogoutError(
                message="Logout service unavailable.",
                error_code=AuthErrorCode.LOGOUT_FAILED,
            ) from error
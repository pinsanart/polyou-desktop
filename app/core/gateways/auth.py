from abc import ABC, abstractmethod

from app.core.schemas.auth.requests import (
    TokenRequest,
    RefreshRequest,
    LogoutRequest
)

from app.core.schemas.auth.response import (
    TokenResponse,
    RefreshResponse,
    LogoutResponse
)

class AuthGateway(ABC):
    @abstractmethod
    def token(self, request: TokenRequest) -> TokenResponse:
        pass

    @abstractmethod
    def refresh(self, request: RefreshRequest) -> RefreshResponse:
        pass

    @abstractmethod
    def logout(self, request: LogoutRequest) -> LogoutResponse:
        pass
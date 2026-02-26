from app.core.gateways.auth import AuthGateway
from app.core.security.access_token_provider import AccessTokenProvider
from app.core.security.refresh_token_vault import RefreshTokenVault

from app.core.schemas.auth.requests import (
    TokenRequest,
    RefreshRequest,
    LogoutRequest 
)

class AuthSessionManager:
    def __init__(self, auth_gateway: AuthGateway, access_token_provider:AccessTokenProvider, refresh_token_vault:RefreshTokenVault):
        self._auth_gateway = auth_gateway
        self._access_token_provider = access_token_provider
        self._refresh_token_vault = refresh_token_vault
    
    def login(self, request: TokenRequest, username: str) -> None:
        response = self._auth_gateway.token(request)    
        self._refresh_token_vault.save(username, response.refresh_token)
        self._access_token_provider.set(response.access_token)

    def refresh(self, username: str) -> None:
        refresh_token = self._refresh_token_vault.get(username)
        
        #INSERT ERROR HERE

        request = RefreshRequest(refresh_token=refresh_token)
        
        response = self._auth_gateway.refresh(request)
        self._access_token_provider.set(response.access_token)

    def logout(self, username: str):
        refresh_token = self._refresh_token_vault.get(username)
        request = LogoutRequest(refresh_token = refresh_token)

        self._auth_gateway.logout(request)
        self._refresh_token_vault.delete(username)
        self._access_token_provider.clear()
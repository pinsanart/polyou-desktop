import requests

from ....core.gateways.auth import AuthGateway
from ....core.schemas.auth.requests import TokenRequest
from ....core.schemas.auth.response import TokenResponse
from ....core.exceptions.auth import (
    AuthenticationServiceError, 
    InvalidCredentialsError
)

from ....dependencies.http.requests_client import RequestsHTTPClient

class AuthGatewayHTTP(AuthGateway):
    def __init__(self, request_http_client: RequestsHTTPClient):
        self._http = request_http_client

    def token(self, request: TokenRequest) -> TokenResponse:
        try:
            response = self._http.post(
                url = '/auth/token',
                body= {
                    'username': request.email, 
                    'password': request.password
                },
                form=True
            )
        except requests.exceptions.HTTPError as error:
            status = error.response.status_code

            if status == 401:
                raise InvalidCredentialsError()
            raise AuthenticationServiceError() from error
        
        return TokenResponse(**response)
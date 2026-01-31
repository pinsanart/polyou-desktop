from ...core.auth.auth_gateway import AuthGateway
from ..http.requests_client import RequestsHTTPClient
from ...core.schemas.tokens import Token
from pydantic import EmailStr

class AuthHTTPGateway(AuthGateway):
    def __init__(self, http_client: RequestsHTTPClient):
        self.http_client = http_client
    
    def login(self, email: EmailStr, password: str) -> Token:
        return self.http_client.post(
            '/auth/token', 
            data = {"username": email, "password": password}
        )
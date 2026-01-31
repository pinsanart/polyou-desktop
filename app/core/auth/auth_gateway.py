from abc import ABC, abstractmethod
from pydantic import EmailStr
from ..schemas.tokens import Token

class AuthGateway(ABC):
    @abstractmethod
    def login(self, email: EmailStr, password: str) -> Token:
        pass
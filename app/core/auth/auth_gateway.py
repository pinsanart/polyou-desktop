from abc import ABC, abstractmethod
from pydantic import EmailStr
from ..shemas.tokens import Token

class AuthGateway(ABC):
    @abstractmethod
    def login(self, email: EmailStr, password: str) -> Token:
        pass
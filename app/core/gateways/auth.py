from abc import ABC, abstractmethod

class AuthGateway(ABC):
    @abstractmethod
    def token(self, request):
        pass
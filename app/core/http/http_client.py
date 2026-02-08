from abc import ABC, abstractmethod
from typing import Dict, Any

class HTTPClient(ABC):
    @abstractmethod
    def get(
        self, 
        url: str, 
        query: Dict[str, Any] | None = None
    ):
        pass
    
    @abstractmethod
    def post(
        self, 
        url: str, 
        data: dict, 
        body: Dict[str, Any] | None = None,
        query: Dict[str, Any] | None = None
    ):
        pass

    @abstractmethod
    def delete(
        self,
        url: str, 
        query: Dict[str, Any] | None = None
    ):
        pass

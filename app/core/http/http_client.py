from abc import ABC, abstractmethod
from typing import Dict, Any, Optional

class HTTPClient(ABC):
    @abstractmethod
    def get(
        self,
        url: str,
        query: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        **kwargs
    ) -> Any:
        pass

    @abstractmethod
    def post(
        self,
        url: str,
        body: Optional[Dict[str, Any]] = None,
        query: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        **kwargs
    ) -> Any:
        pass

    @abstractmethod
    def put(
        self,
        url: str,
        body: Optional[Dict[str, Any]] = None,
        query: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        **kwargs
    ) -> Any:
        pass

    @abstractmethod
    def patch(
        self,
        url: str,
        body: Optional[Dict[str, Any]] = None,
        query: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        **kwargs
    ) -> Any:
        pass

    @abstractmethod
    def delete(
        self,
        url: str,
        query: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        **kwargs
    ) -> Any:
        pass
from typing import Dict, Any, Optional

from app.core.http.http_client import HTTPClient
from app.core.security.access_token_provider import AccessTokenProvider

class AuthenticatedHTTPClient(HTTPClient):
    def __init__(self, http_client: HTTPClient, access_token_provider: AccessTokenProvider):
        self._http = http_client
        self._access_token_provider = access_token_provider
    
    def _inject_auth(self, headers):
        headers = headers or {}
        headers['Authorization'] = f"Bearer {self._access_token_provider.get()}"
        return headers
    
    def get(
        self,
        url: str,
        query: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        **kwargs
    ) -> Any:
        self._http.get(
            url=url,
            query=query,
            headers=self._inject_auth(headers),
            timeout=timeout,
            **kwargs
        )

    def post(
        self,
        url: str,
        body: Optional[Dict[str, Any]] = None,
        query: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        **kwargs
    ) -> Any:
        self._http.post(
            url=url,
            body=body,
            query=query,
            headers=self._inject_auth(headers),
            timeout=timeout,
            **kwargs
        )

    def put(
        self,
        url: str,
        body: Optional[Dict[str, Any]] = None,
        query: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        **kwargs
    ) -> Any:
        self._http.put(
            url=url, 
            body=body,
            query=query,
            headers=self._inject_auth(headers),
            timeout=timeout,
            **kwargs
        )

    def patch(
        self,
        url: str,
        body: Optional[Dict[str, Any]] = None,
        query: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        **kwargs
    ) -> Any:
        self._http.patch(
            url=url,
            body=body,
            query=query,
            headers=self._inject_auth(headers),
            timeout=timeout,
            **kwargs
        )

    def delete(
        self,
        url: str,
        query: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        **kwargs
    ) -> Any:
        self._http.delete(
            url=url,
            query=query,
            headers=self._inject_auth(headers),
            timeout=timeout,
            **kwargs
        )
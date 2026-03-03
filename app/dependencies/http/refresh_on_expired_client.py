from typing import Optional, Dict, Any

from app.core.http.http_client import HTTPClient
from app.dependencies.http.authenticated_client import AuthenticatedHTTPClient
from app.services.managers.auth_session import AuthSessionManager
from app.core.exceptions.http.requests import TokenExpiredError


class RefreshOnExpiredClient(HTTPClient):
    def __init__(
        self,
        authenticated_http_client: AuthenticatedHTTPClient,
        auth_session_manager: AuthSessionManager,
        username: str,
    ):
        self._authenticated_http_client = authenticated_http_client
        self._auth_session_manager = auth_session_manager
        self._username = username

    def _call(self, method, **kwargs):
        try:
            return method(**kwargs)
        except TokenExpiredError:
            self._auth_session_manager.refresh(self._username)
            return method(**kwargs)

    def get(
        self, 
        url: str,
        query: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        **kwargs):
        return self._call(
            self._authenticated_http_client.get,
            url=url, 
            query=query, 
            headers=headers, 
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
        form: bool = False,
        **kwargs
    ):
        return self._call(
            self._authenticated_http_client.post,
            url=url, 
            body=body, 
            query=query, 
            headers=headers, 
            timeout=timeout,
            form=form,
            **kwargs
        )

    def put(
        self,
        url: str,
        body: Optional[Dict[str, Any]] = None,
        query: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        form: bool = False,
        **kwargs
    ):
        return self._call(
            self._authenticated_http_client.put,
            url=url, 
            body=body, 
            query=query,
            headers=headers, 
            timeout=timeout, 
            form=form,
            **kwargs
        )

    def patch(
        self,
        url: str,
        body: Optional[Dict[str, Any]] = None,
        query: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        form: bool = False,
        **kwargs
    ):
        return self._call(
            self._authenticated_http_client.patch,
            url=url, 
            body=body, 
            query=query, 
            headers=headers, 
            timeout=timeout, 
            form=form,
            **kwargs
        )

    def delete(
        self,
        url: str,
        query: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        **kwargs
        ):
        return self._call(
            self._authenticated_http_client.delete,
            url=url, 
            query=query, 
            headers=headers, 
            timeout=timeout, 
            **kwargs
        )
import requests
from typing import Dict, Any, Optional
from ...core.http.http_client import HTTPClient

class RequestsHTTPClient(HTTPClient):
    def __init__(self, base_url: str, token: Optional[str] = None):
        self.base_url = base_url.rstrip("/")
        self.token = token

    def _build_headers(
        self,
        headers: Optional[Dict[str, str]] = None
    ) -> Dict[str, str]:
        default_headers = {}

        if self.token:
            default_headers["Authorization"] = f"Bearer {self.token}"

        if headers:
            default_headers.update(headers)

        return default_headers

    def _handle_response(self, response: requests.Response) -> Any:
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as error:
            print("Status:", error.response.status_code)
            print("Headers:", error.response.headers)
            print("Details:", error.response.text)
            raise

        if response.content:
            try:
                return response.json()
            except ValueError:
                return response.text

        return None

    def _request(
        self,
        method: str,
        url: str,
        body: Optional[Dict[str, Any]] = None,
        query: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        form: bool = False,   # ← NOVO
        **kwargs
    ) -> Any:

        full_url = f"{self.base_url}/{url.lstrip('/')}"

        request_kwargs = {
            "method": method,
            "url": full_url,
            "params": query,
            "headers": self._build_headers(headers),
            "timeout": timeout,
            **kwargs
        }

        if body:
            if form:
                request_kwargs["data"] = body
            else:
                request_kwargs["json"] = body

        response = requests.request(**request_kwargs)

        return self._handle_response(response)

    def get(
        self,
        url: str,
        query: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        **kwargs
    ) -> Any:
        return self._request(
            "GET", url,
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
    ) -> Any:
        return self._request(
            "POST",
            url,
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
        **kwargs
    ) -> Any:
        return self._request(
            "PUT", url,
            body=body,
            query=query,
            headers=headers,
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
        return self._request(
            "PATCH", url,
            body=body,
            query=query,
            headers=headers,
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
        return self._request(
            "DELETE", url,
            query=query,
            headers=headers,
            timeout=timeout,
            **kwargs
        )
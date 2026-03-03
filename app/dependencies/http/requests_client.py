import requests
from requests import Response
from typing import Dict, Any, Optional
from requests.exceptions import (
    HTTPError,
    Timeout,
    ConnectionError,
    RequestException
)
from app.core.exceptions.http.requests import (
    HTTPClientError,
    HTTPStatusError,
    RequestTimeoutError,
    ServiceUnavailableError
)

from app.core.http.http_client import HTTPClient
from app.core.config.http import http_settings

class RequestsHTTPClient(HTTPClient):
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()

    def _build_headers(self, headers: Optional[Dict[str, str]] = None) -> Dict[str, str]:
        default_headers: Dict[str, str] = {}
        if headers:
            default_headers.update(headers)
        return default_headers

    # ----------------------------------

    def _handle_response(self, response: Response) -> Any:
        try:
            response.raise_for_status()
        except HTTPError as exc:
            try:
                detail = response.json()
            except ValueError:
                detail = response.text

            raise HTTPStatusError(
                status_code=response.status_code,
                detail=detail
            ) from exc

        if not response.content:
            return None

        try:
            return response.json()
        except ValueError:
            return response.text

    # ----------------------------------

    def _request(
        self,
        method: str,
        url: str,
        body: Optional[Dict[str, Any]] = None,
        query: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        form: bool = False,
        **kwargs
    ) -> Any:

        full_url = f"{self.base_url}/{url.lstrip('/')}"

        request_kwargs = {
            "method": method,
            "url": full_url,
            "params": query,
            "headers": self._build_headers(headers),
            "timeout": timeout or http_settings.DEFAULT_TIMEOUT_SECONDS,
            **kwargs
        }

        if body is not None:
            request_kwargs["data" if form else "json"] = body

        try:
            response = self.session.request(**request_kwargs)
            return self._handle_response(response)

        except Timeout as exc:
            raise RequestTimeoutError(
                f"Request to {full_url} timed out."
            ) from exc

        except ConnectionError:
            raise ServiceUnavailableError(
                f"Could not connect to {full_url}."
            )

        except RequestException as exc:
            raise HTTPClientError(str(exc)) from exc

    def get(self, url: str, query=None, headers=None, timeout=None, **kwargs):
        return self._request("GET", url, query=query, headers=headers, timeout=timeout, **kwargs)

    def post(self, url: str, body=None, query=None, headers=None, timeout=None, form=False, **kwargs):
        return self._request("POST", url, body=body, query=query, headers=headers, timeout=timeout, form=form, **kwargs)

    def put(self, url: str, body=None, query=None, headers=None, timeout=None, form=False, **kwargs):
        return self._request("PUT", url, body=body, query=query, headers=headers, timeout=timeout, form=form, **kwargs)

    def patch(self, url: str, body=None, query=None, headers=None, timeout=None, form=False, **kwargs):
        return self._request("PATCH", url, body=body, query=query, headers=headers, timeout=timeout, form=form, **kwargs)

    def delete(self, url: str, query=None, headers=None, timeout=None, **kwargs):
        return self._request("DELETE", url, query=query, headers=headers, timeout=timeout, **kwargs)

    def close(self):
        self.session.close()
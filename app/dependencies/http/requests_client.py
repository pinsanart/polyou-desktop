import requests
from .http_client import HTTPClient

class RequestsHTTPClient(HTTPClient):
    def __init__(self, base_url: str, token: str | None = None):
        self.base_url = base_url
        self.token = token
    
    def _headers(self):
        return {"Authorization": f"Bearer {self.token}"} if self.token else {}
    
    def get(self, url:str, query = None):
        response = requests.get(
            self.base_url + url, 
            params=query, 
            headers=self._headers()
        )
        response.raise_for_status()
        return response.json()
    
    def post(self, url: str, data = None, body = None, query = None) -> requests.Response:
        response = requests.post(
            self.base_url + url,
            data=data,
            params=query,
            json=body,
            headers=self._headers()
        )
        response.raise_for_status()
        return response.json()
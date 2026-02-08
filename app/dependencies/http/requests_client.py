import requests
from ...core.http.http_client import HTTPClient

class RequestsHTTPClient(HTTPClient):
    def __init__(self, base_url: str, token: str | None = None):
        self.base_url = base_url
        self.token = token
    
    def _headers(self):
        return {"Authorization": f"Bearer {self.token}"} if self.token else {}
    
    def get(self, url:str, query = None):
        try:
            response = requests.get(
                self.base_url + url, 
                params=query, 
                headers=self._headers()
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as error:
            print("Status: ", error.response.status_code)
            print("Headers: ", error.response.headers)
            print("Details: ", error.response.text)
            raise
    
    def post(self, url: str, data = None, json = None, query = None) -> requests.Response:
        try:
            response = requests.post(
                self.base_url + url,
                data=data,
                params=query,
                json=json,
                headers=self._headers()
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as error:
            print("Status: ", error.response.status_code)
            print("Headers: ", error.response.headers)
            print("Details: ", error.response.text)
            raise

    def delete(self, url: str, query=None) -> requests.Response:
        try:
            response = requests.delete(
                self.base_url + url,
                params=query,
                headers=self._headers()
            )
            response.raise_for_status()

            if response.content:
                return response.json()
            return None

        except requests.exceptions.HTTPError as error:
            print("Status: ", error.response.status_code)
            print("Headers: ", error.response.headers)
            print("Details: ", error.response.text)
            raise

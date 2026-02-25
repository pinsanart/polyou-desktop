class AccessTokenProvider:
    def __init__(self):
        self._access_token: str | None = None
    
    def set(self, token:str) -> None:
        self._access_token = token
    
    def get(self) -> str | None:
        return self._access_token

    def clear(self) -> None:
        self._access_token = None
    
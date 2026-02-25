class HTTPClientError(Exception):
    pass

class ServiceUnavailableError(HTTPClientError):
    pass

class RequestTimeoutError(HTTPClientError):
    pass

class HTTPStatusError(HTTPClientError):
    def __init__(self, status_code: int, detail: str):
        self.status_code = status_code
        self.detail = detail
        super().__init__(f"HTTP {status_code}: {detail}")

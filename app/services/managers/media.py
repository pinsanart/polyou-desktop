import base64
from uuid import uuid4
import mimetypes
import io

from app.dependencies.storages.local import LocalStorage

class MediaManager:
    def __init__(self, local_storage: LocalStorage):
        self._local_storage = local_storage
    
    def save(self, base64_data: str, mime_type: str) -> str:
        if not base64_data:
            raise ValueError("base64_data is empty.")

        if "," in base64_data:
            header, base64_data = base64_data.split(",", 1)

        missing_padding = len(base64_data) % 4
        if missing_padding:
            base64_data += "=" * (4 - missing_padding)

        raw = base64.b64decode(base64_data)

        stream = io.BytesIO(raw)

        ext = mimetypes.guess_extension(mime_type) or '.bin'
        filename = f'{uuid4()}{ext}'

        self._local_storage.save(filename, stream)

        return filename

    def get(self, filename:str) -> str:
        stream = self._local_storage.get(filename)

        raw = stream.read()
        b64 = base64.b64encode(raw).decode()

        mime_type, _ = mimetypes.guess_type(filename)
        mime_type = mime_type or "application/octet-stream"

        return f"data:{mime_type};base64,{b64}"

    def delete(self, filename: str) -> bool:
        try:
            self._local_storage.delete(filename)
            return True
        except:
            return False
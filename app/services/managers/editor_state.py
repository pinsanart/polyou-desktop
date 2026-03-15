from app.dependencies.storages.local import LocalStorage
import json
from io import BytesIO

class EditorStateManager:
    def __init__(self, local_storage:LocalStorage, filename: str):
        self._local_storage = local_storage
        self._filename = filename

    def save(self, json_data: dict):
        json_bytes = json.dumps(json_data, indent=4).encode("utf-8")
        stream = BytesIO(json_bytes)
        self._local_storage.save(self._filename, stream)

    def get(self) -> dict:
        if not self._local_storage.exists(self._filename):
            return {}

        with self._local_storage.get(self._filename) as f:
            return json.load(f)
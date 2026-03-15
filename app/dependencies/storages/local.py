from typing import BinaryIO, IO
from pathlib import Path
import shutil

from app.core.storages.file import FileStorage

class LocalStorage(FileStorage):
    def __init__(self, path:Path):
        self._path = path
        self._path.mkdir(parents=True, exist_ok=True)

    def _get_file_path(self, filename:str):
        return self._path / filename

    def save(self, filename: str, file_stream: BinaryIO) -> None:
        file_path = self._get_file_path(filename)
        
        with open(file_path, 'wb') as f:
            shutil.copyfileobj(file_stream, f)

    def get(self, filename:str) -> IO[bytes]:
        file_path = self._get_file_path(filename)

        if not file_path.exists():
            raise FileNotFoundError(f"{filename} not found.")
        
        return open(file_path, 'rb')

    def delete(self, filename:str) -> None:
        file_path = self._get_file_path(filename)
        
        if file_path.exists():
            file_path.unlink()

    def exists(self, filename:str) -> bool:
        file_path = self._get_file_path(filename)
        return file_path.exists()
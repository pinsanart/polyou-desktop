from abc import ABC, abstractmethod
from typing import BinaryIO

class FileStorage(ABC):
    @abstractmethod
    def save(self, filename:str, file_stream:BinaryIO):
        pass

    @abstractmethod
    def delete(self, filename:str):
        pass

    @abstractmethod
    def get(self, filename:str):
        pass
    
    @abstractmethod
    def exists(self, filename:str) -> bool:
        pass
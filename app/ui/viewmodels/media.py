from PySide6.QtCore import Slot, QObject

from app.services.managers.media import MediaManager

class MediaViewModel(QObject):
    def __init__(self, media_manager: MediaManager):
        super().__init__()
        self._media_manager = media_manager

    @Slot(str, str, result=str)
    def save(self, base64_data: str, mime_type: str) -> str:
        filename = self._media_manager.save(base64_data, mime_type)
        return filename
    
    @Slot(str, result=str)
    def get(self, filename:str) -> str:
        return self._media_manager.get(filename)
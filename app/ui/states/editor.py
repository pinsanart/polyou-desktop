from PySide6.QtCore import QObject, Slot

from app.services.managers.editor_state import EditorStateManager

class EditorState(QObject):
    def __init__(self, editor_state_manager: EditorStateManager):
        super().__init__()
        self._editor_state_manager = editor_state_manager
    
    @Slot("QVariantMap")
    def saveFlashcards(self, data):
        self._editor_state_manager.save(data)
    
    @Slot(result="QVariantMap")
    def getFlashcards(self):
        return self._editor_state_manager.get()
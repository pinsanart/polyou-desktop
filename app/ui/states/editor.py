from PySide6.QtCore import QObject, Slot

class EditorState(QObject):
    def __init__(self):
        super().__init__()
    
    @Slot("QVariantMap")
    def saveFlashcards(self, data):
        print(data)
    
    @Slot(result="QVariantMap")
    def getFlashcards(self):
        data = {
            'flashcards': [
                {
                    'frontHTML': 'test',
                    'backHTML': 'sucess',
                    'audiosFilenames': [],
                    'imagesFilenames': []
                }
            ]
        }

        return data
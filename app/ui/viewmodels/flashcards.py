from PySide6.QtCore import QObject, Slot

class FlashcardViewModel(QObject):
    def __init__(self):
        super().__init__()

    @Slot("QVariantMap")
    def create_one(self, data):
        print(data)

    @Slot("QVariantMap")
    def create_many(self, data):
        print(data)
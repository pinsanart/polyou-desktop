from abc import ABC, abstractmethod

class FlashcardContentService(ABC):
    @abstractmethod
    def info(self, flashcard_id):
        pass

    @abstractmethod
    def change(self, flashcard_id, new_content):
        pass
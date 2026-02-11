from abc import ABC, abstractmethod

class FlashcardGateway(ABC):
    @abstractmethod
    def list_public_ids(self):
        pass

    @abstractmethod
    def get_info(self, public_ids):
        pass
    
    @abstractmethod
    def create_one_flashcard(self, flashcard):
        pass

    @abstractmethod
    def create_many_flashcards(self, flashcards):
        pass

    @abstractmethod
    def delete_one_flashcard(self, public_id):
        pass

    @abstractmethod
    def delete_many_flashcards(self, public_ids):
        pass
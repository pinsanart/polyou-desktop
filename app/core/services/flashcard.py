from abc import ABC, abstractmethod

class FlashcardService(ABC):
    @abstractmethod
    def create_one(self, flashcard_create_info):
        pass

    @abstractmethod
    def create_many(self, flashcards_create_info):
        pass

    @abstractmethod
    def delete_one(self, id):
        pass

    @abstractmethod
    def delete_many(self, ids):
        pass

    @abstractmethod
    def get_public_id_by_id(self, id):
        pass
    
    @abstractmethod
    def get_public_ids_by_ids(self):
        pass
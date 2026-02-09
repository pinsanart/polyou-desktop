from abc import ABC, abstractmethod

from ..repositories.languages import LanguagesRepository

class LanguageService(ABC):
    def __init__(self, language_repository: LanguagesRepository):
        self.language_repositoy = language_repository

    @abstractmethod
    def get_id_by_iso_639_1_or_fail(self, iso_639_1):
        pass
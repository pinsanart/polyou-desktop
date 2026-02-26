from typing import List

from ...core.services.languages.language import LanguageService
from ...infrastructure.repositories.sqlalchemy.languages.language import LanguageRepositorySQLAlchemy

class LanguageServiceSQLAlchemy(LanguageService):
    def __init__(self, language_repository: LanguageRepositorySQLAlchemy):
        self.language_repository = language_repository
    
    def get_available_languages_iso_639_1(self) -> List[str]:
        ids = self.language_repository.list_ids()
        languages_iso_639_1 = []
        for id in ids:
            model = self.language_repository.get_by_id(id)
            languages_iso_639_1.append(model.iso_639_1)
        return languages_iso_639_1

    def get_id_by_iso_639_1_or_fail(self, iso_639_1: str) -> int:
        language_model = self.language_repository.get_by_iso_639_1(iso_639_1)
        if not language_model:
            raise ValueError(f"Language with 'ISO 639-1'={iso_639_1} not found.")
        return language_model.language_id

    def get_iso_639_1_by_id_or_fail(self, id: int) -> str:
        language_model = self.language_repository.get_by_id(id)
        if not language_model:
            raise ValueError(f"Language with id={id} not found.")
        return language_model.iso_639_1
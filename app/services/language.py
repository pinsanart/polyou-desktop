from ..core.services.languages import LanguageService
from ..infrastructure.repositories.languages_sqlalchemy import LanguageRepositorySQLAlchemy

class LanguageServiceSQLAlchemy(LanguageService):
    def __init__(self, language_repository: LanguageRepositorySQLAlchemy):
        super().__init__(language_repository)
    
    def get_id_by_iso_639_1_or_fail(self, iso_639_1:str) -> int:
        language = self.language_repositoy.get_by_iso_639_1(iso_639_1)
        if language is None:
            raise f"The language ISO 639-1 '{iso_639_1}' is not available in the local database."
        return language.language_id
    
    def get_iso_639_1_by_id_or_fail(self, id: int):
        language = self.language_repositoy.get_by_id(id)
        if not language:
            f"The language id '{id}' is not available in the local database."
        return language.iso_639_1
        
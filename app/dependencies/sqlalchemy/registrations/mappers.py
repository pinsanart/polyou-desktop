from ..factory import AppFactory

from ....mappers.flashcard_sqlalchemy import FlashcardSQLAlchemyMapper

from ....services.flashcards.flashcard_type import FlashcardTypeServiceSQLAlchemy
from ....services.languages.language import LanguageServiceSQLAlchemy

@AppFactory.register(FlashcardSQLAlchemyMapper)
def build_flashcard_request_mapper(factory: AppFactory):
    return FlashcardSQLAlchemyMapper(
        flashcard_type_service= factory.create(FlashcardTypeServiceSQLAlchemy),
        language_service= factory.create(LanguageServiceSQLAlchemy)
    )
from app.dependencies.sqlalchemy.factory            import AppFactory

from app.services.flashcards.flashcard_type         import FlashcardTypeServiceSQLAlchemy
from app.services.languages.language                import LanguageServiceSQLAlchemy

from app.mappers.flashcard_sqlalchemy               import FlashcardSQLAlchemyMapper

@AppFactory.register(FlashcardSQLAlchemyMapper)
def build_flashcard_request_mapper(factory: AppFactory):
    return FlashcardSQLAlchemyMapper(
        flashcard_type_service= factory.create(FlashcardTypeServiceSQLAlchemy),
        language_service= factory.create(LanguageServiceSQLAlchemy)
    )
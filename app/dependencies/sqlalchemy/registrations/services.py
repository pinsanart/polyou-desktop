from app.dependencies.sqlalchemy.factory                                                import AppFactory

from app.infrastructure.repositories.sqlalchemy.flashcards.flashcard                    import FlashcardRepositorySQLAlchemy
from app.infrastructure.repositories.sqlalchemy.flashcards.flashcard_type               import FlashcardTypeRepositorySQLAlchemy
from app.infrastructure.repositories.sqlalchemy.flashcards.flashcard_local_metadata     import FlashcardLocalMetadataRepositorySQLAlchemy
from app.infrastructure.repositories.sqlalchemy.languages.language                      import LanguageRepositorySQLAlchemy
from app.infrastructure.repositories.sqlalchemy.flashcards.flashcard_sync_metadata      import FlashcardSyncMetadataRepositorySQLAlchemy
from app.infrastructure.repositories.sqlalchemy.flashcards.flashcard_content            import FlashcardContentRepositorySQLAlchemy

from app.mappers.flashcard_sqlalchemy                                                   import FlashcardSQLAlchemyMapper

from app.services.flashcards.flashcard                                                  import FlashcardServiceSQLAlchemy
from app.services.languages.language                                                    import LanguageServiceSQLAlchemy
from app.services.flashcards.flashcard_type                                             import FlashcardTypeServiceSQLAlchemy
from app.services.flashcards.flashcard_local_metadata                                   import FlashcardLocalMetadataServiceSQLAlchemy
from app.services.flashcards.flashcard_sync_metadata                                    import FlashcardSyncMetadataServiceSQLAlchemy
from app.services.flashcards.flashcard_content                                          import FlashcardContentServiceSQLAlchemy

@AppFactory.register(FlashcardServiceSQLAlchemy)
def build_flashcard_service(factory: AppFactory):
    return FlashcardServiceSQLAlchemy(
        flashcard_repository= factory.create(FlashcardRepositorySQLAlchemy),
        flashcard_sqlalchemy_mapper= factory.create(FlashcardSQLAlchemyMapper)
    )

@AppFactory.register(FlashcardTypeServiceSQLAlchemy)
def build_flashcard_type_service(factory: AppFactory):
    return FlashcardTypeServiceSQLAlchemy(
        flashcard_type_repository= factory.create(FlashcardTypeRepositorySQLAlchemy)
    )

@AppFactory.register(LanguageServiceSQLAlchemy)
def build_language_service(factory: AppFactory):
    return LanguageServiceSQLAlchemy(
        language_repository= factory.create(LanguageRepositorySQLAlchemy)
    )

@AppFactory.register(FlashcardLocalMetadataServiceSQLAlchemy)
def build_flashcard_local_metadata_service(factory: AppFactory):
    return FlashcardLocalMetadataServiceSQLAlchemy(
        flashcard_local_metadata_repository= factory.create(FlashcardLocalMetadataRepositorySQLAlchemy)
    )

@AppFactory.register(FlashcardSyncMetadataServiceSQLAlchemy)
def build_flashcard_sync_metadata_service(factory: AppFactory):
    return FlashcardSyncMetadataServiceSQLAlchemy(
        flashcard_sync_metadata_repository= factory.create(FlashcardSyncMetadataRepositorySQLAlchemy)
    )

@AppFactory.register(FlashcardContentServiceSQLAlchemy)
def build_flashcard_content_service(factory: AppFactory):
    return FlashcardContentServiceSQLAlchemy(
        flashcard_content_repository= factory.create(FlashcardContentRepositorySQLAlchemy)
    )
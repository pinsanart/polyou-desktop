from app.dependencies.sqlalchemy.factory                                              import AppFactory

from app.infrastructure.repositories.sqlalchemy.flashcards.flashcard_content          import FlashcardContentRepositorySQLAlchemy
from app.infrastructure.repositories.sqlalchemy.flashcards.flashcard_fsrs             import FlashcardFSRSRepositorySQLAlchemy
from app.infrastructure.repositories.sqlalchemy.flashcards.flashcard_image            import FlashcardImageRepositorySQLAlchemy
from app.infrastructure.repositories.sqlalchemy.flashcards.flashcard                  import FlashcardRepositorySQLAlchemy
from app.infrastructure.repositories.sqlalchemy.flashcards.flashcard_type             import FlashcardTypeRepositorySQLAlchemy
from app.infrastructure.repositories.sqlalchemy.flashcards.flashcard_sync_metadata    import FlashcardSyncMetadataRepositorySQLAlchemy
from app.infrastructure.repositories.sqlalchemy.flashcards.flashcard_review           import FlashcardReviewRepositorySQLAlchemy
from app.infrastructure.repositories.sqlalchemy.flashcards.flashcard_audio            import FlashcardAudioRepositorySQLAlchemy
from app.infrastructure.repositories.sqlalchemy.flashcards.flashcard_local_metadata   import FlashcardLocalMetadataRepositorySQLAlchemy
from app.infrastructure.repositories.sqlalchemy.languages.language                    import LanguageRepositorySQLAlchemy

@AppFactory.register(FlashcardContentRepositorySQLAlchemy)
def build_flashcard_content_repository(factory: AppFactory):
    return FlashcardContentRepositorySQLAlchemy(factory.container.db)

@AppFactory.register(FlashcardAudioRepositorySQLAlchemy)
def build_flashcard_audio_repository(factory: AppFactory):
    return FlashcardAudioRepositorySQLAlchemy(factory.container.db)

@AppFactory.register(FlashcardFSRSRepositorySQLAlchemy)
def build_flashcard_fsrs_repository(factory: AppFactory):
    return FlashcardFSRSRepositorySQLAlchemy(factory.container.db)

@AppFactory.register(FlashcardImageRepositorySQLAlchemy)
def build_flashcard_image_repository(factory: AppFactory):
    return FlashcardImageRepositorySQLAlchemy(factory.container.db)

@AppFactory.register(FlashcardReviewRepositorySQLAlchemy)
def build_flashcard_review_repository(factory: AppFactory):
    return FlashcardReviewRepositorySQLAlchemy(factory.container.db)

@AppFactory.register(FlashcardRepositorySQLAlchemy)
def build_flashcard_repository(factory: AppFactory):
    return FlashcardRepositorySQLAlchemy(factory.container.db)

@AppFactory.register(FlashcardTypeRepositorySQLAlchemy)
def build_flashcard_type_repository(factory: AppFactory):
    return FlashcardTypeRepositorySQLAlchemy(factory.container.db)

@AppFactory.register(FlashcardSyncMetadataRepositorySQLAlchemy)
def build_flashcard_sync_metadata_repository(factory: AppFactory):
    return FlashcardSyncMetadataRepositorySQLAlchemy(factory.container.db)

@AppFactory.register(LanguageRepositorySQLAlchemy)
def build_language_repository(factory: AppFactory):
    return LanguageRepositorySQLAlchemy(factory.container.db)

@AppFactory.register(FlashcardLocalMetadataRepositorySQLAlchemy)
def build_flashcard_local_metadata_repository(factory: AppFactory):
    return FlashcardLocalMetadataRepositorySQLAlchemy(factory.container.db)
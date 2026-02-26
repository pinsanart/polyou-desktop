from pydantic import ConfigDict

from app.core.schemas.flashcards.bases import (
    FlashcardBase
)

from app.core.schemas.languages.bases import ISOCode

class FlashcardCreateInfo(FlashcardBase):
    model_config = ConfigDict(from_attributes=True)

    flashcard_type_name: str
    language_iso_639_1: ISOCode
from pydantic import BaseModel, ConfigDict


from .bases import (
    FlashcardBase
)

from ..languages.bases import ISOCode

class FlashcardCreateInfo(FlashcardBase):
    model_config = ConfigDict(from_attributes=True)

    flashcard_type_name: str
    language_iso_639_1: ISOCode
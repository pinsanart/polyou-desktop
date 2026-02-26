from pydantic import BaseModel
from typing import List

from app.core.schemas.languages.bases import ISOCode

class AvailableLanguageResponse(BaseModel):
    available_languages: List[ISOCode]
from pydantic import BaseModel
from datetime import datetime
from typing import List
from enum import Enum

class FieldsEnum(str, Enum):
    front = "front"
    back = "back"

class StateEnum(int, Enum):
    LEARNING = 1
    REVIEW = 2
    RELEARNING = 3

class RatingEnum(int, Enum):
    AGAIN = 1
    HARD = 2
    GOOD = 3

class FlashcardContent(BaseModel):
    front_field: str
    back_field: str | None = None

class FlashcardFSRS(BaseModel):
    stability: float
    difficult: float
    due: datetime
    last_review: datetime
    state: StateEnum
    
class FlashcardReview(BaseModel):
    reviewd_at: datetime
    rating: RatingEnum
    response_time_ms: int
    
    scheduled_days: int
    actual_days: int

    prev_stability: float
    prev_difficulty: float
    new_stability: float
    new_difficulty: float

    state_before: StateEnum
    state_after: StateEnum

class FlashcardImage(BaseModel):
    field: FieldsEnum
    image_url: str

class FlashcardAudio(BaseModel):
    field: FieldsEnum
    audio_url: str

class FlashcardInfo(BaseModel):
    flashcard_id: int

    language_id: int
    flashcard_type_id: int
    created_at: datetime
    updated_at: datetime

    content: FlashcardContent
    fsrs: FlashcardFSRS

    reviews: List[FlashcardReview] | None
    images: List[FlashcardImage] | None
    audios: List[FlashcardAudio] | None
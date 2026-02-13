from pydantic import BaseModel, Field
from enum import Enum
from typing import List
from datetime import datetime
from uuid import UUID

# =============================
# ENUMS
# =============================

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

# =============================
# SCHEMAS
# =============================

class FlashcardContent(BaseModel):
    front_field: str
    back_field: str | None = None

class FlashcardImage(BaseModel):
    field: FieldsEnum
    image_url: str

class FlashcardAudio(BaseModel):
    field: FieldsEnum
    audio_url: str

class FlashcardReview(BaseModel):
    reviewed_at: datetime
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

class FlashcardFSRS(BaseModel):
    stability: float = 0.1
    difficulty: float = 5.0
    due: datetime = Field(default_factory=datetime.today)
    last_review: datetime | None = None
    state: StateEnum = StateEnum.LEARNING

class FlashcardServerInfo(BaseModel):
    public_id: str

    language_iso_639_1: str
    flashcard_type: str
    created_at: datetime
    updated_at: datetime

    content: FlashcardContent
    fsrs: FlashcardFSRS

    reviews: List[FlashcardReview] | None
    images: List[FlashcardImage] | None
    audios: List[FlashcardAudio] | None

class FlashcardServerCreateInfo(BaseModel):
    public_id: str

    language_iso_639_1: str
    flashcard_type_name: str

    created_at: datetime
    updated_at: datetime

    content: FlashcardContent
    fsrs: FlashcardFSRS
    reviews: List[FlashcardReview] | None = None
    images: List[FlashcardImage] | None = None
    audios: List[FlashcardAudio] | None = None

class FlashcardLocalCreateInfo(BaseModel):
    language_iso_639_1: str
    flashcard_type_name:str

    content: FlashcardContent
    images: list[FlashcardImage] | None = None
    audios: list[FlashcardAudio] | None = None

class FlashcardLocalInformation(BaseModel):
    has_been_synced: bool = False
    locally_deleted: bool = False
    locally_updated: bool = False
    locally_reviewed: bool = False

class FlashcardInfo(BaseModel):
    flashcard_id: int
    public_id: str
    
    language_iso_639_1: str
    flashcard_type_name:str
    created_at: datetime
    updated_at: datetime

    local_information: FlashcardLocalInformation
    fsrs: FlashcardFSRS
    
    content: FlashcardContent

    reviews: list[FlashcardReview] | None = None
    images: list[FlashcardImage] | None = None
    audios: list[FlashcardAudio] | None = None

class FlashcardInsertInfo(BaseModel):
    public_id: str

    language_iso_639_1: str
    flashcard_type_name:str
    created_at: datetime
    updated_at: datetime

    fsrs: FlashcardFSRS

    content: FlashcardContent

    reviews: list[FlashcardReview] | None = None
    images: list[FlashcardImage] | None = None
    audios: list[FlashcardAudio] | None = None
from pydantic import BaseModel
from typing import List

from .bases import (
    FlashcardBase,
    FlashcardContentBase,
    FlashcardFSRSBase,
    FlashcardImageBase,
    FlashcardTypeBase,
    FlashcardReviewBase,
    FlashcardAudioBase,
    FlashcardSyncMetadataBase
)

from ..languages.bases import ISOCode

class FlashcardPostRequest(FlashcardBase):
    flashcard_type_name: str
    language_iso_639_1: ISOCode

class FlashcardPostBatchRequest(BaseModel):
    flashcards: List[FlashcardPostRequest]

class FlashcardGetInfosRequest(BaseModel):
    public_ids: List[str]

class FlashcardGetSyncMetadataRequest(BaseModel):
    public_id: str

class FlashcardPatchContentRequest(BaseModel):
    public_id: str
    new_content: FlashcardContentBase

class FlashcardPatchFSRSRequest(BaseModel):
    public_id: str
    new_fsrs: FlashcardFSRSBase

class FlashcardPatchImagesRequest(BaseModel):
    public_id: str
    new_images: List[FlashcardImageBase]

class FlashcardPatchReviewsRequest(BaseModel):
    public_id: str
    new_reviews: List[FlashcardReviewBase]

class FlashcardPatchAudiosRequest(BaseModel):
    public_id: str
    new_audios: List[FlashcardAudioBase]
    
class FlashcardPatchSyncMetadataRequest(BaseModel):
    public_id: str
    new_sync_metadata: FlashcardSyncMetadataBase

class FlashcardDeleteRequest(BaseModel):
    public_id: str

class FlashcardDeleteBatchRequest(BaseModel):
    public_ids: List[str]

class FlashcardTypeRequest(FlashcardTypeBase):
    pass
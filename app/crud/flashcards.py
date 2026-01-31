from sqlalchemy import select, update
from typing import List

from ..db.session import SessionLocal
from ..services.flashcards import build_flashcard_model, build_flashcard_info
from ..dependencies.time.utc_safe import utcnow

from ..db.models import (
    FlashcardModel, 
    FlashcardFSRSModel,
    FlashcardImageModel,
    FlashcardAudioModel,
    FlashcardReviewModel
)

from ..core.shemas.flashcards import (
    FlashcardInfo, 
    FlashcardFSRS,
    FlashcardUpdate,
    FlashcardImage,
    FlashcardAudio,
    FlashcardContent,
    FlashcardReview
)

def mark_flashcard_as_updated(flashcard_id: int):
    stmt = update(FlashcardModel).where(FlashcardModel.flashcard_id == flashcard_id).values(updated_at = utcnow())
    with SessionLocal.begin() as session:
        session.execute(stmt)

def get_flashcards_ids() -> List[int]:
    stmt = select(FlashcardModel.flashcard_id)
    with SessionLocal() as session:
        flashcards_ids = session.execute(stmt).scalars().all()
    return flashcards_ids

def get_flashcard_info(flashcard_id: int)->FlashcardInfo | None:
    stmt = select(FlashcardModel).where(FlashcardModel.flashcard_id == flashcard_id)
    
    with SessionLocal() as session:
        flashcard = session.execute(stmt).scalar_one_or_none()

        if not flashcard:
            return None

        return build_flashcard_info(flashcard)

def get_flashcard_updated_at(flashcard_id: int) -> FlashcardUpdate | None:
    stmt = select(FlashcardModel).where(FlashcardModel.flashcard_id == flashcard_id)
    with SessionLocal() as session:
        flashcard = session.execute(stmt).scalar_one_or_none()
    
        if not flashcard:
            return None
        
        return FlashcardUpdate(
            flashcard_id=flashcard.flashcard_id,
            updated_at=flashcard.updated_at
        )

def insert_flashcard(new_flashcard: FlashcardInfo) -> FlashcardModel:
    flashcard = build_flashcard_model(new_flashcard)

    with SessionLocal.begin() as session:
        session.add(flashcard)
        session.refresh(flashcard)
    
    return flashcard

def update_flashcard_fsrs(flashcard_id: int, fsrs: FlashcardFSRS):
    stmt = update(FlashcardFSRSModel).where(FlashcardFSRSModel.flashcard_id == flashcard_id).values(      
        stability = fsrs.stability,
        difficulty = fsrs.difficulty,
        due = fsrs.due,
        last_review = fsrs.last_review,
        state = fsrs.state
    )

    with SessionLocal.begin() as session:
        session.execute(stmt)

    return fsrs

def update_flashcard_images(flashcard_id: int, images: List[FlashcardImage]) -> bool:
    with SessionLocal.begin() as session:
        flashcard: FlashcardModel | None = session.query(FlashcardModel).filter(FlashcardModel.flashcard_id == flashcard_id).one_or_none()

        if not flashcard:
            return False
        
        flashcard.images.clear()
        
        for image in images:
            flashcard.images.append(
                FlashcardImageModel(
                    field = image.field,
                    image_url = image.image_url
                )
            )
    return True

def update_flashcard_audios(flashcard_id: int, audios: List[FlashcardAudio]) -> bool:
    with SessionLocal.begin() as session:
        flashcard: FlashcardModel | None = session.query(FlashcardModel).filter(FlashcardModel.flashcard_id == flashcard_id).one_or_none()

        if not flashcard:
            return False
        
        flashcard.audios.clear()
        
        for audio in audios:
            flashcard.audios.append(
                FlashcardAudioModel(
                    field = audio.field,
                    audio_url = audio.audio_url
                )
            )
    return True

def update_flashcard_content(flashcard_id: int, content: FlashcardContent) -> bool:
    with SessionLocal.begin() as session:
        flashcard: FlashcardModel | None = session.query(FlashcardModel).filter(FlashcardModel.flashcard_id == flashcard_id).one_or_none()

        if not flashcard:
            return False
        
        flashcard.content.front_field_content = content.front_field
        flashcard.content.back_field_content = content.back_field
    return True

def update_flashcard_reviews(flashcard_id: int, reviews: List[FlashcardReview]):
    with SessionLocal.begin() as session:
        flashcard: FlashcardModel | None = session.query(FlashcardModel).filter(FlashcardModel.flashcard_id == flashcard_id).one_or_none()

        if not flashcard:
            return False
        
        flashcard.reviews.clear()

        for review in reviews:
            flashcard.reviews.append(
                FlashcardReviewModel(
                    reviewed_at = review.reviewd_at,
                    rating= review.rating,
                    response_time_ms=review.response_time_ms,
                    scheduled_days= review.scheduled_days,
                    actual_days= review.actual_days,
                    prev_stability= review.prev_stability,
                    prev_difficulty= review.prev_difficulty,
                    new_stability= review.new_stability,
                    new_difficulty= review.new_difficulty,
                    state_before=review.state_before,
                    state_after=review.state_after
                )
            )

    return True

def update_flashcard_language_id(flashcard_id: int, new_language_id: int):
    with SessionLocal.begin() as session:
        flashcard: FlashcardModel | None = session.query(FlashcardModel).filter(FlashcardModel.flashcard_id == flashcard_id).one_or_none()

        if not flashcard:
            return False
        
        flashcard.language_id = new_language_id
    return True   

def update_flashcard_type_id(flashcard_id: int, new_flashcard_type_id: int):
    with SessionLocal.begin() as session:
        flashcard: FlashcardModel | None = session.query(FlashcardModel).filter(FlashcardModel.flashcard_id == flashcard_id).one_or_none()

        if not flashcard:
            return False
        
        flashcard.flashcard_type_id = new_flashcard_type_id
    return True
from sqlalchemy import select, insert
from typing import List

from ..db.models import (
    FlashcardModel, 
    FlashcardContentModel,
    FlashcardFSRSModel,
    FlashcardReviewModel,
    FlashcardImagesModel,
    FlashcardAudiosModel
)
from ..db.session import SessionLocal
from ..core.shemas.flashcards import (
    FlashcardInfo, 
    FlashcardAudio, 
    FlashcardImage, 
    FlashcardReview, 
    FlashcardContent, 
    FlashcardFSRS,
    FlashcardUpdate
)


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
    
    images = [FlashcardImage(field=image.field, image_url=image.image_url) for image in flashcard.images]
    audios = [FlashcardAudio(field=audio.field, audio_url=audio.audio_url) for audio in flashcard.audios]
    reviews = [FlashcardReview(
        reviewd_at=review.reviewed_at,
        rating=review.rating, 
        response_time_ms=review.response_time_ms, 
        scheduled_days=review.scheduled_days, 
        actual_days=review.actual_days, 
        prev_stability=review.prev_stability, 
        prev_difficulty=review.prev_difficulty,
        new_stability=review.new_stability,
        new_difficulty=review.new_difficulty,
        state_before=review.state_before,
        state_after=review.state_after
        ) 
        for review in flashcard.reviews
    ]
    

    content = FlashcardContent(front_field=flashcard.content.front_field_content, back_field=flashcard.content.back_field_content)
    fsrs = FlashcardFSRS(
        stability=flashcard.fsrs.stability, 
        difficulty=flashcard.fsrs.difficulty, 
        due=flashcard.fsrs.due,
        last_review=flashcard.fsrs.last_review,
        state=flashcard.fsrs.state
    )

    return FlashcardInfo(
        flashcard_id=flashcard.flashcard_id,
        
        language_id= flashcard.language_id,
        flashcard_type_id= flashcard.flashcard_type_id,
        created_at= flashcard.created_at,
        updated_at= flashcard.updated_at,

        content=content,
        fsrs = fsrs,

        reviews=reviews,
        images= images,
        audios= audios
    )

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

def insert_flashcard(new_flashcard: FlashcardInfo):
    content = FlashcardContentModel(
        front_field_content= new_flashcard.content.front_field,
        back_field_content=new_flashcard.content.back_field
    )

    fsrs = FlashcardFSRSModel(
        stability = new_flashcard.fsrs.stability,
        difficulty = new_flashcard.fsrs.difficulty,
        due= new_flashcard.fsrs.due,
        last_review = new_flashcard.fsrs.last_review,
        state=new_flashcard.fsrs.state
    )

    flashcard = FlashcardModel(
        flashcard_id = new_flashcard.flashcard_id,
        language_id = new_flashcard.language_id,
        flashcard_type_id = new_flashcard.flashcard_type_id,
        created_at = new_flashcard.created_at,
        updated_at = new_flashcard.updated_at,

        content = content,
        fsrs = fsrs
    )

    if new_flashcard.reviews:
        for review_shema in new_flashcard.reviews:
            flashcard.reviews.append(
                FlashcardReviewModel(
                    reviewed_at= review_shema.reviewd_at,
                    rating = review_shema.rating,
                    response_time_ms = review_shema.response_time_ms,
                    scheduled_days = review_shema.scheduled_days,
                    actual_days = review_shema.actual_days,
                    prev_stability = review_shema.prev_stability,
                    prev_difficulty = review_shema.prev_difficulty,
                    new_stability = review_shema.new_stability,
                    new_difficulty = review_shema.new_difficulty,
                    state_before = review_shema.state_before,
                    state_after = review_shema.state_after
                )
            )

    if new_flashcard.images:
        for image_schema in new_flashcard.images:
            flashcard.images.append(
                FlashcardImagesModel(
                    field=image_schema.field,
                    image_url=image_schema.image_url,
                )
            )

    if new_flashcard.audios:
        for audio_schema in new_flashcard.audios:
            flashcard.audios.append(
                FlashcardAudiosModel(
                    field=audio_schema.field,
                    audio_url=audio_schema.audio_url,
                )
            )
    
    with SessionLocal.begin() as session:
        session.add(flashcard)
        session.flush()
        session.refresh(flashcard)
    
    return flashcard
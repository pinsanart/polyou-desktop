from ..core.shemas.flashcards import (
    FlashcardInfo,
    FlashcardImage,
    FlashcardAudio,
    FlashcardFSRS,
    FlashcardReview,
    FlashcardContent
)
from ..db.models import (
    FlashcardModel,
    FlashcardContentModel,
    FlashcardFSRSModel,
    FlashcardAudioModel,
    FlashcardImageModel,
    FlashcardReviewModel
)

def build_flashcard_model(flashcard_info:FlashcardInfo) -> FlashcardModel:
    content = FlashcardContentModel(
        front_field_content= flashcard_info.content.front_field,
        back_field_content=flashcard_info.content.back_field
    )

    fsrs = FlashcardFSRSModel(
        stability = flashcard_info.fsrs.stability,
        difficulty = flashcard_info.fsrs.difficulty,
        due= flashcard_info.fsrs.due,
        last_review = flashcard_info.fsrs.last_review,
        state=flashcard_info.fsrs.state
    )

    flashcard = FlashcardModel(
        flashcard_id = flashcard_info.flashcard_id,
        language_id = flashcard_info.language_id,
        flashcard_type_id = flashcard_info.flashcard_type_id,
        created_at = flashcard_info.created_at,
        updated_at = flashcard_info.updated_at,

        content = content,
        fsrs = fsrs
    )

    if flashcard_info.reviews:
        for review_shema in flashcard_info.reviews:
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

    if flashcard_info.images:
        for image_schema in flashcard_info.images:
            flashcard.images.append(
                FlashcardImageModel(
                    field=image_schema.field,
                    image_url=image_schema.image_url,
                )
            )

    if flashcard_info.audios:
        for audio_schema in flashcard_info.audios:
            flashcard.audios.append(
                FlashcardAudioModel(
                    field=audio_schema.field,
                    audio_url=audio_schema.audio_url,
                )
            )
    
    return flashcard

def build_flashcard_info(flashcard: FlashcardModel) -> FlashcardInfo:
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
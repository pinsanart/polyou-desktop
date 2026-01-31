from sqlalchemy import select, update
from typing import List

from ...infrastructure.db.session import SessionLocal
from ...services.flashcards import build_flashcard_model, build_flashcard_info
from ...dependencies.time.utc_safe import utcnow

from ..db.models import (
    FlashcardModel, 
    FlashcardFSRSModel,
    FlashcardImageModel,
    FlashcardAudioModel,
    FlashcardReviewModel
)

from ...core.schemas.flashcards import (
    FlashcardInfo, 
    FlashcardFSRS,
    FlashcardUpdate,
    FlashcardImage,
    FlashcardAudio,
    FlashcardContent,
    FlashcardReview
)

from typing import List, Optional
from sqlalchemy import select

from ...infrastructure.db.session import SessionLocal
from ...infrastructure.db.models import (
    FlashcardModel,
    FlashcardFSRSModel,
    FlashcardImageModel,
    FlashcardAudioModel,
    FlashcardReviewModel,
)

from ...core.schemas.flashcards import (
    FlashcardInfo,
    FlashcardFSRS,
    FlashcardUpdate,
    FlashcardImage,
    FlashcardAudio,
    FlashcardContent,
    FlashcardReview,
)

from ...services.flashcards import (
    build_flashcard_model,
    build_flashcard_info,
)

from ...core.flashcards.flashcard_repository import FlashcardRepository

class FlashcardRepositorySQLAlchemy(FlashcardRepository):
    def __init__(self, session_factory=SessionLocal):
        self.session_factory = session_factory

    def list_ids(self) -> List[int]:
        stmt = select(FlashcardModel.flashcard_id)
        with self.session_factory() as session:
            return session.execute(stmt).scalars().all()

    def get_info(self, flashcard_id: int) -> Optional[FlashcardInfo]:
        stmt = select(FlashcardModel).where(FlashcardModel.flashcard_id == flashcard_id)
        with self.session_factory() as session:
            model = session.execute(stmt).scalar_one_or_none()
            return build_flashcard_info(model) if model else None

    def get_updated_at(self, flashcard_id: int) -> Optional[FlashcardUpdate]:
        stmt = select(FlashcardModel).where(FlashcardModel.flashcard_id == flashcard_id)
        with self.session_factory() as session:
            model = session.execute(stmt).scalar_one_or_none()
            if not model:
                return None
            return FlashcardUpdate(
                flashcard_id=model.flashcard_id,
                updated_at=model.updated_at,
            )


    def insert(self, flashcard: FlashcardInfo) -> FlashcardModel:
        model = build_flashcard_model(flashcard)
        with self.session_factory.begin() as session:
            session.add(model)
            session.flush()
            session.refresh(model)
        return model

    def update_fsrs(self, flashcard_id: int, fsrs: FlashcardFSRS) -> None:
        with self.session_factory.begin() as session:
            model: FlashcardFSRSModel | None = (
                session.query(FlashcardFSRSModel)
                .filter(FlashcardFSRSModel.flashcard_id == flashcard_id)
                .one_or_none()
            )

            if not model:
                return

            model.stability = fsrs.stability
            model.difficulty = fsrs.difficulty
            model.due = fsrs.due
            model.last_review = fsrs.last_review
            model.state = fsrs.state

    def replace_images(self, flashcard_id: int, images: List[FlashcardImage]) -> bool:
        with self.session_factory.begin() as session:
            flashcard = session.get(FlashcardModel, flashcard_id)
            if not flashcard:
                return False

            flashcard.images.clear()
            for image in images:
                flashcard.images.append(
                    FlashcardImageModel(
                        field=image.field,
                        image_url=image.image_url,
                    )
                )
        return True

    def replace_audios(self, flashcard_id: int, audios: List[FlashcardAudio]) -> bool:
        with self.session_factory.begin() as session:
            flashcard = session.get(FlashcardModel, flashcard_id)
            if not flashcard:
                return False

            flashcard.audios.clear()
            for audio in audios:
                flashcard.audios.append(
                    FlashcardAudioModel(
                        field=audio.field,
                        audio_url=audio.audio_url,
                    )
                )
        return True

    def update_content(self, flashcard_id: int, content: FlashcardContent) -> bool:
        with self.session_factory.begin() as session:
            flashcard = session.get(FlashcardModel, flashcard_id)
            if not flashcard:
                return False

            flashcard.content.front_field_content = content.front_field
            flashcard.content.back_field_content = content.back_field
        return True

    def replace_reviews(self, flashcard_id: int, reviews: List[FlashcardReview]) -> bool:
        with self.session_factory.begin() as session:
            flashcard = session.get(FlashcardModel, flashcard_id)
            if not flashcard:
                return False

            flashcard.reviews.clear()
            for review in reviews:
                flashcard.reviews.append(
                    FlashcardReviewModel(
                        reviewed_at=review.reviewed_at,
                        rating=review.rating,
                        response_time_ms=review.response_time_ms,
                        scheduled_days=review.scheduled_days,
                        actual_days=review.actual_days,
                        prev_stability=review.prev_stability,
                        prev_difficulty=review.prev_difficulty,
                        new_stability=review.new_stability,
                        new_difficulty=review.new_difficulty,
                        state_before=review.state_before,
                        state_after=review.state_after,
                    )
                )
        return True

    def change_language(self, flashcard_id: int, language_id: int) -> bool:
        with self.session_factory.begin() as session:
            flashcard = session.get(FlashcardModel, flashcard_id)
            if not flashcard:
                return False
            flashcard.language_id = language_id
        return True

    def change_type(self, flashcard_id: int, flashcard_type_id: int) -> bool:
        with self.session_factory.begin() as session:
            flashcard = session.get(FlashcardModel, flashcard_id)
            if not flashcard:
                return False
            flashcard.flashcard_type_id = flashcard_type_id
        return True

    def touch(self, flashcard_id):
        with self.session_factory.begin() as session:
            flashcard = session.get(FlashcardModel, flashcard_id)
            if not flashcard:
                return False
            flashcard.updated_at = utcnow()
        return True
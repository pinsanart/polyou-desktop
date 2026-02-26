from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import (
    String,
    Integer,
    ForeignKey,
    DateTime,
    Enum as SQLEnum,
)
from uuid import UUID, uuid4

from typing import List, Optional
from datetime import datetime

from ...dependencies.time.utc_safe import utcnow

# =========================================================
# Enums
# =========================================================
from ...core.enums import (
    Fields, 
    FSRSRating, 
    FSRSState
)
# =========================================================
# Base
# =========================================================
class PolyouDB(DeclarativeBase):
    pass


# =========================================================
# Languages
# =========================================================
class LanguageModel(PolyouDB):
    __tablename__ = "languages"

    language_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    iso_639_1: Mapped[str] = mapped_column(String(2), nullable=False, unique=True)

    flashcards: Mapped[List["FlashcardModel"]] = relationship(back_populates="language")

# =========================================================
# Flashcards
# =========================================================
class FlashcardTypeModel(PolyouDB):
    __tablename__ = "flashcard_types"

    flashcard_type_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String)

    flashcards: Mapped[List["FlashcardModel"]] = relationship(back_populates="flashcard_type")


class FlashcardSyncMetadataModel(PolyouDB):
    __tablename__ = "flashcards_sync_metadata"

    flashcard_id: Mapped[int] = mapped_column(
        ForeignKey("flashcards.flashcard_id", ondelete="CASCADE"),
        primary_key=True
    )

    last_review_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
    last_content_updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
    last_image_updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
    last_audio_updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)

    flashcard: Mapped["FlashcardModel"] = relationship(
        back_populates="sync_metadata",
        passive_deletes=True
    )

class FlashcardModel(PolyouDB):
    __tablename__ = "flashcards"

    flashcard_id: Mapped[int] = mapped_column(primary_key=True)
    
    public_id: Mapped[str] = mapped_column(
        String,
        default=uuid4,
        unique=True,
        nullable=False,
        index=True
    )

    language_id: Mapped[int] = mapped_column(ForeignKey("languages.language_id"), nullable=False)
    flashcard_type_id: Mapped[int] = mapped_column(ForeignKey("flashcard_types.flashcard_type_id"), nullable=False)
    
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow, nullable=False)

    language: Mapped["LanguageModel"] = relationship(back_populates="flashcards")
    flashcard_type: Mapped["FlashcardTypeModel"] = relationship(back_populates="flashcards")

    sync_metadata: Mapped["FlashcardSyncMetadataModel"] = relationship(
        back_populates="flashcard",
        uselist=False,
        cascade="all, delete-orphan",
        passive_deletes=True
    )

    content: Mapped["FlashcardContentModel"] = relationship(
        back_populates="flashcard",
        uselist=False,
        cascade="all, delete-orphan",
        passive_deletes=True
    )

    fsrs: Mapped["FlashcardFSRSModel"] = relationship(
        back_populates="flashcard",
        uselist=False,
        cascade="all, delete-orphan",
        passive_deletes=True
    )
    
    reviews: Mapped[List["FlashcardReviewModel"]] = relationship(
        back_populates="flashcard",
        cascade="all, delete-orphan",
        passive_deletes=True
    )

    images: Mapped[List["FlashcardImageModel"]] = relationship(
        back_populates="flashcard",
        cascade="all, delete-orphan",
        passive_deletes=True
    )

    audios: Mapped[List["FlashcardAudioModel"]] = relationship(
        back_populates="flashcard",
        cascade="all, delete-orphan",
        passive_deletes=True
    )

class FlashcardContentModel(PolyouDB):
    __tablename__ = "flashcards_content"

    flashcard_id: Mapped[int] = mapped_column(
        ForeignKey("flashcards.flashcard_id", ondelete="CASCADE"),
        primary_key=True
    )

    front_field: Mapped[str] = mapped_column(String, nullable=False)
    back_field: Mapped[Optional[str]] = mapped_column(String)

    flashcard: Mapped["FlashcardModel"] = relationship(
        back_populates="content",
        passive_deletes=True
    )

class FlashcardFSRSModel(PolyouDB):
    __tablename__ = "flashcards_fsrs"

    flashcard_id: Mapped[int] = mapped_column(
        ForeignKey("flashcards.flashcard_id", ondelete="CASCADE"),
        primary_key=True
    )
    stability: Mapped[float] = mapped_column(nullable=False, default=0.3)
    difficulty: Mapped[float] = mapped_column(nullable=False, default=5.0)
    due: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow, nullable=False)
    last_review: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    state: Mapped[FSRSState] = mapped_column(SQLEnum(FSRSState), nullable=False, default=FSRSState.LEARNING)

    flashcard: Mapped["FlashcardModel"] = relationship(
        back_populates="fsrs",
        passive_deletes=True
    )

class FlashcardReviewModel(PolyouDB):
    __tablename__ = "flashcards_reviews"

    review_id: Mapped[int] = mapped_column(primary_key=True)
    
    flashcard_id: Mapped[int] = mapped_column(
        ForeignKey("flashcards.flashcard_id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )
    
    reviewed_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        default=utcnow, 
        nullable=False
    )
    
    rating: Mapped[FSRSRating] = mapped_column(SQLEnum(FSRSRating), nullable=False)
    
    response_time_ms: Mapped[int] = mapped_column(Integer, nullable=False)
    
    scheduled_days: Mapped[int] = mapped_column(Integer, nullable=False)
    actual_days: Mapped[int] = mapped_column(Integer, nullable=False)
    
    prev_stability: Mapped[float] = mapped_column(nullable=False)
    prev_difficulty: Mapped[float] = mapped_column(nullable=False)
    new_stability: Mapped[float] = mapped_column(nullable=False)
    new_difficulty: Mapped[float] = mapped_column(nullable=False)
    
    state_before: Mapped[FSRSState] = mapped_column(SQLEnum(FSRSState), nullable=False)
    state_after: Mapped[FSRSState] = mapped_column(SQLEnum(FSRSState), nullable=False)

    flashcard: Mapped["FlashcardModel"] = relationship(
        back_populates="reviews",
        passive_deletes=True
    )


class FlashcardImageModel(PolyouDB):
    __tablename__ = "flashcards_images"

    image_id: Mapped[int] = mapped_column(primary_key=True)
    
    flashcard_id: Mapped[int] = mapped_column(
        ForeignKey("flashcards.flashcard_id", ondelete="CASCADE"),
        nullable=False
    )

    field: Mapped[Fields] = mapped_column(SQLEnum(Fields), nullable=False)
    url: Mapped[str] = mapped_column(String, nullable=False)

    flashcard: Mapped["FlashcardModel"] = relationship(
        back_populates="images",
        passive_deletes=True
    )

class FlashcardAudioModel(PolyouDB):
    __tablename__ = "flashcards_audios"

    audio_id: Mapped[int] = mapped_column(primary_key=True)
    
    flashcard_id: Mapped[int] = mapped_column(
        ForeignKey("flashcards.flashcard_id", ondelete="CASCADE"),
        nullable=False
    )
    
    field: Mapped[Fields] = mapped_column(SQLEnum(Fields), nullable=False)
    url: Mapped[str] = mapped_column(String, nullable=False)

    flashcard: Mapped["FlashcardModel"] = relationship(
        back_populates="audios",
        passive_deletes=True
    )
from sqlalchemy.orm import Session, selectinload
from sqlalchemy import select, delete
from uuid import UUID
from typing import List, Optional

from .....core.repositories.flashcards.flashcard import FlashcardRepository
from ....db.models import FlashcardModel


class FlashcardRepositorySQLAlchemy(FlashcardRepository):

    def __init__(self, db_session: Session):
        self._session = db_session

    def _base_query(self):
        return (
            select(FlashcardModel)
            .options(
                selectinload(FlashcardModel.sync_metadata),
                selectinload(FlashcardModel.content),
                selectinload(FlashcardModel.fsrs),
                selectinload(FlashcardModel.reviews),
                selectinload(FlashcardModel.images),
                selectinload(FlashcardModel.audios),
            )
        )

    def list_public_ids(self) -> List[UUID]:
        stmt = select(FlashcardModel.public_id)
        return self._session.scalars(stmt).all()

    def list_ids(self) -> List[int]:
        stmt = select(FlashcardModel.flashcard_id)
        return self._session.scalars(stmt).all()

    def get_by_id(self, flashcard_id: int) -> Optional[FlashcardModel]:
        stmt = self._base_query().where(
            FlashcardModel.flashcard_id == flashcard_id
        )
        return self._session.scalars(stmt).first()

    def get_by_ids(self, ids: List[int]) -> List[FlashcardModel]:
        if not ids:
            return []

        stmt = self._base_query().where(
            FlashcardModel.flashcard_id.in_(ids)
        )
        return list(self._session.scalars(stmt))

    def get_by_public_id(self, public_id: UUID) -> Optional[FlashcardModel]:
        stmt = self._base_query().where(
            FlashcardModel.public_id == public_id
        )
        return self._session.scalars(stmt).first()

    def get_by_public_ids(self, public_ids: List[UUID]) -> List[FlashcardModel]:
        if not public_ids:
            return []

        stmt = self._base_query().where(
            FlashcardModel.public_id.in_(public_ids)
        )
        return list(self._session.scalars(stmt))

    def create_one(self, model: FlashcardModel) -> None:
        self._session.add(model)

    def create_many(self, models: List[FlashcardModel]) -> None:
        if models:
            self._session.add_all(models)

    def delete_one(self, flashcard_id: int) -> None:
        stmt = delete(FlashcardModel).where(
            FlashcardModel.flashcard_id == flashcard_id
        )
        self._session.execute(stmt)

    def delete_many(self, ids: List[int]) -> None:
        if not ids:
            return

        stmt = delete(FlashcardModel).where(
            FlashcardModel.flashcard_id.in_(ids)
        )
        self._session.execute(stmt)
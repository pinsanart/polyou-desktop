from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, update, delete
from typing import List
from uuid import UUID

from ...core.repositories.flashcard import FlashcardRepository
from ..db.models import FlashcardModel

class FlashcardRepositorySQLAlchemy(FlashcardRepository):
    def __init__(self, sessionmaker: sessionmaker):
        self.sessionmaker = sessionmaker

    def create_one(self, entity: FlashcardModel) -> int:
        with self.sessionmaker() as session:
            try:
                session.add(entity)
                session.flush()  # garante PK gerada
                flashcard_id = entity.flashcard_id
                session.commit()
                return flashcard_id
            except Exception:
                session.rollback()
                raise

    def create_many(self, entities: List[FlashcardModel]) -> List[int]:
        if not entities:
            return []

        with self.sessionmaker() as session:
            try:
                session.add_all(entities)
                session.flush()
                ids = [e.flashcard_id for e in entities]
                session.commit()
                return ids
            except Exception:
                session.rollback()
                raise

    def list_ids(self, user_id: int) -> List[int]:
        with self.sessionmaker() as session:
            stmt = select(FlashcardModel.flashcard_id).where(
                FlashcardModel.user_id == user_id
            )
            return session.scalars(stmt).all()

    def get_by_id(self, id: int) -> FlashcardModel | None:
        with self.sessionmaker() as session:
            stmt = select(FlashcardModel).where(
                FlashcardModel.flashcard_id == id
            )
            return session.scalar(stmt)

    def get_by_public_id(self, public_id: UUID) -> FlashcardModel | None:
        with self.sessionmaker() as session:
            stmt = select(FlashcardModel).where(
                FlashcardModel.public_id == public_id
            )
            return session.scalar(stmt)

    def list_by_ids(self, ids: List[int]) -> List[FlashcardModel]:
        if not ids:
            return []

        with self.sessionmaker() as session:
            stmt = select(FlashcardModel).where(
                FlashcardModel.flashcard_id.in_(ids)
            )
            return session.scalars(stmt).all()

    def update(self, id: int, data: dict) -> None:
        if not data:
            return

        with self.sessionmaker() as session:
            try:
                stmt = (
                    update(FlashcardModel)
                    .where(FlashcardModel.flashcard_id == id)
                    .values(**data)
                )
                session.execute(stmt)
                session.commit()
            except Exception:
                session.rollback()
                raise

    def delete_one(self, id: int) -> bool:
        with self.sessionmaker() as session:
            try:
                result = session.execute(
                    delete(FlashcardModel).where(
                        FlashcardModel.flashcard_id == id
                    )
                )
                session.commit()
                return result.rowcount > 0
            except Exception:
                session.rollback()
                raise

    def delete_many(self, ids: List[int]) -> bool:
        if not ids:
            return

        with self.sessionmaker() as session:
            try:
                session.execute(
                    delete(FlashcardModel).where(
                        FlashcardModel.flashcard_id.in_(ids)
                    )
                )
                session.commit()
            except Exception:
                session.rollback()
                raise
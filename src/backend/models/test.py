from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Tests(Base):
    __tablename__ = 'Test'

    for_lesson_id: Mapped[int] = mapped_column(
        ForeignKey('lesson.id'),
        index=True,
    )

    options: Mapped[list[str]] = mapped_column(JSONB)

    curr_answer: Mapped[str] = mapped_column(
        nullable=False
    )

    lesson: Mapped['Lessons'] = relationship(
        back_populates='questions'
    )
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Tests(Base):
    __tablename__ = 'test'

    for_lesson_id: Mapped[int] = mapped_column(
        ForeignKey('lesson.id'),
        index=True,
        init=False,
    )

    question_text: Mapped[str] = mapped_column(nullable=False)

    options: Mapped[list[str]] = mapped_column(JSONB)

    curr_answer: Mapped[list[str]] = mapped_column(JSONB, nullable=False)

    lesson: Mapped['Lessons'] = relationship(
        'Lessons', back_populates='questions', default=None
    )

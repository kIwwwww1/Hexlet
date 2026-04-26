from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from .base import Base

class Tests(Base):
    __tablename__ = 'Test'

    for_lesson_id: Mapped[int] = mapped_column(
        ForeignKey('lesson.lesson_id'),
        index=True,
    )

    question_id: Mapped[int] = mapped_column(
        primary_key=True
    )

    options: Mapped[list[str | int]] = mapped_column(JSONB)

    curr_answer: Mapped[str | int] = mapped_column(
        nullable=False
    )

    lesson: Mapped['Lessons'] = relationship(
        back_populates='questions'
    )
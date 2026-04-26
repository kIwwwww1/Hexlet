
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base

class Lessons(Base):
    __tablename__ = 'lesson'

    lesson_id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    title: Mapped[str] = mapped_column(
        unique=True,
        nullable=False,
    )

    information: Mapped[str] = mapped_column(
        unique=True,
        nullable=False,
    )
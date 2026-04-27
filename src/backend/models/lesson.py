from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Lessons(Base):
    __tablename__ = "lesson"

    title: Mapped[str] = mapped_column(
        unique=True,
        nullable=False,
    )

    information: Mapped[str] = mapped_column(
        unique=True,
        nullable=False,
    )

    questions: Mapped[list["Tests"]] = relationship(
        back_populates="lesson", order_by="Tests.question_id"
    )

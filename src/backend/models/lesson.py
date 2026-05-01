from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Lessons(Base):
    __tablename__ = 'lesson'

    title: Mapped[str] = mapped_column(
        unique=True,
        nullable=False,
    )

    information: Mapped[str] = mapped_column(
        unique=True,
        nullable=False,
    )

    questions: Mapped[list['Tests']] = relationship(
        'Tests',
        back_populates='lesson',
        default_factory=list,
        #   order_by='Tests.id'
    )

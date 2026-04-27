from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Users(Base):
    __tablename__ = 'users'

    unique_id: Mapped[str] = mapped_column(unique=True)
    user_name: Mapped[str] = mapped_column(nullable=False, unique=True)

    password: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(unique=True)

    level: Mapped[int] = mapped_column(
        nullable=False,
        default=1,
        server_default='1',
        init=False,
    )

    xp: Mapped[int] = mapped_column(
        nullable=False,
        default=0,
        server_default='0',
        init=False,
    )

    energy: Mapped[int] = mapped_column(
        nullable=False,
        default=10,
        server_default='10',
        init=False,
    )

    floor: Mapped[int] = mapped_column(
        nullable=False,
        default=0,
        server_default='0',
        init=False,
    )

    floor_level: Mapped[int] = mapped_column(
        nullable=False,
        default=0,
        server_default='0',
        init=False,
    )
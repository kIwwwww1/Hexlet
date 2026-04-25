from sqlalchemy.orm import Mapped, mapped_column
from .base import Base

class Users(Base):
    __tablename__ = 'users'

    unique_user_id: Mapped[str] = mapped_column(unique=True)
    user_name: Mapped[str] = mapped_column(nullable=False, unique=True)

    password: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(unique=True)

    level: Mapped[int] = mapped_column(
        nullable=False,
        default=1,
        server_default='1'
    )

    xp: Mapped[int] = mapped_column(
        nullable=False,
        default=0,
        server_default='0'
    )

    energy: Mapped[int] = mapped_column(
        nullable=False,
        default=10,
        server_default='10'
    )

    floor: Mapped[int] = mapped_column(
        nullable=False,
        default=0,
        server_default='0',
    )

    floor_level: Mapped[int] = mapped_column(
        nullable=False,
        default=0,
        server_default='0',
    )
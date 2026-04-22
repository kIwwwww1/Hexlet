from sqlalchemy import func, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from datetime import datetime

class Users(Base):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    
    unique_user_id: Mapped[str] = mapped_column(unique=True)

    user_name: Mapped[str] = mapped_column(
        unique=True,
    )

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

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    @property
    def get_created_at(self):
        '''Вернуть красивую дату регистрации'''
        if self.created_at is None:
            return None
        return self.created_at.strftime('%d.%m.%Y %H:%M')

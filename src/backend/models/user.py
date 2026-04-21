from sqlalchemy import ForeignKey, func, DateTime
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
    user_level: Mapped[int] = mapped_column(
        nullable=False,
        default=0
    )
    creation_data: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    @property
    def get_creation_data(self):
        '''Вернуть красивую дату регистрации'''
        if self.creation_data is None:
            return None
        return self.creation_data.strftime('%d.%m.%Y %H:%M')

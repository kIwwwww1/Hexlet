from collections.abc import AsyncGenerator
from datetime import datetime

from sqlalchemy import DateTime, func
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, MappedAsDataclass, mapped_column

from src.backend.config import settings


class Base(MappedAsDataclass, DeclarativeBase):
    __dataclass_args__ = {'kw_only': True}

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True, 
        init=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        init=False
    )

engine = create_async_engine(settings.db_url)

async_session_factory = async_sessionmaker(engine, expire_on_commit=False)

async def get_session() -> AsyncGenerator[AsyncSession]:
    '''Create DB async session with context manager'''
    
    async with async_session_factory() as session:
        yield session

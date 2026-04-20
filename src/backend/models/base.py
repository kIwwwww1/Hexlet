from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import (create_async_engine, 
                                    async_sessionmaker, 
                                    AsyncSession)
from sqlalchemy.orm import DeclarativeBase
from src.backend.config import settings

class Base(DeclarativeBase):
    pass

engine = create_async_engine(settings.db_url)

async_session_factory = async_sessionmaker(engine, expire_on_commit=False)

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_factory() as session:
        yield session

from sqlalchemy.ext.asyncio import AsyncSession

from .lession_repository import LessonRepository


class LessonService:
    """Designed to work with a database"""

    def __init__(self, session: AsyncSession) -> None:
        self.db = LessonRepository(session)

    async def create_lesson(self) -> ...: ...

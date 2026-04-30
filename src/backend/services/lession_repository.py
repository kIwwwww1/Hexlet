from sqlalchemy.ext.asyncio import AsyncSession

from src.backend.schemas.lesson import LessonData


class LessonRepository:
    """Designed for convenient use of the LessonService class"""

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create_lesson(self, lession_data: LessonData) -> LessonData: ...

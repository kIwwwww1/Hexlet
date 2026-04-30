from sqlalchemy.ext.asyncio import AsyncSession

from src.backend.models.lesson import Lessons
from src.backend.schemas.lesson import LessonData


class LessonService:
    """Designed to work with a database"""

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create_new_lesson(self, lession_data: LessonData) -> Lessons:
        new_lession = Lessons(**lession_data.model_dump())

        self.session.add(new_lession)
        await self.session.commit()
        await self.session.refresh(new_lession)

        return new_lession

from sqlalchemy.ext.asyncio import AsyncSession

from src.backend.models.lesson import Lessons
from src.backend.models.test import Tests
from src.backend.schemas.lesson import LessonData


class LessonService:
    """Designed to work with a database"""

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create_new_lesson(self, lession_data: LessonData) -> Lessons:

        data = lession_data.model_dump()
        questions_data = data.pop('questions', [])
        questions_obj = [Tests(**q) for q in questions_data]

        new_lession = Lessons(**data, questions=questions_obj)

        self.session.add(new_lession)
        await self.session.commit()
        await self.session.refresh(new_lession)

        return new_lession

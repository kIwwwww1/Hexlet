import ijson
from sqlalchemy.ext.asyncio import AsyncSession

from src.backend.schemas.lesson import LessonData
from src.backend.services.lesson_service import LessonService


class TestData:
    PATH: str = 'src/frontend/src/fixtures/test_lessons.json'

    def __init__(self, session: AsyncSession, lesson_service: LessonService) -> None:
        self.session = session
        self.lesson_service = lesson_service

    @staticmethod
    def load_data(path: str):
        with open(path, encoding='utf-8') as f:
            yield from ijson.items(f, 'item')

    async def create_lesson_testdata(self):

        for lesson in self.load_data(self.PATH):
            lesson_data = LessonData.model_validate(lesson)

            await self.lesson_service.create_new_lesson(lesson_data)

            # Логика добавления тестовых уроков

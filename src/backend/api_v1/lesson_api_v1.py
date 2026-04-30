from typing import Annotated

from fastapi import APIRouter, Depends

from src.backend.dependency import SessionDep
from src.backend.schemas.lesson import LessonData
from src.backend.services.lesson_service import LessonService

# the path built relative to -> /api/v1/lesson/...
lesson_router = APIRouter(
    # prefix=/api/v1/lesson/...
    # tags=['Lesson']
)


def get_lesson_service(session: SessionDep) -> LessonService:
    return LessonService(session)


LessonDep = Annotated[LessonService, Depends(get_lesson_service)]


@lesson_router.post('/create')
async def create_lesson(
    lesson_data: LessonData, lesson_service: LessonDep, session: SessionDep
) -> LessonData:
    await lesson_service.create_new_lesson(lesson_data)

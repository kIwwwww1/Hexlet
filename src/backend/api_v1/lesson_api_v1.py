from typing import Annotated

from fastapi import APIRouter, Depends

from src.backend.dependency import SessionDep
from src.backend.schemas.lesson import LessonData
from src.backend.services.lesson_service import LessonService

# the path built relative to -> /api/v1/lessons/...
lesson_router = APIRouter(
    # prefix=/api/v1/lessons/...
    # tags=['Lesson']
)


def get_lesson_service(session: SessionDep) -> LessonService:
    return LessonService(session)


LessonDep = Annotated[LessonService, Depends(get_lesson_service)]


@lesson_router.post('/create', response_model=LessonData)
async def create_lesson(
    lesson_data: LessonData, lesson_service: LessonDep, session: SessionDep
):
    new_lesson = await lesson_service.create_new_lesson(lesson_data)
    return new_lesson


@lesson_router.get('/{id:int}', response_model=LessonData)
async def get_current_lesson(id: int, lesson_service: LessonDep, session: SessionDep):
    lesson_obj = await lesson_service.get_lesson_id(id)

    return lesson_obj

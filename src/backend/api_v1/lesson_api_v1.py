from fastapi import APIRouter

# the path built relative to -> /api/v1/lesson/...
lesson_router = APIRouter(
    # prefix=/api/v1/lesson/...
    # tags=['Lesson']
)


@lesson_router.post('/create')
async def create_lesson(lesson_data: ...) -> ...: ...

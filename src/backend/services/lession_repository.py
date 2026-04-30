from sqlalchemy.ext.asyncio import AsyncSession


class LessonRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

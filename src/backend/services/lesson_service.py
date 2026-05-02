from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from src.backend.logger_config import log
from src.backend.models.lesson import Lessons
from src.backend.models.test import Tests
from src.backend.schemas.lesson import LessonData


class LessonService:
    """Designed to work with a database"""

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create_new_lesson(self, lession_data: LessonData) -> LessonData:
        """Create NEW lesson in DB"""

        try:
            data = lession_data.model_dump()
            questions_data = data.pop('questions', [])
            questions_obj = [Tests(**q) for q in questions_data]

            new_lession = Lessons(**data, questions=questions_obj)

            self.session.add(new_lession)
            await self.session.commit()
            await self.session.refresh(new_lession)

            return lession_data

        except SQLAlchemyError:
            await self.session.rollback()

            log.exception('Error creating lesson')
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='The lesson data is invalid or the lesson already exists',
            )

        except Exception:
            await self.session.rollback()

            log.exception('Internal server error')
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail='Internal server error',
            )

from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from src.backend.logger_config import log
from src.backend.models.user import Users
from src.backend.schemas.user import UserInDB


def hash_password(password: str) -> hash | None: ...


class UserRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create_new_user(self, user_data: UserInDB) -> Users:
        """Creating a new user in db"""

        try:
            new_user = Users(**user_data.model_dump())
            self.session.add(new_user)

            await self.session.commit()
            await self.session.refresh(new_user)
            return new_user

        except SQLAlchemyError:
            await self.session.rollback()

            log.exception('Error creating user')
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='The data is invalid or the user already exists',
            )

        except Exception:
            await self.session.rollback()

            log.exception('Internal server error')
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail='Internal server error',
            )

    async def get_by_id(self, user_id: int) -> Users | None:  # Объект пользователя
        stmt = select(Users).where(Users.id == user_id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

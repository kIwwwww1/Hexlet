import jwt
from fastapi import HTTPException, Response, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from src.backend.config import settings
from src.backend.logger_config import log
from src.backend.models.user import Users
from src.backend.schemas.user import UserInDB
from src.backend.services.secret_repository import SecretRepository

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM


class UserRepository:
    """Designed to work with a database"""

    def __init__(self, session: AsyncSession, secret: SecretRepository) -> None:
        self.session = session
        self.secret = secret

    async def create_new_user(self, user_data: UserInDB, response: Response) -> Users:
        """Creating a new user in db"""

        try:
            hashed_password = self.secret.hash_password(user_data.password)

            user_dict = user_data.model_dump()
            user_dict['password'] = hashed_password

            new_user = Users(**user_dict)
            self.session.add(new_user)

            await self.session.commit()

            user = (
                await self.session.execute(select(Users).where(Users.id == new_user.id))
            ).scalar_one()

            json_data = {
                'db_id': user.id,
                'uid': user.unique_id,
                'username': user.user_name,
                'created_at': user.created_at_readable,
            }

            token = jwt.encode(json_data, SECRET_KEY, ALGORITHM)

            response.set_cookie(
                key='session',
                value=token,
                # !!!   Без других параметров т.к это localhost    !!!
                # max_age=3600,
                # httponly=True,
                # secure=True,
                # samesite="lax"
            )

            return user

        except (SQLAlchemyError, IntegrityError):
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

    async def get_by_id(self, user_id: int) -> Users:
        """Get user in DB by user id"""

        stmt = select(Users).where(Users.id == user_id)
        result = await self.session.execute(stmt)
        user = result.scalar_one_or_none()

        if user:
            log.info('Получение пользователя')
            return user

        raise HTTPException(status_code=404, detail='User not found')

    async def reduce_energy_db(self, user_id: int):
        """Reduce user energy (-1)"""

        user = await self.get_by_id(user_id)
        if user.energy > 0:
            user.energy -= 1
            await self.session.commit()
            return user.energy
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail='User have <= 0 energy'
            )

    async def add_energy_db(self, user_id: int):
        """add user energy (+1)"""

        user = await self.get_by_id(user_id)
        user.energy += 1
        await self.session.commit()
        return user.energy

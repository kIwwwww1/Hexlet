from sqlalchemy.ext.asyncio import AsyncSession

from src.backend.models.user import Users
from src.backend.schemas.user import UserInDB
from src.backend.services.secret_repository import SecretRepository
from src.backend.services.user_repository import UserRepository


class UserService:
    """Designed to work with the UserRepository class"""

    def __init__(self, session: AsyncSession, secret: SecretRepository) -> None:
        self.db = UserRepository(session, secret)

    async def create_user(self, user_data: UserInDB) -> Users:
        return await self.db.create_new_user(user_data)

    # async def get_user(self, id: int) -> str: -> Объект пользователя при работе c бд
    #     Тестовый пример без обращения к базе данных
    #     return await self.db.get_by_id(1)

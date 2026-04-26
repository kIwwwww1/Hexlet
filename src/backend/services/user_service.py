from sqlalchemy.ext.asyncio import AsyncSession
from src.backend.services.user_repository import UserRepository
from src.backend.schemas.user import UserData, UserInDB

class UserService():
    def __init__(self, session: AsyncSession) -> None:
        self.db = UserRepository(session)

    async def create_user(self, user_data: UserData) -> str:
        return await self.db.create_new_user(user_data)

    # async def get_user(self, id: int) -> str: -> Объект пользователя при работе с бд
    #     Тестовый пример без обращения к базе данных
    #     return await self.db.get_by_id(1)

        
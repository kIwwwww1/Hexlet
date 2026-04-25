from sqlalchemy.ext.asyncio import AsyncSession
from src.backend.services.user_repository import UserRepository
from src.backend.schemas.user import UserData, UserResponse

class UserService():
    def __init__(self, session: AsyncSession) -> None:
        self.db = UserRepository(session)

    async def create_user(self, data: UserResponse) -> str:
        ...

    async def get_user(self, id: int) -> str: # -> Объект пользователя при работе с бд
        # Тестовый пример без обращения к базе данных
        return await self.db.get_by_id(1)

        
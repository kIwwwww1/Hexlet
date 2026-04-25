import asyncio
from sqlalchemy.ext.asyncio import AsyncSession

from src.backend.models.user import Users
from src.backend.schemas.user import UserData

class UserRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create_new_user(self, user_data: UserData) -> str:
        new_user = Users(
            user_name=user_data.user_name


        )
        self.session.add(Users)
        await self.session.commit()
        return '...'
    
    async def get_by_id(self, user_id: int) -> str:# Объект пользователя
        await asyncio.sleep(0.5)
        return 'Получили пользователя kIww1 с id: #HwZ91s'
    

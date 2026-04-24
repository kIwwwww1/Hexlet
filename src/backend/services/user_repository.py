import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
class UserRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session
    
    async def get_by_id(self, user_id: int) -> str:# Объект пользователя
        await asyncio.sleep(0.5)
        return 'Получили пользователя kIww1 с id: #HwZ91s'
    

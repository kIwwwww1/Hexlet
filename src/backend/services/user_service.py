from sqlalchemy.ext.asyncio import AsyncSession

class UserService():
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    def get_user(self, id: int): # -> Объект пользователя при работе с бд
        return 'Тестовый пользователь #1'

        
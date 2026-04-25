import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from fastapi import status, HTTPException

from src.backend.models.user import Users
from src.backend.schemas.user import UserData, UserNewData
from src.backend.logger_config import log

class UserRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create_new_user(self, user_data: UserNewData) -> str:
        '''Creating a new user in db'''
        try:
            new_user = Users(
                user_name=user_data.user_name,
                password=user_data.password,
                email=user_data.email,
            )
            self.session.add(new_user)

            await self.session.commit()
            return 'Пользователь успешно создан!'
        
        except SQLAlchemyError as ex:
            await self.session.rollback()
            log.exception('Ошибка при создании пользователя')
            raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail='Данные невалидны или пользователь уже существует'
                )
        
        except Exception as ex:
            await self.session.rollback()
            log.exception('Внутренняя ошибка сервера')
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Внутренняя ошибка сервера"
            )
    
        
    async def get_by_id(self, user_id: int) -> str:# Объект пользователя
        await asyncio.sleep(0.5)
        return 'Получили пользователя kIww1 с id: #HwZ91s'
    

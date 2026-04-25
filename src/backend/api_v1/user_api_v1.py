from typing import Annotated
from fastapi import Depends
from fastapi import APIRouter
from src.backend.dependency import SessionDep
from src.backend.services.user_service import UserService
from src.backend.logger_config import log

user_router = APIRouter(tags=['User'])

def get_user_service(session: SessionDep) -> UserService:
    return UserService(session)

UserDep = Annotated[UserService, Depends(get_user_service)]

@user_router.get('/')
async def test_endpoint(user_service: UserDep) -> str:
    log.exception('!!!Тестовая ошибка!!!')
    return await user_service.get_user(1)

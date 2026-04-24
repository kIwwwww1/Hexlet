from fastapi import Depends
from fastapi import APIRouter
from src.backend.dependency import SessionDep
from src.backend.services.user_service import UserService

user_router = APIRouter(tags=['User'])

def get_user_service(session: SessionDep) -> UserService:
    return UserService(session)


@user_router.get('/')
async def test_endpoint(db:UserService = Depends(get_user_service)) -> str:
    return 'Hello user!'

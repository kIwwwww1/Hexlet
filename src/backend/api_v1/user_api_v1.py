from fastapi import APIRouter
from dependency import SessionDep
from services.user_service import UserService

user_router = APIRouter(tags=['User'])

def get_user_service(session: SessionDep) -> UserService:
    return UserService(session)


# @user_router.get('/')
# async def test_endpoint(db: )
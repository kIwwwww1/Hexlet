from typing import Annotated

from fastapi import APIRouter, Depends

from src.backend.dependency import SessionDep
from src.backend.schemas.user import UserCreate, UserInDB
from src.backend.services.user_service import UserService

# the path built relative to -> /api/v1/user/...
user_router = APIRouter(
    # prefix=/api/v1/user/...
    tags=['User']
)


def get_user_service(session: SessionDep) -> UserService:
    return UserService(session)


UserDep = Annotated[UserService, Depends(get_user_service)]


@user_router.get('/')
async def test_endpoint(user_service: UserDep) -> str:
    """This is a test endpoint (No prod.)"""

    return 'hello world'


@user_router.post('/create')
async def create_user(data: UserCreate, user_service: UserDep):
    """Endpoint to create user in system"""

    # Create unique user id and build final data for add
    user_data = UserInDB(**data.model_dump())
    resp = await user_service.create_user(user_data)
    return {'user_data': resp}

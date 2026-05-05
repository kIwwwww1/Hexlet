from typing import Annotated

from fastapi import APIRouter, Depends

from src.backend.dependency import SecretDep, SessionDep
from src.backend.schemas.user import MainUserData, UserCreate, UserData, UserInDB
from src.backend.services.user_service import UserService

# the path built relative to -> /api/v1/users/...
user_router = APIRouter(
    # prefix=/api/v1/users/...
    # tags=['User']
)


def get_user_service(session: SessionDep, secret: SecretDep) -> UserService:
    return UserService(session, secret)


UserDep = Annotated[UserService, Depends(get_user_service)]


@user_router.get('/')
async def test_endpoint(user_service: UserDep) -> str:
    """This is a test endpoint (No prod.)"""

    return 'hello world'


@user_router.post('/create', response_model=UserData)
async def create_user(data: UserCreate, user_service: UserDep):
    """Endpoint to create user in system"""

    # Create unique user id and build final data for add
    user_data = UserInDB(**data.model_dump())
    resp = await user_service.create_user(user_data)
    return resp


@user_router.get('/{id:int}', response_model=MainUserData)
async def get_user(id: int, user_service: UserDep):
    """Get user by ID in db and return data in model MainUserData"""

    return await user_service.db.get_by_id(id)

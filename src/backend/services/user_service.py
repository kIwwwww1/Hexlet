import json
from typing import Any

from fastapi import Request, Response
from sqlalchemy.ext.asyncio import AsyncSession

from src.backend.models.user import Users
from src.backend.schemas.user import UserInDB
from src.backend.services.secret_repository import SecretRepository
from src.backend.services.user_repository import UserRepository


class UserService:
    """Designed to work with the UserRepository class"""

    def __init__(self, session: AsyncSession, secret: SecretRepository) -> None:
        self.db = UserRepository(session, secret)

    def deserialize_userdata(self, request: Request) -> dict[str, Any]:
        """JSON -> Python obj"""

        json_data = request.cookies.get('session')
        if not json_data:
            return {}
        data = json.loads(json_data)

        return data

    async def create_user(self, user_data: UserInDB, response: Response) -> Users:
        """Created new user in DB"""

        return await self.db.create_new_user(user_data, response)

    async def get_user_data(self, id: int) -> Users:
        """get user data in db by user id"""

        return await self.db.get_by_id(id)

    async def get_my_data(self, request: Request) -> Users:
        """deserialization data and get user by id"""

        user_data = self.deserialize_userdata(request)

        return await self.db.get_by_id(int(user_data.get('db_id', 0)))

    async def reduce_energy(self, request: Request):
        user_data = self.deserialize_userdata(request)
        return await self.db.reduce_energy_db(int(user_data.get('db_id', 0)))

    async def add_energy(self, request: Request):
        user_data = self.deserialize_userdata(request)
        return await self.db.add_energy_db(int(user_data.get('db_id', 0)))

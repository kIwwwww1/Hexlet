from fastapi import APIRouter

user_router = APIRouter(tags=['User'])

@user_router.get('/')
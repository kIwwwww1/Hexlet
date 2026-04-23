from contextlib import asynccontextmanager
from fastapi import FastAPI, middleware
# 
from .user_api_v1 import user_router
from src.backend.logger_config import log

@asynccontextmanager
async def lifespan(app: FastAPI):
    log.info('Запуск приложения')
    yield
    log.info('Выключение приложения')


app = FastAPI(lifespan=lifespan)

# Endpoints
app.include_router(user_router, prefix='/api/v1/user', tags=['User'])
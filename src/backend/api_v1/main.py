import time
from collections.abc import Callable
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware

from src.backend.logger_config import log

from .lesson_api_v1 import lesson_router
from .user_api_v1 import user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    log.info('Запуск приложения')
    yield
    log.info('Выключение приложения')


app = FastAPI(lifespan=lifespan)

origins = [
    'http://localhost',
    'http://127.0.0.1',
    'http://localhost:5173',
    'http://127.0.0.1:5173',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.middleware('http')
async def middleware(request: Request, call_next: Callable) -> Response:
    start_time = time.perf_counter()
    response = await call_next(request)
    end_time = time.perf_counter() - start_time

    log.debug(f'Query execution time - {end_time:.4f}')
    return response


# Endpoints
app.include_router(user_router, prefix='/api/v1/users', tags=['Users'])
app.include_router(lesson_router, prefix='/api/v1/lessons', tags=['Lessons'])

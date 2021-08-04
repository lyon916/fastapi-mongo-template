import app
from typing import Callable
from fastapi import FastAPI
from loguru import logger
import aioredis
from starlette.requests import Request
from api.config import REDIS_URL

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache


# @cache()
# async def get_cache():
#     return 1

# @app.get("/")
# @cache(expire=60)
# async def index(request: Request, response: Response):
#     return dict(hello="world")


def init_redis_cache(redis):
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")

async def get_redis_pool():
    redis = await aioredis.create_redis_pool(REDIS_URL)
    r = init_redis_cache(redis)
    return redis

async def release_redis(app: FastAPI):
    app.state.redis.close()
    await app.state.redis.wait_closed()
    return

def create_start_app_handler(app: FastAPI) -> Callable:  # type: ignore
    async def start_app() -> None:
        # app.state.redis = await get_redis_pool()
        pass
    return start_app


def create_stop_app_handler(app: FastAPI) -> Callable:  # type: ignore
    @logger.catch
    async def stop_app() -> None:
        # await release_redis(app)
        pass

    return stop_app

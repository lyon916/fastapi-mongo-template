import logging
import sys
from typing import List

# from databases import DatabaseURL
from loguru import logger
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret

from core.logging import InterceptHandler

API_PREFIX = ""

JWT_TOKEN_PREFIX = "Token"  # noqa: S105
VERSION = "0.1.0"

config = Config(".env")

DEBUG: bool = config("DEBUG", cast=bool, default=False)

# DATABASE_URL: DatabaseURL = config("DB_CONNECTION", cast=DatabaseURL)
MAX_CONNECTIONS_COUNT: int = config("MAX_CONNECTIONS_COUNT", cast=int, default=10)
MIN_CONNECTIONS_COUNT: int = config("MIN_CONNECTIONS_COUNT", cast=int, default=10)

SECRET_KEY: Secret = config("SECRET_KEY", cast=Secret)
DESCRIPTION: str = config("DESCRIPTION", default="a FastAPI example application")
PROJECT_NAME: str = config("PROJECT_NAME", default="FastAPI example application")
ALLOWED_HOSTS: List[str] = config(
    "ALLOWED_HOSTS",
    cast=CommaSeparatedStrings,
    default="",
)

# logging configuration

REDIS_POOL = "redis://@127.0.0.1:6379/0?encoding=utf-8"

LOGGING_LEVEL = logging.DEBUG if DEBUG else logging.INFO
LOGGERS = ("uvicorn.asgi", "uvicorn.access")

logging.getLogger().handlers = [InterceptHandler()]
for logger_name in LOGGERS:
    logging_logger = logging.getLogger(logger_name)
    logging_logger.handlers = [InterceptHandler(level=LOGGING_LEVEL)]

logger.configure(handlers=[{"sink": sys.stderr, "level": LOGGING_LEVEL}])

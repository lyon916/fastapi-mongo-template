from typing import Callable

from fastapi import FastAPI
from loguru import logger


def create_start_app_handler(app: FastAPI) -> Callable:  # type: ignore
    async def start_app() -> None:
        print("**"*21)

    return start_app


def create_stop_app_handler(app: FastAPI) -> Callable:  # type: ignore
    @logger.catch
    async def stop_app() -> None:
        print("^^"*21)

    return stop_app

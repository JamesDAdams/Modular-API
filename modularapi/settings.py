# coding: utf-8
import os
import logging
from functools import lru_cache

from pydantic import BaseSettings, PostgresDsn


class Setting(BaseSettings):
    ENVIRONMENT: str = "developpment"
    PG_DNS: PostgresDsn

    LOG_TO_STDOUT: bool = True
    LOGGING_LEVEL: int = logging.INFO

    class Config:
        env_file = os.environ.get("DOTENV_PATH", ".env")
        env_file_encoding = "utf-8"


@lru_cache()
def get_setting() -> Setting:
    return Setting()

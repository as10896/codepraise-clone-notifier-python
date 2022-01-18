import os
from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_REGION: str
    REPORT_QUEUE: str


class Development(Settings):
    environment = "development"

    class Config:
        secrets_dir = "config/secrets/dev"


class Production(Settings):
    environment = "production"

    class Config:
        secrets_dir = "config/secrets/prod"


@lru_cache()
def get_settings(mode: str = None, **kwargs) -> Settings:
    env = mode if mode else os.getenv("ENV", "development")
    return {"development": Development, "production": Production,}.get(
        env
    )(**kwargs)

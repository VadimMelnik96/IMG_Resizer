from typing import Sequence, Self

from dotenv import load_dotenv
from pydantic import SecretStr, PostgresDsn, model_validator, RedisDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class EnvBaseSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


class ServerFoldersSettings(EnvBaseSettings):
    """Настройки адресов папок"""
    uploads_folder: str
    resized_folder: str
    model_config = SettingsConfigDict(env_prefix="store_")


class RedisSettings(EnvBaseSettings):
    """Настройки Redis"""
    dsn: RedisDsn | None = None
    prefix: str = ""
    model_config = SettingsConfigDict(env_prefix="redis_")


class AppSettings(EnvBaseSettings):
    """Настройки приложения FastAPI"""
    name: str = ""
    root_path: str = ""
    debug: bool = False
    model_config = SettingsConfigDict(env_prefix="app_")


class Settings(EnvBaseSettings):
    """Настройки приложения"""
    app: AppSettings = AppSettings()
    redis: RedisSettings = RedisSettings()
    server_folders: ServerFoldersSettings = ServerFoldersSettings()


settings = Settings()

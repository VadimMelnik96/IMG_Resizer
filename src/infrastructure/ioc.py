from dishka import Provider, provide, Scope

from src.infrastructure.storages.interfaces import IRedisStorage
from src.infrastructure.storages.redis import RedisStorage
from src.services.interfaces import IUploadService
from src.services.upload_service import UploadService


class ApplicationProvider(Provider):
    """Провайдер зависимостей."""

    redis_storage = provide(RedisStorage, scope=Scope.APP, provides=IRedisStorage)
    upload_service = provide(UploadService, scope=Scope.REQUEST, provides=IUploadService)

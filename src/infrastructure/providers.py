from dishka import Provider, from_context, Scope, provide
import redis.asyncio as redis

from src.infrastructure.settings.settings import RedisSettings


class RedisProvider(Provider):
    """Провайдер для Redis."""

    redis_settings = from_context(provides=RedisSettings, scope=Scope.APP)

    @provide(scope=Scope.APP)
    async def redis_client(self, redis_settings: RedisSettings) -> redis.Redis:
        """Получение клиента Redis."""
        dsn: str = str(redis_settings.dsn)
        connection: redis.Redis = redis.from_url(dsn)
        return connection.client()

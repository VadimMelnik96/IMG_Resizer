import contextlib
from datetime import timedelta
from types import NoneType
from typing import Any, AsyncGenerator, AsyncIterator, Awaitable, Generic, Iterable, Iterator, Union

import redis
from redis.asyncio import Redis
from redis.asyncio.client import Pipeline

from src.infrastructure.storages.interfaces import IRedisStorage


class RedisStorage(IRedisStorage):
    def __init__(self, client: Redis):
        self.client = client

    async def get(self, key: str) -> Any:
        value = await self.client.get(key)
        if value is not None:
            return value.decode()
        return None

    async def set(
            self,
            key: str,
            value: Any,
            ttl: int | None = None,
            uttl: int | None = None,
            is_exists: bool = False,
            not_exist: bool = False,
            get_prev: bool = False,
    ) -> Any:
        return await self.client.set(key, value, ex=ttl, exat=uttl, xx=is_exists, nx=not_exist, get=get_prev)

import abc

from typing import Any


class IRedisStorage(abc.ABC):
    """Протокол хранилища ключ-значение"""

    @abc.abstractmethod
    async def get(self, key: str) -> Any: ...

    @abc.abstractmethod
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
        """

        :param key: Ключ
        :param value: Значение
        :param ttl: Время существования данных
        :param is_exists: Устанавливает значение для ключа, если значение уже существует
        :param not_exist: Устанавливает значение для ключа, только если значения еще не существует
        :param get_prev: Устанавливает значение для ключа, возвращает предыдущее значение, или None, если предыдущего не было
        :param uttl: Время сущеcтвования данных в unix
        :return:
        """
        ...



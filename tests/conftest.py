import uuid
from unittest.mock import AsyncMock
from faker import Faker as faker
import pytest
import pytest_asyncio
from asgi_lifespan import LifespanManager
from dishka import Provider, provide, Scope, make_async_container
from dishka.integrations.fastapi import setup_dishka
from starlette.testclient import TestClient

from src.app.main import create_app
from src.services.interfaces import IUploadService


class FakeServiceProvider(Provider):
    """Временный мок сервиса из - за несовместимости TestClient и асинхронных контейнеров Dishka"""
    @provide(scope=Scope.REQUEST)
    def service(self) -> IUploadService:
        fake_service = AsyncMock()
        resize_file_result = AsyncMock()
        get_task_status_result = AsyncMock()
        resize_file_result.task_id = str(uuid.uuid4())
        get_task_status_result.status = "SUCCESS"
        get_task_status_result.image_url = faker().url()
        fake_service.resize_file.return_value = resize_file_result
        fake_service.get_task_status.return_value = get_task_status_result
        return fake_service


@pytest.fixture
def service_provider():
    """Провайдер мок-сервиса"""
    return FakeServiceProvider()


@pytest_asyncio.fixture
async def client(service_provider):
    """Тестовый клиент"""
    container = make_async_container(service_provider)
    app = create_app()
    setup_dishka(container, app)
    async with LifespanManager(app):
        yield TestClient(app)

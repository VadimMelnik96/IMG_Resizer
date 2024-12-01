from fastapi import FastAPI
from dishka import make_async_container
from dishka.integrations.fastapi import FastapiProvider, setup_dishka

from src.app.routers.upload_router import router
from src.domain.exceptions.exception_handler import exception_config
from src.infrastructure.ioc import ApplicationProvider
from src.infrastructure.providers import RedisProvider
from src.infrastructure.settings.settings import settings, RedisSettings


def create_app() -> FastAPI:
    """Генерация приложения"""
    application = FastAPI(title=settings.app.name
    )
    application.include_router(router)
    container = make_async_container(ApplicationProvider(), FastapiProvider(), RedisProvider(), context={RedisSettings: settings.redis})
    setup_dishka(container, application)
    application.include_router(router)
    for exception, handler in exception_config.items():
        application.add_exception_handler(exception, handler)
    return application


app = create_app()

import structlog
from PIL import Image
from celery import Celery
from celery.result import AsyncResult

from src.infrastructure.settings.settings import settings

celery = Celery(__name__)

celery.conf.broker_url = str(settings.redis.dsn)
celery.conf.result_backend = str(settings.redis.dsn)

logger = structlog.get_logger()

@celery.task(name="resize_file")
def resize_file(file_path: str, new_file_path: str) -> None:
    """Задача изменения размера файла"""
    image = Image.open(file_path)
    logger.info(f"Original image size: {image.size}")
    new_image = image.resize((300, 300))
    logger.info(f"New image size: {new_image.size}")
    new_image.save(new_file_path)

import structlog
from PIL import Image
from celery import Celery


from src.infrastructure.settings.settings import settings

celery = Celery(__name__)

celery.conf.broker_url = str(settings.redis.dsn)
celery.conf.result_backend = str(settings.redis.dsn)

logger = structlog.get_logger()

@celery.task(name="resize_file")
def resize_file(file_path: str, new_file_path: str) -> None:
    """Задача изменения размера файла"""
    image = Image.open(file_path)
    logger.info(f"Оригинальный размер изображения: {image.size}, путь до файла: {file_path}")
    new_image = image.resize((300, 300))
    logger.info(f"Новый размер изображения: {new_image.size}, путь до файла: {new_file_path}")
    new_image.save(new_file_path)

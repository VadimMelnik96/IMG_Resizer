import shutil
import uuid

from celery.result import AsyncResult
from fastapi import UploadFile

from src.app.responses.status_response import StatusResponse
from src.app.responses.upload_responses import UploadResponse
from src.domain.celery.worker import resize_file
from src.domain.exceptions.exceptions import NotAllowedTypeError, NotAllowedSizeError
from src.infrastructure.storages.interfaces import IRedisStorage
from src.infrastructure.utils import make_paths
from src.services.interfaces import IUploadService


class UploadService(IUploadService):
    _allowed_types: list[str] = ["jpg", "jpeg", "png"]

    def __init__(self, storage: IRedisStorage):
        self.storage = storage

    async def resize_file(self, file: UploadFile) -> UploadResponse:
        """Метод сохранения исходного и измененного изображений"""
        await self._check_allowed_type(file)
        file_name = file.filename
        upload_file_path, resize_file_path = make_paths(file_name)
        with open(upload_file_path, 'wb') as f:
            shutil.copyfileobj(file.file, f)
        file.file.close()
        task: AsyncResult = resize_file.delay(upload_file_path, resize_file_path)
        await self.storage.set(key=str(task.task_id), value=resize_file_path)
        return UploadResponse(task_id=task.task_id)

    async def _check_allowed_type(self, file: UploadFile) -> None:
        """Функция проверки типа файла и размера"""
        if file.content_type.split("/")[1] not in self._allowed_types:
            raise NotAllowedTypeError
        elif file.size > 10 * 1024 * 1024:
            raise NotAllowedSizeError

    async def get_task_status(self, task_id: uuid.UUID) -> StatusResponse:
        """Метод получения статуса задачи"""
        task_result = AsyncResult(str(task_id))
        if task_result.state in ["PENDING", "FAILURE"]:
            return StatusResponse(status=task_result.state)
        elif task_result.state == "SUCCESS":
            image_url = await self.storage.get(key=str(task_id))
            return StatusResponse(status=task_result.state, image_url=image_url)

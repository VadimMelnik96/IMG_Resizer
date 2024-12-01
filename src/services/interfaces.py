import abc
import uuid

from fastapi import UploadFile

from src.app.responses.status_response import StatusResponse
from src.app.responses.upload_responses import UploadResponse


class IUploadService(abc.ABC):

    @abc.abstractmethod
    async def resize_file(self, file: UploadFile) -> UploadResponse:
        """Интерфейс метода сохранения файлов"""

    @abc.abstractmethod
    async def get_task_status(self, task_id: uuid.UUID) -> StatusResponse:
        """Интерфейс метода получения сведений о задаче изменения файлов"""

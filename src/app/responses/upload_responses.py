import uuid

from pydantic import BaseModel


class UploadResponse(BaseModel):
    """Схема ответа эндпоинта загрузки файла"""
    task_id: uuid.UUID

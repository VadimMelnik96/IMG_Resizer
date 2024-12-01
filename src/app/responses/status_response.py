from pydantic import BaseModel


class StatusResponse(BaseModel):
    """Схема ответа по статусу задачи"""
    status: str
    image_url: str | None = None

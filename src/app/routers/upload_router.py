import uuid

from dishka.integrations.fastapi import (
    FromDishka,
    inject,
)
from fastapi import APIRouter, UploadFile, File

from src.app.responses.status_response import StatusResponse
from src.app.responses.upload_responses import UploadResponse
from src.services.interfaces import IUploadService

router = APIRouter()


@router.post("/upload")
@inject
async def upload_file(service: FromDishka[IUploadService], file: UploadFile = File(...)) -> UploadResponse:
    """Входная точка загрузки изображения"""
    return await service.resize_file(file)


@router.get("/status/{task_id:uuid}")
@inject
async def get_status(task_id: uuid.UUID, service: FromDishka[IUploadService]) -> StatusResponse:
    """Получение статуса задачи"""
    return await service.get_task_status(task_id)

from fastapi import Request
from fastapi.exceptions import RequestValidationError
from starlette import status
from starlette.responses import JSONResponse

from src.domain.exceptions.exceptions import NotAllowedTypeError, NotAllowedSizeError


async def validation_exception_handler(request: Request, exception: RequestValidationError) -> JSONResponse:
    """Хэндлер ошибок валидации"""
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": "Validation error", "errors": exception.errors()},
    )


async def not_allowed_type_exception_handler(request: Request, exception: NotAllowedTypeError) -> JSONResponse:
    """Хэндлер ошибки типа"""
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": "Not allowed file type error."},
    )


async def not_allowed_size_exception_handler(request: Request, exception: NotAllowedSizeError) -> JSONResponse:
    """Хэндлер ошибки"""
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": "Not allowed file size error."},
    )



exception_config = {
    RequestValidationError: validation_exception_handler,
    NotAllowedTypeError: not_allowed_type_exception_handler,
    NotAllowedSizeError: not_allowed_size_exception_handler,
}

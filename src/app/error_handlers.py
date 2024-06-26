from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src.infrastructure.web_drivers.error import WebDriverException


async def web_driver_exception_error(request: Request, exc: WebDriverException) -> JSONResponse:

    return JSONResponse(
        status_code=500, content={"detail": "Ошибка при парсинге", 'help': 'Проверьте аргументы.', 'e': str(exc)}
        )


def init_exc_handlers(app: FastAPI) -> None:
    pass

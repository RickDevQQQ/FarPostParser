from fastapi import FastAPI

from src.app.error_handlers import init_exc_handlers
from src.app.routers import init_routers


def app_factory() -> FastAPI:
    app = FastAPI(
        title="Тестовое задание",
    )
    init_routers(app)
    init_exc_handlers(app)

    return app

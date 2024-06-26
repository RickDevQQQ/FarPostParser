from fastapi import FastAPI

from src.api.far_post.v1.http import far_post_api_router
from src.api.far_post_parser.v1.http.router import far_post_parser_api_router


def init_routers(app: FastAPI) -> None:
    app.include_router(far_post_parser_api_router)
    app.include_router(far_post_api_router)

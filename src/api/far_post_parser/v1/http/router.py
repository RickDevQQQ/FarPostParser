from typing import List

from fastapi import APIRouter

from src.api.far_post_parser.v1.http.schema import ParseListPostPageSchema
from src.core.entities.postdto import PostDto
from src.domain.parsers.far_post.service import FarPostService
from src.domain.post.repository import PostRepository
from src.domain.post.service import PostService
from src.infrastructure.db.sqlalchemy.settings import SessionAnnotated
from src.infrastructure.web_drivers.chrome import ChromeWebDriverAnnotated

far_post_parser_api_router = APIRouter(
    prefix='/far-post',
    tags=['Far PostDto | PARSER']
)


@far_post_parser_api_router.post(
    path='/parser/',
    response_model=List[PostDto]
)
async def parser(
    schema: ParseListPostPageSchema,
    chrome_web_driver: ChromeWebDriverAnnotated,
    session: SessionAnnotated
):
    far_post_service = FarPostService(web_driver=chrome_web_driver)
    posts = far_post_service.parser_list_page(url=schema.url, limit=schema.limit, offset=schema.offset)
    service = PostService(
        post_repository=PostRepository(
            session=session
        )
    )
    for post in posts:
        await service.create_or_update(post)

    await session.commit()
    return posts

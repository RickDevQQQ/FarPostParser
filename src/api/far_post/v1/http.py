from fastapi import APIRouter

from src.core.entities.postdto import PostDto
from src.domain.post.repository import PostRepository
from src.domain.post.service import PostService
from src.infrastructure.db.sqlalchemy.settings import SessionAnnotated

far_post_api_router = APIRouter(
    prefix='/far-post',
    tags=['Far Post']
)


@far_post_api_router.get(
    '/',
    summary="Получить список всех постов",
)
async def get_posts(session: SessionAnnotated):
    service = PostService(
        post_repository=PostRepository(session)
    )
    posts = await service.get_all()
    return posts


@far_post_api_router.get('/{post_id}')
async def get_post(session: SessionAnnotated, post_id: int):
    service = PostService(
        post_repository=PostRepository(session)
    )
    post = await service.get_by_id(post_id)
    return post

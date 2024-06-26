from typing import List
from src.core.entities.postdto import PostDto
from src.core.mappers.post import PostMapper
from src.core.services.post import AbstractPostService
from src.domain.post.repository import PostRepository


class PostService(AbstractPostService):

    def __init__(self, post_repository: PostRepository):
        self.post_repository = post_repository

    async def create_or_update(self, dto: PostDto) -> PostDto:
        model = await self.post_repository.get_by_id(dto.id)
        if not model:
            model = await self.post_repository.create(dto)
        else:
            model = await self.post_repository.update(model, dto)
        return PostMapper.from_post_model_to_post_dto(model)

    async def get_by_id(self, id_: int) -> PostDto:
        model = await self.post_repository.get_by_id(id_)
        return PostMapper.from_post_model_to_post_dto(model)

    async def get_all(self) -> List[PostDto]:
        models = await self.post_repository.get_all()
        return [
            PostMapper.from_post_model_to_post_dto(model)
            for model in models
        ]

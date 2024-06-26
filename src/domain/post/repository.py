from typing import List, Optional

from src.core.entities.postdto import PostDto
from src.core.mixin.sqlalhemy import SQLAlchemyAsyncSessionMixin
from src.core.repositories.post import AbstractPostRepository
from src.domain.post.model import PostModel


class PostRepository(AbstractPostRepository, SQLAlchemyAsyncSessionMixin):

    async def get_by_id(self, id_: int) -> Optional[PostModel]:
        return await PostModel.get_models(self.session, filters=[PostModel.id == id_], first=True)

    async def get_all(self) -> List[PostModel]:
        return await PostModel.get_models(self.session, filters=[], order_by=PostModel.id.asc())

    async def create(self, post: PostDto) -> PostModel:
        obj = PostModel(
            id=post.id,
            title=post.title,
            author=post.author,
            views_number=post.views_number,
            index=post.index
        )
        self.session.add(obj)
        return obj

    async def update(self, obj: PostModel, post: PostDto) -> PostModel:
        obj.author = post.author
        obj.title = post.title
        obj.index = post.index
        obj.views_number = post.views_number
        return obj

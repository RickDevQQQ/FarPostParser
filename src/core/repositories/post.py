from abc import ABC
from typing import List, Optional

from src.core.entities.postdto import PostDto
from src.domain.post.model import PostModel


class AbstractPostRepository(ABC):

    async def create(self, post: PostDto) -> PostModel:
        ...

    async def update(self, obj: PostModel, post: PostDto) -> PostModel:
        ...

    async def get_by_id(self, id_: int) -> Optional[PostModel]:
        ...

    async def get_all(self) -> List[PostModel]:
        ...


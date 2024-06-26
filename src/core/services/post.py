from abc import ABC, abstractmethod
from typing import List

from src.core.entities.postdto import PostDto


class AbstractPostService(ABC):

    @abstractmethod
    async def create_or_update(self, post: PostDto) -> PostDto:
        ...

    @abstractmethod
    async def get_by_id(self, id_: int) -> PostDto:
        ...

    @abstractmethod
    async def get_all(self) -> List[PostDto]:
        ...

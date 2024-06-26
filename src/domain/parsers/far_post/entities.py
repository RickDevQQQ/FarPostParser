from dataclasses import dataclass
from typing import Self

__all__ = (
    'ListPagePost',
    'DetailPagePost'

)


@dataclass(frozen=True)
class ListPagePost:
    id: int
    title: str
    views_number: int
    detail_url: str
    index: int

    def __eq__(self, other: Self) -> bool:
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)


@dataclass(frozen=True)
class DetailPagePost:
    author: str

    def __eq__(self, other: Self) -> bool:
        return self.author == other.author

    def __hash__(self) -> int:
        return hash(self.author)

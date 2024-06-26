from dataclasses import dataclass


@dataclass(frozen=True)
class PostDto:
    id: int
    title: str
    author: str
    views_number: int
    index: int

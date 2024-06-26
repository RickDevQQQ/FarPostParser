from abc import ABC, abstractmethod
from typing import List

from src.core.entities.postdto import PostDto


class AbstractFarPostParserService(ABC):

    @abstractmethod
    def parser_list_page(self, url: str) -> List[PostDto]:
        """Парсинг списка объявлений"""
        ...

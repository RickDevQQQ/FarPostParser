from abc import abstractmethod, ABC
from typing import List

from src.config import config
from src.domain.parsers.far_post.entities import ListPagePost, DetailPagePost


class AbstractListPageFarPostServiceParserInterface(ABC):
    FAR_POST_MAIN_URL = config.FAR_POST_URL

    @abstractmethod
    def get_posts_from_html(self, html_page: str, obj_limit: int = 10) -> List[ListPagePost]:
        """Метод позволяет получить определенное количество объявлений"""
        ...


class AbstractListPageFarPostServiceHTMLParserInterface(AbstractListPageFarPostServiceParserInterface, ABC):
    ALL_OBJ_SEARCH_INFO = {
        'attr': 'data-source',
        'value': 'actual'
    }
    TITLE_SEARCH_INFO = {
        'attr': 'data-role',
        'value': 'bulletin-link'
    }
    ADDRESS_SEARCH_INFO = {
        'attr': 'class',
        'value': 'address'
    }
    VIEWS_SEARCH_INFO = {
        'attr': 'class',
        'value': 'views'
    }
    ID_ATTR_KEY = 'name'


class AbstractDetailPageFarPostServiceParserInterface(ABC):

    @abstractmethod
    def get_detail_post_from_html(self, html_page: str) -> DetailPagePost:
        """Метод позволяет получить детальную информацию об объявлении"""
        ...


class AbstractDetailPageFarPostServiceHTMLParserInterface(AbstractDetailPageFarPostServiceParserInterface, ABC):
    TITLE_SEARCH_INFO = {
        'attr': 'data-field',
        'value': 'subject'
    }
    AUTHOR_SEARCH_INFO = {
        'attr': 'class',
        'value': 'userNick'
    }

from typing import List

from bs4 import PageElement

from src.core.mixin.bs import BeautifulSoupMixin
from src.domain.parsers.far_post.entities import ListPagePost
from src.core.parsers.far_post import AbstractListPageFarPostServiceHTMLParserInterface


class ListPageFarPostServiceBSHTMLParserInterface(
    AbstractListPageFarPostServiceHTMLParserInterface, BeautifulSoupMixin
):
    """
    Интерфейс для парсинга данных списка объявлений
    Интерфейс реализует парсинг данных из HTML с использованием BS(BeautifulSoup)
    """

    def get_posts_from_html(self, html_page: str, offset: int = 10, limit: int = 10) -> List[ListPagePost]:
        soup = self._get_beautiful_soup(html_page)

        raw_html_posts_info = soup.find_all(attrs={self.ALL_OBJ_SEARCH_INFO['attr']: self.ALL_OBJ_SEARCH_INFO['value']})

        result_list_page_objs = []
        for index, raw_element in enumerate(raw_html_posts_info[offset:limit]):
            title_element = self._get_title_from_element(raw_element)
            title_text = title_element.text
            detail_url = self.FAR_POST_MAIN_URL + title_element.get('href')
            views_element = self._get_views_from_element(raw_element)
            result_list_page_objs.append(
                ListPagePost(
                    id=self._get_id_from_element(raw_element),
                    title=title_text,
                    detail_url=detail_url,
                    index=index,
                    views_number=int(views_element.text)
                )
            )
        return result_list_page_objs

    def _get_id_from_element(self, element: PageElement) -> int:
        return int(element.next.next.next.next.get(self.ID_ATTR_KEY))

    def _get_title_from_element(self, element: PageElement):
        return element.find_next(attrs={self.TITLE_SEARCH_INFO['attr']: self.TITLE_SEARCH_INFO['value']})

    def _get_address_from_element(self, element: PageElement):
        return element.find_next(attrs={self.ADDRESS_SEARCH_INFO['attr']: self.ADDRESS_SEARCH_INFO['value']})

    def _get_views_from_element(self, element: PageElement):
        return element.find_next(attrs={self.VIEWS_SEARCH_INFO['attr']: self.VIEWS_SEARCH_INFO['value']})

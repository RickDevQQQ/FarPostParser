from src.core.mixin.bs import BeautifulSoupMixin
from src.domain.parsers.far_post.entities import DetailPagePost
from src.core.parsers.far_post import AbstractDetailPageFarPostServiceHTMLParserInterface


class DetailPageFarPostServiceBSHTMLParserInterface(
    AbstractDetailPageFarPostServiceHTMLParserInterface, BeautifulSoupMixin
):
    """
       Интерфейс для парсинга данных объявления
       Интерфейс реализует парсинг данных из HTML с использованием BS(BeautifulSoup)
    """

    def get_detail_post_from_html(self, html_page: str) -> DetailPagePost:
        soup = self._get_beautiful_soup(html_page)
        raw_html_detail_post = soup.find(attrs={self.AUTHOR_SEARCH_INFO['attr']: self.AUTHOR_SEARCH_INFO['value']})
        return DetailPagePost(author=raw_html_detail_post.text)

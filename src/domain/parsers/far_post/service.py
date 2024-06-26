from typing import List

from selenium.webdriver.common.by import By

from src.core.entities.postdto import PostDto
from src.core.mappers.post import PostMapper
from src.core.services.fat_post_parser import AbstractFarPostParserService
from src.core.web_driver import AbstractWebDriverInterface
from src.domain.parsers.far_post.detail_post import DetailPageFarPostServiceBSHTMLParserInterface
from src.domain.parsers.far_post.list_post import ListPageFarPostServiceBSHTMLParserInterface


class FarPostService(AbstractFarPostParserService):

    def __init__(self, web_driver: AbstractWebDriverInterface) -> None:
        self.web_driver = web_driver

    def parser_list_page(self, url: str, *, offset: int = 0, limit: int = 10) -> List[PostDto]:

        self.web_driver.load_page(url=url)
        self.web_driver.wait_load_page(attr=By.ID, value="filtersForm")

        # парсим страницу списка объявлений, чтобы получить минимальную информацию об объявлениях
        list_page_far_post_bs_parser = ListPageFarPostServiceBSHTMLParserInterface()
        list_page_post_objs = list_page_far_post_bs_parser.get_posts_from_html(
            html_page=self.web_driver.get_active_page(), limit=limit, offset=offset
        )
        detail_page_far_post_bs_parser = DetailPageFarPostServiceBSHTMLParserInterface()
        author_info = detail_page_far_post_bs_parser.AUTHOR_SEARCH_INFO

        result_posts = []
        for list_page_post in list_page_post_objs:
            # Переходим на страницу объявления для получения более детальной информации
            self.web_driver.load_page(url=list_page_post.detail_url)
            self.web_driver.wait_load_page(attr=By.CLASS_NAME, value=author_info['value'])

            detail_page_post = detail_page_far_post_bs_parser.get_detail_post_from_html(
                html_page=self.web_driver.get_active_page()
            )
            # Преобразуем данные получение со списка объявлений и объявлений в одним объект
            result_posts.append(PostMapper.from_parser_page_obj_to_post(list_page_post, detail_page_post))
        return result_posts

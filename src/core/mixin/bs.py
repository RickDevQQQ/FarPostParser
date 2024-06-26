from bs4 import BeautifulSoup


class BeautifulSoupMixin:
    @staticmethod
    def _get_beautiful_soup(html_page: str) -> BeautifulSoup:
        return BeautifulSoup(html_page, 'html.parser')

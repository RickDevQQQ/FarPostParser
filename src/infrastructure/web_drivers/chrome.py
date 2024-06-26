from typing import Optional, Annotated

from fastapi import Depends
from selenium import webdriver
from selenium.common import TimeoutException, WebDriverException as SeleniumWebDriverException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.core.web_driver import AbstractWebDriverInterface
from src.infrastructure.web_drivers.error import WebDriverTimeoutError, WebDriverException as AppWebDriverException

__all__ = (
    'ChromeWebDriverInterface',
    'ChromeWebDriverAnnotated'
)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')


class ChromeWebDriverInterface(AbstractWebDriverInterface):

    def __init__(self, options: Optional[webdriver.ChromeOptions] = None):
        self.driver = webdriver.Chrome(options=options)

    def get_active_page(self) -> str:
        return self.driver.page_source

    def load_page(self, url: str) -> None:
        try:
            self.driver.get(url)
        except SeleniumWebDriverException:
            raise AppWebDriverException()

    def wait_load_page(self, attr: str, value: str) -> None:
        try:
            WebDriverWait(self.driver, self.TIME_OUT).until(
                EC.presence_of_element_located((attr, value))
            )
        except TimeoutException:
            raise WebDriverTimeoutError()


def get_chrome_web_driver() -> ChromeWebDriverInterface:
    web_driver = ChromeWebDriverInterface(options=chrome_options)
    yield web_driver
    web_driver.driver.close()


ChromeWebDriverAnnotated = Annotated[ChromeWebDriverInterface, Depends(get_chrome_web_driver)]

from abc import ABC, abstractmethod
from selenium.webdriver.common.by import By

from src.config import config

__all__ = (
    'AbstractWebDriverInterface',
)


class AbstractWebDriverInterface(ABC):
    TIME_OUT = config.WEB_DRIVER_TIME_OUT

    @abstractmethod
    def load_page(self, url: str) -> None:
        """Метод загружает страницу"""
        ...

    @abstractmethod
    def get_active_page(self) -> str:
        """Метод возвращает актуальную страницу"""
        ...

    @abstractmethod
    def wait_load_page(self, attr: By, value: str) -> None:
        """
        Метод ожидает когда на странице появится элемент

        :param attr: Атрибут по которому ищем.
        :param value: Значение которое должно быть.
        :raise WebDriverTimeoutError: Превышено время ожидания страницы.
        """
        ...

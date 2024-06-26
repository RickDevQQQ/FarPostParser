from src.core.exception import AppException

__all__ = (
    'WebDriverException',
    'WebDriverTimeoutError',
)


class WebDriverException(AppException):
    """Ошибка связанные с веб драйвером"""


class WebDriverTimeoutError(WebDriverException):
    """Превышено время ожидания"""

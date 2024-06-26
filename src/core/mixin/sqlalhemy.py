from sqlalchemy.ext.asyncio import AsyncSession


class SQLAlchemyAsyncSessionMixin:

    def __init__(self, session: AsyncSession):
        self.__session = session

    @property
    def session(self):
        return self.__session


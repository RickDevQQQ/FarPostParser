from typing import Annotated

from fastapi import Depends
from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession

from src.config import config

async_engine = create_async_engine(
    url=config.default_asyncpg_url,
    echo=config.ECHO,
)

async_session_factory = async_sessionmaker(async_engine, expire_on_commit=False)

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}
metadata_obj = MetaData(naming_convention=convention)


async def get_async_session() -> AsyncSession:
    async with async_session_factory() as session:
        yield session


SessionAnnotated = Annotated[AsyncSession, Depends(get_async_session)]

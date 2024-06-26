from typing import List, Optional, Self, Union

from sqlalchemy import MetaData, Integer, BinaryExpression, ColumnElement, select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column, Load

from src.infrastructure.db.sqlalchemy.settings import metadata_obj


class Model(DeclarativeBase):
    __abstract__ = True
    metadata = metadata_obj

    repr_cols_num = 3
    repr_cols = tuple()

    def __repr__(self):
        """Relationships не используются в repr(), т.к. могут вести к неожиданным подгрузкам"""
        cols = []
        for idx, col in enumerate(self.__table__.columns.keys()):
            if col in self.repr_cols or idx < self.repr_cols_num:
                cols.append(f"{col}={getattr(self, col)}")

        return f"<{self.__class__.__name__} {', '.join(cols)}>"

    @classmethod
    @declared_attr
    def __tablename__(cls) -> str:
        result = ""
        for item in cls.__name__:
            if item.isupper():
                result += "_"
            result += item
        return result[1:].lower()

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, doc="ИД записи")

    @classmethod
    async def get_models(
        cls,
        session: AsyncSession,
        filters: List[BinaryExpression | bool],
        load_options: Optional[List[Load]] = None,
        joins: Optional[List] = None,
        order_by: Optional[ColumnElement] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        first: bool = False
    ) -> Union[List[Self] | Self]:
        query = select(cls)
        if limit:
            query = query.limit(limit)
        if offset:
            query = query.offset(offset)
        if joins:
            for join_model, on_clause in joins:
                if on_clause is not None:
                    query = query.join(join_model, on_clause)
                else:
                    query = query.join(join_model)
        if filters:
            query = query.filter(*filters)
        if load_options:
            for option in load_options:
                query = query.options(option)

        query = query.order_by(order_by)
        result = await session.execute(query)
        if first:
            return result.scalars().first()
        return list(result.scalars().all())
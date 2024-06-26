from sqlalchemy.orm import Mapped

from src.infrastructure.db.sqlalchemy.model import Model


class PostModel(Model):
    __tablename__ = 'post'

    title: Mapped[str]
    author: Mapped[str]
    views_number: Mapped[int]
    index: Mapped[int]

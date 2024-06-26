from pydantic import BaseModel, HttpUrl, Field


class ParseListPostPageSchema(BaseModel):
    url: str
    offset: int = Field(default=0, ge=0)
    limit: int = Field(default=10, ge=0)

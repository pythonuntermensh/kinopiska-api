import datetime
from uuid import UUID, uuid4

from typing import Optional
from pydantic import BaseModel, Field

DEFAULT_PICTURE_URL: str = ("https://ei.phncdn.com/(m=bJWs4Lp)("
                            "mh=0tJZQUu3Z1Onu_2j)2294c515-f5b8-4542-8ba9-bbba927c6c9f.jpg")


class FilmModel(BaseModel):
    uuid: UUID = Field(default_factory=uuid4)
    name: str = Field(min_length=1)
    release_year: Optional[str] = Field(default_factory=lambda: str(datetime.datetime.now().year))
    description: Optional[str] = Field(default="")
    genre: Optional[list[str]] = Field(default_factory=list)
    picture_url: Optional[str] = Field(default=DEFAULT_PICTURE_URL)

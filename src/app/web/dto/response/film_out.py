from pydantic import BaseModel
from typing import Optional
from uuid import UUID


class FilmOut(BaseModel):
    uuid: UUID
    name: Optional[str]
    release_year: Optional[str]
    picture_url: Optional[str]

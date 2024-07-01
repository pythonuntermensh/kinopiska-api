from pydantic import BaseModel
from uuid import UUID


class FilmDetailedOut(BaseModel):
    uuid: UUID
    name: str
    release_year: str
    description: str
    genre: list
    picture_url: str

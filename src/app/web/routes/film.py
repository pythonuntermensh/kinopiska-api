from fastapi import APIRouter, Depends

from data.film import get_films, get_film_by_id
from model import FilmModel
from web.dto.response import FilmOut, FilmDetailedOut

router = APIRouter(prefix="/films")


@router.get("/", response_model=list[FilmOut])
async def get_all_films(films: list[FilmModel] = Depends(get_films)) -> list[FilmModel]:
    return films


@router.get("/{uuid}", response_model=FilmDetailedOut)
async def get_all_films(uuid: str) -> FilmModel:
    return get_film_by_id(uuid)

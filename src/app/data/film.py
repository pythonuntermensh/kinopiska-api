from model import FilmModel

_test_data: list[FilmModel] = [
    FilmModel(name="Test1"),
    FilmModel(name="Test2",
              description="One more simple film description",
              release_year="2000",
              genre=list(["anime", "porn"]))
]


def get_films() -> list[FilmModel]:
    return _test_data


def get_film_by_id(uuid: str) -> FilmModel:
    for film in _test_data:
        print(film.uuid, uuid)
        if str(film.uuid) == uuid:
            return film

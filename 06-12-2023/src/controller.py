from utils import Album
from typing import Callable

import db


def add(name: str, year: str | int, author: str, debut: int | bool = False) -> Album:
    """
    Validates all data and then writes it into the file
    """

    if name.isspace() or len(name) == 0:  # Validates album's name
        raise ValueError("Nome do álbum não pode ser vazio!")

    if not year.isdigit():  # Validate album's release year
        raise ValueError("Ano de lançamento deve ser um número!")

    if author.isspace() or len(author) == 0:  # Validate album's author name
        raise ValueError("Nome do artista/banda não pode ser vazio!")

    return db.write(Album(name, year, author, debut))  # Writes it to the file


def get(filter: Callable[[Album], bool] = (lambda _: True), order: Callable[[Album], any] = (lambda album: album.name)) -> list[Album]:
    """
    Returns all registered albums that matches the filter
    """

    albums: list[Album] = []

    for album in db.index():
        if filter(album):  # Applies filter
            albums.append(album)  # Add those that matches it

    return sorted(albums, key=order)

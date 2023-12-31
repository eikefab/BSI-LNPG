import db


def create_album(album: str, release_year: str, author: str, debut: bool, alert):
    if len(album) == 0:
        alert("O título do álbum não pode ser vazio!")

        return False

    if not release_year.isdigit():
        alert("O ano do álbum deve ser um ano válido!")

        return False

    if len(author) == 0:
        alert("O autor do álbum não pode ser vazio!")

        return False

    db.register(album, release_year, author, debut)

    alert(f"Álbum {album} criado!")

    return True


def list_albums():
    return db.index()


def sort_albums(data=[], by: int = 0, descending: bool = False):
    if len(data) == 0:
        return []
    
    if by > len(data[0]):
        return []

    return sorted(data, key=lambda item: item[by], reverse=descending)


def list_albums_sorted(by: int = 0, descending: bool = False):
    return sorted(list_albums(), key=lambda item: item[by], reverse=descending)


def get_albums_by_author(author: str):
    albums = []

    for data in list_albums():
        if author.lower() in data[2].lower():
            albums.append(data)

    return albums


def get_albums_by_year(year: int):
    albums = []

    for data in list_albums():
        if year == int(data[1]):
            albums.append(data)

    return albums


def filter_albums_by_year(year: int, greater: bool = False):
    albums = []

    for data in list_albums():
        release_year = int(data[1])

        if greater:
            if release_year >= year:
                albums.append(data)
        else:
            if release_year <= year:
                albums.append(data)

    return albums

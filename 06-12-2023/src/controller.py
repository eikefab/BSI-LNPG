import db

def create_album(album: str, release_year: int, author: str, debut: bool):
    db.register(album, release_year, author, debut)

def list_albums():
    return db.index()

def list_albums_sorted(by: int = 0, descending: bool = False):
    return sorted(list_albums(), key=lambda item: item[by], reverse=descending)

def get_albums_by_author(author: str):
    pass

def get_albums_by_year(year: int):
    pass

def filter_albums_by_year(year: int, greater: bool = False):
    pass
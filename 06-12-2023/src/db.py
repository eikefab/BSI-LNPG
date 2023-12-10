from utils import Album


file_path = "data.txt" # File where all previous data were written


def index() -> list[Album]:
    """
    Returns all registered albums
    """

    albums: list[Album] = []

    with open(file_path, "r") as file:
        raw = file.read()

        for line in raw.split("\n"):
            info = line.split("\t")

            if len(info) < 4:  # Check if it's not a empty line nor invalid info
                continue

            name, year, author, debut = info  # Decomposes the info

            albums.append(Album(name, year, author, debut))

    return albums


def write(album: Album) -> Album:
    """
    Writes album data to file
    """

    with open(file_path, "a") as file:
        file.write(f"\n{album.name}\t{album.year}\t{album.author}\t{album.debut}\n")

    return album
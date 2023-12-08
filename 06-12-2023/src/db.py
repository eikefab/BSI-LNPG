path = 'data.txt'

def index():
    data = []

    with open(path, 'r') as file:
        raw = file.read()

        for line in raw.split("\n"):
            info = line.split('\t')

            if len(info) < 4:
                continue

            data.append(info)
        
    return data

def register(album: str, release_year: int, author: str, debut: bool):
    with open(path, 'a') as file:
        file.write(f"{album}\t{release_year}\t{author}\t{debut}\n")
path = 'data.txt'

def index():
    data = []

    with open(path, 'r') as file:
        info = file.read()

        for line in info.split('\n'):
            person = line.split("\t")

            if len(person) < 4:
                continue

            data.append(person)

    return data

def fetch_by_sex(target: str):
    if len(target) > 1:
        target = target[0]

    if target not in ['M', 'F']:
        return []

    fetched = []

    for data in index():
        sex = data[2]

        if sex == target:
            fetched.append(data)

    return fetched

def fetch_by_name(target: str):
    fetched = []

    for data in index():
        name = data[0]

        if target in name:
            fetched.append(data)
    
    return fetched

def write(data: str):
    with open(path, 'a') as file:
        file.write(data)
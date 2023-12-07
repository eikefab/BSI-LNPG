from db import index, write, fetch_by_name, fetch_by_sex

def run():
    for line in [
        '1 - Ver pessoas cadastradas',
        '2 - Filtrar pessoas cadastradas por sexo',
        '3 - Filtrar pessoas cadastradas por nome',
        '4 - Cadastrar novas pessoas',
        '5 - Sair'
    ]:
        print(line)
    
    option = input('> ')

    while not option.isdigit() or (int(option) < 1 or int(option) > 5):
        print('Opção inválida! (1-5)')

        option = input('> ')

    option = int(option)

    return option

def output(data):
    name, age, sex, telephone = data

    for line in [
            'Nome: ' + name,
            'Sexo: ' + ('Masculino' if sex == 'M' else 'Feminino'),
            'Idade: ' + age + ' anos',
            'Telefone: ' + telephone,
            ''
        ]:
            print(line)

def list_people():
    raw = index()

    print(f"Pessoas cadastradas até então ({len(raw)}):")
    print()

    for data in index():
        output(data)

def fetch_people_by_sex():
    sex = input('Sexo (M ou F): ')

    while sex not in ['M', 'F']:
        print('Sexo inválido!')

        sex = input('Sexo (M ou F): ')

    raw = fetch_by_sex(sex)

    print(f'Foram encontradas {len(raw)} pessoas.')
    print()

    for data in raw:
        output(data)

def fetch_people_by_name():
    name = input('Nome: ')
    raw = fetch_by_name(name)

    print(f'Foram encontradas {len(raw)} pessoas.')
    print()

    for data in raw:
        output(data)

def register_people():
    name = input('Nome: ')
    age = input('Idade: ')
    sex = input('Sexo (M ou F): ')
    telephone = input('Telefone: ')

    while not age.isdigit() or int(age) < 1:
        print('Idade inválida!')

        age = input('Idade: ')
    
    while sex not in ['M', 'F']:
        print('Sexo inválido!')

        sex = input('Sexo: ')

    write(f'{name}\t{age}\t{sex}\t{telephone}\n')
    print('Pessoa cadastrada com sucesso!')
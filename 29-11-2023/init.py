from menu import run, list_people, fetch_people_by_name, fetch_people_by_sex, register_people

def __init__():
    option = run()
    handlers = [list_people, fetch_people_by_sex, fetch_people_by_name, register_people]

    while option != 5:
        handler = handlers[option - 1]
        handler()

        option = run()
    
    print('Programa encerrado.')

__init__()
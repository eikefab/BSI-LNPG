def read():
    with open('data.txt', 'r', encoding='UTF-8') as file:
        data = file.read()
        
        for info in data.split("\n"):
            print(info)

def write(data: str):
    with open('data.txt', 'a', encoding='UTF-8') as file:
        file.write(data)
    
def main():
    print("Dados já cadastrados:")
    read()

    data = ""

    while 1:
        name = input("Nome: ")

        if name == '0':
            print("Programa encerrado, dados salvos.")

            break
            
        name = input("Nome: ")

        if name == '0':
            print("Programa encerrado.")

            break
        
        age = input("Idade: ")

        while not age.isdigit() or int(age) < 1:
            print("Idade inválida!")

            age = input("Idade: ")
        
        age = int(age)

        sex = input("Sexo (M ou F): ").upper()

        while sex not in ['M', 'F']:
            print("Sexo inválido!")

            sex = input("Sexo (M ou F): ")

        number = input("Telefone: ")
    
        data += f"{name}\t{age}\t{sex}\t{number}\n"
    
    write(data)

main()
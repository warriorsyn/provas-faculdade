import models

from clients import get_activated_clients, create_client, get_all_clients
from vacancy import create_vacancy, get_vacancies

# Main program
# Local variables
menus = [
    '1 - Cadastrar clientes',
    '2 - Registro de aluguel',
    '3 - Relatório de vagas',
    '4 - Relatório de clientes ativos',
    '0 - Fechar programa'
]


# End local variables

# Local functions


# Local functiob to add clients
def add_clients():
    # Utilizar o bloco try catch quando status diferente de ativo ou inativo e perfuntar novamente
    name = input("Insira o nome: ")
    cpf = input("Insira o CPF: ")
    car_board = input("Insira a placa do carro: ")
    status = int(input("Insira o status: "))

    # if status != Status.ACTIVE or status != Status.INACTIVE:
    #     raise Exception("Insira um status valido (1 - ATIVO ou 2 - INATIVO)")

    client = models.Client(name, cpf, car_board, status)

    create_client(client)


# Local function to load all clients
def load_activated_clients():
    active_clients = get_activated_clients()
    print("=============================")
    print("RELATÓRIO DE CLIENTES")
    for active in active_clients:
        print(active)
    print("=============================")


# Local function nto add vacancies
def add_vacancies():
    cpf = input("Informe o CPF: ")

    client = [x for x in get_all_clients() if x.cpf == cpf]

    if not client:
        raise ('Nenhum CPF foi encontrado!')

    create_vacancy(models.Vacancy(client))


# Local function to
def load_vacancies():
    data = get_vacancies()
    print("=============================")
    print("RELATÓRIO DE VAGAS")
    for vc in data:
        print(vc)
    print("=============================")


# Local function to handle menu selection
def handle_menu_option(option):
    if option == 1:
        add_clients()
    if option == 2:
        add_vacancies()
    if option == 3:
        load_vacancies()
    if option == 4:
        load_activated_clients()


# End functions
while True:
    for menu in menus:
        print(menu)

    options = int(input("Escolha uma Opção: "))

    if not options:
        break

    handle_menu_option(option=options)

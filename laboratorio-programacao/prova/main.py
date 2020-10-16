# Models
class Client:
    def __init__(self, name, cpf, board, status):
        self.name = name
        self.cpf = cpf
        self.board = board
        self.status = status

    def __str__(self):
        return f"Nome: {self.name}\nCPF: {self.cpf}\nPlaca:{self.board}\nStatus:{self.get_status_name()}\n-----------------"

    def __repr__(self):
     return f"Nome: {self.name} CPF: {self.cpf} Placa:{self.board} Status:{self.get_status_name()}"

    def get_status_name(self):
        if self.status == Status.ACTIVE:
            return 'Ativo'
        
        if self.status == Status.INACTIVE:
            return 'Inativo'


class Vacancy:
    def __init__(self, client):
        self.client = client

    def __str__(self):
        return f'{self.client}'


class Status:
    ACTIVE = 1
    INACTIVE = 2

# End models

# external functions

clients = []

vacancies = []

def createClient(client: Client):
    if(any(x.cpf == client.cpf for x in clients)):
        raise('Cliente com este cpf já cadastrado')
    clients.append(client)

def getAllClients():
    return clients

def getActivatedClients():
    return filter(lambda client: client.status == Status.ACTIVE, clients)

def createVacancy(vacancy: Vacancy):
    if(len(vacancies) >= 20):
        raise('Cliente com este cpf já cadastrado')
    vacancies.append(vacancy)

def getVacancies():
    return vacancies
# End external functions

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
def addClients():
    # Utilizar o bloco try catch quando status diferente de ativo ou inativo e perfuntar novamente
    name = input("Insira o nome: ")
    cpf = input("Insira o CPF: ")
    car_board = input("Insira a placa do carro: ")
    status = int(input("Insira o status: "))

    # if status != Status.ACTIVE or status != Status.INACTIVE:
    #     raise Exception("Insira um status valido (1 - ATIVO ou 2 - INATIVO)")

    client = Client(name,cpf,car_board, status)

    createClient(client)

# Local functio to load all clients
def loadActivatedClients():
    active_clients = getActivatedClients()
    print("=============================")
    print("RELATÓRIO DE CLIENTES")
    for active in active_clients:
        print(active)
    print("=============================")


# Local functio nto add vacancies
def addVacancies():
    cpf = input("Informe o CPF: ")

    client = [x for x in getAllClients() if x.cpf == cpf ]

    if not client:
        raise('Nenhum CPF foi encontrado!')

    createVacancy(Vacancy(client))

# Local function to
def loadVacancies():
    data = getVacancies()
    print("=============================")
    print("RELATÓRIO DE VAGAS")
    for vc in data:
        print(vc)
    print("=============================")

# Local function to handle menu selection
def handleMenuOption(option):
    if(option == 1):
        addClients()
    if(option == 2):
        addVacancies()
    if(option == 3):
        loadVacancies()
    if(option == 4):
        loadActivatedClients()
       
    
# End functions
while True:
    for menu in menus:
        print(menu)

    option = int(input("Escolha uma Opção: "))

    if not option:
        break

    handleMenuOption(option=option)

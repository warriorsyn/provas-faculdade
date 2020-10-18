class Client:
    def __init__(self, name, cpf, board, status):
        self.name = name
        self.cpf = cpf
        self.board = board
        self.status = status

    def __str__(self):
        return f"----------------- " \
               f"\nNome: {self.name}\nCPF: {self.cpf}\nPlaca:{self.board}\nStatus:{self.get_status_name()}\n" \
               f"----------------- "

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
    INACTIVE = 2,



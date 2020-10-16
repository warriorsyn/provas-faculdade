class Clients:
    def __init__(self, name, cpf, board, status):
        self.name = name
        self.cpf = cpf
        self.board = board
        self.status = status

class Status:
    ACTIVE = 1,
    INACTIVE = 2

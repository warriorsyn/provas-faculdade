import models

clients = []


def create_client(client: models.Client):
    if any(x.cpf == client.cpf for x in clients):
        raise Exception('Cliente com este CPF já cadastrado!')
    clients.append(client)


def get_all_clients():
    return clients


def get_activated_clients():
    return filter(lambda client: client.status == models.Status.ACTIVE, clients)

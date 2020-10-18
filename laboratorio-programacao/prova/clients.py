import models
import csv

clients = []
clients_csv = []


def get_clients_csv():
    with open('database/clients.csv', 'rt') as csv_out:
        for row in csv.reader(csv_out, delimiter=',', quotechar='|'):
            if row:
                clients_csv.append(','.join(row))


def add_clients_to_file(data):
    with open('database/clients.csv', 'a') as csv_out:
        write = csv.writer(csv_out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        write.writerow(data)


def populate_clients():
    for seed in clients_csv:
        seed_split = seed.split(',')
        client = models.Client(seed_split[0], seed_split[1], seed_split[2], int(seed_split[3]))
        clients.append(client)


def create_client(client: models.Client):
    if any(x.cpf == client.cpf for x in clients):
        raise Exception('Cliente com este CPF já cadastrado!')
    clients.append(client)

    client_data = f"{client.name},{client.cpf},{client.board},{client.status}"
    add_clients_to_file(client_data.split(','))


def get_all_clients():
    return clients


def get_activated_clients():
    return filter(lambda client: client.status == models.Status.ACTIVE, clients)


get_clients_csv()
populate_clients()

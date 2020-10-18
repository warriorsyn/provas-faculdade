import models
import csv

vacancies = []
vacancy_csv = []


def get_vacancy_csv():
    with open('database/vacancy.csv', 'rt') as csv_out:
        for row in csv.reader(csv_out, delimiter=',', quotechar='|'):
            if row:
                vacancy_csv.append(','.join(row))


def populate_vacancy():
    for seed in vacancy_csv:
        seed_split = seed.split(',')
        client = models.Client(seed_split[0], seed_split[1], seed_split[2], int(seed_split[3]))
        vacancy = models.Vacancy(client)

        vacancies.append(vacancy)


def add_vacancy__to_file(data):
    with open('database/vacancy.csv', 'a') as csv_out:
        write = csv.writer(csv_out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        write.writerow(data)


def create_vacancy(vacancy: models.Vacancy):
    if len(vacancies) >= 20:
        raise Exception('Todas as vagas já foram preenchidas!')
    vacancies.append(vacancy)

    vacancy_client = f"{vacancy.client.name},{vacancy.client.cpf},{vacancy.client.board},{vacancy.client.status}"

    add_vacancy__to_file(vacancy_client.split(','))


def get_vacancies():
    return vacancies


get_vacancy_csv()
populate_vacancy()

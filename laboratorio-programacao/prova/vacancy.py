import models

vacancies = []


def create_vacancy(vacancy: models.Vacancy):
    if len(vacancies) >= 20:
        raise ('Cliente com este cpf já cadastrado')
    vacancies.append(vacancy)


def get_vacancies():
    return vacancies

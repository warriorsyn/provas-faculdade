import models

vacancies = []


def create_vacancy(vacancy: models.Vacancy):
    if len(vacancies) >= 20:
        raise Exception('Todas as vagas já foram preenchidas')
    vacancies.append(vacancy)


def get_vacancies():
    return vacancies

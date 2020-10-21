from models import Patient

import csv

file_path = 'database/patient.csv'

patients = []
patient_csv = []


def get_patients_csv():
    with open(file_path, 'rt') as csv_out:
        for row in csv.reader(csv_out, delimiter=',', quotechar='|'):
            if row:
                patient_csv.append(','.join(row))


def populate_patient():
    for seed in patient_csv:
        seed_split = seed.split(',')
        patient = Patient(seed_split[0], seed_split[1], seed_split[2])
        patients.append(patient)


def add_patient_to_file(data):
    with open(file_path, 'a') as csv_out:
        write = csv.writer(csv_out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        write.writerow(data)


def create_patient(patient: Patient):
    if any(x.cpf == patient.cpf for x in patients):
        raise Exception('Paciente com este CPF já cadastrado!')

    patients.append(patient)

    patient_data = f"{patient.name},{patient.cpf},{patient.genre}"
    add_patient_to_file(patient_data.split(','))


def get_patient_by_cpf(cpf):
    return [x for x in patients if x.cpf == cpf]


def get_patients():
    return patients


get_patients_csv()
populate_patient()

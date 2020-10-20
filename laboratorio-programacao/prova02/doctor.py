from models import Doctor, Status, Genre

import csv

file_path = 'database/doctor.csv'

doctors = []
doctor_csv = []


def get_doctors_csv():
    with open(file_path, 'rt') as csv_out:
        for row in csv.reader(csv_out, delimiter=',', quotechar='|'):
            if row:
                doctor_csv.append(','.join(row))


def populate_doctor():
    for seed in doctor_csv:
        seed_split = seed.split(',')
        doctor = Doctor(seed_split[0], seed_split[1], seed_split[2], seed_split[3],int( seed_split[4]))
        doctors.append(doctor)


def add_doctor_to_file(data):
    with open(file_path, 'a') as csv_out:
        write = csv.writer(csv_out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        write.writerow(data)


def create_doctor(doctor: Doctor):
    if any(x.cpf == doctor.cpf and x.crm == doctor.crm for x in doctors):
        raise Exception('Médico com este CPF ou CRM já cadastrado!')

    doctors.append(doctor)

    doctor_data = f"{doctor.name},{doctor.cpf},{doctor.crm},{doctor.genre},{doctor.status}"
    add_doctor_to_file(doctor_data.split(','))


def get_activated_doctors():
    return filter(lambda dc: dc.status == Status.ACTIVE, doctors)


def get_doctor():
    return doctors


get_doctors_csv()
populate_doctor()

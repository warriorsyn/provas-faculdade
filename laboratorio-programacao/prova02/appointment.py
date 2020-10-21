from models import Doctor, Patient, Appointment, Status

import csv

file_path = 'database/appointment.csv'

appointments = []
appointment_csv = []


def get_appointments_csv():
    with open(file_path, 'rt') as csv_out:
        for row in csv.reader(csv_out, delimiter=',', quotechar='|'):
            if row:
                appointment_csv.append(','.join(row))


def populate_appointment():
    for seed in appointment_csv:
        seed_split = seed.split(',')
        date = seed_split[0]
        apt_type = int(seed_split[1])
        status = int(seed_split[2])
        doctor = Doctor(seed_split[3], seed_split[4], seed_split[5], seed_split[6], int(seed_split[7]))
        patient = Patient(seed_split[8], seed_split[9], seed_split[10])

        appointment_class = Appointment(date, doctor, patient, apt_type, status)
        appointments.append(appointment_class)


def add_appointments_to_file(data):
    with open(file_path, 'a') as csv_out:
        write = csv.writer(csv_out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        write.writerow(data)


def create_appointment(appointment: Appointment):
    appointments.append(appointment)

    appointment_data = f"{appointment.date},{appointment.type},{appointment.status},{appointment.doctor.name},{appointment.doctor.cpf},{appointment.doctor.crm},{appointment.doctor.genre},{appointment.doctor.status},{appointment.patient.name},{appointment.patient.cpf},{appointment.patient.genre}"
    add_appointments_to_file(appointment_data.split(','))


def update_appointment_csv(date, crm, cpf):
    with open(file_path, newline="") as file:
        readData = [row for row in csv.reader(file, delimiter=',', quotechar='|')]

        rows = [x for x in readData]

        for i in rows:
            if i:
                if i[0] == date and i[5] == crm and i[9] == cpf:
                    i[2] = str(Status.INACTIVE)
        print(rows)

    with open(file_path, 'w') as csv_out:
        write = csv.writer(csv_out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        write.writerows(rows)


def delete_appointment(date, crm, cpf):
    appointment = [x for x in appointments if x.doctor.crm == crm and x.date == date and x.patient.cpf == cpf]

    if not appointment:
        raise Exception("Nenhuma consulta encontrada!")

    appointment[0].status = 2
    update_appointment_csv(date, crm, cpf)


def get_appointments(date):
    return filter(lambda apt: apt.date == date and apt.status == Status.ACTIVE, appointments)


get_appointments_csv()
populate_appointment()

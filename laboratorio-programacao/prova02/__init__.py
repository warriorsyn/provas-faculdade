from models import Patient, Genre, Status, Doctor, Appointment, AppointmentType
from patient import create_patient, get_patients, get_patient_by_cpf
from doctor import create_doctor, get_activated_doctors, get_doctor_by_crm
from appointment import create_appointment, get_appointments, delete_appointment

# Main program

# Local variables
menus = [
    '1 - Cadastrar pacientes',
    '2 - Cadastrar médicos',
    '3 - Registrar consulta',
    '4 - Cancelar consulta',
    '5 - Relatório de pacientes',
    '6 - Relatório de médicos',
    '7 - Relatório de consultas',
    '0 - Fechar programa'
]


# End local variables

def add_patients():
    name = input("Insira o nome do cliente: ")
    cpf = input("Insira o cpf do cliente: ")

    while True:
        try:
            genre = input("Insira o sexo do cliente (F - Feminino ou M - Masculino): ")

            if genre.upper() != Genre.FEMALE and genre.upper() != Genre.MALE:
                raise Exception("Insira um sexo válido (F - Feminino ou M - Masculino) ")
        except Exception as e:
            print(e)
        else:
            break

    patient_class = Patient(name, cpf, genre.upper())

    try:
        create_patient(patient_class)
    except Exception as e:
        print(e)


def load_patients():
    print('==================')
    print("Relatório de pacientes")
    for pt in get_patients():
        print(pt)
    print('==================')


def add_doctors():
    name = input("Insira o nome do médico: ")
    cpf = input("Insira o CPF do médico: ")
    crm = input("Insira a CRM do médico: ")

    while True:
        try:
            genre = input("Insira o sexo do médico (F - Feminino ou M - Masculino): ")

            if genre.upper() != Genre.FEMALE and genre.upper() != Genre.MALE:
                raise Exception("Insira um sexo válido (F - Feminino ou M - Masculino) ")
        except Exception as e:
            print(e)
        else:
            break

    while True:
        try:
            status = int(input("Insira o Status do cliente (1 - Ativo ou 2 - Inativo): "))

            if status != Status.ACTIVE and status != Status.INACTIVE:
                raise Exception("Insira um status válido(1 - Ativo ou 2 - Inativo)")
        except Exception as e:
            print(e)
        else:
            break

    doctor_class = Doctor(name, cpf, crm, genre.upper(), status)

    try:
        create_doctor(doctor_class)
    except Exception as e:
        print(e)


def load_active_doctors():
    print('==================')
    print("Relatório de médicos")
    for dc in get_activated_doctors():
        print(dc)
    print('==================')


def add_appointment():
    date = input('Insira a data da consulta (dd/MM/YYYY): ')

    while True:
        try:
            crm = input('Insira o crm do médico: ')
            _doctor = get_doctor_by_crm(crm)

            if not _doctor:
                raise Exception("Nenhum médico encontrado!")
        except Exception as e:
            print(e)
        else:
            break

    while True:
        try:
            cpf = input('Insira o CPF do paciente: ')
            _patient = get_patient_by_cpf(cpf)

            if not _patient:
                raise Exception("Nenhum paciente foi encontrado!")
        except Exception as e:
            print(e)
        else:
            break

    while True:
        try:
            appointment_type = int(
                input("Insira o tipo da consulta (1 - Primeira consulta ou 2 - Consulta de retorno): "))

            if appointment_type != AppointmentType.FIRST_APPOINTMENT and appointment_type != AppointmentType.RETURN_APPOINTMENT:
                raise Exception("Insira um tipo válido (1 - Primeira consulta ou 2 - Consulta de retorno)")

        except Exception as e:
            print(e)
        else:
            break

    try:
        _appointment = Appointment(date, _doctor[0], _patient[0], appointment_type, Status.ACTIVE)
        create_appointment(_appointment)
    except Exception as e:
        print(e)


def get_appointments_by_date():
    date = input("Insira a data da consulta (dd/MM/YYYY): ")
    sum = 0
    print('==================')
    print("Relatório de consultas")

    if not len(list(get_appointments(date))):
        print('----------------------------------')
        print(f"Nenhuma consulta marcada para {date}")
        print('----------------------------------')
        return

    for ap in get_appointments(date):
        sum += ap.price
        print(ap)
    print(f"Valor total arrecadado: R$ {sum}")
    print('==================')


def cancel_appointment():
    date = input('Insira a data da consulta (dd/MM/YYYY): ')

    while True:
        try:
            crm = input('Insira o crm do médico: ')
            _doctor = get_doctor_by_crm(crm)

            if not _doctor:
                raise Exception("Nenhum médico encontrado!")
        except Exception as e:
            print(e)
        else:
            break

    while True:
        try:
            cpf = input('Insira o CPF do paciente: ')
            _patient = get_patient_by_cpf(cpf)

            if not _patient:
                raise Exception("Nenhum paciente foi encontrado!")
        except Exception as e:
            print(e)
        else:
            break

    try:
        delete_appointment(date, crm, cpf)
    except Exception as e:
        print(e)


# Local functions

def handle_menu_option(option):
    if option == 1:
        add_patients()
    if option == 2:
        add_doctors()
    if option == 3:
        add_appointment()
    if option == 4:
        cancel_appointment()
    if option == 5:
        load_patients()
    if option == 6:
        load_active_doctors()
    if options == 7:
        get_appointments_by_date()

# End Local functions

while True:
    for menu in menus:
        print(menu)

    try:
        options = int(input("Escolha uma Opção: "))
        menus[options]
    except Exception as e:
        print("Escolha uma opção válida!")

    if not options:
        break
    handle_menu_option(options)

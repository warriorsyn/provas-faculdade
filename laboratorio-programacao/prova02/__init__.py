from models import Patient, Genre, Status, Doctor, Appointment
from patient import create_patient, get_patients
from doctor import create_doctor, get_activated_doctors

# Main program

# Local variables
menus = [
    '1 - Cadastrar pacientes',
    '2 - Cadastrar médicos',
    '3 - Registrar consulta',
    '4 - Cancelar consulta',
    '5 - Relatório de pacientes',
    '6 - Relatório de médicos',
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
# Local functions

def handle_menu_option(option):
    if option == 1:
        add_patients()
    if option == 2:
        add_doctors()
    if option == 5:
        load_patients()
    if option == 6:
        load_active_doctors()


#  if option == 2:
#     add_vacancies()
# if option == 3:
#   load_vacancies()
# if option == 4:
#   load_activated_clients()

# End Local functions

while True:
    for menu in menus:
        print(menu)

    options = int(input("Escolha uma Opção: "))

    if not options:
        break
    handle_menu_option(options)

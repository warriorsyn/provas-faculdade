class Patient:
    def __init__(self, name, cpf, genre):
        self.name = name
        self.cpf = cpf
        self.genre = genre

    def __str__(self):
        return f"--------------------\nNome: {self.name}\nCPF: {self.cpf}\n--------------------"


class Doctor:
    def __init__(self, name, cpf, crm, genre, status):
        self.name = name
        self.cpf = cpf
        self.crm = crm
        self.genre = genre
        self.status = status

    def __str__(self):
        return f"--------------------\nNome: {self.name}\nCPF: {self.cpf}\nCRM: {self.crm}\nSexo: {self.genre}\nStatus: {self.status}\n--------------------"


class Appointment:
    def __init__(self, date, doctor: Doctor, patient: Patient, appointment_type, status):
        self.date = date
        self.doctor = doctor
        self.patient = patient
        self.type = appointment_type
        self.status = status
        self.price = 0

        self.get_price()

    def __str__(self):
        return f"--------------------\nData agendada: {self.date}\nMédico: {self.doctor.name} - {self.doctor.crm}\nPaciente: {self.patient.name} - {self.patient.cpf}\nTipo da consulta: {self.get_type_str()}\nValor consulta: {self.price}\n--------------------"

    def get_price(self):
        if self.type == AppointmentType.FIRST_APPOINTMENT:
            self.price = 300.0

        if self.type == AppointmentType.RETURN_APPOINTMENT:
            self.price = 100.0

    def get_type_str(self):
        if self.type == AppointmentType.FIRST_APPOINTMENT:
            return 'Primeira consulta'

        if self.type == AppointmentType.RETURN_APPOINTMENT:
            return 'Consulta de retorno'


class Status:
    ACTIVE = 1
    INACTIVE = 2


class Genre:
    MALE = 'M'
    FEMALE = 'F'


class AppointmentType:
    FIRST_APPOINTMENT = 1
    RETURN_APPOINTMENT = 2

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
    def __init__(self, date, doctor: Doctor, patient: Patient, type):
        self.date = date
        self.doctor = doctor
        self.patient = patient
        self.type = type


class Status:
    ACTIVE = 1
    INACTIVE = 2


class Genre:
    MALE = 'M'
    FEMALE = 'F'

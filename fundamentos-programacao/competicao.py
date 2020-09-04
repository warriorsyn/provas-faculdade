# JOAO VICTOR DE ANDRADE

import random
from tabulate import tabulate


class Inscricao:
    def __init__(self, nome, idade, ano_cursado: int):
        self.nome = nome
        self.idade = idade
        self.ano_cursado = ano_cursado


def porcentagem_total_parte(total, parte) -> str:
    return f"{(parte * 100) / total}%"


equipe_01 = []
equipe_02 = []
equipe_03 = []
equipe_04 = []

counter = 1

while counter <= 12:

    nome = input("Insira seu nome: ")

    idade = int(input("Insira sua idade: "))

    ano = int(input("Insira o ano cursado (1, 2 ou 3): "))

    random_num = random.randint(1, 4)

    if random_num == 1:
        if len(equipe_01) < 3:
            equipe_01.append(Inscricao(nome, idade, ano))

        if len(equipe_02) < 3:
            random_num = random.randint(2, 4)
            equipe_02.append(Inscricao(nome, idade, ano))

        if len(equipe_03) < 3:
            random_num = random.randint(3, 4)
            equipe_03.append(Inscricao(nome, idade, ano))

        if len(equipe_04) < 3:
            random_num = 4
            equipe_04.append(Inscricao(nome, idade, ano))

    print(random_num)
    counter += 1

resultA = []
resultB = []
resultC = []
resultD = []

primeiroA = []
primeiroB = []
primeiroC = []
primeiroD = []

terceiroA = []
terceiroB = []
terceiroC = []
terceiroD = []


mediaA = 0
mediaB = 0
mediaC = 0
mediaD = 0


for one in equipe_01:
    if one.ano_cursado == 1:
        primeiroA.append(one)

    if one.ano_cursado == 3:
        terceiroA.append(one)

    mediaA += one.idade
    resultA.append([one.nome, one.idade, one.ano_cursado])


print("===================")


for two in equipe_02:
    if two.ano_cursado == 1:
        primeiroB.append(two)

    if two.ano_cursado == 3:
        terceiroB.append(two)
    mediaB += one.idade
    resultB.append([one.nome, one.idade, one.ano_cursado])


print("===================")

for trhee in equipe_03:
    if trhee.ano_cursado == 1:
        primeiroC.append(trhee)

    if trhee.ano_cursado == 3:
        terceiroC.append(trhee)
    mediaC += one.idade
    resultC.append([one.nome, one.idade, one.ano_cursado])


print("===================")

for four in equipe_04:
    if four.ano_cursado == 1:
        primeiroD.append(four)

    if four.ano_cursado == 3:
        terceiroD.append(four)
    mediaD += one.idade
    resultD.append([one.nome, one.idade, one.ano_cursado])


total_alunos = len(equipe_01) + len(equipe_02) + \
    len(equipe_03) + len(equipe_04)

total_alunos_primeiro_ano = len(
    primeiroA) + len(primeiroB) + len(primeiroC) + len(primeiroD)

print("===============================")
print('Equipe A')
print(tabulate(resultA, headers=[
      'Nome', 'Idade', 'Ano'], tablefmt='orgtbl'))
print(f'Média de idades da equipe {mediaA / len(equipe_01)}')
print(f'Quantidade de aluno do terceiro ano: {len(terceiroA)}')

print("===============================")


print("===============================")
print('Equipe B')
print(tabulate(resultB, headers=[
      'Nome', 'Idade', 'Ano'], tablefmt='orgtbl'))
print(f'Média de idades da equipe {mediaB / len(equipe_02)}')
print(f'Quantidade de aluno do terceiro ano: {len(terceiroB)}')
print("===============================")


print("===============================")
print('Equipe C')
print(tabulate(resultC, headers=[
      'Nome', 'Idade', 'Ano'], tablefmt='orgtbl'))
print(f'Média de idades da equipe {mediaC / len(equipe_03)}')
print(f'Quantidade de aluno do terceiro ano: {len(terceiroC)}')
print("===============================")


print("===============================")
print('Equipe D')
print(tabulate(resultD, headers=[
      'Nome', 'Idade', 'Ano'], tablefmt='orgtbl'))
print(f'Média de idades da equipe {mediaD / len(equipe_04)}')
print(f'Quantidade de aluno do terceiro ano: {len(terceiroD)}')
print("===============================")


print(
    f"Percentual de estudantes do 1º ano: {porcentagem_total_parte(total_alunos, total_alunos_primeiro_ano)}")

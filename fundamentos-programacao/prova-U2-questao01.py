# QUESTAO 01
# JOAO VICTOR DE ANDRADE - 1201136048
class Questoes:
    def __init__(self, question, anwser, pontuation):
        self.question = question
        self.anwser = anwser
        self.pontuation = pontuation

    def __str__(self):
        return f"{self.question} ({self.pontuation}) - {self.anwser}"


class Aluno:
    def __init__(self, matricula, nome):
        self.matricula = matricula
        self.nome = nome
        self.respostas = []
        self.nota = 0

    def __str__(self):
        return f"{self.matricula} ({self.nome}) Respostas {self.respostas} | Nota {self.nota}"

    def __lt__(self, other):
        return self.nota < other.nota


def porcentagem_total_parte(total: float, parte: float) -> str:
    return f"{(parte * 100) / total}%"


questions = []
alunos = []

count = 1
while count <= 6:
    resposta = input(f"Insira a resposta da questão {count}: ")

    if resposta != 'a' and resposta != 'b' and resposta != 'c' and resposta != 'd' and resposta != 'e':
        print("Valor inválido, insira os valores (a,b,c ou d)")
        resposta = input(f"Insira a resposta da questão {count}: ")
        pass

    questions.append(Questoes(count, resposta, 1.5 if count <= 4 else 2))

    count += 1

quantidade = int(input("Insira a quantidade de alunos que farão a prova: "))

for i in range(quantidade):
    nome = input("Insira o nome do aluno: ")

    matricula = input("Insira a matricula do aluno: ")

    aluno = Aluno(matricula, nome)

    questao_01 = input("Resposta da questao 01: ")
    aluno.respostas.append(questao_01)

    questao_02 = input("Resposta da questao 02: ")
    aluno.respostas.append(questao_02)

    questao_03 = input("Resposta da questao 03: ")
    aluno.respostas.append(questao_03)

    questao_04 = input("Resposta da questao 04: ")
    aluno.respostas.append(questao_04)

    questao_05 = input("Resposta da questao 05: ")
    aluno.respostas.append(questao_05)

    questao_06 = input("Resposta da questao 06: ")
    aluno.respostas.append(questao_06)

    alunos.append(aluno)

print("=================================")

print("Gabarito: ")
for q in questions:
    print(q)

print("=================================")
print("Relatorio")
print("=================================")
aprovados = []
abaixo_media = []
nota_geral = 0
for k in range(len(alunos)):
    for j in range(len(questions)):
        if questions[j].anwser == alunos[k].respostas[j]:
            alunos[k].nota += questions[j].pontuation

    if alunos[k].nota >= 6:
        nota_geral += alunos[k].nota
        aprovados.append(alunos[k])

    if alunos[k].nota < 6:
        abaixo_media.append(alunos[k])

print("=================================")
print("Aprovados")
for a in aprovados:
    print(a)
print("=================================")


alunos.sort()

alunos_menor_nota = []

for l in range(len(alunos)):
    if alunos[l].nota == alunos[0].nota:
        alunos_menor_nota.append(alunos[l])

print("=================================")
print(f"Alunos com menor nota: ({alunos[0].nota} pontos) ")
for menor in alunos_menor_nota:
    print(menor)
print("=================================")

print("=================================")
print(
    f"A média das notas dos alunos aprovados é {nota_geral / len(aprovados)}")
print("=================================")

print("=================================")
print(
    f"O percentual de alunos  que obtiveram  nota abaixo da média é de {porcentagem_total_parte(len(alunos), len(abaixo_media))}")
print("=================================")

# Questao 02

class Interview:
    def __init__(self, name, genre, salary, persons_number):
        self.name = name
        self.genre = genre
        self.salary = salary
        self.persons_number = persons_number

    def __str__(self):
        return f"{self.name} com salário de R$ {self.salary}"

    def __lt__(self, other):
        return self.salary < other.salary


def porcentagem_total_parte(total: float, parte: float) -> str:
    return f"{(parte * 100) / total}%"


interviews = []

quantity = int(input("Insira a quantidade de entrevistados: "))

for i in range(quantity):

    nome = input("Insira o nome do entrevistado: ")

    sexo = input("Insira o sexo do entrevistado (M ou F): ")

    salario = float(input("Insira o salário do entrevistado: "))

    pessoas = int(
        input("Insira a quantidade de pessoas que vivem na casa do entrevistado: "))

    interviews.append(Interview(nome, sexo, salario, pessoas))


under_1500 = []
women = []
men = []
full_salary = 0
women_salary = 0
women_counter = 0
for j in range(len(interviews)):
    if interviews[j].salary < 1500:
        under_1500.append(interviews[j])

    if interviews[j].genre == 'F':
        women.append(interviews[j])
        women_salary += interviews[j].salary
        women_counter += 1

    if interviews[j].genre == 'M':
        men.append(interviews[j])

    full_salary += interviews[j].salary


interviews.sort()

print("Pessoas com salário abaixo de R$ 1500,00: ")


for under in under_1500:
    print(under)


print(
    f"A média de salário nas residências que as mulheres são responsáveis é de R$ {women_salary / women_counter}")


print(
    f"O percentual de homens que são responsáveis pela sua residência é de {porcentagem_total_parte(len(interviews), len(men))}")

print(
    f"O nome do responsável com menor salário dentre os entrevistados é {interviews[0].name} com salário de R$ {interviews[0].salary}")

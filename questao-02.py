# Questão 02

class Pandemia:
    def __init__(self, codigo_estado, nome_estado, covid_positivo, obitos):
        self.codigo_estado = codigo_estado
        self.nome_estado = nome_estado
        self.covid_positivo = covid_positivo
        self.obitos = obitos

    def __lt__(self, other):
        return self.covid_positivo > other.covid_positivo


def porcentagem_valor_e_total(total: float, parte: float) -> float:
    return (parte * 100) / total


pandemias = []

while True:
    codigo = input("Insira o código do Estado: ")

    if codigo == "-1":
        break

    nome = input("Insira o nome do Estado: ")

    covid = int(
        input("Insira a quantidade de pacientes que testaram positivo para COVID-19: "))

    obito = int(input("Insira a quantidades de óbitos por COVID-19: "))

    pandemias.append(Pandemia(codigo, nome, covid, obito))


soma = 0

for i in range(len(pandemias)):
    soma += pandemias[i].obitos

media_obitos = soma / len(pandemias)


obito_primeiro_estado = pandemias[0].obitos

pandemias.sort()

print(
    f"A qmédia de óbitos que ocorreram nos Estados cadastrados é {media_obitos} óbitos")

print(
    f"O Etado com maior numéros de pacientes com coronavírus é {pandemias[0].nome_estado}")

print(
    f"O percentual de óbitos que ocorreram no primeiro estado cadastrado é: {porcentagem_valor_e_total(soma, obito_primeiro_estado)} %")

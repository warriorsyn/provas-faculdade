import functools

prestacoes = []


def getValorPorcentage(porcentagem: float) -> float:
    return porcentagem / 100


def valorPagamento(prestacao: float, dias_atrasado: int) -> float:
    multa = prestacao * getValorPorcentage(3)
    multa_dia = (prestacao + multa) * (dias_atrasado * getValorPorcentage(0.1))
    return prestacao + multa + multa_dia


while True:
    valor_prestacao = float(input("Qual o valor da prestação? "))

    if valor_prestacao == 0:
        break

    dias_atrasado = int(input("Quantos dias está atrasado? "))

    prestacoes.append(valorPagamento(valor_prestacao, dias_atrasado))


print("=============================================")
print(
    f"As prestações pagas valem {functools.reduce(lambda a,b: a+b, prestacoes)}")
print(f"A quantidade de prestações é {len(prestacoes)}")
print("=============================================")

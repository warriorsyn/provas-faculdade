# JOAO VICTOR DE ANDRADE
# 1201136048

from tabulate import tabulate

# ----------------------Models----------------------------------


class Tec:
    def __init__(self, tecnologia):
        self.tecnologia = tecnologia


class Participante:
    def __init__(self, participante):
        self.participante = participante


class Votos:
    def __init__(self, tec: Tec, participante: Participante):
        self.tec = tec
        self.participante = participante

    def __str__(self):
        return f"{self.tec.tecnologia} | {self.participante.participante}"
# ---------------------------------------------------------


def porcentagem_total_parte(total: float, parte: float) -> str:
    return f"{(parte * 100) / total}%"


windows = Tec('Windows')
linux = Tec('Linux')
mac = Tec('Mac Os')
outros = Tec('Outro')

votos = []

while True:

    print("Qual o melhor Sistema operacional ?")
    print("1 - Widows\n2 - Linux\n3 - Mac Os\n4 - Outros")

    escolha = int(input("Qual seu voto ? "))

    if escolha == 0:
        print("Obrigado por votar!!")
        break

    if escolha > 4:
        print("Esse valor não é válido!")

    nome = input("Insira seu nome: ")

    participante = Participante(nome)

    if escolha == 1:
        votos.append(Votos(windows, participante))
    elif escolha == 2:
        votos.append(Votos(linux, participante))
    elif escolha == 3:
        votos.append(Votos(mac, participante))
    elif escolha == 4:
        votos.append(Votos(outros, participante))


windowsVotes = []
linuxVotes = []
macVotes = []
outrosVotes = []

for i in range(len(votos)):
    if votos[i].tec is windows:
        windowsVotes.append(votos[i])

    if votos[i].tec is linux:
        linuxVotes.append(votos[i])

    if votos[i].tec is mac:
        macVotes.append(votos[i])

    if votos[i].tec is outros:
        outrosVotes.append(votos[i])


higher_voted = None

if len(windowsVotes) > len(linuxVotes) and len(windowsVotes) > len(macVotes) and len(windowsVotes) > len(outrosVotes):
    higher_voted = windows
elif len(linuxVotes) > len(windowsVotes) and len(linuxVotes) > len(macVotes) and len(linuxVotes) > len(outrosVotes):
    higher_voted = linux
elif len(macVotes) > len(windowsVotes) and len(macVotes) > len(linuxVotes) and len(macVotes) > len(outrosVotes):
    higher_voted = mac
else:
    higher_voted = outros

print('----------------------------------------------------------')

print(f"O TOTAL DE VOTOS COMPUTADOS É {(len(votos))}")

results = [
    [windows.tecnologia, len(windowsVotes), porcentagem_total_parte(
        len(votos), len(windowsVotes))],
    [linux.tecnologia, len(linuxVotes), porcentagem_total_parte(
        len(votos), len(linuxVotes))],
    [mac.tecnologia, len(macVotes), porcentagem_total_parte(
        len(votos), len(macVotes))],
    [outros.tecnologia, len(outrosVotes), porcentagem_total_parte(
        len(votos), len(outrosVotes))]
]

print(tabulate(results, headers=[
      'Sistema', 'Votos', 'Porcentagem de votos'], tablefmt='orgtbl'))


print(f'O SISTEMA OPERACIONAL MAIS VOTADO É O {higher_voted.tecnologia}')
print('----------------------------------------------------------')

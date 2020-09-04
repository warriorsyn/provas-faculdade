# Questão 01

class Produto:
    def __init__(self, valor, quantidade):
        self.valor = valor
        self.quantidade = quantidade

    def __str__(self):
        return f"Preco {self.valor} quantidade {self.quantidade}"

    def __lt__(self, other):
        return self.valor < other.valor


class SuperMarket():
    def __init__(self, cod_cliente, nome_cliente, sexo_cliente):
        self.cod_cliente = cod_cliente
        self.nome_cliente = nome_cliente
        self.sexo_cliente = sexo_cliente
        self.produtos = []

    def __lt__(self, other):
        for prod in self.produtos:
            for ot in other.produtos:
                return prod.valor < ot.valor


def porcentagem_total_parte(total, parte) -> float:
    return (parte * 100) / total


supermarkets = []

while True:
    produto_loop = True

    codigo = input("Informe o código do cliente: ")

    nome = input("Informe o nome do cliente: ")

    sexo = input("Informe o sexo do cliente (M OU F): ")

    supermarket = SuperMarket(codigo, nome, sexo)

    while produto_loop:
        print("====================================================")
        preco = float(input("Insira o valor do produto: "))

        quantidade = int(input("Insira a quantidade do produto: "))

        supermarket.produtos.append(Produto(preco, quantidade))

        fim_produto = input(
            "Deseja finalizar os produtos ? (S - SIM OU N - NÃO): ")

        if fim_produto == "S":
            produto_loop = False
            print("====================================================")

    supermarkets.append(supermarket)
    fim = input("Deseja encerrar o dia ? (S OU N): ")

    if fim == "S":
        break


soma_total_clientes = len(supermarkets)
soma_total_mulheres = []
produtos_qtd = []
masculino_menor_compra = []
for i in range(len(supermarkets)):
    if supermarkets[i].sexo_cliente == 'F':
        soma_total_mulheres.append(supermarkets[i])

    for j in range(len(supermarkets[i].produtos)):
        produtos_qtd.append(supermarkets[i].produtos[j])

        if supermarkets[i].sexo_cliente == 'M':
            masculino_menor_compra.append(supermarkets[i])


print(f"A quantidade total de produtos vendidos é {len(produtos_qtd)}")

print(
    f"A média de quantidades de produtos vendidos por compras realizadas é {len(produtos_qtd) / soma_total_clientes}")

masculino_menor_compra.sort()

print(
    f"O nome do cliente (sexo masculino) com menor valor de compra é {masculino_menor_compra[0].nome_cliente}")

print(
    f"O percentual de clientes do sexo feminino é de {porcentagem_total_parte(soma_total_clientes, len(soma_total_mulheres))} %")

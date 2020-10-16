def getAvarage(*numbers) -> float:
    sum = 0
    for n in numbers:
        sum += n
    return sum / len(numbers)

nome = input("Atleta: ")

salto01 = float(input("Primeiro salto: "))
salto02 = float(input("Segundo salto: "))
salto03 = float(input("Terceiro salto: "))
salto04 = float(input("Quarto salto: "))
salto05 = float(input("Quinto salto: "))


print("Resultado final:")
print(f"Atleta: {nome}")
print(f"Saltos: {salto01} - {salto02} - {salto03} - {salto04} - {salto05}")
print(f"Média dos saltos: {getAvarage(salto01, salto02, salto03, salto04, salto05)}m")



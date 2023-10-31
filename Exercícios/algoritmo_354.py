num = []

for i in range(15):
    numero = int(input(f"Digite o {i + 1} número: "))
    num.append(numero)

print("\nRelação dos números")

for i, valor in enumerate(num): #o enumerate percorrerá a lista o "i" tem como função andar as posições, enquanto o "valor" tem objetivo de coletar o valor dessa posição, mt pika.
    print(f"\n{i + 1} - {valor}")
    if (valor % 2) == 0:
        print(f"O número {valor} é par")
    else:
        print(f"O número {valor} é ímpar")

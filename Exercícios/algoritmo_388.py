n = []

for i in range(10):
    k = int(input(f"Digite o {i + 1} número inteiro: "))
    n.append(k)

print("\nVetor ordenado")

n.sort(reverse=True)

for elemento in n:
    print(elemento)
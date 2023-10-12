numbers = int(input("Digite um número inteiro maior que 1: "))
pairsNumbers = []
oddNumbers = []

while numbers <= 1:
    numbers = int(input("Digite um número inteiro maior ou igual a 1: "))

for i in range(1, numbers + 1, 1):
    if i % 2 == 0:
        pairsNumbers.append(i)
    elif i % 2 != 0:
        oddNumbers.append(i)

print(f"Números pares: {pairsNumbers}\n"
      f"Números ímpares: {oddNumbers}")
listNumber = []

for i in range(10):
    while True:
        j = int(input(f"Digite o {i+1}° número ímpar para armazenar na lista: "))
        if j % 2 != 0:  # Verifique se o número é ímpar
            listNumber.append(j)
            break
        else:
            print("Digite apenas números ímpares.")

print("Números ímpares inseridos:", listNumber)

import time

listNumber = []
pairsNumbers = []
oddNumbers = []

for i in range(20):
    while True:
        j = input(f"Digite o {i+1}° número para armazenar na lista: ")
        if j.isalpha():
            print("Digite apenas números. Letras não são válidas.")
        elif j.isdigit():
            listNumber.append(int(j))  # Converta a entrada para um número inteiro
            break
        else:
            print("Error")  
            exit()

time.sleep(2)
print("Informações da lista:\n"
      f"Lista completa: {listNumber}\n"
      f"Quantidade de números na lista: {len(listNumber)}\n")

time.sleep(2)

for k in listNumber:
    if k % 2 == 0: # Aqui ocorre um erro caso a conversão na linha 13 não exista
        pairsNumbers.append(k)
    elif k % 2 != 0:
        oddNumbers.append(k)
    else:
        print("Error")

print(f"Quantidade de números pares: {len(pairsNumbers)}\n"
      f"Lista dos números pares: {pairsNumbers}\n"
      f"Quantidade de números ímpares: {len(oddNumbers)}\n"
      f"Lista de números ímpares: {oddNumbers}.")
list = [9, 41, 7, 56, 3, 66, 70, 848, 19, 10, 27, 12, 444]
print(len(list))

valorEscolhido01 = int(input("Você irá digitar duas vezes um valor de 0 a 12.\n"
                           "Digite o primeiro: "))

valorEscolhido02 = int(input("Digite o segundo valor. Você poderá escolher o mesmo valor escolhido anteriormente.\n"
                             "Digite o segundo: "))

list01 = list[valorEscolhido01]
list02 = list[valorEscolhido02]

print(f"O número {valorEscolhido01} escolhido equivale a {list01}")
print(f"O número {valorEscolhido02} escolhido equivale a {list02}")

somaList = list01 + list02

print(f"A soma de {list01} e {list02} é de {somaList}.")
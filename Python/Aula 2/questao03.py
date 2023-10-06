import time

numbersList = []
flag = False

print("You're gonna type 10 numbers.")
for i in range(10):
    answer = numbersList.append(int(input(f"Type the {i+1}° number: ")))

randomNumber = int(input("Now type a random number: "))

for j in numbersList:
    if j == randomNumber:
        print(f"{randomNumber} found in {numbersList} in position {numbersList.index(j+1)}") # Index mostra a posição em que o valor se encontra + 1 (por começar em 0).
        flag = True
        break
if not flag: # Condicional que verifica se o valor da flag continua sendo falsa. Ou seja, se ela não foi encontrada em "if j == randomNumber e a flag se tornou verdadeira".
    print(f"{randomNumber} not found in {numbersList}")
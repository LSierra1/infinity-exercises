# checkNumber = lambda x: "pair" if x % 2 == 0 else "odd"

# print(checkNumber(int(input("Digite um número: "))))

print((lambda x: "pair" if x % 2 == 0 else "odd")(int(input("Digite um número: "))))
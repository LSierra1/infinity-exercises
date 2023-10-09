# x = input("Digite algo (preferencialmente mais de 5 caracteres): ")
# y = input("Digite algo (preferencialmente mais de 5 caracteres): ")
# concatenate = lambda x, y: x + y if len(x) > 5 and len(y) > 5 else "Error"

# print(concatenate(x, y))

x = input("Digite algo (preferencialmente mais de 5 caracteres): ")
y = input("Digite algo (preferencialmente mais de 5 caracteres): ")

print((lambda x, y: x + y if len(x) > 5 and len(y) > 5 else "Error") (x, y))
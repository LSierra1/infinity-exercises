from functools import reduce

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

valor_maximo = reduce(lambda x, y: x + y, numeros)

print(valor_maximo)
x = int(input("Enter a number: "))
checker = lambda x: "Divisível" if (x % 3 == 0) and (x % 5 == 0) else "Não divisível"

print(checker(x))
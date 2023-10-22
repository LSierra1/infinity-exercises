from calc import *

if __name__ == "__main__":
    n1 = 
    n2 = 
    escolhas = int(input(
        "Escolha uma das opções:\n"
        "1 - Somar dois números\n"
        "2- Subtrair dois números\n"
        "3- Multiplicar dois números\n"
        "4 - Dividir dois números"
    ))

    match escolhas:
        case 1:
            print(soma(n1, n2))
        case 2:
            print(subtração(n1, n2))
        case 3:
            print(multiplicacao(n1, n2))    
        case 4:
            print(divisao(n1, n2))
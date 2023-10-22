# while True:
#     def media(*args):
#         soma = 0
#         contador = 0

#         for i in args:
#             soma += i
#             contador += 1
        
#         media = soma / contador

#         print(media)



# # escolha = int(input("escolha uma das opções: \n"
# #                     "1 - Media 3 notas: \n"
# #                     "2 - Media 4 notas: \n"
# #                     "3 - Media 5 notas: \n"))

# # n1 = float(input("Digite o valor: "))
# # n2 = float(input("Digite o valor: "))
# # n3 = float(input("Digite o valor: "))

# # match escolha:
# #     case 1:
# #         media(n1, n2, n3)
    
# #     case 2:
# #         n4 = float(input("Digite o valor: "))

# #         media(n1, n2, n3, n4)

# #     case 3:
# #         n4 = float(input("Digite o valor: "))
# #         n5 = float(input("Digite o valor: "))

# #         media(n1, n2, n3, n4, n5)

# def info(**kwargs):
#     for chave, valor in kwargs.items():
#         print(f"{chave} : {valor}")

# info(Name= "Sierra", Age= 19)

# soma = lambda a, b, c : a + b + c
# print(soma(1, 2, 3))

# pairNumber = lambda x: "pair" if x % 2 == 0 else "odd"

# print(pairNumber(6))

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# quadrados = list(map(lambda x: x % 2 == 0, numbers))

# print(quadrados)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# pairs = list(filter(lambda x: x % 2 == 0, numbers))

# print(pairs)

# def listar_nomes(pessoas):
#     nomes = list()

#     for i in pessoas:
#         nomes.append(i['nome'])

#     print(nomes)

# pessoas = [
#     {
#         "nome": "Getulio",
#         "idade": 22
#     },
#     {
#         "nome": "Vagner",
#         "idade": 17
#     },
#     {
#         "nome": "Maria",
#         "idade": 21
#     }
# ]

# # nomes = list(map(lambda x: x["nome"], pessoas))

# listar_nomes(pessoas)

# import random

# jogadas = ["pedra", "papel", "tesoura"]

# # Def com return = função
# def jogador():
#     escolha = int(input(
#                         "Escolha uma das opções:\n"
#                         "1 - Pedra\n"
#                         "2 - Papel\n"
#                         "3 - Tesoura\n"
#     ))  -1
#     return jogadas[escolha]

# def computador():
#     escolha = random.choice(jogadas)

#     return escolha

# # Def sem return = procedimento
# def jogo(jogador, computador):
#     if jogador == computador:
#         print("Empate")
#     elif (
#         (jogador == "Pedra" and computador == "Tesoura") or
#         (jogador == "Tesoura" and computador == "Papel") or
#         (jogador == "Papel" and computador == "Pedra")
# ):
#         print("O jogador venceu.\n"
#               f"j: {jogador} x c: {computador}")
#     else:
#         print("O jogador perdeu.\n"
#               f"j: {jogador} x c: {computador}")
            
# j = jogador()
# c = computador()
# jogo(j, c)

import aspose.pdf as ap

# Inicializar objeto de documento
document = ap.Document()

# Adicionar Página
page = document.pages.add()

# Inicializar objeto textfragment
text_fragment = ap.text.TextFragment("Hello,world!")

# Adicionar fragmento de texto à nova página
page.paragraphs.add(text_fragment)

# Salvar PDF atualizado
document.save("output.pdf")

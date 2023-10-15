pessoas = [
    {
        "nome": "Getulio",
        "idade": 22
    },
    {
        "nome": "Vagner",
        "idade": 17
    },
    {
        "nome": "Maria",
        "idade": 21
    },
    {
        "nome": "João",
        "idade": 30
    },
    {
        "nome": "Luisa",
        "idade": 25
    },
    {
        "nome": "Pedro",
        "idade": 28
    },
    {
        "nome": "Ana",
        "idade": 19
    },
    {
        "nome": "Paula",
        "idade": 32
    },
    {
        "nome": "Lucas",
        "idade": 23
    },
    {
        "nome": "Mariana",
        "idade": 26
    },
    {
        "nome": "Ricardo",
        "idade": 35
    },
    {
        "nome": "Camila",
        "idade": 29
    },
    {
        "nome": "Gustavo",
        "idade": 24
    },
    {
        "nome": "Carla",
        "idade": 31
    },
    {
        "nome": "Daniel",
        "idade": 27
    },
    {
        "nome": "Fernanda",
        "idade": 22
    },
    {
        "nome": "José",
        "idade": 40
    },
    {
        "nome": "Isabela",
        "idade": 18
    },
    {
        "nome": "Henrique",
        "idade": 33
    },
    {
        "nome": "Sofia",
        "idade": 20
    },
]

# names = list(map(lambda x: x["nome"], pessoas))
# age = list(map(lambda y: y["idade"], pessoas))

print(
    list(map(lambda x: x["nome"], pessoas)),
    "\n",
    list(map(lambda y: y["idade"], pessoas))
)
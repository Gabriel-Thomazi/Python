"""
Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos através de uma função.
Seu script também deve fornecer a média dos três números, através de uma segunda função que chama a primeira.
"""

def arg(a, b, c):
    return a + b + c

def media():
    soma = arg(3, 3, 6)
    media = soma / 3
    print(f"A média é: {media}. ")
media()
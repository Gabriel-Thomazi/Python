"""
Faca um programa que receba duas frases distintas e imprima de maneira invertida,
trocando as letras A por *.
"""

frase1 = str(input("Digite a primeira frase: "))
frase2 = str(input("Digite a segunda frase: "))

concatenado = frase1 + ' ' + frase2
invertido = concatenado[::-1]
nova_frase = ''
for i in invertido:
    if i == 'a':
        nova_frase += '*'
    else:
        nova_frase += i

print(nova_frase)

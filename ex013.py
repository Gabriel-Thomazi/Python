"""Faca um programa que receba uma palavra e calcule quantas vogais (a, e, i, o, u) possui
essa palavra. Entre com um caractere (vogal ou consoante) e substitua todas as vogais
da palavra dada por esse caractere.
"""

palavra = str(input("Digite uma palavra: ")).lower()
vogais = ['a', 'e', 'i', 'o', 'u']
identifica_vogais = ''

for i in palavra:
    if i in vogais:
        identifica_vogais += i

print(len(identifica_vogais))

caractere = str(input("Digite um novo caractere: "))
nova_palavra = ''

for i in palavra: #banana
    if i in vogais:
        nova_palavra += caractere
    else:
        nova_palavra += i

print(nova_palavra)

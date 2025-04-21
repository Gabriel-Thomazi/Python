"""
Faca um programa que leia uma palavra e some 1 no valor ASCII de cada caractere da
palavra. Imprima a string resultante.
"""
palavra = str(input("Digite uma palvra: "))
nova_palavra = ' '

for i in palavra:
    nova_palavra += chr((ord(i) + 1))

print(nova_palavra)
"""
escreva um programa para converter uma cadeia de caracteres de letras maiusculas em
letras minusculas
"""

palavras = str(input("Digite uma palavra: "))
nova_palavra = ""

for i in palavras:
    if i == " ":
        nova_palavra += " "
    else:
        nova_palavra += chr(ord(i) + 32)

print(nova_palavra)

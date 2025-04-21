"""
Leia uma cadeia de caracteres e converta todos os caracteres para maiuscula. Dica:
subtraia 32 dos caracteres cujo codigo ASCII esta entre 65 e 90.
"""

palavras = str(input("digite alguma palavra: "))

nova_palavra = ""

for i in palavras: 
    if i == ' ':
        nova_palavra += " "
    else:
        nova_palavra += chr(ord(i) - 32)

print(nova_palavra)

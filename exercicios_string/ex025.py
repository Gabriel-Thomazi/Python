"""
Escreva um programa que recebe do usuario uma string S, um caractere C, e uma
posicao I e devolve o ındice da primeira posicao da string onde foi encontrado o caractere
C. A procura deve comecar a partir da posicao I
"""

S = str(input("digite alguma coisa: "))
C = str(input("Digite um caractere: "))
I = int(input("Digite uma posição: "))

retorna_indice = None

print(f"Começando a busca em: {S[I]}")

for i in range(I, len(S)):
    print(f"Procurando por: {C} \t caracter:{S[i]} indice:\'{i}\'")
    if S[i] == C:
        retorna_indice = i
        print(f"Caractere {C} encontrado no indice {i}")
        break



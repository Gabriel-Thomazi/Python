"""
escreva um programa que recebe uma string S e inteiros nao-negativos I e J e imprima
o segmento S[I..J].
"""

S = str(input("Digite uma String: "))
I = int(input("Digite um numero: "))
J = int(input("Digite outro numero: "))

print(S[I:J+1])
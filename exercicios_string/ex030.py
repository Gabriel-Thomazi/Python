"""
implemente um programa que leia duas strings, str1 e str2, e um valor inteiro positivo
N. Concatene nao mais que N caracteres da string str2 a string str1 e termine str1 com
NULL.
"""

str1 = str(input("Digite aqui: "))
str2 = str(input("Digite aqui: "))
N = int(input("Digite um valor inteiro: "))

a_ser_concatenado = ''
contador = 0

for i in str2:
    contador += 1
    a_ser_concatenado += i
    if contador >= N:
        break

concatena_tudo = a_ser_concatenado + str1
str1 = None

print(f'{concatena_tudo}, Str1: {str1}')

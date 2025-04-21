"""
Faca um programa em que troque todas as ocorrencias de uma letra L1 pela letra L2 em
uma string. A string e as letras L1 e L2 devem ser fornecidas pelo usuario
"""

frase, L1, L2 = str(input("Digite uma frase: ")), str(input("Digite L1: ")), str(input("Digite L2: "))

nova_frase = ''

for i in frase:
    if i == L1:
        nova_frase += L2
    else:
        nova_frase += i

print(nova_frase)

"""
leia um vetor contendo letras de uma frase inclusive os espacos em branco. Retirar os
espacos em branco do vetor e depois escrever o vetor resultante.
"""

vetor = ['o rato roeu a roupa do rei de roma', 'se a roupa é bege bege sou']
novo_vet = ''
for frase in vetor:
    for i in frase:
        if i == " ":
            novo_vet += ''
        else:
            novo_vet += i

print(novo_vet)
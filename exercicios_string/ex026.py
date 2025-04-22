"""
Escreva um programa que leia duas palavras e diga qual deles vem primeiro na ordem
alfabetica. Dica: ‘a’ ´e menor do que ‘b’.
"""
palavra1 = str(input("Digite a primeira palavra: "))
palavra2 = str(input("Digite a segunda palavra: "))

if palavra1 < palavra2:
    print(f"A palavra '{palavra1}' vem primeiro na ordem alfabetica.")
else:
    print(f"A palavra '{palavra2}' vem primeiro na ordem alfabetica")



# def cria_alfabeto():
#     alfabeto = []
#     for i in range(97, 123):  # Criar a lista de letras de 'a' a 'z'
#         alfabeto.append(chr(i))
#     return alfabeto

# # Leitura das palavras
# palavra1 = str(input("Digite a primeira palavra: "))
# palavra2 = str(input("Digite a segunda palavra: "))

# # Variável para armazenar o "menor" valor (letra) em cada palavra
# menor_palavra1 = ''
# menor_palavra2 = ''

# # Comparando as letras da palavra1
# for i in range(len(palavra1)):
#     if menor_palavra1 == '':  # Se ainda não foi definido, pega a primeira letra
#         menor_palavra1 = palavra1[i]
#     elif palavra1[i] < menor_palavra1:
#         menor_palavra1 = palavra1[i]

# # Comparando as letras da palavra2
# for i in range(len(palavra2)):
#     if menor_palavra2 == '':  # Se ainda não foi definido, pega a primeira letra
#         menor_palavra2 = palavra2[i]
#     elif palavra2[i] < menor_palavra2:
#         menor_palavra2 = palavra2[i]

# # Comparando qual palavra tem a menor letra (lexicograficamente)
# if menor_palavra1 < menor_palavra2:
#     print(f"A palavra '{palavra1}' vem primeiro na ordem alfabética.")
# else:
#     print(f"A palavra '{palavra2}' vem primeiro na ordem alfabética.")

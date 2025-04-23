"""
Faca um programa que, dada uma string, diga se ela e um palındromo ou nao. Lem-
brando que um palındromo e uma palavra que tenha a propriedade de poder ser lida
tanto da direita para a esquerda como da esquerda para a direita. Exemplo:
ovo
arara
Socorram-me, subi no onibus em Marrocos.
Anotaram a data da maratona
"""

especiais = ['!', '@', '#', '$', '%', '&', '*', '(', ')', ':', ',', '?', '.', ':', '~', '´', ' ', '-']

palavra = str(input("Digite uma palavra: "))
nova_palavra = ''

for i in palavra:
    if i not in especiais:
        nova_palavra += i

lower_case = nova_palavra.lower()
palavra_invertida = lower_case[::-1]

if lower_case == palavra_invertida:
    print("É palindromo")
else:
    print("Não é palindromo.")
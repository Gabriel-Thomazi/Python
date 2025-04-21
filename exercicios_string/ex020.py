"""
Escreva um programa que leia a idade e o primeiro nome de varias pessoas. Seu pro-
grama deve terminar quando uma idade negativa for digitada. Ao terminar, seu programa
deve escrever o nome e a idade das pessoas mais jovens e mais velhas.
"""
pessoa_mais_velha = ''
mais_velha = -1

pessoa_mais_nova = ''
mais_nova = 999

while True:
    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite sua idade: "))

    if idade < 0:
        break
    
    if idade > mais_velha:
        mais_velha = idade
        pessoa_mais_velha = nome
    
    if idade < mais_nova:
        mais_nova = idade
        pessoa_mais_nova = nome

print(f"A pessoa mais nova é: {pessoa_mais_nova.title()} com idade: {mais_nova}\nA pessoa mais velha é: {pessoa_mais_velha.title()} com idade: {mais_velha}")
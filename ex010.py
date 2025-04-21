# Entre com um nome e imprima o nome somente se a primeira letra do nome for “a” (maiuscula ou minuscula).

nome = str(input("Digite seu nome: "))

if nome[0] == 'A' or nome[0] == 'a':
    print(nome)
#faça um programa para converter uma letra maiúscula em letra minúscula. Use a tabela ASCII para resolver o problema

letra_maiuscula = str(input("Digite uma letra maiúscula: "))
converte = ord(letra_maiuscula) + 32

print(chr(converte))
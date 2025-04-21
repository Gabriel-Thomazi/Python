#Faça um programa que conte o numero de 1’s que aparecem em um string. Exemplo: 0011001 -> 3

nums = str(input("Digite uma sequencia de 0 e 1's: "))
contagem = nums.count("1")

print(f"A quantidade de 1's que aparecem na string é {contagem}")
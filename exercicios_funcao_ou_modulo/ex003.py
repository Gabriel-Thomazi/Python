"""
Faça um programa que recebe três números do usuário, e identifica o maior através de uma função e o menor número
através de outra função.
"""

num1, num2, num3 = int(input("Digite o numero 1: ")), int(input("Digite o numero 2: ")), int(input("Digite o numero 3: "))

def verifica_maior(num1, num2, num3):
   maior = max(num1, num2, num3)
   print(f"O maior numero entre: {num1}, {num2}, {num3} é: {maior}. ")

def verifica_menor(num1, num2, num3):
    menor = min(num1, num2, num3)
    print(f"O menor numero entre: {num1}, {num2}, {num3} é: {menor}. ")

verifica_maior(num1, num2, num3)
verifica_menor(num1, num2, num3)
    
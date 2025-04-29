"""
Escreva um script que pergunta ao usuário se ele deseja converter uma temperatura de grau Celsius para Farenheit ou vice-versa. 
Para cada opção, crie uma função. Crie uma terceira, que é um menu para o usuário escolher a opção desejada, 
onde esse menu chama a função de conversão correta.
"""

def opcao1():
    print("Você escolheu converter de Celsius para Farenheit. ")
    celsius = float(input("Digite os graus em Celsius: "))
    farenheit = celsius * 1.8 + 32
    print(f"\n{celsius}º Celsius em farenheits é: {farenheit:.2f}. ")

def opcao2():
    print("Você escolheu converter de Farenheit para Celsius. ")
    farenheit = float(input("Digite os graus em Farenheit. "))
    celsius = (farenheit - 32) / 1.8
    print(f"\n{farenheit:.2f}º Farenheits em graus Celsius é: {celsius}. ")

def sair():
    print("Saindo do menu... ")

while True:
    print("Menu de opções:\n")
    print("1 - Opção 1: Transforma de Celsius para Farenheit. ")
    print("2 - Opção 2 - Transforma de Farenheit para Celsius. ")
    print("0 - Sair")

    escolha = input("Digite sua escolha: ")

    match escolha:
        case '1':
            opcao1()
        case '2':
            opcao2()
        case '0':
            sair()
            break
        case _:
            print("Opção Inválida, tente novamente.\n")
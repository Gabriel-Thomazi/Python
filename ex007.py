#ler nome, sexo e idade. Se sexo for feminino e idade menor que 25, imprime o nome da
#pessoa e a palavra “ACEITA”, caso contrario imprimir “NAO ACEITA”

nome = str(input("Digite seu nome: ")).strip()
sexo = ''
while sexo != 'F' and sexo != 'M':
    sexo = str(input("Digite seu sexo(F or M): "))

idade = int(input("Digite sua idade: "))

if sexo == 'F' and idade < 25:
    print(nome, 'ACEITA')
else:
    print('NAO ACEITA')
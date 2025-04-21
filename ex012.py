#Faça um programa que receba do usuario uma string. O programa imprime a string sem suas vogais.

palavra = str(input("Digite uma palavra: ")).lower()
vogais = ['a', 'e', 'i', 'o', 'u']
resultado = ''

for i in palavra:
    if i not in vogais:
        resultado += i

print(resultado)
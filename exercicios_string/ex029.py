"""
construa um programa que leia duas strings fornecidas pelo usuario e verifique se a 
segunda string lida esta contida no final da primeira, retornando o resultado da verificacao
"""

string1 = str(input("Digite alguma palavra/frase: "))
string2 = str(input("Digite outra palavra/frase: "))

verifica = string1.endswith(string2)
print(verifica)
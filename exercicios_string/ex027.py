"""
O codigo de Cesar e uma das mais simples e conhecidas tecnicas de criptografia. E um
tipo de substituicao na qual cada letra do texto e substituıda por outra, que se apresenta
no alfabeto abaixo dela um numero fixo de vezes. Por exemplo, com uma troca de tres
posicoes, ‘A’ seria substituıdo por ‘D’, ‘B’ se tornaria ‘E’, e assim por diante. Implemente
um programa que faca uso desse Codigo de Cesar (3 posicoes), entre com uma string e
retorne a string codificada. Exemplo:
String: a ligeira raposa marrom saltou sobre o cachorro cansado
Nova string: D OLJHLUD UDSRVD PDUURP VDOWRX VREUH R FDFKRUUR FDQVDGR
"""

frase = str(input("Digite uma frase: "))
nova_frase = ''

for i in frase:    
    if i == ' ':
        nova_frase += ' '     
    else:
        nova_frase += chr(ord(i) - 29)

print(nova_frase)

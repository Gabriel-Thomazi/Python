"""
Faca um programa que preencha um vetor com os modelos de cinco carros (exemplos de
modelos: Fusca, Gol, Vectra, etc.). Preencha outro vetor com o consumo desses carros,
isto e, quantos quilometros cada um deles faz com um litro de combustıvel. Calcule e
mostre:
(a) O modelo de carro mais economico;
(b) Quantos litros de combustıvel cada um dos carros cadastrados consomem para
percorrer uma distancia de 1.000 quilometros.
"""

modelos_carros = []
consumo_carros = []
quantos_litros = []

modelo_mais_economico = ''
consumo_mais_barato = 9999999

while True:
    mdl = str(input("Digite o modelo do carro(\"sair\" para encerrar o loop.): ")).title()
    if mdl == 'Sair':
        break

    modelos_carros.append(mdl)

    csm = float(input(f"Digite quantos km o modelo {mdl} faz com 1l de combustivel. "))
    consumo_carros.append(csm)

    if csm < consumo_mais_barato:
        consumo_mais_barato = csm
        modelo_mais_economico = mdl
    
    litros_para_1000km = 1000/csm
    quantos_litros.append(litros_para_1000km)


print(f"\nLista de modelos de carro: {modelos_carros}")
print(f"Lista de consumo de carros (km/l): {consumo_carros}")

print(f"\nO modelo mais econômico é: {modelo_mais_economico}")

print("\nConsumo de litros para percorrer 1000 km de cada modelo:")
for i in range(len(modelos_carros)):
    print(f"{modelos_carros[i]}: {quantos_litros[i]:.2f} litros")
"""
Ler o nome e o valor de uma determinada mercadoria de uma loja. Sabendo que o
desconto para pagamento a vista e de 10% sobre o valor total, calcular o valor a ser
pago a vista. Escrever o nome da mercadoria, o valor total, o valor do desconto e o valor
a ser pago a vista
"""

lista_nome_produtos = [] 
lista_valor_produtos = [] 

soma_valor_produto = 0

while True:
    nome = str(input("Digite o nome do produto: "))
    lista_nome_produtos.append(nome)
    valor = float(input("Digite o valor do produto: "))
    lista_valor_produtos.append(valor)

    soma_valor_produto += valor
    valor_desconto = soma_valor_produto * 0.10
    valor_total_a_vista = soma_valor_produto - valor_desconto
    pagamento = str(input("Deseja finalizar a compra?(sim ou nao) "))

    if pagamento == 'sim':
        break

for i in range(len(lista_valor_produtos)):
    print(f"{lista_nome_produtos[i]}: {lista_valor_produtos[i]} reais")
   
   
print(f"Valor total: {soma_valor_produto:.2f}\nValor do desconto: {valor_desconto:.2f}")
print(f"Valor total a vista: {valor_total_a_vista:.2f}")

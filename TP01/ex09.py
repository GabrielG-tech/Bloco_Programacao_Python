# Desenvolva um programa que aplique descontos diferentes com base no valor da compra: desconto de 10% para compras acima de R$100, 15% para compras acima de R$200, etc.

valor = float(input("Digite o valor da compra: "))

# Definindo os descontos com base nas faixas de valor
if valor >= 100:
    # Desconto relativo ao valor (máximo de 95%)
    desconto = min(0.95, 0.05 + (valor - 100) / 1000) 
else:
    # 0% de desconto para compras abaixo de R$100
    desconto = 0

# Calculando o valor com desconto
valor_descontado = valor * (1 - desconto)

# Exibindo os resultados
print("O desconto para R$%.2f é %.0f%%" % (valor, desconto * 100))
print("Valor com desconto: R$%.2f" % valor_descontado)

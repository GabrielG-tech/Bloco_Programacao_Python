# Nivel 1 - Ex 3
# Crie um dicionário que represente um catálogo de produtos de uma loja. Cada chave deve ser o nome do produto e o valor no dicionário é o preço do produto. Em seguida adicione pelo menos três produtos ao catálogo. E depois, deve haver uma funcionalidade para aplicar um desconto de 10% em todos os produtos.

catalogo = {
    "Camiseta": 25.00,
    "Calça Jeans": 50.00,
    "Tênis": 80.00
}

def aplicar_desconto(catalogo, desconto):
    for produto, preco in catalogo.items():
        novo_preco = preco * (1 - desconto)
        catalogo[produto] = novo_preco

aplicar_desconto(catalogo, 0.10)

print("Catálogo com desconto aplicado:")
for produto, preco in catalogo.items():
    print(f"{produto}: R${preco:.2f}")

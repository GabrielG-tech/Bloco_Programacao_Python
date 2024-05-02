# Crie um dicionario que represente um catalogo de produtos de uma loja. Cada chave é o nome do produto e o valor é o preco do produto. Adicione pelo menos tres produtos ao catalogo. Em seguida, adicione uma funcionalidade para aplicar um desconto de 10% em todos os produtos.

livros = {
    "Harry Potter": 30.00,
    "O Menino do Pijama Listrado": 40.00,
    "O diario de um banana": 40.00
}

livrosDesconto = {livro: preco * 0.9 for livro, preco in livros.items()}

[print("{} - R${:.2f}".format(livro, preco)) 
for livro, preco in livros.items()]

print()

[print("{} - R${:.2f}".format(livro, preco)) 
for livro, preco in livrosDesconto.items()]
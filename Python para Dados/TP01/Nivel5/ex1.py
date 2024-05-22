# Nivel 5 - Ex 1
# Filtragem em Listas de Dicionários com Mais de uma Condição: Crie um programa que dada uma lista de dicionários representando informações de produtos (exemplo: {"nome": "caneta", "preço": 1.50, "estoque": 200}, {“nome” : “lápis, “preço” : 0.80, “estoque”: 47}, …), filtre e mostre produtos com preço acima de R$60 e em estoque acima de 50 unidades e gere uma lista de dicionários chamada “ProdutosEmPromocao” que deverá conter os itens filtrados porém o campo preço deverá conter uma tupla onde o primeiro item é o preço anterior e o segundo item o novo preço com um desconto de 20%.

produtos = [
    {"nome": "caneta", "preço": 1.50, "estoque": 200},
    {"nome": "lápis", "preço": 0.80, "estoque": 47},
    {"nome": "caderno", "preço": 5.00, "estoque": 120},
    {"nome": "borracha", "preço": 0.50, "estoque": 85},
    {"nome": "mochila", "preço": 50.00, "estoque": 30}
]

def listar_produtos(produtos):
    print("Lista de produtos:")
    for produto in produtos:
        print(f"Nome: {produto['nome']}, Preço: {produto['preço']}, Estoque: {produto['estoque']}")

def valor_total_estoque(produtos):
    total = sum(produto['preço'] * produto['estoque'] for produto in produtos)
    return total

def produto_mais_caro(produtos):
    mais_caro = max(produtos, key=lambda x: x['preço'])
    return mais_caro

listar_produtos(produtos)

total_estoque = valor_total_estoque(produtos)
print(f"\nValor total do estoque: R$ {total_estoque:.2f}")

mais_caro = produto_mais_caro(produtos)
print(f"\nProduto mais caro: Nome: {mais_caro['nome']}, Preço: {mais_caro['preço']}, Estoque: {mais_caro['estoque']}")

# Nivel 5 - Ex 1
# Filtragem em Listas de Dicionários com Mais de uma Condição: Crie um programa que dada uma lista de dicionários representando informações de produtos (exemplo: {"nome": "caneta", "preço": 1.50, "estoque": 200}, {“nome” : “lápis, “preço” : 0.80, “estoque”: 47}, …), filtre e mostre produtos com preço acima de R$60 e em estoque acima de 50 unidades e gere uma lista de dicionários chamada “ProdutosEmPromocao” que deverá conter os itens filtrados porém o campo preço deverá conter uma tupla onde o primeiro item é o preço anterior e o segundo item o novo preço com um desconto de 20%.

def filtrar_produtos_em_promocao(produtos):
    produtosFiltrados = [
        produto for produto in produtos if produto['preço'] > 60 and produto['estoque'] > 50
    ]
    
    # lista de dic com tupla em que o 1º item é o preço anterior e o 2º item é o novo preço com 20% de desconto.
    ProdutosEmPromocao = [
        {
            'nome': produto['nome'],
            'preço': (produto['preço'], round(produto['preço'] * 0.8, 2)),
            'estoque': produto['estoque']
        } for produto in produtosFiltrados
    ]
    return ProdutosEmPromocao

produtos = [
    {"nome": "caneta", "preço": 1.50, "estoque": 200},
    {"nome": "bloco de papel", "preço": 70.50, "estoque": 90},
    {"nome": "lápis", "preço": 0.80, "estoque": 47},
    {"nome": "caderno", "preço": 5.00, "estoque": 120},
    {"nome": "borracha", "preço": 60.00, "estoque": 85},
    {"nome": "apontador", "preço": 60.55, "estoque": 85},
    {"nome": "mochila", "preço": 60.05, "estoque": 30}
]

ProdutosEmPromocao = filtrar_produtos_em_promocao(produtos)

print("\033[1mProdutos em promoção:\033[0m")
for produto in ProdutosEmPromocao:
    nome = produto['nome']
    preco_anterior, preco_novo = produto['preço']
    estoque = produto['estoque']
    print(f"Produto: {nome.capitalize()}\nPreço anterior: R${preco_anterior}\nPreço com desconto: R${preco_novo}\nEstoque: {estoque}\n")
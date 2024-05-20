# Nivel 4 - Ex 1
# Condições para Remoção: Considerando um dicionário que represente um controle de estoque (ex.: {“mouse”: 26, “monitor” : 13, “Pendrive” : 83, …}) implemente uma função que leia este dicionário e remova os itens que estiverem com estoque abaixo de uma certa quantidade utilizando comprehensions e retorne este novo dicionário atualizado e exiba ele para o usuário.

def remover_itens_com_pouco_estoque(estoque, quantidade_minima):
    estoque_atualizado = {item: quantidade for item, quantidade in estoque.items() if quantidade >= quantidade_minima}
    return estoque_atualizado

dicionario = {
    'mouse': 26,
    'monitor': 13,
    'Pendrive': 83
}

quantidade_minima = 20

dicionario_atualizado = remover_itens_com_pouco_estoque(dicionario, quantidade_minima)

print(f"Produtos com estoque a cima de {quantidade_minima}:\n {dicionario_atualizado}")


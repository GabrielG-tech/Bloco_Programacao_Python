# Desenvolva um programa que, dado uma lista de nomes com possíveis duplicatas, retorne um dicionário contendo a contagem de cada nome. Além disso, ele deve remover qualquer nome que apareça apenas uma vez, utilizando técnicas de manipulação de dicionários.

def contar_nomes(nomes):
    contador = {}
    for nome in nomes:
        contador[nome] = contador.get(nome, 0) + 1
    return {nome: count for nome, count in contador.items() if count > 1}

nomes = ["João", "Maria", "João", "Pedro", "Maria", "João", "Ana"]
print(contar_nomes(nomes))  # Saída: {'João': 3, 'Maria': 2}


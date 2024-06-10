# Desenvolva um programa que, dado uma lista de nomes com possíveis duplicatas, retorne um dicionário contendo a contagem de cada nome. Além disso, ele deve remover qualquer nome que apareça apenas uma vez, utilizando técnicas de manipulação de dicionários.

def contar_nomes(lista_de_nomes):
    contagem = {}
    for nome in lista_de_nomes:
        if nome in contagem:
            contagem[nome] += 1
        else:
            contagem[nome] = 1

    contagem_filtrada = {nome: contagem for nome, contagem in contagem.items() if contagem > 1}

    return contagem_filtrada

lista_de_nomes = ["Ana", "João", "Ana", "Maria", "João", "Pedro", "Ana", "Maria"]
resultado = contar_nomes(lista_de_nomes)
print(resultado)

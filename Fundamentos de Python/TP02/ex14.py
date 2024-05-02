# Simulador de Lançamento de Dados
# Problema: Crie um programa que simule o lançamento de um dado n vezes, armazenando os resultados em uma lista, depois calcule a média dos resultados e calcule a distribuição de frequência dos elementos da lista.

import random

def simular_lancamento_dado(n_lancamentos):
    """
    Simula o lançamento de um dado n vezes.

    Args:
        n_lancamentos (int): O número de vezes que o dado será lançado.

    Returns:
        tuple: Uma tupla contendo a lista dos resultados dos lançamentos e a média dos resultados.
    """
    lista_resultados = []

    for _ in range(n_lancamentos):
        resultado = random.randint(1, 6)
        lista_resultados.append(resultado)

    media = sum(lista_resultados) / n_lancamentos

    return lista_resultados, media

def calcular_distribuicao_frequencia(lista):
    """
    Calcula a distribuição de frequência dos elementos em uma lista.

    Args:
        lista (list): A lista contendo os elementos.

    Returns:
        dict: Um dicionário onde as chaves são os elementos únicos da lista e os valores são as frequências desses elementos.
    """
    distribuicao_frequencia = {}

    for elemento in lista:
        if elemento in distribuicao_frequencia:
            distribuicao_frequencia[elemento] += 1
        else:
            distribuicao_frequencia[elemento] = 1

    return distribuicao_frequencia

# Simula lançamento de dado 5 vezes
n_lancamentos = 5
resultados, media = simular_lancamento_dado(n_lancamentos)

print("Resultados dos lançamentos:", resultados)
print("Média dos resultados:", media)

distribuicao_frequencia = calcular_distribuicao_frequencia(resultados)
print("Distribuição de frequência:", distribuicao_frequencia)


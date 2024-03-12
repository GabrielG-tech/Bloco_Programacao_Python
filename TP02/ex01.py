# Contador de Números Positivos
# Problema: Escreva um programa que utilize um loop for para percorrer uma lista de números gerados aleatoriamente e conte quantos são positivos.

import random

def geradorLista(inicial, final):
    """
    Gera uma lista de números inteiros aleatórios dentro de um intervalo.

    Args:
        inicial (int): O limite inferior do intervalo.
        final (int): O limite superior do intervalo.

    Returns:
        list: Uma lista de 5 números inteiros aleatórios dentro do intervalo especificado.
    """
    lista = []
    for i in range(5):  # Gera 5 números aleatórios
        lista.append(random.randint(inicial, final))
    return lista

def contadorPositivos(lista):
    """
    Conta o número de elementos positivos em uma lista.

    Args:
        lista (list): Uma lista de números inteiros.

    Returns:
        int: O número de elementos positivos na lista.
    """
    numPositivos = 0
    for i in lista:
        if i > 0:
            numPositivos += 1
    return numPositivos

# Gerar uma lista de números aleatórios entre -50 e 50
lista_gerada = geradorLista(-50, 50)
print("Lista gerada:", lista_gerada)

# Contar o número de elementos positivos na lista gerada
num_positivos = contadorPositivos(lista_gerada)
print("A lista tem", num_positivos, "números positivos.")

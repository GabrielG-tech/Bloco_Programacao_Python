# Função Geradora de Histograma
# Problema: Escreva uma função que receba uma lista de números e imprima um histograma na tela (usando asteriscos para representar a frequência dos números).

import random

def gerarLista(tamanho, valor_minimo, valor_maximo):
    """
    Gera uma lista de números aleatórios.

    Args:
        tamanho (int): O tamanho da lista a ser gerada.
        valor_minimo (int): O valor mínimo que pode ser gerado na lista.
        valor_maximo (int): O valor máximo que pode ser gerado na lista.

    Returns:
        list: Uma lista de números inteiros aleatórios com o tamanho especificado e dentro do intervalo especificado.
    """
    return [random.randint(valor_minimo, valor_maximo) for i in range(tamanho)]

def histograma(lista):
    """
    Imprime um histograma na tela usando asteriscos para representar a frequência dos números na lista.

    Args:
        lista (list): Uma lista de números inteiros.

    Returns:
        None
    """
    largura = max(lista)  # Determina a largura máxima do histograma
    for i in range(largura, 0, -1):
        linha = ""
        for n in lista:
            if n >= i:
                linha += "\033[1;41m * \033[m "
            else:
                linha += "    "  # Adiciona espaços em branco para manter o alinhamento
        print(linha)
    print(end=" ")
    for n in range(0, len(lista)):
        if lista[n] < 10:
            print(lista[n], end="   ")
        else:
            print(lista[n], end="  ")

# Exemplo de uso:
tamanho_da_lista = 10
valor_minimo = 1
valor_maximo = 10
lista = gerarLista(tamanho_da_lista, valor_minimo, valor_maximo)
histograma(lista)

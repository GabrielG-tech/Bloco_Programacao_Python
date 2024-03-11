# Função Geradora de Histograma
# Problema: Escreva uma função que receba uma lista de números e imprima um histograma na tela (usando asteriscos para representar a frequência dos números).

import random 
def gerarLista(tamanho, valor_minimo, valor_maximo):
    return [random.randint(valor_minimo, valor_maximo) for _ in range(tamanho)]

def histograma(lista):
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
    
# Gerar uma lista de números aleatórios
tamanho_da_lista = 10
valor_minimo = 1
valor_maximo = 10
lista = gerarLista(tamanho_da_lista, valor_minimo, valor_maximo)

histograma(lista)
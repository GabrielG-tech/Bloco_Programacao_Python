# Função Geradora de Histograma
# Problema: Escreva uma função que receba uma lista de números e imprima um histograma na tela (usando asteriscos para representar a frequência dos números).

lista = list(range(0, 10, 1)) + list(range(10, 0, -1))

def histograma(lista):
    largura = 60
    for n in range(0, len(lista)//2):
        print("\033[1;34m*\033[m"*lista[n] + "\033[1;37m*\033[m"*(largura-lista[n]))
    for n in range(len(lista)//2, len(lista)):
        print("\033[1;34m*\033[m"*lista[n] + "\033[1;31m*\033[m"*(largura-lista[n]))

histograma(lista)
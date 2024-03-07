# Função Geradora de Histograma
# Problema: Escreva uma função que receba uma lista de números e imprima um histograma na tela (usando asteriscos para representar a frequência dos números).

lista = list(range(0, 20, 1)) + list(range(20, 0, -1))

def histograma(lista):
    largura = 80
    for n in range(0, len(lista)//2):
        print("\033[1;44m \033[m"*lista[n] + "\033[1;47m \033[m"*(largura-lista[n]))
    for n in range(len(lista)//2, len(lista)):
        print("\033[1;44m \033[m"*lista[n] + "\033[1;41m \033[m"*(largura-lista[n]))

histograma(lista)
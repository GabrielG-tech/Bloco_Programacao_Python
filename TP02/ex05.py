# Gerador de Lista de Quadrados
# Problema: Escreva um programa que utilize um loop for para gerar uma lista dos quadrados dos números de 1 a 20.

def gerar_lista_quadrados():
    """
    Gera uma lista dos quadrados dos números de 1 a 20.

    Returns:
        list: Lista dos quadrados dos números de 1 a 20.
    """
    lista = []  # Inicializa uma lista vazia para armazenar os quadrados
    for i in range(1, 21):  # Loop de 1 a 20
        lista.append(i ** 2)  # Adiciona o quadrado do número atual à lista
    return lista  # Retorna a lista de quadrados


# Chama a função e imprime a lista gerada
print(gerar_lista_quadrados())
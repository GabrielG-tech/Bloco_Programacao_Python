# Filtragem de Lista por Condição
# Problema: Desenvolva um programa que filtre uma lista de números, removendo aqueles que não satisfazem uma condição específica (por exemplo, ser par).

lista = [12345, 1234, 1234567, 12345, 12345678, 123456789, 123]

def filtrar_numeros_pares(lista):
    """
    Filtra uma lista de números, removendo aqueles que não são pares.

    Args:
        lista (list): Uma lista de números inteiros.

    Returns:
        list: Uma nova lista contendo apenas os números pares da lista original.
    """
    lista_filtrada = [num for num in lista if num % 2 == 0]
    return lista_filtrada

# Exemplo de uso da função
lista_filtrada = filtrar_numeros_pares(lista)
print("Lista original:", lista)
print("Lista filtrada (apenas números pares):", lista_filtrada)
